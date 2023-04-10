from PyQt6.QtCore import QObject, QTimer
from PyQt6.QtWidgets import QSlider

from Model.eq_patterns import EQPatterns


class EQContr(QObject):
    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__()
        self.parent = parent
        self.EQ_view = parent.mw_view.EQView
        self.EQPatterns = EQPatterns()
        self.EQpattern = None
        self.Sliders = parent.mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(self.onSliderDragged)
        self.frozen = False
        self._onSliderDraggedBlocked = False

    def onSliderDragged(self, value):
        if self._onSliderDraggedBlocked:
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
        self.blockOnSliderDragged(True)
        self.EQ_view.resetEQ(self.EQpattern['EQ_boost_cut'])
        self.blockOnSliderDragged(False)
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

    def getEQValues(self):
        if self.EQ_view.Filters is None:
            return None
        values = [F.freq * F.Slider.value() for F in self.EQ_view.Filters if F.Slider.value() != 0]
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

    def blockOnSliderDragged(self, arg):
        self._onSliderDraggedBlocked = arg
