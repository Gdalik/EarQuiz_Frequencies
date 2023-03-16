from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    _playbackStoppedEndedBlocked: bool

    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Test'
        self.currentDrillFreq = None
        self.view.SliceLenSpin.setEnabled(False)
        self.view.EQSetView.setEnabled(False)
        self.setEQBandsOrderMenuVisible(False)
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(False)
        self.view.NextExercise.setVisible(True)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.restart_test()
        self.parent.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.updateSliceRegion()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.view.ExScoreInfo.show()
        self.parent.ExScore.showTestStatus()
        self.showAudioCursor()

    def generateDrill(self, fromStart=False):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.updAudioToEqSettings(refreshAfter=False)
        self.updateCurrentAudio()
        return self.parent.ADGen.output(audio_path=self.parent.CurrentAudio, force_freq=None, fromStart=fromStart)[0]

    def nextDrill(self, fromStart=False, play_after=True, **kwargs):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.view.setActionNextExerciseEnabled(False)
        self.parent.EQContr.resetEQ()
        self.currentDrillFreq = self.generateDrill(fromStart=fromStart)
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=play_after)
        self.parent.ExScore.nextEx()

    def acceptAnswer(self):
        eq_values = self.parent.EQContr.getEQValues()
        self.parent.ExScore.onAnswerAccepted(RightAnswer=self.currentDrillFreq, UserAnswer=eq_values)
        self.parent.EQContr.freezeEQ()
        self.parent.EQContr.highlightEQFreq(self.currentDrillFreq)
        self.view.setActionNextExerciseEnabled(self.parent.ExScore.test_status == 'in progress')
        self.parent.ExScore.showTestStatus()

    def updateSliceRegion(self):
        if self.parent.ADGen is None:
            return
        slicerange = self.parent.ADGen.audiochunk.currentSliceRange
        self.view.TransportPanelView.AudioSliderView.SliceRegion.setValues(slicerange[0], slicerange[1])

    def restart_test(self):
        self.parent.ExScore.refresh()
        self.parent.ExScore.showTestStatus()
