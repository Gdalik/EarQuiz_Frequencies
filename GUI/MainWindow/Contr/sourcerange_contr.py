import contextlib
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from definitions import SineWaveCalibrationFilename
from Model.calc import optimal_range_length


class SourceRangeContr:     # parent: MainWindowContr
    def __init__(self, parent):
        self.parent = parent
        self.TransportContr = self.parent.TransportContr
        self.mw_view = self.parent.mw_view

    def setInitSourceRangeView(self):
        self.disconnectSourceRangeSig()
        self.autoSetSourceRange()
        self.mw_view.TransportPanelView.CropRegionTstr.noAudioState(False)
        self.parent.SourceRange.rangeChanged.connect(self.TransportContr.onSourceRangeChanged)
        self.parent.SourceRange.sliceLengthChanged.connect(self.TransportContr.onSliceLenChanged)

    def autoSetSourceRange(self, reset=True):
        # TODO: Load Source Range + Slice length options if stored
        self.setOptimalSourceRange(reset)

    def setOptimalSourceRange(self, reset=True):
        range_params = self._getOptSourceRangeParameters(reset=reset)
        if reset:
            self.parent.SourceRange = PreviewAudioCrop(self.parent.SourceAudio.duration, range_params[0], range_params[1],
                                                range_params[2])
        elif self.parent.SourceRange is not None:
            self.parent.SourceRange.setStrictModeActive(True)
            self.parent.SourceRange.starttime = 0
            self.parent.SourceRange.endtime = range_params[1]
            self.parent.SourceRange.setStrictModeActive(False)
        self.parent.SourceRange.slice_length = range_params[2]

    def _getOptSourceRangeParameters(self, reset=True):
        duration = self.parent.SourceAudio.duration
        if self.parent.SourceAudio.name == SineWaveCalibrationFilename:
            slice_length = 10
        elif reset:
            slice_length = self.parent.CurrentSourceMode.default_slice_length
        else:
            slice_length = self.mw_view.TransportPanelView.SliceLenSpin.value()
        slice_length = int(min(duration, slice_length))
        opt_length = optimal_range_length(duration, slice_length)
        return (0, opt_length, slice_length)

    def disconnectSourceRangeSig(self):
        with contextlib.suppress(AttributeError, TypeError):
            self.parent.SourceRange.rangeChanged.disconnect(self.TransportContr.onSourceRangeChanged)
            self.parent.SourceRange.sliceLengthChanged.disconnect(self.TransportContr.onSliceLenChanged)