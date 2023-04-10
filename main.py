import shutil
from multiprocessing import freeze_support
import platform
import os
from PyQt6.QtGui import QIcon
from tendo.singleton import SingleInstance

from GUI.MainWindow.Contr.mw_contr import MainWindowContr
from GUI.StartScreen import StartLogo
from definitions import app, app_name, TEMP_AUDIO_DIR


def delTempAudio():
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)


def setAudioBackend():
    if platform.system() == 'Windows':
        os.environ['QT_MEDIA_BACKEND'] = 'windows'


if __name__ == '__main__':
    freeze_support()
    me = SingleInstance()
    StartLogo.show()
    app.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    app.setOrganizationDomain("earquiz.org")
    setAudioBackend()
    delTempAudio()
    mw = MainWindowContr()
    app.aboutToQuit.connect(delTempAudio)
    app.exec()
