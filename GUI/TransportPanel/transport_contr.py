from PyQt6.QtCore import QObject
from GUI.TransportPanel.player_contr import PlayerContr
from Model.calc import optimal_range_length
from Utilities.common_calcs import hhmmss
from Model.AudioEngine.preview_audio import PreviewAudioCrop


class TransportContr(QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent    # parent: MainWindowContr
        self.TransportView = parent.mw_view.TransportPanelView
        self.PlayerContr = PlayerContr(self)
        self.PlayerContr.positionChanged.connect(lambda x: self.TransportView.AudioSliderView.Cursor.update_pos(int(x / 1000)))
        self.TransportView.AudioSliderView.CropRegion.sigRegionChanged.connect(self.onCropRegionChanged)
        self.TransportView.SliceLenSpin.valueChanged.connect(self.onSliceLenChanged)

    def onCropRegionChanged(self):
        if self.parent.SourceRange is None:
            return
        range = self.TransportView.AudioSliderView.CropRegion.getRegion()
        self.parent.SourceRange.blockSignals(True)
        self.parent.SourceRange.starttime = range[0] / 1000
        self.parent.SourceRange.endtime = range[1] / 1000
        self.parent.SourceRange.blockSignals(False)
        if range != self.parent.SourceRange.range:
            self.onSourceRangeChanged()

    def onLoadSourceAudio(self):
        if self.parent.CurrentMode.name != 'Preview':
            return
        self.TransportView.setHeader(self.PlayerContr.sourceAudioData())
        duration_s = self.PlayerContr.duration() / 1000
        self.TransportView.Duration_Lab.setText(hhmmss(duration_s))
        self.TransportView.AudioSliderView.setNewDataLength(duration_s)
        self.parent._setSourceRange()
        self.TransportView.AudioSliderView.Cursor.show()

    def onSourceRangeChanged(self):
        self.TransportView.AudioSliderView.CropRegion.blockSignals(True)
        self.TransportView.AudioSliderView.CropRegion.setValues(self.parent.SourceRange.starttime,
                                                                self.parent.SourceRange.endtime)
        self.TransportView.AudioSliderView.CropRegion.blockSignals(False)
        # print(f'{self.parent.SourceRange.starttime=} {self.parent.SourceRange.endtime=}')

    def onSliceLenChanged(self, value):
        if self.parent.SourceRange is None:
            return
        self.parent.SourceRange.slice_length = value
        self.TransportView.SliceLenSpin.setValue(self.parent.SourceRange.slice_length)

    def initCropRegion(self):
        self.onSourceRangeChanged()
        self.TransportView.AudioSliderView.CropRegion.show()

    @property
    def currentAudio(self):
        return self.parent.CurrentMode.CurrentAudio
