import contextlib

from Model.AudioEngine.preview_audio import PreviewAudioCrop
from Model.calc import optimal_range_length
from Model.sourcerange_manager import SourceRangeManager
from definitions import SineWaveCalibrationFilename


class SourceRangeContr:  # parent: MainWindowContr
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
        srm = SourceRangeManager()
        range_params = srm.get(self.parent.LoadedFileHash) if self.parent.LoadedFileHash is not None else None
        if range_params is None:
            self.setOptimalSourceRange(reset=reset)
            return
        self.setSourceRange(range_params, reset=reset)

    def setSourceRange(self, params, reset=True):
        if reset:
            self.parent.SourceRange = PreviewAudioCrop(self.parent.SourceAudio.duration, params[0],
                                                       params[1],
                                                       params[2])
        else:
            self.parent.SourceRange.setStrictModeActive(True)
            self.parent.SourceRange.starttime, self.parent.SourceRange.endtime, _ = params
            self.parent.SourceRange.setStrictModeActive(False)

    def setOptimalSourceRange(self, reset=True):
        range_params = self._getOptSourceRangeParameters(reset=reset)
        if reset or self.parent.SourceRange is None:
            self.parent.SourceRange = PreviewAudioCrop(self.parent.SourceAudio.duration, range_params[0],
                                                       range_params[1], range_params[2])
        else:
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
        return 0, opt_length, slice_length

    def disconnectSourceRangeSig(self):
        with contextlib.suppress(AttributeError, TypeError):
            self.parent.SourceRange.rangeChanged.disconnect(self.TransportContr.onSourceRangeChanged)
            self.parent.SourceRange.sliceLengthChanged.disconnect(self.TransportContr.onSliceLenChanged)

    def savePrevSourceAudioRange(self):
        if self.parent.LoadedFileHash is None or self.parent.SourceAudio is None or self.parent.SourceRange is None:
            return
        srm = SourceRangeManager()
        srm.save(self.parent.LoadedFileHash, self.parent.SourceAudio.name, self.parent.SourceRange)
