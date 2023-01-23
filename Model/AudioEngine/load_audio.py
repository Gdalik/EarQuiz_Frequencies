import math
import time

from Model.AudioEngine.process import chunked_proc
from Model.calc import find_divider
import numpy as np
from pedalboard import Gain
from pedalboard.io import AudioFile
from copy import copy
import itertools


class AudioChunk:
    def __init__(self, audiofile: AudioFile, starttime: int or float, endtime: int or float,
                 slice_length=15, norm_level=None, callback=None):
        self.audiofile = audiofile
        self._starttime = max(0, starttime)
        self._endtime = max(0, endtime)
        self._starttime = min(self.starttime, self.endtime)
        self._endtime = max(self.starttime + 10, self.endtime)
        self._slice_length = max(slice_length, 10)
        self.samplerate = audiofile.samplerate
        self.source_length = audiofile.frames / audiofile.samplerate
        self._endtime = min(self._endtime, self.source_length)
        self._slice_length = min(self._slice_length, self._endtime - self._starttime, 30)
        self.cropped = None
        self.norm_level = norm_level
        self.cropped_normalized = None
        self.cropped_norm_split = None
        self._slices_num = self.chunk_length // self.slice_length
        self.callback = callback
        self.reset()

    def _callback_out(self, arg: dict):
        if self.callback is not None:
            self.callback(arg)

    def _read_and_crop(self):
        self.cropped = np.empty((self.audiofile.num_channels, 0))
        output = {'State': 'Reading / cropping audiofile', 'Percent': 0}
        self._callback_out(output)
        self.audiofile.seek(int(self.sec2fr(self.starttime)))
        starttime_fr = int(self.sec2fr(self.starttime))
        target_length_fr = int(self.sec2fr(self.slice_length * self._slices_num))
        divider = find_divider(target_length_fr, min=5)
        while self.cropped[0].size != starttime_fr + target_length_fr:
            ch = self.audiofile.read(int(target_length_fr/divider))
            self.cropped = np.concatenate((self.cropped, ch), axis=1)
            output['Percent'] = int(self.cropped[0].size / target_length_fr * 100)
            self._callback_out(output)
        output.clear()

    def reset(self):
        a = time.time()
        self._read_and_crop()
        self.cycle = self.cycle_id = None
        if self.norm_level is None:
            self.cropped_normalized = copy(self.cropped)
            self.split()
        else:
            self.normalize(self.norm_level)
        print(f'Processing time = {time.time() - a}')


    @property
    def starttime(self):
        return self._starttime

    @starttime.setter
    def starttime(self, value):
        old_value = self._starttime
        self._starttime = max(value, 0)
        self._starttime = min(self._starttime, self.endtime - self.slice_length)
        if old_value != self._starttime:
            self.reset()

    @property
    def endtime(self):
        return self._endtime

    @endtime.setter
    def endtime(self, value):
        self._endtime = max(self.starttime + self.slice_length, value)
        self._endtime = min(self._endtime, self.source_length)
        a = self.slices_num

    @property
    def slice_length(self):
        return self._slice_length

    @slice_length.setter
    def slice_length(self, value):
        old_value = self._slice_length
        self._slice_length = min(value, self.endtime - self.starttime, 30)
        self._slice_length = max(self._slice_length, 10)
        if old_value != self._slice_length:
            self.reset()

    @property
    def chunk_length(self):
        return self.endtime - self.starttime

    @property
    def input_db_array(self):
        chunk = self.cropped
        chunk_abs = np.absolute(chunk)
        return 20*np.emath.log10(chunk_abs)

    @property
    def max_level(self):
        db_ar = self.input_db_array
        max_ch_values = [max(Ch) for Ch in db_ar]
        return max(max_ch_values)

    @property
    def rms_level(self):
        rms_ar = np.sqrt(np.mean(self.cropped**2))
        return 20*math.log10(rms_ar)

    @property
    def slices_num(self):
        new_value = self.chunk_length // self.slice_length
        if new_value != self._slices_num:
            self._slices_num = self.chunk_length // self.slice_length
            self.reset()
        return new_value

    def sec2fr(self, sec: int or float):
        return int(self.samplerate * sec)

    def normalize(self, head_level: int or float):
        delta = head_level - self.max_level
        gain = Gain(delta)
        self.cropped_normalized = chunked_proc(self.cropped, self.audiofile.samplerate, gain,
                                               proc_name='Normalizing audio', callback=self.callback)
        self.split()
        if self.cycle_id is not None:
            cycle_id = next(self.cycle_id)
            self.cycle = None
            for _ in range(cycle_id):
                self.slice_iter()
        return self.cropped_normalized

    def split(self):
        self.cropped_norm_split = np.hsplit(self.cropped_normalized, self.slices_num)
        return self.cropped_norm_split

    def slice_iter(self):
        if self.cycle is None:
            self.cycle = itertools.cycle(self.cropped_norm_split)
            self.cycle_id = itertools.cycle(range(len(self.cropped_norm_split)))
        next(self.cycle_id)
        return next(self.cycle)

