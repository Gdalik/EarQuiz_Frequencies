from PySide6.QtWidgets import QSlider


class EQContr:
    def __init__(self, mw_view):
        self.EQ_view = mw_view.EQ
        self.Sliders = mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(self.onSliderDragged)
        self.ActiveFreqRange = (2000, 20000)
        self.EQ_view.setCurrentEQ('EQ2')
        self.EQ_view.resetEQ('+')
        self.EQ_view.rangeSetEnabled(20, 20000, False)
        self.EQ_view.rangeSetEnabled(*self.ActiveFreqRange, True)
        self.EQ_view.disableAdjacentFiltersMode(True, num=1)

    def onSliderDragged(self, value):
        self.EQ_view.case_disableAdjacentFiltersModeOn(value, self.ActiveFreqRange)