import time
from PyQt6.QtGui import QIcon
from definitions import app, app_name, TEMP_AUDIO_DIR
from GUI.MainWindow.Contr.mw_contr import MainWindowContr
from PyQt6.QtCore import QTimer
from GUI.StartScreen import StartLogo
from tendo.singleton import SingleInstance
from multiprocessing import freeze_support
import shutil


def onAppAboutToQuit():
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)


if __name__ == '__main__':
    freeze_support()
    me = SingleInstance()
    StartLogo.show()
    time_a = time.time()
    app.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    app.setOrganizationDomain("earquiz.org")
    shutil.rmtree(TEMP_AUDIO_DIR, ignore_errors=True)
    mw = MainWindowContr()
    app.aboutToQuit.connect(onAppAboutToQuit)
    '''time_diff = time.time() - time_a
    show_time = max(0, int(2000 - time_diff * 1000))
    QTimer.singleShot(show_time, StartLogo.hide)'''
    app.exec()
