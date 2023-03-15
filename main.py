from PyQt6.QtGui import QIcon
from definitions import app, app_name, TEMP_AUDIO_DIR
from GUI.MainWindow.mw_contr import MainWindowContr
from GUI.StartScreen import StartScreen
from PyQt6.QtCore import QDir
from tendo.singleton import SingleInstance
from multiprocessing import freeze_support
import shutil


def onAppAboutToQuit():
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)


if __name__ == '__main__':
    freeze_support()
    QDir.addSearchPath('icons', 'GUI/Icons')
    me = SingleInstance()
    app.setWindowIcon(QIcon("icons:/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    StartLogo = StartScreen()
    StartLogo.show()
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)
    mw = MainWindowContr()
    app.aboutToQuit.connect(onAppAboutToQuit)
    StartLogo.hide()
    app.exec()
