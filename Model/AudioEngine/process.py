from pedalboard import PeakFilter
from Misc.calc import proc_unproc_len, rand_buffer
import numpy as np


def eq_proc(cur_sample, samplerate: int, freq1: int or float, freq2=None, boost_cut1='+', boost_cut2='+', gain_depth=12, Q=1.41, proc_t_perc=40):
    def sec2fr(sec: int or float):
        return int(samplerate * sec)

    def equalize(buffer_size: int = 8192):
        _equalized = eq1.process(audio_parts[1], samplerate, buffer_size=buffer_size, reset=True)
        if eq2:
            _equalized = eq2.process(_equalized, samplerate, buffer_size=buffer_size, reset=True)
        return _equalized
    cur_sample_length = cur_sample[0].size / samplerate
    proc_len, unproc_len = proc_unproc_len(cur_sample_length, proc_t_perc)
    gain = gain_depth*-1 if boost_cut1 == '-' else gain_depth
    eq1 = PeakFilter(cutoff_frequency_hz=freq1, gain_db=gain, q=Q)
    if freq2:
        gain2 = gain_depth*-1 if boost_cut2 == '-' else gain_depth
        eq2 = PeakFilter(cutoff_frequency_hz=freq2, gain_db=gain2, q=Q)
    else:
        eq2 = None
    proc_len_fr = sec2fr(proc_len)
    unproc_len_fr = sec2fr(unproc_len)
    audio_parts = np.hsplit(cur_sample, [unproc_len_fr, unproc_len_fr+proc_len_fr])
    pre_eq = audio_parts[0]
    equalized = equalize()
    while equalized.size != audio_parts[1].size:
        equalized = equalize(buffer_size=rand_buffer())
    post_eq = audio_parts[2]
    return np.concatenate((pre_eq, equalized, post_eq), axis=1)
