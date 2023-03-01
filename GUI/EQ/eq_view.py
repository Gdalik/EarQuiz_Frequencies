from dataclasses import dataclass, field
from PyQt6.QtWidgets import QSlider, QLabel
from Utilities.common_calcs import findAdjacentEl
import re


class EqView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.TabWidget = mw_view.EQtabWidget
        self.TabWidget.setTabText(0, '10-Band Equalizer')
        self.TabWidget.setTabText(1, '30-Band Equalizer')
        self.handleStyle = '.QSlider::handle:vertical{background: white; border: 2px solid rgb(15, 128, 255); ' \
                           'height: 5px; width: 10px; margin: 0px -5px}'
        self.disabledHandleStyle = '.QSlider::handle:vertical{background: white; ' \
                                   'border: 2px solid rgb(191, 191, 191); height: 5px; width: 10px; margin: 0px -5px}'
        self.basicSliderStyleNoHandle = '.QSlider::groove:vertical{border: 1px solid #262626; ' \
                                'background: rgb(191, 191, 191); width: 5px; margin: 0 12px;}'
        self.basicSliderStyle = self.basicSliderStyleNoHandle + self.handleStyle
        self.disabledSliderStyle = self.basicSliderStyle + self.disabledHandleStyle
        self._DisableAdjacentFiltersMode = False
        self.currentEQ = None
        self.Filters = None

    @dataclass
    class Filter:
        EQ: str
        freq: int
        Slider: field(default_factory=QSlider)
        Label: field(default_factory=QLabel)

        @property
        def PermDisabled(self):
            return self.freq < 30 or self.freq > 16000

    def setCurrentEQ(self, EQ: str):    # 'EQ1' (10-band) / 'EQ2' (30-band)
        if EQ == 'EQ1':
            self.TabWidget.setTabVisible(0, True)
            self.TabWidget.setTabVisible(1, False)
        elif EQ == 'EQ2':
            self.TabWidget.setTabVisible(0, False)
            self.TabWidget.setTabVisible(1, True)
        self.currentEQ = EQ
        self.Filters = self.makeFilters()

    def highlight_right_Filter(self, freq: int, highlightHandle=False):
        F = self.getFilter(abs(freq))
        _slider_style = F.Slider.styleSheet()
        norm_handle_style = self.disabledHandleStyle if self.disabledHandleStyle in _slider_style else self.handleStyle
        green_slider_set = '.QSlider::groove:vertical{margin: 0 12px; background: green; ' \
                                'width: 5px;border: 1px solid #262626}'
        green_handle_style = '.QSlider::handle:vertical{background: white; border: 2px solid green; ' \
                           'height: 5px; width: 10px; margin: 0px -5px}'
        handle_style = green_handle_style if highlightHandle else norm_handle_style
        slider_style = f'{handle_style}{green_slider_set}'
        F.Slider.setStyleSheet(slider_style)
        labtext = F.Label.text()
        if not labtext.endswith(')'):
            F.Label.setText(f'{labtext}\n(+)') if freq > 0 else F.Label.setText(f'{labtext}\n(-)')
        F.Label.setStyleSheet('color: green; font-weight: bold')
        return F

    def getFilter(self, freq: int):
        for F in self.Filters:
            if F.EQ == self.currentEQ and F.freq == freq:
                return F

    def makeFilters(self):
        getEQ = lambda SliderLabel: SliderLabel[0].objectName().split('_')[0]
        getfreq = lambda SliderLabel: int(SliderLabel[0].objectName().split('_')[-1])
        SliderList = [Slider for Slider in self.TabWidget.findChildren(QSlider) if Slider.objectName().startswith(self.currentEQ)]
        LabelList = [self.TabWidget.findChild(QLabel, f'{SliderName}_Lab') for SliderName in map(QSlider.objectName, SliderList)]
        return [self.Filter(getEQ(El), getfreq(El), *El) for El in zip(SliderList, LabelList)]

    def resetFilterStyle(self, freq: int, enabled=True):
        return self._resetFilterStyle(self.getFilter(freq), enabled=enabled)

    def _resetFilterStyle(self, F: Filter, enabled=True):
        sliderStyle = self.disabledSliderStyle if F.PermDisabled or not enabled else self.basicSliderStyle
        F.Slider.setStyleSheet(sliderStyle)
        F.Label.setStyleSheet('')
        labtext = F.Label.text()
        if labtext.endswith(')'):
            F.Label.setText(labtext.removesuffix('\n(+)').removesuffix('\n(-)'))
        return F

    def resetEQStyle(self, enabled=True):
        for Filter in self.Filters:
            self._resetFilterStyle(Filter, enabled=enabled)
        return self.Filters

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
            F.Slider.setMinimum(min_value)
            F.Slider.setMaximum(max_value)
            F.Slider.setValue(value)
            self._filterSetEnabled(F, True)
        return Filters

    def freezeEQ(self):
        for F in self.Filters:
            self._filterSetEnabled(F, False)

    def filterHandle(self, freq: int, boost_cut: str, blockSignals=False):      # boost_cut: '+'/'-'
        return self._filterHandle(self.getFilter(freq), boost_cut, blockSignals=blockSignals)

    @staticmethod
    def _filterHandle(F: Filter, boost_cut: str, blockSignals=False):     # boost_cut: '+'/'-'
        F.Slider.blockSignals(blockSignals)
        if boost_cut == '+':
            F.Slider.setValue(F.Slider.maximum())
        elif boost_cut == '-':
            F.Slider.setValue(F.Slider.minimum())
        F.Slider.blockSignals(False)
        return F.Slider

    def filterSetEnabled(self, freq: int, arg: bool):
        return self._filterSetEnabled(self.getFilter(freq), arg)

    def _filterSetEnabled(self, F: Filter, arg: bool):
        if F.PermDisabled:
            return F
        F.Slider.setEnabled(arg)
        F.Label.setEnabled(arg)
        slider_style = F.Slider.styleSheet().replace(self.disabledHandleStyle, self.handleStyle) if arg else F.Slider.styleSheet().replace(self.handleStyle, self.disabledHandleStyle)
        F.Slider.setStyleSheet(slider_style)
        return F

    def rangeSetEnabled(self, freq1: int, freq2: int, arg: bool):
        freqs = [freq1, freq2]
        freqs.sort()
        for F in self.Filters:
            if freqs[0] <= F.freq <= freqs[1]:
                self._filterSetEnabled(F, arg)
        return self.Filters

    def rangeCrop(self, freq1: int, freq2: int):
        self.rangeSetEnabled(20, 20000, False)
        self.rangeSetEnabled(freq1, freq2, True)

    def setHandles(self, values: int or tuple, blockSignals=True):
        def freq_bc(_freq: int, _values: int or tuple):
            values_l = [values] if isinstance(values, int) else list(values)
            for v in values_l:
                if _freq == abs(v):
                    return '+' if v > 0 else '-'
            return '0'
        for F in self.Filters:
            self.filterHandle(F.freq, freq_bc(F.freq, values), blockSignals=blockSignals)

    def sortedFilters(self):
        filter_list = self.Filters
        filter_list.sort(key=lambda F: F.freq)
        return filter_list

    def getAdjacentFilters(self, F: Filter, arg: int or bool):     # arg: the number of adjacent filters from each side or False
        if not arg:
            return
        sorted_filters = self.sortedFilters()
        return findAdjacentEl(sorted_filters, F, num=arg)

    def disableAdjacentFilters(self, freq: int, num=1):   # num: the number of adjacent filters from each side
        if not num:
            return
        adj_filt = self.getAdjacentFilters(self.getFilter(freq), num)
        for F in adj_filt:
            self._filterSetEnabled(F, False)

    def enableAdjacentFilters(self, freq: int, num=1):   # num: the number of adjacent filters from each side
        adj_filt = self.getAdjacentFilters(self.getFilter(freq), num)
        for F in adj_filt:
            self._filterSetEnabled(F, True)

    def disableAdjacentFiltersMode(self, arg: int or bool):    # arg: the number of adjacent filters from each side or False
        self._DisableAdjacentFiltersMode = arg

    def case_DisableAdjacentFiltersModeOn(self, sliderValue: int, activeFreqRange=(20, 20000)):
        if not self._DisableAdjacentFiltersMode:
            return
        if sliderValue == 0:
            self.rangeSetEnabled(*activeFreqRange, True)
        for F in self.Filters:
            if F.Slider.value() != 0:
                self.disableAdjacentFilters(F.freq, num=self._DisableAdjacentFiltersMode)
