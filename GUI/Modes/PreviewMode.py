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

    @property
    def currentAudioCursorStartPos(self):
        return 0
