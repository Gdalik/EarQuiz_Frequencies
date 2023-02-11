class PreviewMode:
    def __init__(self, parent):
        self.name = 'Preview'
        self.parent = parent
        self.view = parent.mw_view
        self.view.AudiofileRBut.setChecked(True)
        self.playPause_toggleable = True
        self.view.TransportPanelView.PlayerView.setPlayPause2Play()
        self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.setPlayerControls()
        self.view.TransportPanel.show()
        self.view.NextExercise.hide()
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
