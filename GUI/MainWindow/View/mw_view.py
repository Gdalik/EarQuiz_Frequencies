from PySide6.QtWidgets import QMainWindow, QWidget, QProgressBar
from PySide6.QtCore import Qt
from GUI.MainWindow.View.mainwindow import Ui_MainWindow
from GUI.TransportPanel.transport_view import TransportPanelView
from GUI.PatternBox.patternbox_view import PatternBoxView
from GUI.EQ.eq_view import EqView
from GUI.EQSettings.eqset_view import EQSetView
import definitions


class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(definitions.app_name)
        self.TransportPanelView = TransportPanelView(self)
        self.PatternBoxView = PatternBoxView(self)
        self.EQView = EqView(self)
        self.EQSetView = EQSetView(self)
        self.status = self.statusBar()

        '''self.progress = QProgressBar(self)
        self.progress.setMaximumWidth(100)
        self.progress.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.progress.setTextVisible(True)
        self.status.addWidget(self.progress)
        self.progress.hide()'''

    def win_os_settings(self):
        widget_list = self.centralwidget.findChildren(QWidget) + self.dockWidgetContents.findChildren(QWidget) + self.dockWidgetContents_2.findChildren(QWidget) + self.dockWidgetContents_3.findChildren(QWidget)
        for W in widget_list:
            w_font = W.font()
            w_fontsize = w_font.pointSize()
            # print(f'{W.objectName()}:{w_fontsize}')
            if w_fontsize < 10:
                w_font.setPointSize(10)
            elif w_fontsize >= 18:
                w_font.setPointSize(w_fontsize - 4)
            elif 'TimeEdit' in W.objectName():
                w_font.setPointSize(11)
            W.setFont(w_font)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            print(event.mimeData().urls())
        else:
            event.ignore()

