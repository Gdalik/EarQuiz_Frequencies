from PyQt6.QtWidgets import QWidget
from GUI.TransportPanel.audioslider_view import AudioSliderView
from GUI.TransportPanel.player_view import PlayerView


class TransportPanelView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.PlayerView = PlayerView(self.mw_view)
        self.AudioSliderView = AudioSliderView(self.mw_view.AudioSlider)
        self.setHeader()

    def setHeader(self, audio_name='No audio'):
        self.mw_view.TransportPanel.setWindowTitle(f'Transport Panel: {audio_name}')
