import math
from PyQt6.QtCore import QObject, pyqtSignal
import numpy
from Model.calc import optimize_divider
from Model.AudioEngine.preview_audio import PreviewAudioCrop
import numpy as np
from pedalboard.io import AudioFile
from copy import copy
import itertools
from Utilities.exceptions import InterruptedException
from Model.globals import pinknoise, MinAudioDuration, PinknoiseLength
import copy


class AudioChunkSignals(QObject):
    showNormalizationLevel = pyqtSignal(float)


class AudioChunk(PreviewAudioCrop, QObject):
    signals = AudioChunkSignals()

    def __init__(self, audiofile_path: str, starttime: int or float, endtime: int or float,
                 slice_length=15, norm_level=None, cropped=None, cropped_normalized=None, callback=None):
        self.audiofile_path = audiofile_path
        self._init_audiosource()
        self._check_source_length()
        super().__init__(audiofile_length=self.source_length,
                         starttime=starttime, endtime=endtime, slice_length=slice_length, strictMode=True)
        self.norm_level = self.last_norm_level = norm_level
        self.norm_proc = None
        self.cropped = cropped
        self.cropped_normalized = self.old_cropped_normalized = cropped_normalized
        self.cropped_norm_split = \
            self.cycle = self.cycle_id_gen = self.cycle_id = self.current_slice = None
        self.callback = callback
        self.user_stopped = None
        self._reset(readcrop=(self.cropped is None), normalize=(self.cropped_normalized is None))

    def _init_pinknoise(self):
        self.audiofile = None
        self.source_length = PinknoiseLength
        self.samplerate = 44100

    def _init_audiofile(self):
        self.audiofile = AudioFile(self.audiofile_path)
        self.source_length = self.audiofile.duration
        self.samplerate = int(self.audiofile.samplerate)

    def _init_audiosource(self):
        if self.audiofile_path == 'Pink noise':
            self._init_pinknoise()
        else:
            self._init_audiofile()

    def _check_source_length(self):
        if self.source_length < MinAudioDuration:
            self._close_audiofile()
            raise ValueError(f'Audio file length cannot be less than {MinAudioDuration} sec')

    def _callback_out(self, arg: dict, callback=None):
        _callback = callback or self.callback
        if _callback is not None:
            _callback(arg)

    def _read_and_crop(self, callback=None):
        if self.audiofile_path == 'Pink noise':
            self.cropped = pinknoise
            return
        self._open_audiofile()  # makes no effect if audiofile is already opened
        self.user_stopped = False
        self.cropped = np.empty((self.audiofile.num_channels, 0))
        output = {'State': 'Reading / cropping audiofile', 'Percent': 0}
        self._callback_out(output, callback=callback)
        self.audiofile.seek(int(self.sec2fr(self.starttime)))
        read_ch_samples = int(self.chunk_length_fr / self._find_rc_divider()) if self.audiofile.exact_duration_known \
            else int(self.samplerate)
        while self.cropped[0].size < self.chunk_length_fr:
            ch = self.audiofile.read(read_ch_samples)
            self.cropped = np.concatenate((self.cropped, ch), axis=1)
            output['Percent'] = int(self.cropped[0].size / self.chunk_length_fr * 100)
            try:
                self._callback_out(output, callback=callback)
            except InterruptedException:
                self._stop()
                return
            if self.audiofile.tell() == self.audiofile.frames:
                break   # to avoid infinite loop for some 'broken' MP3 files
        self._close_audiofile()

    def _open_audiofile(self):
        if self.audiofile is None or not self.audiofile.closed:
            return self.audiofile
        self.audiofile = AudioFile(self.audiofile_path)
        return self.audiofile

    def _find_rc_divider(self, max_div=100):
        min_div = self.chunk_length // 300 if self.chunk_length >= 600 else 2
        return optimize_divider(self.chunk_length_fr, ref_div=min_div, max_div=max_div)

    @property
    def chunk_length_fr(self):
        return int(self.sec2fr(self.chunk_length))

    def _close_audiofile(self):
        if self.audiofile is None or self.audiofile.closed:
            return
        self.audiofile.close()

    def _stop(self):
        self.user_stopped = True
        self.cropped = self.cropped_normalized = self.cropped_norm_split = self.cycle = \
            self.cycle_id_gen = self.cycle_id = None
        self._close_audiofile()

    def _reset(self, readcrop=True, normalize=True, callback=None):
        if readcrop:
            self._read_and_crop(callback=callback)
            if self.user_stopped:
                return
        self._refresh_old_values()
        self.cycle = self.cycle_id_gen = self.cycle_id = None
        if self.norm_level is None:
            self.cropped_normalized = copy(self.cropped)
            self.split()
        elif not normalize:
            self.split()
        else:
            self.normalize(norm_level=self.norm_level, resetAudio=True)

    @property
    def max_level(self):
        with np.errstate(divide='ignore'):
            return 20 * np.emath.log10(max(numpy.max(np.absolute(self.cropped), axis=1)))

    @property
    def rms_level(self):
        rms_ar = np.sqrt(np.mean(self.cropped ** 2))
        with np.errstate(divide='ignore'):
            return 20 * math.log10(rms_ar)

    def sec2fr(self, sec: int or float):
        return int(self.samplerate * sec)

    def normalize(self, resetAudio=False, norm_level=None, callback=None):
        _callback = callback or self.callback if self.audiofile is not None else None
        head_level = norm_level or self.norm_level or 0
        if not resetAudio and self.last_norm_level == head_level and self.cropped_normalized is not None:
            return
        proc_name = 'Normalizing audio'
        self._callback_out({'State': proc_name, 'Percent': 0}, callback=_callback)
        delta = head_level - self.max_level
        self._callback_out({'State': proc_name, 'Percent': 50}, callback=_callback)
        self.cropped_normalized = self.cropped * 10 ** (delta / 20)
        self._callback_out({'State': proc_name, 'Percent': 100}, callback=_callback)
        self.split()
        self._restore_current_audio_slice_cycle()
        self.last_norm_level = head_level
        return self.cropped_normalized

    def _restore_current_audio_slice_cycle(self):
        if self.cycle_id_gen is not None:
            if self.cycle_id is None:
                self.cycle_id = next(self.cycle_id_gen)
            self.cycle = None
            for _ in range(self.cycle_id + 1):
                self.slice_iter()

    def split(self):
        target_length_fr = int(self.sec2fr(self.slice_length * self.slices_num))
        cropped_norm_adj = self.cropped_normalized[:, :target_length_fr]
        self.cropped_norm_split = np.hsplit(cropped_norm_adj, self.slices_num)
        return self.cropped_norm_split

    def slice_iter(self, refresh=False):
        if self.cycle is None or refresh:
            self.cycle = itertools.cycle(self.cropped_norm_split)
            self.cycle_id_gen = itertools.cycle(range(len(self.cropped_norm_split)))
        self.cycle_id = next(self.cycle_id_gen)
        self.current_slice = next(self.cycle)
        return self.current_slice

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

    def checkActionNeeded(self):
        if not self._old_values:
            return None
        reset_cond1 = self._old_values['starttime'] != self.starttime
        reset_cond2 = self._old_values['chunk_length'] != self.chunk_length and \
                      (self._old_values['slices_num'] != self.slices_num or self._old_values['slice_length']
                       != self.slice_length)
        if reset_cond1 or reset_cond2:
            return 'reset'
        elif self._old_values['slice_length'] != self.slice_length:
            return 'reslice'
        else:
            return 'refresh_old_values'

    def update(self, mode: str, callback=None):
        if mode == 'reset':
            self._reset(callback=callback)
        elif mode == 'reslice':
            self._reslice()
        elif mode == 'refresh_old_values':
            self._refresh_old_values()

    def _refresh_old_values(self):
        self._old_values = {'starttime': self.starttime, 'chunk_length': self.chunk_length,
                            'slices_num': self.slices_num, 'slice_length': self.slice_length}
