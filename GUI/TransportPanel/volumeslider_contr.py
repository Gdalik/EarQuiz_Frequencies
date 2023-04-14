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
