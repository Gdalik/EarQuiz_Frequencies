from PySide6.QtWidgets import QWidget

class EqView():
    """@DynamicAttrs"""
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.TabWidget = mw_view.EQtabWidget
        self.TabWidget.setTabText(0, '10-Band Equalizer')
        self.TabWidget.setTabText(1, '30-Band Equalizer')
        for W in mw_view.EQtabWidget.findChildren(QWidget):
            self.__setattr__(W.objectName(), W)

    def setCurrentEq(self, eq: str):    # 'EQ1' / 'EQ2'
        if eq == 'EQ1':
            self.TabWidget.setTabVisible(0, True)
            self.TabWidget.setTabVisible(1, False)
        elif eq == 'EQ2':
            self.TabWidget.setTabVisible(0, False)
            self.TabWidget.setTabVisible(1, True)
        # set the style sheet
        # self.TabWidget.setStyleSheet("QTabBar::EQ2::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")