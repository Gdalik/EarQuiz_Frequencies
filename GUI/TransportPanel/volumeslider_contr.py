#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

from PyQt6.QtWidgets import QMenu
from PyQt6.QtMultimedia import QAudio


class VolumeSliderContr():
    VolumeSliderContextMenu: QMenu

    def __init__(self, parent):  # parent: PlayerContr
        self.parent = parent
        self.mw_view = parent.mw_view
        self.VolumeSlider = parent.VolumeSlider
        self.savedVolume = None
        self.mw_view.actionIncrease_Volume.triggered.connect(self.increaseVolume)
        self.mw_view.actionDecrease_Volume.triggered.connect(self.decreaseVolume)
        self.mw_view.actionSave_Volume_Level.triggered.connect(self.onSaveVolumeTriggered)
        self.mw_view.actionRestore_Volume_Level.triggered.connect(self.onRestoreVolumeTriggered)
        self.mw_view.actionRestore_Volume_Level.setEnabled(False)
        self._createContextMenu()
        self.VolumeSlider.valueChanged.connect(self.applyVolume)
        self.VolumeSlider.customContextMenuRequested.connect(self.onVolumeCustomContextMenuRequested)

    def increaseVolume(self):
        self.VolumeSlider.setValue(self.mw_view.VolumeSlider.value() + 5)

    def decreaseVolume(self):
        self.VolumeSlider.setValue(self.mw_view.VolumeSlider.value() - 5)

    def applyVolume(self, volumeSliderValue):
        linearVolume = QAudio.convertVolume(volumeSliderValue / 100,
                                            QAudio.VolumeScale.LogarithmicVolumeScale,
                                            QAudio.VolumeScale.LinearVolumeScale)
        self.parent.audioOutput.setVolume(linearVolume)

    def _createContextMenu(self):
        self.VolumeSliderContextMenu = QMenu()
        self.VolumeSliderContextMenu.addActions((self.mw_view.actionSave_Volume_Level,
                                                 self.mw_view.actionRestore_Volume_Level))

    def onVolumeCustomContextMenuRequested(self, pos):
        self.VolumeSliderContextMenu.exec(self.VolumeSlider.mapToGlobal(pos))

    def onSaveVolumeTriggered(self):
        self.savedVolume = self.parent.VolumeSlider.value()
        self.mw_view.actionRestore_Volume_Level.setEnabled(True)

    def onRestoreVolumeTriggered(self):
        if self.savedVolume is None:
            return
        self.parent.VolumeSlider.setValue(self.savedVolume)
