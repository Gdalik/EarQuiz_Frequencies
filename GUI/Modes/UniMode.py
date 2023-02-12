class UniMode:
    def __init__(self, parent):
        self.name = 'Uni'
        self.view = parent.mw_view
        self.parent = parent
        self.CurrentAudio = None
        # self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.playPause_toggleable = False
        self.parent.TransportContr.PlayerContr.stop()
        self.view.actionNext_Exercise.setEnabled(False)
        self.view.NextExercise.hide()
        self.view.EqOnOffLab.hide()
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

    def updateCurrentAudio(self):
        pass
