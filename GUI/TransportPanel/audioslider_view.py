import numpy as np
import pyqtgraph as pg
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class AudioSliderView:
    def __init__(self, parent, length=30):
        self.parent = parent    # parent: TransportPanelView
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
        self.CropRegion.setBounds([0, self.data_arr.size])
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
        bounds = [0, self.data_arr.size]
        self.CropRegion.setBounds(bounds)
        self.Cursor.setBounds(bounds)

    def _hline_draw(self):
        self.hline = self.parent.plot(self.data_arr)
        self.hline.setPen(style=Qt.PenStyle.NoPen)
        self.hline.setDownsampling(method='subsample')

    def genData(self):
        return np.zeros(int(self.audioLength * 1000))


class AudioCursor(pg.InfiniteLine):
    def __init__(self, parent):
        super().__init__(movable=False)
        self.setPen(style=Qt.PenStyle.SolidLine, color='red', width=8)
        self.setHoverPen(style=Qt.PenStyle.SolidLine, color='darkred', width=8)
        self.setAngle(90)
        self.setPos(0)
        self.parent = parent
        self.hide()

    def update_pos(self, s):
        self.setPos(int(s*1000))


class CropRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        super().__init__(pen=pg.mkPen('k'), hoverPen=pg.mkPen('blue', width=3), swapMode='block')
        self.setValues(a_pos, b_pos)
        self.setBrush(pg.mkBrush(color='w'))
        self.setHoverBrush(pg.mkBrush(color='w'))
        self.hide()

    def setValues(self, a_pos, b_pos):
        print(f'{a_pos=} {b_pos=}')
        self.setRegion((a_pos * 1000, b_pos * 1000))


class SliceRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float):
        self.brushColor = QColor(0, 255, 255, 65)
        super().__init__(pen=pg.mkPen(self.brushColor, width=0), swapMode='block', movable=False)
        self.setBrush(pg.mkBrush(self.brushColor))
        self.setHoverBrush(pg.mkBrush(self.brushColor))
        self.setValues(a_pos, b_pos)
        self.hide()

    def setValues(self, a_pos, b_pos):
        self.setRegion((int(a_pos * 1000), int(b_pos * 1000)))
