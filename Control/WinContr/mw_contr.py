from View.mw_view import MainWindowView
from Control.WinContr.eq_contr import EQContr
import platform


class MainWindowContr:
    def __init__(self):
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.mw_view.show()
        self.EQContr = EQContr(self.mw_view)
        self.mw_view.PatternBox.currentIndexChanged.connect(self.onPatternBoxIndexChanged)
        self.mw_view.NextPatternBut.clicked.connect(self.onNextPatternBut_clicked)

    def onPatternBoxIndexChanged(self, index):
        self.EQContr.setEQMode(mode_num=index + 1)
        self.mw_view.NextPatternBut.setEnabled(index < self.mw_view.PatternBox.count() - 1)

    def onNextPatternBut_clicked(self):
        PBindex = self.mw_view.PatternBox.currentIndex()
        max_index = self.mw_view.PatternBox.count() - 1
        index = PBindex+1 if PBindex < max_index else max_index
        self.mw_view.PatternBox.setCurrentIndex(index)
