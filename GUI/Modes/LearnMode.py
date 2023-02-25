from GUI.Modes.UniMode import UniMode


class LearnMode(UniMode):
    _playbackStoppedEndedBlocked: bool
    def __init__(self, parent):     # parent: MainWindowContr
        self.blockPlaybackStoppedEnded(True)
        super().__init__(parent)
        self.name = 'Learn'
        self.currentDrillFreq = None
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(True)
        self.parent.setAudioDrillGen()
        self.nextDrill(fromStart=False)
        self.blockPlaybackStoppedEnded(False)

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
        self.updateCurrentAudio()
        eq_values = self.parent.EQContr.getEQValues()
        force_freq = eq_values or None
        return self.parent.ADGen.output(audio_path=self.CurrentAudio, force_freq=force_freq, fromStart=fromStart)[0]

    def nextDrill(self, fromStart=False):
        if self.parent.ADGen is None:
            return
        player = self.parent.TransportContr.PlayerContr
        if player.playbackState() == player.PlaybackState.PlayingState:
            self.parent.TransportContr.PlayerContr.onStopTriggered()
        self.currentDrillFreq = self.generateDrill(fromStart=fromStart)
        self.parent.mw_view.EQView.setHandles(self.currentDrillFreq, blockSignals=True)
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=True)

    def playbackStoppedEnded(self):
        if self._playbackStoppedEndedBlocked:
            return
        self.parent.EQContr.resetEQ()

    def blockPlaybackStoppedEnded(self, arg: bool):
        self._playbackStoppedEndedBlocked = arg
