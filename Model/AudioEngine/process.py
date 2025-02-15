#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from pedalboard import PeakFilter, Pedalboard
import Model.AudioEngine.audio_proc_settings as APS
from Model.calc import proc_unproc_len, rand_buffer


def eq_proc(cur_sample, samplerate: int, freq1: int or float, freq2=None,
            gain_depth=12, Q=1.41, proc_t_perc=APS.getEQOnTimePerc()):
    def sec2fr(sec: int or float):
        return int(samplerate * sec)

    eq_transition_len_s = APS.getEQTransitionDur()
    fade_inout_len_s = APS.getExFadeInOutDur()

    pre_eq, to_eq, post_eq = _eq_audio_parts(cur_sample, samplerate, proc_t_perc=proc_t_perc)
    gain = gain_depth * -1 if freq1 < 0 else gain_depth
    eq1 = PeakFilter(cutoff_frequency_hz=abs(freq1), gain_db=gain, q=Q)
    if freq2:
        gain2 = gain_depth * -1 if freq2 < 0 else gain_depth
        eq2 = PeakFilter(cutoff_frequency_hz=abs(freq2), gain_db=gain2, q=Q)
    else:
        eq2 = None
    chain = Pedalboard([eq1, eq2])

    crossfade_len_fr = sec2fr(eq_transition_len_s)
    fade_inout_len_fr = sec2fr(fade_inout_len_s)

    equalized = _pb_process(to_eq, chain, samplerate)

    if proc_t_perc < 100:
        pre_eq = pre_eq * fadeInCurveGen(pre_eq[0].size, fade_inout_len_fr)
        post_eq = post_eq * fadeOutCurveGen(post_eq[0].size, fade_inout_len_fr)
        eq_in_curve = eqGainCurveGen(0, 1, to_eq[0].size, crossfade_len_fr)
        eq_out_curve = eqGainCurveGen(1, 0, to_eq[0].size, crossfade_len_fr)
        eq_proc_in = equalized * eq_in_curve
        eq_unproc_out = to_eq * eq_out_curve
        equalized = eq_proc_in + eq_unproc_out
        concat = np.concatenate((pre_eq, equalized, post_eq), axis=1)
    else:
        concat = equalized * fadeInCurveGen(equalized[0].size, fade_inout_len_fr) * \
                fadeOutCurveGen(to_eq[0].size, fade_inout_len_fr)
    return concat


def _eq_audio_parts(cur_sample: np.ndarray, samplerate: int,
                    proc_t_perc=APS.getEQOnTimePerc()):  # -> pre_eq / to_eq / post_eq
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


def eqGainCurveGen(value1: int or float, value2: int or float, duration_fr: int, trans_len_fr: int):
    start = np.linspace(value1, value2, trans_len_fr)
    end = np.linspace(value2, value1, trans_len_fr)
    body = np.ndarray((duration_fr - trans_len_fr * 2, ))
    body.fill(value2)
    return np.concatenate((start, body, end))


def fadeInCurveGen(duration_fr: int, fade_in_len_fr: int):
    fade_in_len_fr = min(duration_fr, fade_in_len_fr)
    start = np.linspace(0, 1, fade_in_len_fr)
    body = np.ndarray((duration_fr - fade_in_len_fr, ))
    body.fill(1)
    return np.concatenate((start, body))


def fadeOutCurveGen(duration_fr: int, fade_out_len_fr: int):
    fade_out_len_fr = min(duration_fr, fade_out_len_fr)
    body = np.ndarray((duration_fr - fade_out_len_fr, ))
    body.fill(1)
    end = np.linspace(1, 0, fade_out_len_fr)
    return np.concatenate((body, end))
