import os
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaDevices
from Model.AudioEngine.pinknoise_gen import generate_pinknoise


app_name = 'EarQuiz Frequencies'
ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
app = QApplication(sys.argv)
MediaDevices = QMediaDevices()
pinknoise = generate_pinknoise()
