from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon


class PlayerView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.upd_VolumeLab()
        self.mw_view.VolumeSlider.valueChanged.connect(self.upd_VolumeLab)
        self.setPlayerButtons()

    def upd_VolumeLab(self):
        self.mw_view.VolumePerc.setText(f'{self.mw_view.VolumeSlider.value()}%')

    def setPlayerButtons(self):
        self.mw_view.Player_PlayPause.setDefaultAction(self.mw_view.actionPlayPause)
        self.mw_view.Player_Stop.setDefaultAction(self.mw_view.actionStop)
        self.mw_view.Player_SkipBackw.setDefaultAction(self.mw_view.actionPrevious_Track)
        self.mw_view.Player_SkipForw.setDefaultAction(self.mw_view.actionNext_Track)
        self.mw_view.LoopButton.setDefaultAction(self.mw_view.actionLoop_Playback)
        self.setPlayPause2Play()

    def setPlayPause2Play(self):
        self.mw_view.actionPlayPause.setText("Play")
        icon = QIcon()
        icon.addFile(u"icons:Player/Actions-media-playback-start-icon.png", QSize(32, 32),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.mw_view.actionPlayPause.setIcon(icon)

    def setPlayPause2Pause(self):
        self.mw_view.actionPlayPause.setText("Pause")
        icon = QIcon()
        icon.addFile(u"icons:/Player/Actions-media-playback-pause-icon.png", QSize(32, 32),
                     QIcon.Mode.Normal, QIcon.State.Off)
        self.mw_view.actionPlayPause.setIcon(icon)
