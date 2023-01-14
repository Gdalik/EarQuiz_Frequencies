from PySide6.QtWidgets import QMainWindow
from View.mainwindow import Ui_MainWindow


class MainWindowContr(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
