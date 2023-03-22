from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import math


class PlayerView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.setPlayerButtons()

    def upd_VolumeLevelLab(self, value: float):
        try:
            level_db = round(20 * math.log10(value), 1)
        except ValueError:
            level_db = '-∞'

        self.mw_view.VolumeLevelLab.setText(f'{self.mw_view.VolumeSlider.value()}% ({level_db}dB)')

    def setPlayerButtons(self):
        self.mw_view.Player_PlayPause.setDefaultAction(self.mw_view.actionPlayPause)
        self.mw_view.Player_Stop.setDefaultAction(self.mw_view.actionStop)
        self.mw_view.Player_SkipBackw.setDefaultAction(self.mw_view.actionPrevious_Track)
        self.mw_view.Player_SkipForw.setDefaultAction(self.mw_view.actionNext_Track)
        self.mw_view.LoopButton.setDefaultAction(self.mw_view.actionLoop_Playback)
        self.mw_view.SequencePlayBut.setDefaultAction(self.mw_view.actionSequential_Playback)
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

    @staticmethod
    def pb_state2str(state):
        return str(state).split('.')[1].replace('State', '')
