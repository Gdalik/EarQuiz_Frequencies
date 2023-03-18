import contextlib
import time

import numpy as np
from pedalboard.io import AudioFile
from definitions import SineWaveCalibrationPath
from pathlib import Path


def sine_gen(freq: int, length_s=5, samplerate=44100):
    frames = int(length_s * samplerate)
    samples = np.arange(frames) / samplerate
    signal = np.sin(2 * np.pi * freq * samples)
    signal = np.float32(signal)
    signal /= np.max(np.abs(signal), axis=0)
    signal.resize((1, frames))
    return signal


def silence_gen(length_s=1, samplerate=44100):
    return np.zeros((1, int(samplerate * length_s)))


def generateCalibrationSineTones():
    sil = silence_gen()
    sil_half = silence_gen(length_s=0.5)
    cs = np.concatenate((sil_half, sine_gen(1000), sil, sine_gen(10000), sil, sine_gen(100), sil,
                         sine_gen(15000), sil, sine_gen(40), sil_half), axis=1)
    cs = cs * 0.2
    Path.mkdir(Path(SineWaveCalibrationPath).parent, exist_ok=True)
    with contextlib.suppress(Exception):
        with AudioFile(SineWaveCalibrationPath, 'w', 44100, 1) as f:
            f.write(cs)
    if Path(SineWaveCalibrationPath).is_file():
        return SineWaveCalibrationPath
    else:
        return False
