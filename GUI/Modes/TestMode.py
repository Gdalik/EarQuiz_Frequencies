from GUI.Modes.UniMode import UniMode
from GUI.ExScoreInfo.exscoreinfo_contr import ExScoreInfoContr


class TestMode(UniMode):
    _playbackStoppedEndedBlocked: bool
    def __init__(self, parent):     # parent: MainWindowContr
        self.blockPlaybackStoppedEnded(True)
        super().__init__(parent)
        self.name = 'Test'
        self.currentDrillFreq = None
        self.ExScore = ExScoreInfoContr(parent)
        self.view.SliceLenSpin.setEnabled(False)
        self.view.EQSetView.setEnabled(False)
        self.view.menuEQ_Bands_Playback_Order.setEnabled(False)
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(False)
        self.parent.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.view.ExScoreInfo.show()
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
        return self.parent.ADGen.output(audio_path=self.CurrentAudio, force_freq=None, fromStart=fromStart)[0]

    def nextDrill(self, fromStart=False, play_after=True):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.currentDrillFreq = self.generateDrill(fromStart=fromStart)
        print(f'{self.currentDrillFreq=}')
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=play_after)
        self.updateSliceRegion()
        self.ExScore.nextEx()

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
