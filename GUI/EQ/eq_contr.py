#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

from PyQt6.QtCore import QObject, QTimer
from PyQt6.QtWidgets import QSlider
from Model.eq_patterns import EQPatterns
from GUI.globals import SliderAmplitude as SA
from functools import partial


class EQContr(QObject):
    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__()
        self.parent = parent
        self.EQ_view = parent.mw_view.EQView
        self.EQPatterns = EQPatterns()
        self.EQpattern = None
        self.Sliders = parent.mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(partial(self.onSliderValueChanged, Slider))
            Slider.sliderPressed.connect(partial(self.onSliderPressed, Slider))
            Slider.actionTriggered.connect(partial(self.onSliderActionTriggered, Slider))
        self.frozen = False
        self._onSliderValueChangeBlocked = False

    def _normSliderValue(self, Slider: QSlider):
        v = Slider.value()
        if v != 0 and abs(v) < SA:
            Slider.setValue(int(v / abs(v) * SA))

    def onSliderActionTriggered(self, Slider, action):
        if action == QSlider.SliderAction.SliderMove.value:
            return
        sp = Slider.sliderPosition()
        sv = Slider.value()
        if sp != 0 and sv != 0 and abs(sp) < abs(sv):
            Slider.setValue(0)

    def onSliderPressed(self, Slider):
        if self.EQpattern['EQ_boost_cut'] == '+-':
            return
        v = 1 if self.EQpattern['EQ_boost_cut'] == '+' else -1
        Slider.setValue(SA * v)

    def onSliderValueChanged(self, Slider: QSlider, value):
        if self._onSliderValueChangeBlocked:
            return
        if value != 0 and abs(value) < SA:
            self._normSliderValue(Slider)
            return
        self.EQ_view.case_DisableAdjacentFiltersModeOn(value, self.EQpattern['ActiveFreqRange'])
        if self.parent.CurrentMode.name in ['Uni', 'Preview'] and self.freqAccepted and self.parent.SourceAudio:
            self.parent.mw_view.actionLearn_Mode.setChecked(True)
        elif self.parent.CurrentMode.name == 'Learn' and self.freqAccepted:
            self.parent.CurrentMode.nextDrill(raiseInterruptedException=False)
        elif self.parent.CurrentMode.name == 'Test' and self.freqAccepted:
            self.parent.CurrentMode.acceptAnswer()
            if self.parent.ExScore.test_status != 'in progress':
                self.parent.endTest()
        self._checkSourceAudio()

    def _checkSourceAudio(self):
        if not self.parent.SourceAudio:
            QTimer.singleShot(300, self.resetEQ)

    def setEQMode(self, mode_num=1):
        self.EQpattern = self.EQPatterns.get(mode_num)

        self.EQ_view.setCurrentEQ(self.EQpattern['EQtype'])
        self.blockSliderValueChange(True)
        self.EQ_view.resetEQ(self.EQpattern['EQ_boost_cut'])
        self.blockSliderValueChange(False)
        self.EQ_view.rangeCrop(*self.EQpattern['ActiveFreqRange'])
        self.EQ_view.disableAdjacentFiltersMode(self.EQpattern.get('DisableAdjacentFiltersMode', False))
        self.frozen = False

    def getAvailableFreq(self):
        return [F.freq for F in self.EQ_view.Filters
                if self.EQpattern['ActiveFreqRange'][0] <= F.freq <= self.EQpattern['ActiveFreqRange'][1]]

    def resetEQ(self):
        self.setEQMode(self.parent.mw_view.PatternBox.currentIndex() + 1)

    def freezeEQ(self):
        self.EQ_view.freezeEQ()
        self.frozen = True

    @staticmethod
    def _slider_value(v: int):
        if v > 0:
            return 1
        elif v < 0:
            return -1
        else:
            return 0

    def getEQValues(self):
        if self.EQ_view.Filters is None:
            return None
        values = [F.freq * self._slider_value(F.Slider.value()) for F in self.EQ_view.Filters if F.Slider.value() != 0]
        if not values:
            return None
        elif len(values) == 1:
            return values[0]
        else:
            return tuple(values)

    def highlightEQFreq(self, freq: int or tuple):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or self.parent.ADGen is None:
            return
        freq = (freq,) if isinstance(freq, int) else freq
        for f in freq:
            self.EQ_view.highlight_right_Filter(f)

    @property
    def freqAccepted(self):
        if self.EQpattern is None:
            return None
        num_pattern = 2 if self.EQpattern['DualBandMode'] else 1
        eq_values = self.getEQValues()
        if isinstance(eq_values, int):
            num_entered = 1
        elif isinstance(eq_values, tuple):
            num_entered = len(eq_values)
        else:
            num_entered = 0
        return num_pattern == num_entered

    def blockSliderValueChange(self, arg):
        self._onSliderValueChangeBlocked = arg
