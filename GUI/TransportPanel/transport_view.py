from GUI.TransportPanel.audioslider_view import AudioSliderView
from GUI.TransportPanel.player_view import PlayerView
from GUI.TransportPanel.cropregiontimestr import CropRegionTimestr
from Utilities.common_calcs import hhmmss


class TransportPanelView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.PlayerView = PlayerView(self.mw_view)
        self.AudioSliderView = AudioSliderView(self.mw_view.AudioSlider)
        self.Duration_Lab = mw_view.Duration_Lab
        self.Position_Lab = mw_view.Position_Lab
        self.SliceLenSpin = mw_view.SliceLenSpin
        self.SlicesNum_Lab = mw_view.SlicesNum_Lab
        self.StartTimeEdit = mw_view.StartTimeEdit
        self.EndTimeEdit = mw_view.EndTimeEdit
        self.StartPointBut = mw_view.StartPointBut
        self.EndPointBut = mw_view.EndPointBut
        self.RangeToStart = mw_view.RangeToStart
        self.RangeToEnd = mw_view.RangeToEnd
        self.ClearRangeBut = mw_view.ClearRangeBut
        self.CropRegionTstr = CropRegionTimestr(self)
        self.SaveSliceLengthAsDefault = mw_view.SaveSliceLengthAsDefault
        self.setHeader()

    def setHeader(self, audio_name='No audio'):
        self.mw_view.TransportPanel.setWindowTitle(f'Transport Panel: {audio_name}')

    def setSlicesNum(self, value: int):
        self.SlicesNum_Lab.setText(f'Number of Slices: {value}')

    def noSongState(self):
        self.setHeader()
        self.AudioSliderView.SliceRegion.hide()
        self.AudioSliderView.CropRegion.hide()
        self.AudioSliderView.Cursor.hide()
        self.CropRegionTstr.noAudioState(True)
        zero_time_str = hhmmss(0)
        self.Position_Lab.setText(zero_time_str)
        self.Duration_Lab.setText(zero_time_str)
        self.setSlicesNum(0)

    def setDurationLabValue(self, value: int or float):  # value in sec
        self.Duration_Lab.setText(hhmmss(value))

    def setPositionLabValue(self, value: int or float):  # value in sec
        self.Position_Lab.setText(hhmmss(value))
