import time

from PySide6.QtWidgets import QSlider, QLabel
from Misc.common_calcs import findAdjacentEl

class EqView:
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
        self._disableAdjacentFiltersMode = False
        self.currentEQ = None

    def setCurrentEQ(self, EQ: str):    # 'EQ1' (10-band) / 'EQ2' (30-band)
        if EQ == 'EQ1':
            self.TabWidget.setTabVisible(0, True)
            self.TabWidget.setTabVisible(1, False)
        elif EQ == 'EQ2':
            self.TabWidget.setTabVisible(0, False)
            self.TabWidget.setTabVisible(1, True)
        self.currentEQ = EQ

    def highlight_right_Filter(self, freq: int, mode: str):    # mode: 'full'/'half+'/'half-'
        green_slider_settings = '{margin: 0 12px; background: green; width: 5px;border: 1px solid #262626}'
        Slider, Label = self.getFilter(freq)
        slider_style = Slider.styleSheet()
        handle_style = self.disabledHandleStyle if self.disabledHandleStyle in slider_style else self.handleStyle
        if mode == 'half+':
            slider_style += f'.QSlider::sub-page:vertical{green_slider_settings}'
        elif mode == 'half-':
            slider_style += f'.QSlider::add-page:vertical{green_slider_settings}'
        else:
            slider_style = f'.QSlider::groove:vertical{green_slider_settings}{handle_style}'
        Slider.setStyleSheet(slider_style)
        Label.setStyleSheet('color: green; font-weight: bold')
        return Slider, Label

    def _getEQ(self, Filter: tuple):
        return Filter[0].objectName().split('_')[0]

    def _getfreq(self, Filter: tuple):
        return int(Filter[0].objectName().split('_')[-1])

    def getFilter(self, freq: int):
        Slider = self.TabWidget.findChild(QSlider, name=f'{self.currentEQ}_{freq}')
        Label = self.TabWidget.findChild(QLabel, name=f'{self.currentEQ}_{freq}_Lab')
        return Slider, Label

    def getFilters(self):
        SliderList = [Slider for Slider in self.TabWidget.findChildren(QSlider) if Slider.objectName().startswith(self.currentEQ) and Slider.objectName() not in self._permDisabledFilters]
        LabelList = [self.TabWidget.findChild(QLabel, f'{SliderName}_Lab') for SliderName in map(QSlider.objectName, SliderList)]
        FilterList = zip(SliderList, LabelList)
        return [*FilterList]

    def resetFilterStyle(self, freq: int):
        return self._resetFilterStyle(self.getFilter(freq))

    def _resetFilterStyle(self, Filter: tuple):
        Slider, Label = Filter
        sliderStyle = self.basicSliderStyle if Slider.objectName() not in self._permDisabledFilters else self.disabledSliderStyle
        Slider.setStyleSheet(sliderStyle)
        Label.setStyleSheet('')
        return Slider, Label

    def resetEQStyle(self):
        Filters = self.getFilters()
        for Filter in Filters:
            self._resetFilterStyle(Filter)
        return Filters

    def resetEQ(self, mode: str):  # mode: '+', '-', '+-'
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
        Filters = self.resetEQStyle()
        for F in Filters:
            F[0].setMinimum(min_value)
            F[0].setMaximum(max_value)
            F[0].setValue(value)
            self._filterSetEnabled(F, True)
        return Filters

    def filterHandle(self, freq: int, boost_cut: str, blockSignals=False):      # boost_cut: '+'/'-'
        return self._filterHandle(self.getFilter(freq), boost_cut, blockSignals=blockSignals)

    @staticmethod
    def _filterHandle(Filter: tuple, boost_cut: str, blockSignals=False):     # boost_cut: '+'/'-'
        Slider, _ = Filter
        Slider.blockSignals(blockSignals)
        if boost_cut == '+':
            Slider.setValue(Slider.maximum())
        elif boost_cut == '-':
            Slider.setValue(Slider.minimum())
        Slider.blockSignals(False)
        return Slider

    def filterSetEnabled(self, freq: int, arg: bool):
        return self._filterSetEnabled(self.getFilter(freq), arg)

    def _filterSetEnabled(self, Filter: tuple, arg: bool):
        Slider, Label = Filter
        if Slider.objectName() in self._permDisabledFilters:
            return Filter
        Slider.setEnabled(arg)
        Label.setEnabled(arg)
        slider_style = Slider.styleSheet().replace(self.disabledHandleStyle, self.handleStyle) if arg else Slider.styleSheet().replace(self.handleStyle, self.disabledHandleStyle)
        Slider.setStyleSheet(slider_style)
        return Slider, Label

    def rangeSetEnabled(self, freq1: int, freq2: int, arg: bool):
        freqs = [freq1, freq2]
        freqs.sort()
        Filters = self.getFilters()
        for F in Filters:
            if freqs[0] <= self._getfreq(F) <= freqs[1]:
                self._filterSetEnabled(F, arg)
        return Filters

    def rangeCrop(self, freq1: int, freq2: int):
        self.rangeSetEnabled(20, 20000, False)
        self.rangeSetEnabled(freq1, freq2, True)

    def _sortedFilters(self):
        filter_list = self.getFilters()
        key_func = lambda Filter: self._getfreq(Filter)
        filter_list.sort(key=key_func)
        return filter_list

    def _getAdjacentFilters(self, Filter: tuple, arg: int or bool):     # arg: the number of adjacent filters from each side or False
        if not arg:
            return
        sorted_filters = self._sortedFilters()
        return findAdjacentEl(sorted_filters, Filter, num=arg)

    def disableAdjacentFilters(self, freq: int, num=1):   # num: the number of adjacent filters from each side
        if not num:
            return
        adj_filt = self._getAdjacentFilters(self.getFilter(freq), num)
        for F in adj_filt:
            self._filterSetEnabled(F, False)

    def enableAdjacentFilters(self, freq: int, num=1):   # num: the number of adjacent filters from each side
        adj_filt = self._getAdjacentFilters(self.getFilter(freq), num)
        for F in adj_filt:
            self._filterSetEnabled(F, True)

    def disableAdjacentFiltersMode(self, arg: int or bool):    # arg: the number of adjacent filters from each side or False
        self._disableAdjacentFiltersMode = arg

    def case_disableAdjacentFiltersModeOn(self, sliderValue: int, activeFreqRange=(20, 20000)):
        if not self._disableAdjacentFiltersMode:
            return
        filters = self.getFilters()
        if sliderValue == 0:
            self.rangeSetEnabled(*activeFreqRange, True)
        for F in filters:
            if F[0].value() != 0:
                self.disableAdjacentFilters(self._getfreq(F), num=self._disableAdjacentFiltersMode)
