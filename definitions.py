import os
import sys
from PySide6.QtWidgets import QApplication


app_name = 'EarQuiz Frequencies'
ROOT_DIR = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
app = QApplication(sys.argv)