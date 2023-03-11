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
        self.playPause_toggleable = False
        self.view.setActionNextExerciseEnabled(False)
        self.view.NextExercise.setVisible(False)
        self.enableTimeSettingsChanges(False)
        self.view.EqOnOffLab.hide()
        self.view.menuEQ_Bands_Playback_Order.setEnabled(True)
        self.setPlayerControls()
        self.view.SliceLenSpin.setEnabled(True)
        self.view.EQSetView.setEnabled(True)
        self.view.TransportPanelView.AudioSliderView.SliceRegion.hide()
        self.parent.ExScore.showTestStatus()
        if self.sourceRangeStartTime is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.update_pos(self.sourceRangeStartTime)

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
        # self.parent.LoadedFilePath = self.parent.CurrentAudio
        # self.cleanTempAudio()
        self.parent.CurrentAudio = create_temp_wavefile()

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

    def acceptAnswer(self):
        pass

    def restart_test(self):
        pass

    def cleanTempAudio(self):
        with contextlib.suppress(AttributeError, PermissionError):
            print(f'{self.parent.LoadedFilePath=}')
            if self.parent.LoadedFilePath is not None and Path(self.parent.LoadedFilePath).parent == Path(TEMP_AUDIO_DIR):
                Path(self.parent.LoadedFilePath).unlink(missing_ok=True)


