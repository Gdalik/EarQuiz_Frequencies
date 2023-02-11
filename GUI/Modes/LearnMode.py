class LearnMode:
    def __init__(self, parent):
        self.name = 'Learn'
        self.view = parent.mw_view
        self.parent = parent
        if self.parent.LastMode is not None and self.parent.LastMode.name != 'Preview':
            self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.playPause_toggleable = False
        self.view.TransportPanelView.PlayerView.setPlayPause2Play()

        self.setPlayerControls()

    def setPlayerControls(self):
        self.view.actionPlayPause.setEnabled(True)
        self.view.actionStop.setEnabled(True)
        self.view.actionPrevious_Track.setEnabled(False)
        self.view.actionNext_Track.setEnabled(False)
        self.view.actionLoop_Playback.setEnabled(False)
        self.view.actionLoop_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setEnabled(False)