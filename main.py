from PySide6.QtGui import QIcon
from definitions import app, app_name
from GUI.MainWindow.mw_contr import MainWindowContr
import sys


if __name__ == '__main__':

    app.setWindowIcon(QIcon(":/App/Icons/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    mw = MainWindowContr()
    app.exec()

