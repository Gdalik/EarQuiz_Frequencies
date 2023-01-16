from View.mw_view import MainWindowView
import platform


class MainWindowContr:
    def __init__(self):
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.mw_view.show()
        self.mw_view.EQ.setCurrentEq('EQ2')
        self.mw_view.EQ.highlight_right_Filter('EQ2', 10000, 'full')
        self.mw_view.EQ.resetEQ('EQ2', '+-')
