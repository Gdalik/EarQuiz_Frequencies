from GUI.MainWindow.View.mw_view import MainWindowView
from GUI.EQ.eq_contr import EQContr
from GUI.EQSettings.eqset_contr import EQSetContr
from GUI.PatternBox.patternbox_contr import PatternBoxContr
import platform


class MainWindowContr:
    def __init__(self):
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.EQContr = EQContr(self)
        self.EQSetContr = EQSetContr(self)
        self.PatternBoxContr = PatternBoxContr(self)
        self.mw_view.show()


