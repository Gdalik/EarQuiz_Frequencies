from PyQt6.QtWidgets import QWidget
from GUI.TransportPanel.audioslider_view import AudioSliderView
from GUI.TransportPanel.player_view import PlayerView
from Utilities.common_calcs import hhmmss


class TransportPanelView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.PlayerView = PlayerView(self.mw_view)
        self.AudioSliderView = AudioSliderView(self.mw_view.AudioSlider)
        self.Duration_Lab = mw_view.Duration_Lab
        self.Position_Lab = mw_view.Position_Lab
        self.SliceLenSpin = mw_view.SliceLenSpin
        self.setHeader()

    def setHeader(self, audio_name='No audio'):
        self.mw_view.TransportPanel.setWindowTitle(f'Transport Panel: {audio_name}')

    def noSongState(self):
        self.setHeader()
        self.AudioSliderView.SliceRegion.hide()
        self.AudioSliderView.CropRegion.hide()
        self.AudioSliderView.Cursor.hide()
        zero_time_str = hhmmss(0)
        self.Position_Lab.setText(zero_time_str)
        self.Duration_Lab.setText(zero_time_str)
