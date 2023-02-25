from Model.audiodrill_gen import AudioDrillGen
from Model.audiodrill_gen import create_temp_wavefile


class UniMode:
    def __init__(self, parent):     # parent: MainWindowContr
        self.TimeSettingsChangesEnabled = None
        self.name = 'Uni'
        self.view = parent.mw_view
        self.parent = parent
        self.parent.CurrentMode = self
        self.CurrentAudio = None
        self.playPause_toggleable = False
        self.parent.TransportContr.PlayerContr.onStopTriggered()
        self.view.setActionNextExerciseEnabled(False)
        self.enableTimeSettingsChanges(False)
        self.view.EqOnOffLab.hide()
        self.view.menuEQ_Bands_Playback_Order.setEnabled(True)
        self.setPlayerControls()

    @property
    def currentAudioCursorStartPos(self):   # in sec
        if self.parent.ADGen is None or self.parent.ADGen.audiochunk.currentSliceRange is None:
            return self.sourceRangeStartTime or 0
        return self.parent.ADGen.audiochunk.currentSliceRange[0]

    @property
    def proxyCursorPos(self):   # in sec
        player_pos = self.parent.TransportContr.PlayerContr.position()
        if player_pos == 0:
            zero_start = self.sourceRangeStartTime or 0
            return zero_start + self.currentAudioStartTime
        return player_pos / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0

    @property
    def sourceRangeStartTime(self):
        return self.parent.SourceRange.starttime if self.parent.SourceRange else None

    @property
    def sourceRangeEndTime(self):
        return self.parent.SourceRange.endtimeif if self.parent.SourceRange else None

    @property
    def currentAudioStartTime(self):    # in sec
        return self.sourceRangeStartTime or 0

    @property
    def currentAudioEndTime(self):  # in sec
        return self.parent.SourceRange.endtime or 0

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
        self.CurrentAudio = create_temp_wavefile()

    def enableTimeSettingsChanges(self, arg: bool):
        self.view.TransportPanelView.AudioSliderView.Cursor.setMovable(arg)
        self.view.TransportPanelView.AudioSliderView.CropRegion.setMovable(arg)
        self.view.TransportPanelView.CropRegionTstr.setChangesEnabled(arg)
        self.TimeSettingsChangesEnabled = arg

    def nextDrill(self):
        pass

    def playbackStoppedEnded(self):
        pass

