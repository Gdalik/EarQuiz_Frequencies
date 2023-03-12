from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    _playbackStoppedEndedBlocked: bool
    def __init__(self, parent):     # parent: MainWindowContr
        self.blockPlaybackStoppedEnded(True)
        super().__init__(parent)
        self.name = 'Test'
        self.currentDrillFreq = None
        self.view.SliceLenSpin.setEnabled(False)
        self.view.EQSetView.setEnabled(False)
        self.view.menuEQ_Bands_Playback_Order.setEnabled(False)
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(False)
        self.view.NextExercise.setVisible(True)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.parent.CurrentMode.restart_test()
        self.parent.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.view.ExScoreInfo.show()
        self.view.TransportPanelView.AudioSliderView.Cursor.show()
        self.parent.ExScore.showTestStatus()
        self.blockPlaybackStoppedEnded(False)
        self._playing_started = None

    @property
    def currentAudioStartTime(self):
        return 0

    @property
    def currentAudioCursorStartPos(self):   # in sec
        if self.parent.ADGen is None or self.parent.ADGen.audiochunk.currentSliceRange is None:
            return self.sourceRangeStartTime or 0
        return self.parent.ADGen.audiochunk.currentSliceRange[0]

    @property
    def proxyCursorPos(self):   # in sec
        return self.parent.TransportContr.PlayerContr.position() / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0

    def generateDrill(self, fromStart=False):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.updAudioToEqSettings(refreshAfter=False)
        self.updateCurrentAudio()
        return self.parent.ADGen.output(audio_path=self.parent.CurrentAudio, force_freq=None, fromStart=fromStart)[0]

    def nextDrill(self, fromStart=False, play_after=True):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.view.setActionNextExerciseEnabled(False)
        self.parent.EQContr.resetEQ()
        self.currentDrillFreq = self.generateDrill(fromStart=fromStart)
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=play_after)
        self.updateSliceRegion()
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

    def playbackStoppedEnded(self):
        if self._playbackStoppedEndedBlocked:
            return
        self.view.EqOnOffLab.setVisible(False)

    def blockPlaybackStoppedEnded(self, arg: bool):
        self._playbackStoppedEndedBlocked = arg

    def oncePlayingStarted(self):
        self.view.EqOnOffLab.setVisible(True)

    def whilePlaying(self):
        self.view.setEQStateIndicatorOn(self.parent.TransportContr.eqStateOnOff())

    def restart_test(self):
        self.parent.ExScore.refresh()
