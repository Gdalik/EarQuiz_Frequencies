from multiprocessing import freeze_support
import multiprocessing as mp
import shutil
import platform
import os
from tendo.singleton import SingleInstance
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
from GUI.MainWindow.Contr.mw_contr import MainWindowContr
from GUI.Misc.StartScreen import StartLogo
from definitions import app, app_name, TEMP_AUDIO_DIR


def delTempAudio():
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)


def setAudioBackend():
    if platform.system() == 'Windows':
        os.environ['QT_MEDIA_BACKEND'] = 'windows'
    elif platform.system() == 'Darwin':
        os.environ['QT_MEDIA_BACKEND'] = 'darwin'


if __name__ == '__main__':
    freeze_support()
    if platform.system() == 'Darwin':
        mp.set_start_method('fork')
    me = SingleInstance()
    QTimer.singleShot(0, StartLogo.show)
    app.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    app.setOrganizationDomain("earquiz.org")
    setAudioBackend()
    delTempAudio()
    mw = MainWindowContr()
    app.aboutToQuit.connect(delTempAudio)
    app.exec()
