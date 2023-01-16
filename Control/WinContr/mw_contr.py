from View.mw_view import MainWindowView
import platform


class MainWindowContr:
    def __init__(self):
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.mw_view.show()
        self.mw_view.EQ.setCurrentEq('EQ2')
        self.mw_view.EQ.resetEQ('EQ2', '+-')
        self.mw_view.EQ.highlight_right_Filter('EQ2', 1000, 'half-')
        # self.mw_view.EQ.FilterSetEnabled('EQ2', 1000, False)
        self.mw_view.EQ.rangeSetEnabled('EQ2', 6000, 100, False)
        # self.mw_view.EQ.rangeSetEnabled('EQ2', 0, 5000, True)
        self.mw_view.EQ.filterHandle('EQ2', 2000, '-')
        self.mw_view.EQ.filterHandle('EQ2', 8000, '+')