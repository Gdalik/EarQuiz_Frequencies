from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtCore import Qt


class StartScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        logo = QPixmap("icons:/Logo/EarQuiz_Splash.png")
        self.setPixmap(logo)
        self.showMessage('Version 0.3.0', Qt.AlignmentFlag.AlignCenter, color=QColor('black'))