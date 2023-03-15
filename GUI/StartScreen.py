from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap


class StartScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        logo = QPixmap("icons:/Logo/EarQuiz_Splash.png")
        self.setPixmap(logo)