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

#   The 'spectrum_noise' and 'pink_spectrum' functions were taken from:
#   https://www.socsci.ru.nl/wilberth/python/noise.html
#   Copyright (C) 2012-2023 Wilbert van Ham, Stichting Katholieke Universiteit, KVK 41055629, Nijmegen
#   License: General Public License version 3 or later.


import numpy as np


def spectrum_noise(spectrum_func, samples=1024, rate=44100):
    """
    make noise with a certain spectral density
    """
    freqs = np.fft.rfftfreq(samples, 1.0 / rate)  # real-fft frequencies (not the negative ones)
    spectrum = np.zeros_like(freqs, dtype='complex')  # make complex numbers for spectrum
    spectrum[1:] = spectrum_func(freqs[1:])  # get spectrum amplitude for all frequencies except f=0
    phases = np.random.uniform(0, 2 * np.pi, len(freqs) - 1)  # random phases for all frequencies except f=0
    spectrum[1:] *= np.exp(1j * phases)  # apply random phases
    noise = np.fft.irfft(spectrum)  # return the reverse fourier transform
    noise = np.pad(noise, (0, samples - len(noise)), 'constant')  # add zero for odd number of input samples

    return noise


def pink_spectrum(f, f_min=0, f_max=np.inf, att=np.log10(2.0) * 10):
    """
    Define a pink (1/f) spectrum
        f     = array of frequencies
        f_min = minimum frequency for band pass
        f_max = maximum frequency for band pass
        att   = attenuation per factor two in frequency in decibel.
                Default is such that a factor two in frequency increase gives a factor two in power attenuation.
    """
    # numbers in the equation below explained:
    #  0.5: take the square root of the power spectrum so that we get an amplitude (field) spectrum
    # 10.0: convert attenuation from decibel to bel
    #  2.0: frequency factor for which the attenuation is given (octave)
    s = f ** -(0.5 * (att / 10.0) / np.log10(2.0))  # apply attenuation
    s[np.logical_or(f < f_min, f > f_max)] = 0  # apply band pass
    return s


def generate_pinknoise(length_s=30):
    pn = spectrum_noise(lambda x: pink_spectrum(x, 20, 20000), samples=44100 * length_s)
    pn = pn / max(abs(pn)) * 0.8  # adjusting gain level
    pn.resize((1, 44100 * length_s))  # resizing/reshaping array to fit pedalboard requirements
    return pn
