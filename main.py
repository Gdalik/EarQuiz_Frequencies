from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from Control.WinContr.mw_contr import MainWindowContr
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/App/Icons/Logo/EM_Logo.png"))
    mw = MainWindowContr()
    app.exec()
