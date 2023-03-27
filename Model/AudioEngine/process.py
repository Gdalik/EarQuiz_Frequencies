from pedalboard import PeakFilter, Pedalboard
from Model.calc import proc_unproc_len, rand_buffer, optimize_divider
import numpy as np
from Utilities.exceptions import InterruptedException


def eq_proc(cur_sample, samplerate: int, freq1: int or float, freq2=None, gain_depth=12, Q=1.41, proc_t_perc=40):
    # freq > 0 -- boost; freq < 0 -- cut
    args = [cur_sample, samplerate, freq1]
    kwargs = {'freq2': freq2, 'gain_depth': gain_depth, 'Q': Q, 'proc_t_perc': proc_t_perc}
    # return _rough_eq(*args, **kwargs) if gain_depth <= 3 else _smooth_eq(*args, **kwargs)
    return _rough_eq(*args, **kwargs)


def _eq_audio_parts(cur_sample, samplerate: int, proc_t_perc=40):   # -> pre_eq / to_eq / post_eq
    def sec2fr(sec: int or float):
        return int(samplerate * sec)
    cur_sample_length = cur_sample[0].size / samplerate
    proc_len, unproc_len = proc_unproc_len(cur_sample_length, proc_t_perc)
    proc_len_fr = sec2fr(proc_len)
    unproc_len_fr = sec2fr(unproc_len)
    return np.hsplit(cur_sample, [unproc_len_fr, unproc_len_fr + proc_len_fr])


def _pb_process(audio_sample: np.ndarray, chain: Pedalboard, samplerate: int or float):
    def _process(buffer_size: int = 8192):
        _processed = chain.process(audio_sample, samplerate, buffer_size=buffer_size, reset=True)
        return _processed
    processed = _process()
    while processed.size != audio_sample.size:
        processed = _process(buffer_size=rand_buffer())  # Solving possible buffering issues (see Pedalboard docs).
    return processed


def _smooth_eq(cur_sample: np.ndarray, samplerate: int, freq1: int or float,
               freq2=None, gain_depth=12, Q=1.41, proc_t_perc=40):
    def sec2fr(sec: int or float):
        return int(samplerate * sec)

    def fade_eq(audio_sample: np.ndarray, fade_mode='in'):
        equalized = np.empty((len(cur_sample), 0))
        eq1 = PeakFilter(cutoff_frequency_hz=abs(freq1), gain_db=0, q=Q)
        if freq2:
            eq2 = PeakFilter(cutoff_frequency_hz=abs(freq2), gain_db=0, q=Q)
        else:
            eq2 = None
        chain = Pedalboard([eq1, eq2])
        step_gain_depth = gain_depth % gain_step if fade_mode == 'in' else gain_depth - gain_depth % 2
        for i in range(int(fade_steps_num)):
            step_chunk = audio_sample[:, i * step_len_fr:(i + 1) * step_len_fr]
            step_gain_depth = step_gain_depth + gain_step if fade_mode == 'in' else step_gain_depth - gain_step
            eq1.gain_db = step_gain_depth * -1 if freq1 < 0 else step_gain_depth
            if eq2 is not None:
                eq2.gain_db = step_gain_depth * -1 if freq2 < 0 else step_gain_depth
            eq_chunk = _pb_process(step_chunk, chain, samplerate)
            equalized = np.concatenate((equalized, eq_chunk), axis=1)
        return equalized

    pre_eq, to_eq, post_eq = _eq_audio_parts(cur_sample, samplerate, proc_t_perc=proc_t_perc)

    #   each fade step is ±2-3dB
    gain_step = 1
    fade_steps_num = gain_depth // gain_step
    step_len_s = 0.01
    step_len_fr = sec2fr(step_len_s)
    fade_len_fr = sec2fr(step_len_s * fade_steps_num)

    fade_in_to_eq = to_eq[:, :fade_len_fr]
    body_to_eq = to_eq[:, fade_len_fr:to_eq[0].size - fade_len_fr]
    fade_out_to_eq = to_eq[:, to_eq[0].size - fade_len_fr:]

    fade_in_eq = fade_eq(fade_in_to_eq, fade_mode='in')
    fade_out_eq = fade_eq(fade_out_to_eq, fade_mode='out')

    # eq body
    peak_gain1 = gain_depth * -1 if freq1 < 0 else gain_depth
    eq1_b = PeakFilter(cutoff_frequency_hz=abs(freq1), gain_db=peak_gain1, q=Q)
    if freq2:
        peak_gain2 = gain_depth * -1 if freq2 < 0 else gain_depth
        eq2_b = PeakFilter(cutoff_frequency_hz=abs(freq2), gain_db=peak_gain2, q=Q)
    else:
        eq2_b = None
    chain = Pedalboard([eq1_b, eq2_b])
    body_eq = _pb_process(body_to_eq, chain, samplerate)

    equalized = np.concatenate((fade_in_eq, body_eq, fade_out_eq), axis=1)
    return np.concatenate((pre_eq, equalized, post_eq), axis=1)


def _rough_eq(cur_sample: np.ndarray, samplerate: int, freq1: int or float, freq2=None,
              gain_depth=12, Q=1.41, proc_t_perc=40):
    # freq > 0 -- boost; freq < 0 -- cut
    pre_eq, to_eq, post_eq = _eq_audio_parts(cur_sample, samplerate, proc_t_perc=proc_t_perc)
    gain = gain_depth * -1 if freq1 < 0 else gain_depth
    eq1 = PeakFilter(cutoff_frequency_hz=abs(freq1), gain_db=gain, q=Q)
    if freq2:
        gain2 = gain_depth * -1 if freq2 < 0 else gain_depth
        eq2 = PeakFilter(cutoff_frequency_hz=abs(freq2), gain_db=gain2, q=Q)
    else:
        eq2 = None
    chain = Pedalboard([eq1, eq2])
    equalized = _pb_process(to_eq, chain, samplerate)
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
        divider = optimize_divider(self.source[0].size, ref_div=min_div)
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
