from PyQt6.QtCore import QObject
from GUI.TransportPanel.player_contr import PlayerContr
from Utilities.common_calcs import hhmmss


class TransportContr(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.TransportView = parent.mw_view.TransportPanelView
        self.PlayerContr = PlayerContr(self)

    def noSongState(self):
        self.TransportView.setHeader()
        self.TransportView.AudioSliderView.SliceRegion.hide()
        self.TransportView.AudioSliderView.CropRegion.hide()
        self.TransportView.AudioSliderView.Cursor.hide()
        zero_time_str = hhmmss(0)
        self.TransportView.Duration_Lab.setText(zero_time_str)
        self.TransportView.Position_Lab.setText(zero_time_str)

    def onLoadSourceAudio(self):
        if self.parent.CurrentMode.name != 'Preview':
            return
        self.TransportView.setHeader(self.PlayerContr.sourceAudioData())
        self.TransportView.Duration_Lab.setText(hhmmss(self.PlayerContr.duration()/1000))

    @property
    def currentAudio(self):
        return self.parent.CurrentMode.CurrentAudio
