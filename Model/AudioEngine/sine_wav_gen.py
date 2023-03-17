import numpy as np
from pedalboard.io import AudioFile


def sine_gen(freq: int, length_s=5, samplerate=44100):
    samples = np.arange(length_s * samplerate) / samplerate
    signal = np.sin(2 * np.pi * freq * samples)
    signal = np.float32(signal)
    signal /= np.max(np.abs(signal), axis=0)
    signal.resize((1, 44100*length_s))
    return signal


def silence_gen(length_s=1, samplerate=44100):
    return np.zeros((1, samplerate*length_s))


sil = silence_gen()
cs = np.concatenate((sil, sine_gen(1000), sil, sine_gen(10000), sil, sine_gen(100), sil,
                     sine_gen(15000), sil, sine_gen(40)), axis=1)
cs = cs * 0.2

with AudioFile('1kHz 10kHz 100Hz 15kHz 40Hz Sinus Tones.wav', 'w', 44100, 1) as f:
    f.write(cs)
