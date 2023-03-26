from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt
from definitions import version


class StartScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        # logo = QPixmap("icons:/Logo/EarQuiz_Splash.png")
        logo = QPixmap(":/Logo/Icons/Logo/EarQuiz_Splash.png")
        self.setPixmap(logo)
        self.showMessage(f'Version {version}', Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom,
                         color=QColor('blue'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)