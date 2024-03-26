#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
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

import contextlib
from Model.eq_patterns import EQPatterns
from Utilities.exceptions import InterruptedException
from application import Settings


class PatternBoxContr(object):
    def __init__(self, mw_contr):
        self.EQPatterns = EQPatterns()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.PatternBoxView.loadItems(self.getPatternNames())
        self.PatternBox = self.mw_view.PatternBox
        self.NextPatternBut = self.mw_view.NextPatternBut
        self.loadStoredPattern()
        self.onPatternBoxIndexChanged()
        self.PatternBox.currentIndexChanged.connect(self.onPatternBoxIndexChanged)
        self.NextPatternBut.clicked.connect(self.onNextPatternBut_clicked)
        self._nextPatternButEnable()

    def onPatternBoxIndexChanged(self, index=None):
        index = self.PatternBox.currentIndex() if index is None else index
        self.mw_contr.EQContr.setEQMode(mode_num=index + 1)
        self._nextPatternButEnable()
        if not self.mw_view.actionLockEQSettings.isChecked():
            self.mw_contr.EQSetContr.refreshSet()
        self.setExGenToPattern()
        self._restartExamples()
        self.saveLastPattern()

    def _restartExamples(self):
        with contextlib.suppress(AttributeError):
            if self.mw_contr.CurrentMode.name == 'Test':
                self.mw_contr.CurrentMode.restart_test()
            elif self.mw_contr.CurrentMode.name == 'Uni':
                self.mw_view.actionPreview_Mode.setChecked(True)
                return
            try:
                self.mw_contr.CurrentMode.nextDrill(fromStart=True, play_after=True)
            except InterruptedException:
                self.mw_view.actionPreview_Mode.setChecked(True)

    def setExGenToPattern(self):
        if not hasattr(self.mw_contr, 'SourceAudio') or self.mw_contr.SourceAudio is None:
            return
        if not hasattr(self.mw_contr, 'ADGen') or self.mw_contr.ADGen is None:
            return
        eq_pattern = self.mw_contr.EQContr.EQpattern
        exgen_order = self.mw_contr.freqOrder()
        self.mw_contr.ADGen.resetExGen(self.mw_contr.EQContr.getAvailableFreq(),
                                       boost_cut=eq_pattern['EQ_boost_cut'],
                                       DualBandMode=eq_pattern['DualBandMode'],
                                       order=exgen_order,
                                       boost_cut_priority=self.mw_contr.boostCutPriority,
                                       disableAdjacent=eq_pattern['DisableAdjacentFiltersMode'],
                                       inf_cycle=True)

    def onNextPatternBut_clicked(self):
        PBindex = self.PatternBox.currentIndex()
        max_index = self.PatternBox.count() - 1
        index = PBindex + 1 if PBindex < max_index else max_index
        self.PatternBox.setCurrentIndex(index)

    def _nextPatternButEnable(self):
        self.NextPatternBut.setEnabled(self.PatternBox.currentIndex() <
                                       self.PatternBox.count() - 1)

    def getPatternNames(self):
        return [mode['Name'] for mode in self.EQPatterns.List]

    def saveLastPattern(self):
        Settings.setValue('LastStuff/EQ_Pattern', self.PatternBox.currentText())

    def loadStoredPattern(self):
        stored_value = Settings.value('LastStuff/EQ_Pattern', self.PatternBox.itemText(0))
        self.PatternBox.setCurrentText(stored_value)
