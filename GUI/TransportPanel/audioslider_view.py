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

import numpy as np
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class AudioSliderView:
    def __init__(self, parent, length=30):
        self.parent = parent  # parent: TransportPanelView
        self.setCommonView()

        self.audioLength = length
        self.data_arr = self.genData()

        self.GScene = self.ViewBox = self.CropRegion = self.SliceRegion = self.Cursor = None
        self.initSliderBox()
        self.initCropRegion()
        self.initSliceRegion()
        self.initCursor()

    def setCommonView(self):
        self.parent.setBackground('darkgray')
        self.parent.getPlotItem().hideAxis('left')
        self.parent.getPlotItem().hideAxis('bottom')
        self.parent.setMenuEnabled(False)
        self.parent.hideButtons()

    def initSliderBox(self):
        self._hline_draw()
        self.GScene = self.hline.scene()
        self.ViewBox = self.hline.getViewBox()
        self.ViewBox.setLimits(xMin=0, xMax=self.data_arr.size, yMin=-1, yMax=1)
        self.ViewBox.setMouseEnabled(x=False, y=False)

    def initCropRegion(self):
        self.CropRegion = CropRegion(0, 0)
        self.parent.addItem(self.CropRegion)

    def initSliceRegion(self):
        self.SliceRegion = SliceRegion(0, 0)
        self.parent.addItem(self.SliceRegion)

    def initCursor(self):
        self.Cursor = AudioCursor(self)
        self.parent.addItem(self.Cursor)

    def setNewDataLength(self, length: int or float):
        self.audioLength = length
        self.data_arr = self.genData()
        self.hline.setData([])
        self._hline_draw()
        self.ViewBox.setLimits(xMin=0, xMax=self.data_arr.size, yMin=-1, yMax=1)

    def _hline_draw(self):
        self.hline = self.parent.plot(self.data_arr)
        self.hline.setPen(style=Qt.PenStyle.NoPen)
        self.hline.setDownsampling(method='subsample')

    def genData(self):
        return np.zeros(int(self.audioLength * 1000))


class AudioCursor(pg.InfiniteLine):
    def __init__(self, parent):  # parent: AudioSliderView
        super().__init__(movable=False)
        self.showEnabled(True)
        self.setHoverPen(style=Qt.PenStyle.SolidLine, color='darkred', width=8)
        self.setAngle(90)
        self.setPos(0)
        self.parent = parent
        self.hide()

    def update_pos(self, s):
        self.blockSignals(True)
        self.setPos(int(s * 1000))
        self.blockSignals(False)

    def showEnabled(self, arg: bool):
        if arg:
            self.setPen(style=Qt.PenStyle.SolidLine, color='red', width=8)
        else:
            self.setPen(style=Qt.PenStyle.SolidLine, color=QColor(170, 85, 85), width=8)


class CropRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        super().__init__(pen=pg.mkPen('k'), hoverPen=pg.mkPen('blue', width=3), swapMode='block')
        self.setValues(a_pos, b_pos)
        brush = pg.mkBrush(color='w')
        self.setBrush(brush)
        self.setHoverBrush(brush)
        self.hide()

    def setValues(self, a_pos, b_pos):
        self.blockSignals(True)
        self.setRegion((int(a_pos * 1000), int(b_pos * 1000)))
        self.blockSignals(False)


class SliceRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        brushColor = QColor(0, 255, 255, 65)
        super().__init__(pen=pg.mkPen(brushColor, width=0), swapMode='block', movable=False)
        brush = pg.mkBrush(brushColor)
        self.setBrush(brush)
        self.setHoverBrush(brush)
        self.setValues(a_pos, b_pos)
        self.hide()

    def setValues(self, a_pos, b_pos):
        self.setRegion((int(a_pos * 1000), int(b_pos * 1000)))
