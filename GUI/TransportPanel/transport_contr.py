from PyQt6.QtCore import QObject
from GUI.TransportPanel.player_contr import PlayerContr


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

    @property
    def currentAudio(self):
        return self.parent.CurrentMode.CurrentAudio
