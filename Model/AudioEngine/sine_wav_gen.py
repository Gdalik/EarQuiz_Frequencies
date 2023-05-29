#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

import contextlib
from pathlib import Path

import numpy as np
from pedalboard.io import AudioFile

from definitions import SineWaveCalibrationPath


def sine_gen(freq: int, length_s=5, samplerate=44100):
    frames = int(length_s * samplerate)
    samples = np.arange(frames) / samplerate
    signal = np.sin(2 * np.pi * freq * samples)
    signal = np.float32(signal)
    signal /= np.max(np.abs(signal), axis=0)
    signal.resize((1, frames))
    return signal


def silence_gen(length_s=1.0, samplerate=44100):
    return np.zeros((1, int(samplerate * length_s)))


def generateCalibrationSineTones():
    sil = silence_gen()
    cs = np.concatenate((sil, sine_gen(1000), sil, sine_gen(10000), sil, sine_gen(100), sil,
                         sine_gen(15000), sil, sine_gen(40)), axis=1)
    cs = cs * 0.2
    Path.mkdir(Path(SineWaveCalibrationPath).parent, parents=True, exist_ok=True)
    with contextlib.suppress(Exception):
        with AudioFile(SineWaveCalibrationPath, 'w', 44100, 1) as f:
            f.write(cs)
    if Path(SineWaveCalibrationPath).is_file():
        return SineWaveCalibrationPath
    else:
        return False
