from PySide6.QtWidgets import QSlider
from Model.eq_patterns import eqPatterns


class EQContr:
    def __init__(self, mw_view):
        self.EQ_view = mw_view.EQView
        self.EQpattern = {}
        self.Sliders = mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(self.onSliderDragged)

    def onSliderDragged(self, value):
        self.EQ_view.case_disableAdjacentFiltersModeOn(value, self.EQpattern['ActiveFreqRange'])

    def setEQMode(self, mode_num=1):
        self.EQpattern = eqPatterns[mode_num - 1]

        self.EQ_view.setCurrentEQ(self.EQpattern['EQtype'])
        self.EQ_view.resetEQ(self.EQpattern['EQ_boost_cut'])
        self.EQ_view.rangeCrop(*self.EQpattern['ActiveFreqRange'])
        self.EQ_view.disableAdjacentFiltersMode(self.EQpattern.get('disableAdjacentFiltersMode', False))
        # print(self.getAvailableFreq())

    def getAvailableFreq(self):
        return [F for F in list(map(self.EQ_view.getfreq, self.EQ_view.getFilters())) if self.EQpattern['ActiveFreqRange'][0] <= F <= self.EQpattern['ActiveFreqRange'][1]]

