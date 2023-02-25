from GUI.Modes.UniMode import UniMode


class PreviewMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Preview'
        self.view.AudiofileRBut.setChecked(True)
        self.playPause_toggleable = True
        self.parent.EQContr.resetEQ()
        self.view.TransportPanel.show()
        if self.parent.SourceAudio is not None:
            self.enableTimeSettingsChanges(True)
        if self.updateCurrentAudio():
            self.parent.TransportContr.PlayerContr.loadCurrentAudio()

    @property
    def proxyCursorPos(self):   # in sec
        player_pos = self.parent.TransportContr.PlayerContr.position()
        if player_pos == 0:
            return self.sourceRangeStartTime or 0
        return player_pos / 1000 if self.parent.SourceAudio is not None else 0

    @property
    def currentAudioStartTime(self):    # in sec
        return self.sourceRangeStartTime or 0

    @property
    def currentAudioEndTime(self):  # in sec
        return self.parent.SourceRange.endtime or 0

    def setPlayerControls(self):
        self.view.actionPlayPause.setEnabled(True)
        self.view.actionStop.setEnabled(True)
        self.view.actionPrevious_Track.setEnabled(True)
        self.view.actionNext_Track.setEnabled(True)
        self.view.actionLoop_Playback.setEnabled(True)
        self.view.actionLoop_Playback.setChecked(True)
        self.view.actionShuffle_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setEnabled(True)

    def updateCurrentAudio(self):
        old_value = self.CurrentAudio
        self.CurrentAudio = self.parent.SourceAudio.path if self.parent.SourceAudio else None
        return self.CurrentAudio != old_value

