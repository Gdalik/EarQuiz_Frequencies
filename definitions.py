#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
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

import os
import platform
import sys
from PyQt6.QtCore import QSettings
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtWidgets import QApplication

app_name = 'EarQuiz Frequencies'

app = QApplication(sys.argv)
MediaDevices = QMediaDevices()
launch_files_onstart = sys.argv[1:] if len(sys.argv) > 1 else None
NativeAudioBackend = False

ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = ''
if platform.system() == 'Darwin':
    DATA_DIR = os.path.expanduser('~/Library/Application Support/EarQuiz/Frequencies')
elif platform.system() == 'Windows':
    DATA_DIR = os.path.normpath(os.path.join(os.path.expandvars('%AppData%'), 'EarQuiz', 'Frequencies'))
SETTINGS_PATH = os.path.normpath(os.path.join(DATA_DIR, 'config.ini'))
TEMP_AUDIO_DIR = os.path.normpath(os.path.join(DATA_DIR, 'temp_audio'))
CURRENT_PLAYLIST_PATH = os.path.normpath(os.path.join(DATA_DIR, 'Playlists', 'current.m3u8'))
os.makedirs(DATA_DIR, exist_ok=True)
USER_DOCS_DIR = os.path.normpath(os.path.expanduser('~/Documents/EarQuiz Frequencies'))
EXERCISE_DIR = os.path.normpath(os.path.join(USER_DOCS_DIR, 'Exercises'))
PLAYLIST_DIR = os.path.normpath(os.path.join(USER_DOCS_DIR, 'Playlists'))

SineWaveCalibrationFilename = '1kHz__10kHz__100Hz__15kHz__40Hz Sinus Tones.wav'
SineWaveCalibrationPath = os.path.normpath(os.path.join(DATA_DIR, 'Audio', SineWaveCalibrationFilename))

SourceRangeLib_DIR = os.path.normpath(os.path.join(DATA_DIR, 'SourceRangeLib'))

Settings = QSettings(SETTINGS_PATH, QSettings.Format.IniFormat)

PN = 'Pink noise'
