from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QSplashScreen

from Model.get_version import version


class StartScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        logo = QPixmap(":/Logo/Icons/Logo/EarQuiz_Splash.png")
        self.setPixmap(logo)
        self.showMessage(f'v{version()}', Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop,
                         color=QColor('blue'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)


StartLogo = StartScreen()
