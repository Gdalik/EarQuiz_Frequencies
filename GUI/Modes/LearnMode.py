from GUI.Modes.UniMode import UniMode


class LearnMode(UniMode):
    # _playbackStoppedEndedBlocked: bool
    def __init__(self, parent):     # parent: MainWindowContr
        # self.blockPlaybackStoppedEnded(True)
        super().__init__(parent)
        self.name = 'Learn'
        self.currentDrillFreq = None
        self.view.SliceLenSpin.setEnabled(False)
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.EQContr.resetEQ()
        self.view.setActionNextExampleEnabled(True)
        self.view.NextExample.setVisible(True)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.parent.ADGC.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.updateSliceRegion()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.parent.ExScore.view.init_texts(onlyLastExcInfo=True)
        self.showAudioCursor()
        # self.blockPlaybackStoppedEnded(False)

    def generateDrill(self, fromStart=False, raiseInterruptedException=True):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.updAudioToEqSettings(refreshAfter=False,
                                                        raiseInterruptedException=raiseInterruptedException)
        self.updateCurrentAudio()
        eq_values = self.parent.EQContr.getEQValues()
        force_freq = eq_values or None
        return self.parent.ADGen.output(audio_path=self.parent.CurrentAudio,
                                        force_freq=force_freq, fromStart=fromStart)[0]

    def nextDrill(self, fromStart=False, play_after=True, raiseInterruptedException=True):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.currentDrillFreq = self.generateDrill(fromStart=fromStart,
                                                   raiseInterruptedException=raiseInterruptedException)
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=play_after)

    def updateSliceRegion(self):
        if self.parent.ADGen is None:
            return
        slicerange = self.parent.ADGen.audiochunk.currentSliceRange
        self.view.TransportPanelView.AudioSliderView.SliceRegion.setValues(slicerange[0], slicerange[1])

    def playbackStoppedEnded(self):
        '''if self._playbackStoppedEndedBlocked:
            return'''
        self.parent.EQContr.resetEQ()
        self.view.EQSetView.setEnabled(True)
        # self.view.PatternBoxView.setEnabled(True)

    '''def blockPlaybackStoppedEnded(self, arg: bool):
        self._playbackStoppedEndedBlocked = arg'''

    def oncePlayingStarted(self):
        super(LearnMode, self).oncePlayingStarted()
        if not self.parent.EQContr.frozen:
            self.parent.EQContr.freezeEQ()
        self.view.EQSetView.setEnabled(False)
        if not self._checkSliders():
            self.view.EQView.setHandles(self.currentDrillFreq, blockSignals=True)

    def whilePlaying(self):
        eqStateOn = self.parent.TransportContr.eqStateOnOff()
        self.view.setEQStateIndicatorOn(eqStateOn)
        if eqStateOn:
            self.parent.EQContr.highlightEQFreq(self.currentDrillFreq)
        else:
            self.view.EQView.resetEQStyle(enabled=False)

    def _checkSliders(self):
        slider_freq = self.parent.EQContr.getEQValues()
        current_freq = self.currentDrillFreq
        if isinstance(slider_freq, tuple):
            slider_freq = set(slider_freq)
        if isinstance(current_freq, tuple):
            current_freq = set(current_freq)
        return slider_freq == current_freq
