from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import numpy as np
import pyqtgraph as pg


class TransportPanelView:
    """@DynamicAttrs"""
    def __init__(self, mw_view):
        for W in mw_view.dockWidgetContents.findChildren(QWidget):
            self.__setattr__(W.objectName(), W)
        self.upd_VolumeLab()
        self.VolumeSlider.valueChanged.connect(self.upd_VolumeLab)
        self.AudioSliderView = AudioSliderView(self.AudioSlider)

    def upd_VolumeLab(self):
        self.VolumePerc.setText(f'{self.VolumeSlider.value()}%')


class AudioSliderView:
    def __init__(self, parent, samplerate=44100, length=30, downsampling=10):
        self.parent = parent
        self.parent.setBackground('darkgray')
        self.parent.getPlotItem().hideAxis('left')
        self.parent.getPlotItem().hideAxis('bottom')
        self.parent.setMenuEnabled(False)
        self.parent.hideButtons()

        empty_range = np.zeros(int(samplerate*length/downsampling))
        maxPos = len(empty_range)

        self.hline = self.parent.plot(empty_range)
        self.hline.setDownsampling(method='subsample')
        self.hline.setPen(style=Qt.NoPen)
        self.GScene = self.hline.scene()
        self.ViewBox = self.hline.getViewBox()
        self.ViewBox.setLimits(xMin=0, xMax=maxPos, yMin=-1, yMax=1)
        self.ViewBox.setMouseEnabled(x=False, y=False)
        self.CropRegion = CropRegion(0, 30)
        self.CropRegion.setBounds([0, maxPos])
        self.parent.addItem(self.CropRegion)
        self.SliceRegion = SliceRegion(10, 20)
        self.parent.addItem(self.SliceRegion)
        self.SliceRegion.show()
        self.Cursor = AudioCursor(self)
        self.parent.addItem(self.Cursor)
        self.Cursor.show()
        self.Cursor.update_pos(10)


class AudioCursor(pg.InfiniteLine):
    def __init__(self, parent, samplerate=44100, downsampling=10):
        super().__init__(movable=True)
        self.setAngle(90)
        self.hide()
        self.setPos(0)
        self.parent = parent
        self.samplerate = samplerate
        self.downsampling = downsampling

    def update_pos(self, s):
        self.setPos(int(s*self.samplerate/self.downsampling))

    def show(self):
        self.setPen(style=Qt.SolidLine, color='red', width=8)
        self.setHoverPen(style=Qt.SolidLine, color='darkred', width=8)

    def hide(self):
        self.setPen(style=Qt.NoPen)


class CropRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float, samplerate=44100, downsampling=10):
        super().__init__(pen=pg.mkPen('k'), hoverPen=pg.mkPen('blue', width=3), swapMode='block')
        self.samplerate = samplerate
        self.downsampling = downsampling
        self.a_pos_samp = int(a_pos*self.samplerate/self.downsampling)
        self.b_pos_samp = int(b_pos*self.samplerate/self.downsampling)
        self.setRegion([self.a_pos_samp, self.b_pos_samp])
        self.setBrush(pg.mkBrush(color='w'))
        self.setHoverBrush(pg.mkBrush(color='w'))

class SliceRegion(pg.LinearRegionItem):
    def __init__(self, a_pos: int or float, b_pos: int or float, samplerate=44100, downsampling=10):
        self.TranspColor = QColor(0, 255, 255, 0)
        super().__init__(pen=pg.mkPen(self.TranspColor, width=0), swapMode='block', movable=False)
        self.samplerate = samplerate
        self.downsampling = downsampling
        self.a_pos_samp = int(a_pos*self.samplerate/self.downsampling)
        self.b_pos_samp = int(b_pos*self.samplerate/self.downsampling)
        self.setRegion([self.a_pos_samp, self.b_pos_samp])
        self.brushColor = QColor(0, 255, 255, 65)
        self.setHoverBrush(pg.mkBrush(self.brushColor))
        self.hide()

    def show(self):
        self.setBrush(pg.mkBrush(color=self.brushColor))

    def hide(self):
        self.setBrush(pg.mkBrush(color=self.TranspColor))
