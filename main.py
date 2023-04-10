import time
from PyQt6.QtGui import QIcon
from definitions import app, app_name, TEMP_AUDIO_DIR
from GUI.MainWindow.Contr.mw_contr import MainWindowContr
from GUI.StartScreen import StartLogo
from tendo.singleton import SingleInstance
from multiprocessing import freeze_support
import shutil


def delTempAudio():
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)


if __name__ == '__main__':
    freeze_support()
    me = SingleInstance()
    StartLogo.show()
    app.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    app.setOrganizationDomain("earquiz.org")
    delTempAudio()
    mw = MainWindowContr()
    app.aboutToQuit.connect(delTempAudio)
    app.exec()
