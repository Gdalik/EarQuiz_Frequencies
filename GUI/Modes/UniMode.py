import contextlib

from Model.audiodrill_gen import create_temp_wavefile
from pathlib import Path
from definitions import TEMP_AUDIO_DIR


class UniMode:
    def __init__(self, parent):     # parent: MainWindowContr
        self.TimeSettingsChangesEnabled = None
        self.name = 'Uni'
        self.view = parent.mw_view
        self.parent = parent
        self.parent.CurrentMode = self
        self.CurrentAudio = None
        self.playPause_toggleable = False
        self.view.setActionNextExerciseEnabled(False)
        self.enableTimeSettingsChanges(False)
        self.view.EqOnOffLab.hide()
        self.view.menuEQ_Bands_Playback_Order.setEnabled(True)
        self.setPlayerControls()
        self.view.SliceLenSpin.setEnabled(True)
        self.view.EQSetView.setEnabled(True)

    @property
    def currentAudioCursorStartPos(self):   # in sec
        return 0

    @property
    def proxyCursorPos(self):   # in sec
        return 0

    @property
    def sourceRangeStartTime(self):     # in sec
        return self.parent.SourceRange.starttime if self.parent.SourceRange else None

    @property
    def sourceRangeEndTime(self):   # in sec
        return self.parent.SourceRange.endtime if self.parent.SourceRange else None

    @property
    def currentAudioStartTime(self):    # in sec
        return 0

    @property
    def currentAudioEndTime(self):  # in sec
        return 0

    def setPlayerControls(self):
        self.view.actionPlayPause.setEnabled(True)
        self.view.actionStop.setEnabled(True)
        self.view.actionPrevious_Track.setEnabled(False)
        self.view.actionNext_Track.setEnabled(False)
        self.view.actionLoop_Playback.setEnabled(False)
        self.view.actionLoop_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setEnabled(False)

    def updateCurrentAudio(self):
        self.cleanTempAudio()
        self.CurrentAudio = create_temp_wavefile()

    def enableTimeSettingsChanges(self, arg: bool):
        self.view.TransportPanelView.AudioSliderView.Cursor.setMovable(arg)
        self.view.TransportPanelView.AudioSliderView.CropRegion.setMovable(arg)
        self.view.TransportPanelView.CropRegionTstr.setChangesEnabled(arg)
        self.TimeSettingsChangesEnabled = arg

    def generateDrill(self, **kwargs):
        pass

    def nextDrill(self, **kwargs):
        pass

    def playbackStoppedEnded(self):
        pass

    def oncePlayingStarted(self):
        pass

    def whilePlaying(self):
        pass

    def cleanTempAudio(self):
        with contextlib.suppress(AttributeError):
            if self.CurrentAudio is not None and Path(self.CurrentAudio).parent == Path(TEMP_AUDIO_DIR):
                Path(self.CurrentAudio).unlink(missing_ok=True)


