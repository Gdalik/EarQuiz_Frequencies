class TestMode:
    def __init__(self, parent):
        self.name = 'Test'
        self.view = parent.mw_view
        self.parent = parent
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