#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from GUI.Modes.UniMode import UniMode


class LearnMode(UniMode):
    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Learn'
        self.currentDrillFreq = None
        self.view.SliceLenSpin.setEnabled(False)
        if self.parent.LastMode.name != 'Preview':
            self.parent.EQContr.resetEQ()
        self.setControls()
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.parent.ADGC.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.updateSliceRegion()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.parent.ExScore.view.init_texts(onlyLastExcInfo=True)
        self.showAudioCursor()

    def setControls(self):
        self.view.setActionNextExampleEnabled(True)
        self.setNextExampleVisible(True)
        self.view.actionSequential_Playback.setVisible(True)
        self.view.SequencePlayBut.setVisible(True)
        self.view.actionLoop_Sequence.setVisible(True)
        self.view.onActionSequentialPlaybackTriggered()

    def generateDrill(self, fromStart=False, raiseInterruptedException=True):
        if self.parent.ADGen is None:
            return
        self.showProcessingSourceMessage()
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
        self.parent.TransportContr.PlayerContr.t_loadCurrentAudio(play_after=play_after)

    def updateSliceRegion(self):
        if self.parent.ADGen is None:
            return
        slicerange = self.parent.ADGen.audiochunk.currentSliceRange
        self.view.TransportPanelView.AudioSliderView.SliceRegion.setValues(slicerange[0], slicerange[1])

    def playbackStoppedEnded(self):
        self.parent.EQContr.resetEQ()
        self.view.EQSetView.setEnabled(True)
        self.hideEQState()

    def playbackEnded(self):
        if self.parent.mw_view.actionSequential_Playback.isChecked():
            if not self.parent.mw_view.actionLoop_Sequence.isChecked() and \
                    self.parent.ADGen.exercise_gen.isLastItemInSeq:
                return
            self.nextDrill()

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
