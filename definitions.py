import os
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
import platform


app_name = 'EarQuiz Frequencies'
version = '0.1.0'
ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
app = QApplication(sys.argv)
MediaDevices = QMediaDevices()
DATA_DIR = ''
if platform.system() == 'Darwin':
    DATA_DIR = os.path.expanduser('~/Library/Application Support/EarQuiz/Frequencies')
elif platform.system() == 'Windows':
    DATA_DIR = os.path.normpath(os.path.join(os.path.expandvars('%AppData%'), 'EarQuiz', 'Frequencies'))
TEMP_AUDIO_DIR = os.path.normpath(os.path.join(DATA_DIR, 'temp_audio'))
os.makedirs(DATA_DIR, exist_ok=True)
EXERCISE_DIR = os.path.normpath(os.path.expanduser('~/Documents/EarQuiz/Frequencies'))

SineWaveCalibrationFilename = '1kHz__10kHz__100Hz__15kHz__40Hz Sinus Tones.wav'
SineWaveCalibrationPath = os.path.normpath(os.path.join(DATA_DIR, 'Audio', SineWaveCalibrationFilename))

SourceRangeLib_DIR = os.path.normpath(os.path.join(DATA_DIR, 'SourceRangeLib'))
