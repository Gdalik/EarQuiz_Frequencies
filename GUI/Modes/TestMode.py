#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from PyQt6.QtCore import QThreadPool
from GUI.Modes.UniMode import UniMode
from Model.AudioEngine.audio_to_buffer import a2b
from GUI.Misc.adg_thread_run import ADGProc
import numpy as np


class TestMode(UniMode):
    _playbackStoppedEndedBlocked: bool
    ADGRun: ADGProc

    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Test'
        self.currentDrillFreq = None
        self.view.SliceLenSpin.setEnabled(False)
        self.view.EQSetView.setEnabled(False)
        self.parent.EQContr.resetEQ()
        self.view.setActionNextExampleEnabled(False)
        self.setNextExampleVisible(True)
        self.setEQBandsOrderMenuEnabled(False)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.restart_test()
        self.parent.ADGC.setAudioDrillGen()
        self.nextDrill(fromStart=True)
        self.updateSliceRegion()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.show()
        self.view.ExScoreInfo.show()
        self.parent.ExScore.showTestStatus()
        self.showAudioCursor()

    def generateDrill(self, fromStart=False):
        if self.parent.ADGen is None:
            return
        self.showProcessingSourceMessage()
        self.parent.TransportContr.updAudioToEqSettings(refreshAfter=False)
        self.ADGRun = ADGProc(self.parent.ADGen.output, audio_path=None, force_freq=None,
                                                                       fromStart=fromStart)
        self.ADGRun.signals.drillGenerated.connect(self._onDrillGenerated)
        threadPool = QThreadPool()
        threadPool.start(self.ADGRun)

    def _onDrillGenerated(self, freq: int or tuple, audio: np.ndarray):
        self.ADGRun.signals.drillGenerated.disconnect()
        self.currentDrillFreq = freq
        self.parent.CurrentAudio = a2b(audio, self.parent.ADGen.af_samplerate)
        self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=True)
        self.parent.ExScore.nextEx()

    def nextDrill(self, fromStart=False, play_after=True, **kwargs):
        if self.parent.ADGen is None:
            return
        self.parent.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.view.setActionNextExampleEnabled(False)
        self.parent.EQContr.resetEQ()
        self.generateDrill(fromStart=fromStart)

    def playbackEnded(self):
        self.parent.TransportContr.PlayerContr.waitForLoadedMedia()

    def acceptAnswer(self):
        eq_values = self.parent.EQContr.getEQValues()
        self.parent.ExScore.onAnswerAccepted(RightAnswer=self.currentDrillFreq, UserAnswer=eq_values)
        self.parent.EQContr.freezeEQ()
        self.parent.EQContr.highlightEQFreq(self.currentDrillFreq)
        self.view.setActionNextExampleEnabled(self.parent.ExScore.test_status == 'in progress')
        self.parent.ExScore.showTestStatus()

    def updateSliceRegion(self):
        self._updateSliceRegion()

    def restart_test(self):
        self.parent.ExScore.refresh()
        self.parent.ExScore.showTestStatus()
