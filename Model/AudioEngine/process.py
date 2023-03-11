import time

from pedalboard import PeakFilter, Pedalboard
from Model.calc import proc_unproc_len, rand_buffer, find_divider, minimize_divider
import numpy as np
from Utilities.exceptions import InterruptedException


def eq_proc(cur_sample, samplerate: int, freq1: int or float, freq2=None, gain_depth=12, Q=1.41, proc_t_perc=40):
    # freq > 0 -- boost; freq < 0 -- cut
    def sec2fr(sec: int or float):
        return int(samplerate * sec)

    def equalize(buffer_size: int = 8192):
        _equalized = chain.process(audio_parts[1], samplerate, buffer_size=buffer_size, reset=True)
        return _equalized

    cur_sample_length = cur_sample[0].size / samplerate
    proc_len, unproc_len = proc_unproc_len(cur_sample_length, proc_t_perc)
    gain = gain_depth * -1 if freq1 < 0 else gain_depth
    eq1 = PeakFilter(cutoff_frequency_hz=abs(freq1), gain_db=gain, q=Q)
    if freq2:
        gain2 = gain_depth * -1 if freq2 < 0 else gain_depth
        eq2 = PeakFilter(cutoff_frequency_hz=abs(freq2), gain_db=gain2, q=Q)
    else:
        eq2 = None
    chain = Pedalboard([eq1, eq2])
    proc_len_fr = sec2fr(proc_len)
    unproc_len_fr = sec2fr(unproc_len)
    audio_parts = np.hsplit(cur_sample, [unproc_len_fr, unproc_len_fr + proc_len_fr])
    pre_eq = audio_parts[0]
    equalized = equalize()
    while equalized.size != audio_parts[1].size:  # Solving possible buffering issues (see Pedalboard docs).
        equalized = equalize(buffer_size=rand_buffer())
    post_eq = audio_parts[2]
    return np.concatenate((pre_eq, equalized, post_eq), axis=1)


class ChunkedProc:
    def __init__(self, source: np.array, samplerate: int, DSP, proc_name='Processing audio', callback=None):
        self.source = source
        self.samplerate = samplerate
        self.DSP = DSP
        self.callback = callback
        self.stopped = None
        self.out_stat = {'State': proc_name, 'Percent': 0}

    def call(self):
        def callback_out():
            if self.callback is not None:
                self.callback(self.out_stat)
        self.stopped = False
        output = np.empty((len(self.source), 0))
        min_div = self.source[0].size // (300 * self.samplerate) if self.source[0].size >= 600 * self.samplerate else 2
        divider = minimize_divider(self.source[0].size, min_div=min_div)
        chunks = np.hsplit(self.source, divider)
        callback_out()
        for ind, chunk in enumerate([*chunks]):
            processed = self.DSP.process(chunk, self.samplerate)
            while processed.size != chunk.size:  # Solving possible buffering issues (see Pedalboard docs).
                processed = self.DSP.process(chunk, self.samplerate, buffer_size=rand_buffer(), reset=True)
            output = np.concatenate((output, processed), axis=1)
            self.out_stat['Percent'] = int((ind + 1) / len(chunks) * 100)
            try:
                callback_out()
            except InterruptedException:
                self._stop()
                return None
        return output

    def _stop(self):
        self.stopped = True
