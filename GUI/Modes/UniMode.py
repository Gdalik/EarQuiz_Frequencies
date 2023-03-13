import contextlib
from Model.audiodrill_gen import create_temp_wavefile
from pathlib import Path
from definitions import TEMP_AUDIO_DIR
from PyQt6.QtCore import QTimer


class UniMode:
    def __init__(self, parent, contrEnabled=True):     # parent: MainWindowContr
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
        self.view.menuEQ_Bands_Playback_Order.setEnabled(contrEnabled)
        self.setPlayerControls()
        self.view.SliceLenSpin.setEnabled(contrEnabled)
        self.view.EQSetView.setEnabled(contrEnabled)
        self.parent.ExScore.showTestStatus()

    @property
    def currentAudioCursorStartPos(self):   # in sec
        if self.parent.ADGen is None or self.parent.ADGen.audiochunk.currentSliceRange is None:
            return self.sourceRangeStartTime or 0
        return self.parent.ADGen.audiochunk.currentSliceRange[0]

    @property
    def proxyCursorPos(self):   # in sec
        return self.parent.TransportContr.PlayerContr.position() / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0

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
        self.view.EqOnOffLab.setVisible(False)

    def oncePlayingStarted(self):
        self.view.EqOnOffLab.setVisible(True)
        QTimer.singleShot(200, self.updateSliceRegion)

    def whilePlaying(self):
        self.view.setEQStateIndicatorOn(self.parent.TransportContr.eqStateOnOff())

    def acceptAnswer(self):
        pass

    def restart_test(self):
        pass

    def cleanTempAudio(self):
        with contextlib.suppress(AttributeError, PermissionError):
            print(f'{self.parent.LoadedFilePath=}')
            if self.parent.LoadedFilePath is not None and Path(self.parent.LoadedFilePath).parent == Path(TEMP_AUDIO_DIR):
                Path(self.parent.LoadedFilePath).unlink(missing_ok=True)

    def showAudioCursor(self):
        if self.parent.CurrentAudio is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.show()

    def updateSliceRegion(self):
        pass



