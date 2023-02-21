import numpy as np


def spectrum_noise(spectrum_func, samples=1024, rate=44100):
    """
    make noise with a certain spectral density
    """
    freqs = np.fft.rfftfreq(samples, 1.0 / rate)  # real-fft frequencies (not the negative ones)
    spectrum = np.zeros_like(freqs, dtype='complex')  # make complex numbers for spectrum
    spectrum[1:] = spectrum_func(freqs[1:])  # get spectrum amplitude for all frequencies except f=0
    phases = np.random.uniform(0, 2*np.pi, len(freqs)-1)  # random phases for all frequencies except f=0
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
    pn = pn / max(abs(pn)) * 0.8
    pn.resize((1, 44100*length_s))
    return pn
