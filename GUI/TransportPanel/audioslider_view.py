import numpy as np
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class AudioSliderView:
    def __init__(self, parent, length=30):
        self.parent = parent
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
        self.CropRegion = CropRegion(0, 30)
        self.CropRegion.setBounds([0, self.data_arr.size])
        self.parent.addItem(self.CropRegion)

    def initSliceRegion(self):
        self.SliceRegion = SliceRegion(0, 0)
        self.parent.addItem(self.SliceRegion)

    def initCursor(self):
        self.Cursor = AudioCursor(self)
        self.parent.addItem(self.Cursor)

    def setNewDataLength(self, length: int):
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
    def __init__(self, parent):
        super().__init__(movable=True)
        self._isShown = None
        self.setAngle(90)
        self.hide()
        self.setPos(0)
        self.parent = parent

    def update_pos(self, s):
        self.setPos(int(s*1000))

    def show(self):
        self.setPen(style=Qt.PenStyle.SolidLine, color='red', width=8)
        self.setHoverPen(style=Qt.PenStyle.SolidLine, color='darkred', width=8)
        self._isShown = True

    def hide(self):
        self.setPen(style=Qt.PenStyle.NoPen)
        self.setMovable(False)
        self._isShown = False

    def isShown(self):
        return self._isShown


class CropRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        super().__init__(pen=pg.mkPen('k'), hoverPen=pg.mkPen('blue', width=3), swapMode='block')
        self.a_pos_samp = int(a_pos*1000)
        self.b_pos_samp = int(b_pos*1000)
        self.setRegion([self.a_pos_samp, self.b_pos_samp])
        self.setBrush(pg.mkBrush(color='w'))
        self.setHoverBrush(pg.mkBrush(color='w'))


class SliceRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        self._isShown = None
        self.TranspColor = QColor(0, 255, 255, 0)
        super().__init__(pen=pg.mkPen(self.TranspColor, width=0), swapMode='block', movable=False)
        self.a_pos_samp = int(a_pos*1000)
        self.b_pos_samp = int(b_pos*1000)
        self.setRegion([self.a_pos_samp, self.b_pos_samp])
        self.brushColor = QColor(0, 255, 255, 65)
        self.setHoverBrush(pg.mkBrush(self.brushColor))
        self.hide()

    def show(self):
        self.setBrush(pg.mkBrush(color=self.brushColor))
        self._isShown = True

    def hide(self):
        self.setBrush(pg.mkBrush(color=self.TranspColor))
        self._isShown = False

    def isShown(self):
        return self._isShown
