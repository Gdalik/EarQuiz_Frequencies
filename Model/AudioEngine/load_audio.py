import math
import time
from Model.AudioEngine.process import ChunkedProc
from Model.calc import find_divider
from Model.AudioEngine.preview_audio import PreviewAudioCrop
import numpy as np
from pedalboard import Gain
from pedalboard.io import AudioFile
from copy import copy
import itertools
from Utilities.exceptions import InterruptedException
from definitions import pinknoise


class AudioChunk(PreviewAudioCrop):
    def __init__(self, audiofile_path: str, starttime: int or float, endtime: int or float,
                 slice_length=15, norm_level=None, callback=None):
        self.audiofile_path = audiofile_path
        if self.audiofile_path == 'pinknoise':
            self.audiofile = None
            self.source_length = 30
            self.samplerate = 44100
        else:
            self.audiofile = AudioFile(self.audiofile_path)
            self.source_length = self.audiofile.frames / self.audiofile.samplerate
            self.samplerate = int(self.audiofile.samplerate)
        if self.source_length < 30:
            raise ValueError('Audio file length cannot be less than 30 sec')
        super().__init__(audiofile_length=self.source_length,
                         starttime=starttime, endtime=endtime, slice_length=slice_length)
        self.norm_level = norm_level
        self.norm_proc = None
        self.cropped = self.cropped_normalized = self.cropped_norm_split = \
            self.cycle = self.cycle_id_gen = self.cycle_id = None
        self.callback = callback
        self.user_stopped = None
        self._reset()  # self.audiofile is closed during self._read_and_crop(), called from self.reset()

    def _callback_out(self, arg: dict, callback=None):
        _callback = callback or self.callback
        if _callback is not None:
            _callback(arg)

    def _read_and_crop(self, callback=None):
        if self.audiofile_path == 'pinknoise':
            self.cropped = pinknoise
            return
        self._open_audiofile()  # makes no effect if audiofile is already opened
        self.user_stopped = False
        self.cropped = np.empty((self.audiofile.num_channels, 0))
        output = {'State': 'Reading / cropping audiofile', 'Percent': 0}
        self._callback_out(output, callback=callback)
        self.audiofile.seek(int(self.sec2fr(self.starttime)))
        chunk_length_fr = int(self.sec2fr(self.chunk_length))
        min_div = self.chunk_length // 300 if self.chunk_length >= 600 else 2
        divider = find_divider(chunk_length_fr, Min=min_div)
        # print(f'{divider=}')
        while self.cropped[0].size != chunk_length_fr:
            ch = self.audiofile.read(int(chunk_length_fr / divider))
            self.cropped = np.concatenate((self.cropped, ch), axis=1)
            output['Percent'] = int(self.cropped[0].size / chunk_length_fr * 100)
            # print(f'{self.cropped[0].size=} {chunk_length_fr=}')
            try:
                self._callback_out(output, callback=callback)
            except InterruptedException:
                self._stop()
                return
        # output.clear()
        self._close_audiofile()

    def _open_audiofile(self):
        if self.audiofile is None or not self.audiofile.closed:
            return self.audiofile
        self.audiofile = AudioFile(self.audiofile_path)
        return self.audiofile

    def _close_audiofile(self):
        if self.audiofile is None or self.audiofile.closed:
            return
        self.audiofile.close()

    def _stop(self):
        print('Process stopped by user!')
        self.user_stopped = True
        self.cropped = self.cropped_normalized = self.cropped_norm_split = self.cycle = \
            self.cycle_id_gen = self.cycle_id = None
        self._close_audiofile()

    def _reset(self, callback=None):
        a = time.time()
        self._read_and_crop(callback=callback)
        if self.user_stopped:
            return
        self._refresh_old_values()
        self.cycle = self.cycle_id_gen = self.cycle_id = None
        if self.norm_level is None:
            self.cropped_normalized = copy(self.cropped)
            self.split()
        else:
            self.normalize(self.norm_level)
        print(f'Processing time = {time.time() - a}')

    @property
    def input_db_array(self):
        chunk = self.cropped
        chunk_abs = np.absolute(chunk)
        with np.errstate(divide='ignore'):
            return 20 * np.emath.log10(chunk_abs)

    @property
    def max_level(self):
        db_ar = self.input_db_array
        max_ch_values = [max(Ch) for Ch in db_ar]
        return max(max_ch_values)

    @property
    def rms_level(self):
        rms_ar = np.sqrt(np.mean(self.cropped ** 2))
        with np.errstate(divide='ignore'):
            return 20 * math.log10(rms_ar)

    def sec2fr(self, sec: int or float):
        return int(self.samplerate * sec)

    def normalize(self, norm_level=None, callback=None):
        _callback = callback or self.callback if self.audiofile is not None else None
        head_level = norm_level or self.norm_level or 0
        delta = head_level - self.max_level
        gain = Gain(delta)
        self.norm_proc = ChunkedProc(self.cropped, self.samplerate, gain,
                                     proc_name='Normalizing audio', callback=_callback)
        self.cropped_normalized = self.norm_proc.call()
        if self.cropped_normalized is None and self.norm_proc.stopped:
            self._stop()
            return None
        self.split()
        if self.cycle_id_gen is not None:
            self.cycle_id = next(self.cycle_id_gen)
            self.cycle = None
            for _ in range(self.cycle_id):
                self.slice_iter()
        return self.cropped_normalized

    def split(self):
        target_length_fr = int(self.sec2fr(self.slice_length * self.slices_num))
        cropped_norm_adj = self.cropped_normalized[:, :target_length_fr]
        print(f'{target_length_fr=} ; {self.cropped_normalized[0].size=} ; {cropped_norm_adj[0].size=}')
        self.cropped_norm_split = np.hsplit(cropped_norm_adj, self.slices_num)
        return self.cropped_norm_split

    def slice_iter(self, refresh=False):
        if self.cycle is None or refresh:
            self.cycle = itertools.cycle(self.cropped_norm_split)
            self.cycle_id_gen = itertools.cycle(range(len(self.cropped_norm_split)))
        self.cycle_id = next(self.cycle_id_gen)
        return next(self.cycle)

    def _reslice(self):
        self.split()
        self.cycle = self.cycle_id = self.cycle_id_gen = None
        self._refresh_old_values()

    @property
    def currentSliceRange(self):
        if self.cycle_id is None:
            return None
        StartTime = self.starttime + self.slice_length * self.cycle_id
        EndTime = self.starttime + self.slice_length * (self.cycle_id + 1)
        return StartTime, EndTime

    def update(self, callback=None):
        if not self._old_values:
            return
        reset_cond1 = self._old_values['starttime'] != self.starttime
        reset_cond2 = self._old_values['chunk_length'] != self.chunk_length and \
                      (self._old_values['slices_num'] != self.slices_num or self._old_values['slice_length']
                       != self.slice_length)
        if reset_cond1 or reset_cond2:
            self._reset(callback=callback)
        elif self._old_values['slice_length'] != self.slice_length:
            self._reslice()
        else:
            self._refresh_old_values()

    def _refresh_old_values(self):
        self._old_values = {'starttime': self.starttime, 'chunk_length': self.chunk_length,
                            'slices_num': self.slices_num, 'slice_length': self.slice_length}
