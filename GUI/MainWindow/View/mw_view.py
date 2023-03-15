import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QSizePolicy, QToolButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from GUI.MainWindow.View.mainwindow import Ui_MainWindow
from GUI.TransportPanel.transport_view import TransportPanelView
from GUI.PatternBox.patternbox_view import PatternBoxView
from GUI.EQ.eq_view import EqView
from GUI.EQSettings.eqset_view import EQSetView
from GUI.MainWindow.View.audiodevices_view import AudioDevicesView
from GUI.Misc.error_message import error_message
import definitions


class MainWindowView(QMainWindow, Ui_MainWindow):
    actionUni_Mode: QAction
    UniBut: QToolButton
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._flags = self.windowFlags()
        self.setDockOptions(self.dockOptions().AnimatedDocks)
        self.setWindowTitle(definitions.app_name)
        self.TransportPanelView = TransportPanelView(self)
        self.PatternBoxView = PatternBoxView(self)
        self.EQView = EqView(self)
        self.EQSetView = EQSetView(self)
        self.setViewMenuActions()
        self.AudioDevicesView = AudioDevicesView(self)
        self.status = self.statusBar()
        self.setMinimalistView()
        self.actionMinimal.triggered.connect(self.setMinimalistView)
        self.setUniActBut()
        self.alt_pressed = None
        self.setFocus()

        '''
        self.status.addWidget(self.progress)'''

    def win_os_settings(self):
        widget_list = self.centralwidget.findChildren(QWidget) + self.dockWidgetContents.findChildren(QWidget) + \
                      self.dockWidgetContents_2.findChildren(QWidget) + self.dockWidgetContents_3.findChildren(QWidget)
        for W in widget_list:
            w_font = W.font()
            w_fontsize = w_font.pointSize()
            # print(f'{W.objectName()}:{w_fontsize}')
            if w_fontsize < 10:
                w_font.setPointSize(10)
            elif w_fontsize >= 16:
                w_font.setPointSize(w_fontsize - 4)
            elif 'TimeEdit' in W.objectName():
                w_font.setPointSize(11)
            W.setFont(w_font)
        timelab_fonts = self.Position_Lab.font()
        timelab_fonts.setPointSize(15)
        self.Position_Lab.setFont(timelab_fonts)
        self.Duration_Lab.setFont(timelab_fonts)
        self.NextPatternBut.setMinimumSize(26, 26)
        self.NextPatternBut.setMaximumSize(26, 26)

    def keyPressEvent(self, event):
        super(MainWindowView, self).keyPressEvent(event)
        if event.key() == Qt.Key.Key_Alt:
            self.alt_pressed = True
        event.accept()

    def keyReleaseEvent(self, event):
        super(MainWindowView, self).keyReleaseEvent(event)
        if event.key() == Qt.Key.Key_Alt:
            self.alt_pressed = False
        event.accept()

    def setViewMenuActions(self):
        DockActions = self.createPopupMenu().actions()
        for item in DockActions:
            self.menuView.addAction(item)

    def setUniActBut(self):
        self.actionUni_Mode = QAction(parent=self)
        self.actionUni_Mode.setCheckable(True)
        self.UniBut = QToolButton(parent=self.ModeButtonsGroupBox)
        self.UniBut.setVisible(False)
        self.UniBut.setCheckable(True)
        self.UniBut.setDefaultAction(self.actionUni_Mode)
        self.buttonGroup.addButton(self.UniBut)

    def setMinimalistView(self):
        if self.isFullScreen():
            self.setWindowFlags(self._flags)
            self.showNormal()
        self.ExScoreInfo.hide()
        self.Eq_Settings.hide()
        self.SupportProject.hide()
        self.TransportPanel.hide()
        self.set_size(1080, 700)

    def set_size(self, width: int, height: int):
        self.setFixedSize(width, height)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self.setMinimumSize(width, height)
        self.setMaximumSize(16777215, 16777215)

    def setActionNextExerciseEnabled(self, arg):
        self.actionNext_Exercise.setEnabled(arg)
        self.actionNext_Exercise.setVisible(arg)
        # self.NextExercise.setVisible(arg)

    def mousePressEvent(self, event):
        super(MainWindowView, self).mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.setFocus()

    def error_msg(self, message: str):
        error_message(self, message)

    def setEQStateIndicatorOn(self, arg: bool):
        self.EqOnOffLab.setVisible(True)
        if arg:
            self.EqOnOffLab.setText('EQ On')
            self.EqOnOffLab.setStyleSheet('color: green; font-weight: bold')
        else:
            self.EqOnOffLab.setText('EQ Off')
            self.EqOnOffLab.setStyleSheet('color: gray; font-weight: bold')
