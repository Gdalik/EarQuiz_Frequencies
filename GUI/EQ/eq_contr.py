from PyQt6.QtWidgets import QSlider
from Model.eq_patterns import EQPatterns


class EQContr:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent
        self.EQ_view = parent.mw_view.EQView
        self.EQPatterns = EQPatterns()
        self.EQpattern = None
        self.Sliders = parent.mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(self.onSliderDragged)

    def onSliderDragged(self, value):
        self.EQ_view.case_DisableAdjacentFiltersModeOn(value, self.EQpattern['ActiveFreqRange'])
        if self.parent.CurrentMode.name in ['Uni', 'Preview'] and value != 0:
            self.parent.mw_view.actionLearn_Mode.toggle()

    def setEQMode(self, mode_num=1):
        self.EQpattern = self.EQPatterns.get(mode_num)

        self.EQ_view.setCurrentEQ(self.EQpattern['EQtype'])
        self.EQ_view.resetEQ(self.EQpattern['EQ_boost_cut'])
        self.EQ_view.rangeCrop(*self.EQpattern['ActiveFreqRange'])
        self.EQ_view.disableAdjacentFiltersMode(self.EQpattern.get('DisableAdjacentFiltersMode', False))
        # print(self.getAvailableFreq())

    def getAvailableFreq(self):
        return [F.freq for F in self.EQ_view.Filters
                if self.EQpattern['ActiveFreqRange'][0] <= F.freq <= self.EQpattern['ActiveFreqRange'][1]]
