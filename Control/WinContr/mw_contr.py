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
