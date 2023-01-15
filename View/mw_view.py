from PySide6.QtWidgets import QMainWindow, QWidget
from View.mainwindow import Ui_MainWindow
from View.transport_view import TransportPanelView
from View.eq_view import EqView


class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.TransportPanel = TransportPanelView(self)
        self.EQ = EqView(self)
        self.EQ.setCurrentEq('EQ2')

    def win_os_settings(self):
        widget_list = self.centralwidget.findChildren(QWidget) + self.dockWidgetContents.findChildren(QWidget) + self.dockWidgetContents_2.findChildren(QWidget) + self.dockWidgetContents_3.findChildren(QWidget)
        for W in widget_list:
            w_font = W.font()
            w_fontsize = w_font.pointSize()
            print(f'{W.objectName()}:{w_fontsize}')
            if w_fontsize < 10:
                w_font.setPointSize(10)
            elif 18 <= w_fontsize <= 20:
                w_font.setPointSize(w_fontsize - 2)
            elif w_fontsize > 20:
                w_font.setPointSize(w_fontsize - 4)
            W.setFont(w_font)
