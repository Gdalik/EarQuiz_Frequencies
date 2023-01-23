from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import definitions
from GUI.MainWindow.mw_contr import MainWindowContr
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/App/Icons/Logo/EM_Logo.png"))
    app.setApplicationDisplayName(definitions.app_name)
    app.setApplicationName(definitions.app_name)
    mw = MainWindowContr()
    app.exec()

