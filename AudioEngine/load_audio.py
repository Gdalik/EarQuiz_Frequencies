import math
from Misc.calc import rand_buffer
import numpy as np
from pedalboard import Gain


class AudioChunk:
    def __init__(self, audiofile, starttime: int or float, length: int or float):
        self.audiofile = audiofile
        self.starttime = starttime
        self.length = min(length, 30)
        self.length = max(self.length, 10)
        self.samplerate = audiofile.samplerate
        source_length = audiofile.frames / audiofile.samplerate
        if source_length - self.starttime < self.length:
            raise ValueError(f'Cannot extract {self.length}s chunk starting at {self.starttime}s, since the audiofile length is {source_length}s!')
        self.croped = None
        self.reset()

    def reset(self):
        self.audiofile.seek(int(self.sec2fr(self.starttime)))
        self.croped = self.audiofile.read(int(self.sec2fr(self.length)))

    @property
    def input_db_array(self):
        chunk = self.croped
        chunk_abs = np.absolute(chunk)
        return 20*np.emath.log10(chunk_abs)

    @property
    def max_level(self):
        db_ar = self.input_db_array
        max_ch_values = [max(Ch) for Ch in db_ar]
        return max(max_ch_values)

    @property
    def rms_level(self):
        rms_ar = np.sqrt(np.mean(self.croped**2))
        return 20*math.log10(rms_ar)

    def sec2fr(self, sec: int or float):
        return int(self.samplerate * sec)

    def normalize(self, head_level: int or float):
        delta = head_level - self.max_level
        gain = Gain(delta)
        gained = gain.process(self.croped, self.samplerate)
        while gained.size != self.croped.size:
            gained = gain.process(self.croped, self.samplerate, buffer_size=rand_buffer(), reset=True)
        self.croped = gained
        return self.croped

    def split(self, slices_num:int):
        return np.hsplit(self.croped, slices_num)
