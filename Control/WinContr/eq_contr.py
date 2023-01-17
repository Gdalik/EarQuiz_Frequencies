from PySide6.QtWidgets import QSlider


class EQContr:
    def __init__(self, mw_view):
        self.EQ_view = mw_view.EQ
        self.Sliders = mw_view.EQtabWidget.findChildren(QSlider)
        for Slider in self.Sliders:
            Slider.valueChanged.connect(self.onSliderDragged)
        self.setEQMode(mw_view.PatternBox.currentIndex()+1)

    def onSliderDragged(self, value):
        self.EQ_view.case_disableAdjacentFiltersModeOn(value, self.ActiveFreqRange)

    def setEQMode(self, mode_num=1):  # sourcery skip: switch
        disableAdjacentFiltersMode = (False, 0)
        self.dualBandMode = False
        if mode_num == 1:   # 1. Lowest five (31-500 Hz) 1-octave bands boosted (+)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 500)
            self.EQ_boost_cut = '+'
        elif mode_num == 2:   # 2. Middle five (250-4000 Hz) 1-octave bands boosted (+)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (250, 4000)
            self.EQ_boost_cut = '+'
        elif mode_num == 3:   # 3. Highest five (1-16 kHz) 1-octave bands boosted (+)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (1000, 16000)
            self.EQ_boost_cut = '+'
        elif mode_num == 4:   # 4. Lowest five (31-500 Hz) 1-octave bands cut (-)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 500)
            self.EQ_boost_cut = '-'
        elif mode_num == 5:   # 5. Middle five (250-4000 Hz) 1-octave bands cut (-)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (250, 4000)
            self.EQ_boost_cut = '-'
        elif mode_num == 6:   # 6. Highest five (1-16 kHz) 1-octave bands cut (-)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (1000, 16000)
            self.EQ_boost_cut = '-'
        elif mode_num == 7:   # 7. All ten 1-octave bands boosted (+)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 16000)
            self.EQ_boost_cut = '+'
        elif mode_num == 8:   # 8. All ten 1-octave bands cut (-)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 16000)
            self.EQ_boost_cut = '-'
        elif mode_num == 9:   # 9. All ten 1-octave bands boosted (+) or cut(-)
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 16000)
            self.EQ_boost_cut = '+-'
        elif mode_num == 10:    # 10. Low (32-315 Hz) 1/3-octave bands boosted (+) or cut (-)
            self.EQtype = 'EQ2'
            self.ActiveFreqRange = (32, 315)
            self.EQ_boost_cut = '+-'
        elif mode_num == 11:    # 11. Mid (315-1250 Hz) 1/3-octave bands boosted (+) or cut (-)
            self.EQtype = 'EQ2'
            self.ActiveFreqRange = (315, 1250)
            self.EQ_boost_cut = '+-'
        elif mode_num == 12:    # 12. High (1.6 kHz - 16 kHz) 1/3-octave bands boosted (+) or cut (-)
            self.EQtype = 'EQ2'
            self.ActiveFreqRange = (1600, 16000)
            self.EQ_boost_cut = '+-'
        elif mode_num == 13:    # 13. All 1/3-octave bands boosted (+) or cut (-)
            self.EQtype = 'EQ2'
            self.ActiveFreqRange = (32, 16000)
            self.EQ_boost_cut = '+-'
        elif mode_num == 14:
            self.EQtype = 'EQ1'
            self.ActiveFreqRange = (31, 16000)
            self.EQ_boost_cut = '+-'
            disableAdjacentFiltersMode = (True, 1)
            self.dualBandMode = True

        self.EQ_view.setCurrentEQ(self.EQtype)
        self.EQ_view.resetEQ(self.EQ_boost_cut)
        self.EQ_view.rangeCrop(*self.ActiveFreqRange)
        self.EQ_view.disableAdjacentFiltersMode(*disableAdjacentFiltersMode)
