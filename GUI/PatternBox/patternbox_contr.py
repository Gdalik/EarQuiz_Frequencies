import contextlib
from Utilities.exceptions import InterruptedException
from Model.eq_patterns import EQPatterns


class PatternBoxContr(object):
    def __init__(self, mw_contr):
        self.EQPatterns = EQPatterns()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.PatternBoxView.loadItems(self.getPatternNames())
        self.onPatternBoxIndexChanged()
        self.mw_view.PatternBox.currentIndexChanged.connect(self.onPatternBoxIndexChanged)
        self.mw_view.NextPatternBut.clicked.connect(self.onNextPatternBut_clicked)
        self._nextPatternButEnable()

    def onPatternBoxIndexChanged(self, index=None):
        index = self.mw_view.PatternBox.currentIndex() if index is None else index
        self.mw_contr.EQContr.setEQMode(mode_num=index + 1)
        self._nextPatternButEnable()
        self.mw_contr.EQSetContr.refreshSet()
        self.setExGenToPattern()
        with contextlib.suppress(AttributeError):
            if self.mw_contr.CurrentMode.name == 'Test':
                self.mw_contr.CurrentMode.restart_test()
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
        exgen_order = self.mw_contr.freqOrder
        self.mw_contr.ADGen.resetExGen(self.mw_contr.EQContr.getAvailableFreq(),
                                       boost_cut=eq_pattern['EQ_boost_cut'],
                                       DualBandMode=eq_pattern['DualBandMode'],
                                       order=exgen_order,
                                       boost_cut_priority=self.mw_contr.boostCutPriority,
                                       disableAdjacent=eq_pattern['DisableAdjacentFiltersMode'],
                                       inf_cycle=True)

    def onNextPatternBut_clicked(self):
        PBindex = self.mw_view.PatternBox.currentIndex()
        max_index = self.mw_view.PatternBox.count() - 1
        index = PBindex+1 if PBindex < max_index else max_index
        self.mw_view.PatternBox.setCurrentIndex(index)

    def _nextPatternButEnable(self):
        self.mw_view.NextPatternBut.setEnabled(self.mw_view.PatternBox.currentIndex() <
                                               self.mw_view.PatternBox.count() - 1)

    def getPatternNames(self):
        return [mode['Name'] for mode in self.EQPatterns.List]
