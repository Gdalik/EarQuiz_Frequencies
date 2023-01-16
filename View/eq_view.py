from PySide6.QtWidgets import QWidget, QSlider, QLabel

class EqView():
    """@DynamicAttrs"""
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.TabWidget = mw_view.EQtabWidget
        self.TabWidget.setTabText(0, '10-Band Equalizer')
        self.TabWidget.setTabText(1, '30-Band Equalizer')
        self._permDisabledFilters = ('EQ2_25', 'EQ2_20000')
        self.handleStyle = '.QSlider::handle:vertical{background: white; border: 2px solid rgb(15, 128, 255); height: 5px; width: 10px; margin: 0px -5px}'
        self.disabledHandleStyle = '.QSlider::handle:vertical{background: white; border: 2px solid rgb(191, 191, 191); height: 5px; width: 10px; margin: 0px -5px}'
        self.basicSliderStyle = '.QSlider::groove:vertical{border: 1px solid #262626; background: rgb(191, 191, 191); width: 5px; margin: 0 12px;}'+self.handleStyle
        self.disabledSliderStyle = self.basicSliderStyle + self.disabledHandleStyle
        #for W in mw_view.EQtabWidget.findChildren(QWidget):
        #    self.__setattr__(W.objectName(), W)

    def setCurrentEq(self, eq: str):    # 'EQ1' (10-band) / 'EQ2' (30-band)
        if eq == 'EQ1':
            self.TabWidget.setTabVisible(0, True)
            self.TabWidget.setTabVisible(1, False)
        elif eq == 'EQ2':
            self.TabWidget.setTabVisible(0, False)
            self.TabWidget.setTabVisible(1, True)

    def highlight_right_Filter(self, EQ: str, freq: int, mode: str):    # EQ: 'EQ1' / 'EQ2' ; mode: 'full'/'half+'/'half-'
        slider_style = self.basicSliderStyle
        green_slider_settings = '{margin: 0 12px; background: green; width: 5px;border: 1px solid #262626}'
        if mode == 'half+':
            slider_style += f'.QSlider::sub-page:vertical{green_slider_settings}'
        elif mode == 'half-':
            slider_style += f'.QSlider::add-page:vertical{green_slider_settings}'
        else:
            slider_style = f'.QSlider::groove:vertical{green_slider_settings}{self.handleStyle}'

        Slider, Label = self.getFilter(EQ, freq)
        Slider.setStyleSheet(slider_style)
        Label.setStyleSheet('color: green; font-weight: bold')
        return Slider, Label

    def getFilter(self, EQ: str, freq: int):   # EQ: 'EQ1'/'EQ2'
        Slider = self.TabWidget.findChild(QSlider, name=f'{EQ}_{freq}')
        Label = self.TabWidget.findChild(QLabel, name=f'{EQ}_{freq}_Lab')
        return Slider, Label

    def getFilters(self, EQ: str):  # EQ: 'EQ1'/'EQ2'
        SliderList = [Slider for Slider in self.TabWidget.findChildren(QSlider) if Slider.objectName().startswith(EQ)]
        LabelList = [self.TabWidget.findChild(QLabel, f'{SliderName}_Lab') for SliderName in map(QSlider.objectName, SliderList)]
        FilterList = zip(SliderList, LabelList)
        return [*FilterList]

    def resetEQStyle(self, EQ: str):    # EQ: 'EQ1'/'EQ2'
        Filters = self.getFilters(EQ)
        for Filter in Filters:
            Slider, Label = Filter
            sliderStyle = self.basicSliderStyle if Slider.objectName() not in self._permDisabledFilters else self.disabledSliderStyle
            Slider.setStyleSheet(sliderStyle)
            Label.setStyleSheet('')
        return Filters

    def resetEQ(self, EQ: str, mode: str):  # EQ: 'EQ1'/'EQ2'; mode: '+', '-', '+-'
        if mode == '+':
            min_value = value = 0
            max_value = 1
        elif mode == '-':
            min_value = -1
            max_value = value = 0
        else:
            min_value = -1
            value = 0
            max_value = 1
        Filters = self.resetEQStyle(EQ)
        for F in Filters:
            F[0].setMinimum(min_value)
            F[0].setMaximum(max_value)
            F[0].setValue(value)
        return Filters