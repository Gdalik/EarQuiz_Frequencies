from GUI.Modes.UniMode import UniMode


class PreviewMode(UniMode):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Preview'
        self.view.AudiofileRBut.setChecked(True)
        self.playPause_toggleable = True
        self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.view.TransportPanel.show()
        self.updateCurrentAudio()

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
        self.CurrentAudio = self.parent.SourceAudio.path if self.parent.SourceAudio else None
