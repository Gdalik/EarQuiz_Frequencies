#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QSplashScreen
from Model.get_version import version
from GUI.MainWindow.View.dark_theme import blue_color
import multiprocessing as mp


class StartScreen(QSplashScreen):
    def __init__(self):
        super().__init__()
        logo = QPixmap(":/Logo/Icons/Logo/EarQuiz_Splash.png")
        self.setPixmap(logo)
        self.showMessage(f'v{version()}', Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop,
                         color=QColor(f'{blue_color()}'))
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)


StartLogo = StartScreen()
StartLogoTime = 1000
