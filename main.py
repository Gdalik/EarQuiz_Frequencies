from PyQt6.QtGui import QIcon
from definitions import app, app_name
from GUI.MainWindow.mw_contr import MainWindowContr
from PyQt6.QtCore import QDir
from tendo.singleton import SingleInstance
from multiprocessing import freeze_support


if __name__ == '__main__':
    freeze_support()
    QDir.addSearchPath('icons', 'GUI/Icons')
    me = SingleInstance()
    app.setWindowIcon(QIcon("icons:/Logo/EarQuiz_Icon.png"))
    app.setApplicationDisplayName(app_name)
    app.setApplicationName(app_name)
    mw = MainWindowContr()
    app.exec()

