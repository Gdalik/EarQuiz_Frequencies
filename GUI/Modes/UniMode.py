import contextlib
import time

from Model.audiodrill_gen import create_temp_wavefile
from pathlib import Path
from definitions import TEMP_AUDIO_DIR
from PyQt6.QtCore import QTimer


class UniMode:
    def __init__(self, parent, contrEnabled=True, setPlayerContr=True):     # parent: MainWindowContr
        self.TimeSettingsChangesEnabled = None
        self.name = 'Uni'
        self.view = parent.mw_view
        self.parent = parent
        self.parent.CurrentMode = self
        self.playPause_toggleable = False
        self.parent.TransportContr.CursorBeingDragged = False
        # True CursorBeingDragged value, caused by previous Audio Cursor position change, may result in further
        # glitches.
        self.view.setActionNextExampleEnabled(False)
        self.view.NextExample.setVisible(False)
        self.enableTimeSettingsChanges(False)
        self.view.EqOnOffLab.hide()
        self.setEQBandsOrderMenuVisible(contrEnabled)
        if setPlayerContr:
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
        self.view.actionPrevious_Track.setVisible(False)
        self.view.actionNext_Track.setEnabled(False)
        self.view.actionNext_Track.setVisible(False)
        self.view.actionSkip_Unavailable_Tracks.setVisible(False)
        self.view.actionLoop_Playback.setVisible(False)
        self.view.actionLoop_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setVisible(False)
        self.view.LoopButton.setVisible(False)
        self.view.Player_SkipBackw.setVisible(False)
        self.view.Player_SkipForw.setVisible(False)

    def updateCurrentAudio(self):
        self.parent.CurrentAudio = create_temp_wavefile()

    def enableTimeSettingsChanges(self, arg: bool):
        self.view.TransportPanelView.AudioSliderView.Cursor.setMovable(arg)
        self.view.TransportPanelView.AudioSliderView.CropRegion.setMovable(arg)
        self.view.TransportPanelView.CropRegionTstr.setChangesEnabled(arg)
        self.TimeSettingsChangesEnabled = arg

    def generateDrill(self, **kwargs):
        pass

    def nextDrill(self, **kwargs):      # The case when test is complete, and user changes EQ pattern
        self.parent.TransportContr.PlayerContr.clearSource()
        self.cleanTempAudio()
        self.parent.ExScore.refresh(onlyLastExcInfo=True)

    def playbackStoppedEnded(self):
        self.view.EqOnOffLab.setVisible(False)

    def playbackEnded(self):
        pass

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
            if self.parent.LoadedFilePath is not None \
                    and Path(self.parent.LoadedFilePath).parent == Path(TEMP_AUDIO_DIR):
                Path(self.parent.LoadedFilePath).unlink(missing_ok=True)

    def showAudioCursor(self):
        if self.parent.CurrentAudio is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.show()

    def updateSliceRegion(self):
        pass

    def setEQBandsOrderMenuVisible(self, arg: bool):
        for item in self.view.menuEQ_Bands_Playback_Order.children():
            item.setVisible(arg)
