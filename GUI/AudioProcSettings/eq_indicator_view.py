#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from PyQt6.QtCore import Qt, QObject, QRect
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QPixmap, QColor
from GUI.MainWindow.View.dark_theme import green_color
from Utilities.common_calcs import eq_off_perc
import Model.AudioEngine.audio_proc_settings as aps
import platform


class EqOnOffIndicatorView(QObject):
    def __init__(self, IndicatorLabel: QLabel, EqOnPerc=aps.getEQOnTimePerc()):
        super().__init__()
        self.IndLab = IndicatorLabel
        if platform.system() != 'Darwin':
            self.IndLab.setMinimumWidth(385)
        self.EqOnPerc = EqOnPerc
        self.IndLab.setScaledContents(True)
        self.update(self.EqOnPerc)

    @property
    def w(self) -> int:
        return self.IndLab.width()

    @property
    def h(self) -> int:
        return self.IndLab.height()

    def update(self, EqOnPerc=aps.getEQOnTimePerc()):
        self.EqOnPerc = EqOnPerc
        canvas = QPixmap(self.w, self.h)
        canvas.fill(Qt.GlobalColor.gray)
        color = QColor(green_color())
        painter = QPainter(canvas)
        painter.setBrush(color)
        painter.drawRect(self.eqOnRect(EqOnPerc))
        painter.end()
        self.IndLab.setPixmap(canvas)

    def eqOnRect(self, EqOnPerc: int or float) -> QRect:
        return QRect(int(self.w * eq_off_perc(EqOnPerc) / 100), -5, int(self.w * EqOnPerc / 100) - 1, self.h + 5)
