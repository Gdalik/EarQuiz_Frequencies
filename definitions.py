import os
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
from Model.AudioEngine.pinknoise_gen import generate_pinknoise
import platform


app_name = 'EarQuiz Frequencies'
version = '0.1.0'
ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
app = QApplication(sys.argv)
MediaDevices = QMediaDevices()
pinknoise = generate_pinknoise()
DATA_DIR = ''
if platform.system() == 'Darwin':
    DATA_DIR = os.path.expanduser('~/Library/Application Support/EarQuiz/Frequencies')
elif platform.system() == 'Windows':
    DATA_DIR = os.path.normpath(os.path.join(os.path.expandvars('%AppData%'), 'EarQuiz', 'Frequencies'))
TEMP_AUDIO_DIR = os.path.normpath(os.path.join(DATA_DIR, 'temp_audio'))
os.makedirs(DATA_DIR, exist_ok=True)

MinAudioDuration = 10   # in sec
PinknoiseLength = 30    # in sec

SineWaveCalibrationFilename = '1kHz 10kHz 100Hz 15kHz 40Hz Sinus Tones.wav'
SineWaveCalibrationPath = os.path.normpath(os.path.join(DATA_DIR, 'Audio', SineWaveCalibrationFilename))