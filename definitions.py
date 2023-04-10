import os
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtCore import QSettings
import platform


app_name = 'EarQuiz Frequencies'
version = '0.1.0'

app = QApplication(sys.argv)
MediaDevices = QMediaDevices()

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
