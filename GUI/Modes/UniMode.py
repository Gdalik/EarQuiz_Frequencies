from Model.audiodrill_gen import AudioDrillGen


class UniMode:
    def __init__(self, parent):     # parent: MainWindowContr
        self.TimeSettingsChangesEnabled = None
        self.name = 'Uni'
        self.view = parent.mw_view
        self.parent = parent
        self.CurrentAudio = None
        self.playPause_toggleable = False
        self.parent.TransportContr.PlayerContr.onStopTriggered()
        self.view.setActionNextExerciseEnabled(False)
        self.enableTimeSettingsChanges(False)
        self.view.EqOnOffLab.hide()
        self.view.menuEQ_Bands_Playback_Order.setEnabled(True)
        self.setPlayerControls()

    @property
    def currentAudioCursorStartPos(self):
        return 0

    @property
    def proxyCursorPos(self):   # in sec
        player_pos = self.parent.TransportContr.PlayerContr.position()
        if player_pos == 0:
            return self.currentAudioStartTime
        return player_pos / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0

    @property
    def currentAudioStartTime(self):    # in sec
        return self.parent.SourceRange.starttime if self.parent.SourceRange is not None else 0

    @property
    def currentAudioEndTime(self):  # in sec
        return self.parent.SourceRange.endtime if self.parent.SourceRange is not None else 0

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
        pass

    def enableTimeSettingsChanges(self, arg: bool):
        self.view.TransportPanelView.AudioSliderView.Cursor.setMovable(arg)
        self.view.TransportPanelView.AudioSliderView.CropRegion.setMovable(arg)
        self.view.TransportPanelView.CropRegionTstr.setChangesEnabled(arg)
        self.TimeSettingsChangesEnabled = arg

