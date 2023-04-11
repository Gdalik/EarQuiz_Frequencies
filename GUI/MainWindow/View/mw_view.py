import contextlib
import datetime
from functools import partial
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QDockWidget
from PyQt6.QtWidgets import QMainWindow, QWidget, QToolButton
import definitions
from GUI.EQ.eq_view import EqView
from GUI.EQSettings.eqset_view import EQSetView
from GUI.MainWindow.View.StatusBar import StatusBar
from GUI.MainWindow.View.audiodevices_view import AudioDevicesView
from GUI.MainWindow.View.mainwindow import Ui_MainWindow
from GUI.Misc.error_message import error_message
from GUI.PatternBox.patternbox_view import PatternBoxView
from GUI.TransportPanel.transport_view import TransportPanelView
from Utilities.str2bool import str2bool
from definitions import Settings


class MW_Signals(QObject):
    appClose = pyqtSignal()


class MainWindowView(QMainWindow, Ui_MainWindow):
    actionUni_Mode: QAction
    actionTransportPanelView: QAction
    UniBut: QToolButton
    signals = MW_Signals()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._flags = self.windowFlags()
        self.setDockOptions(self.dockOptions().AnimatedDocks)
        self.setWindowTitle(definitions.app_name)
        self.status = StatusBar(self)
        self.PatternBoxView = PatternBoxView(self)
        self.EQView = EqView(self)
        self.EQSetView = EQSetView(self)
        self._setUpEQSettingsButtons()
        self.AudioDevicesView = AudioDevicesView(self)
        self.restoreWindowView()
        self._setWinViewActions()
        self.TransportPanelView = TransportPanelView(self)
        self.setUniActBut()
        self.alt_pressed = None
        self.setFocus()
        self.SupportProject.visibilityChanged.connect(self.onSupportProjectVisibilityChanged)
        self.TransportPanelViewBut.setDefaultAction(self.actionTransport_Panel_view)
        self._restoreActionsState()
        self._connectActionsToSaver()

    def win_os_settings(self):
        widget_list = self.centralwidget.findChildren(QWidget) + self.dockWidgetContents.findChildren(QWidget) + \
                      self.dockWidgetContents_2.findChildren(QWidget) + self.dockWidgetContents_3.findChildren(QWidget)
        for W in widget_list:
            w_font = W.font()
            w_fontsize = w_font.pointSize()
            if w_fontsize >= 16:
                w_font.setPointSize(w_fontsize - 4)
            elif w_fontsize >= 11:
                w_font.setPointSize(w_fontsize - 2)
            elif 'TimeEdit' in W.objectName():
                w_font.setPointSize(11)
            W.setFont(w_font)
        NextPatternBut_font = self.NextPatternBut.font()
        NextPatternBut_font.setPointSize(16)
        self.NextPatternBut.setFont(NextPatternBut_font)
        timelab_fonts = self.Position_Lab.font()
        timelab_fonts.setPointSize(14)
        self.Position_Lab.setFont(timelab_fonts)
        self.Duration_Lab.setFont(timelab_fonts)
        pl_stats_font = self.PL_Stats_Lab.font()
        pl_stats_font.setPointSize(8)
        self.PL_Stats_Lab.setFont(pl_stats_font)
        self.VolumeSlider.setStyleSheet("")

    def _setWinViewActions(self):
        self.actionMinimal.triggered.connect(self.setMinimalistView)
        self.actionMaximal.triggered.connect(self.setMaximalistView)
        self.actionMinimize.triggered.connect(self.showMinimized)
        self.actionZoom.triggered.connect(self.showMaximized)
        self.actionMinimize_All_Windows.triggered.connect(self.minimizeAllWindows)

    def keyPressEvent(self, event):
        super(MainWindowView, self).keyPressEvent(event)
        if event.key() == Qt.Key.Key_Alt:
            self.alt_pressed = True
            self.PlaylistView.alt_pressed = True
        event.accept()

    def keyReleaseEvent(self, event):
        super(MainWindowView, self).keyReleaseEvent(event)
        if event.key() == Qt.Key.Key_Alt:
            self.alt_pressed = False
            self.PlaylistView.alt_pressed = False
        event.accept()

    def _setUpEQSettingsButtons(self):
        icon = self.EQSettings_But1.icon()
        self.actionEQ_Settings_view.setIconVisibleInMenu(False)
        self.actionEQ_Settings_view.setIcon(icon)
        self.EQSettings_But1.setDefaultAction(self.actionEQ_Settings_view)
        self.EQSettings_But2.setDefaultAction(self.actionEQ_Settings_view)

    def setUniActBut(self):
        self.actionUni_Mode = QAction(parent=self)
        self.actionUni_Mode.setCheckable(True)
        self.UniBut = QToolButton(parent=self.ModeButtonsGroupBox)
        self.UniBut.setVisible(False)
        self.UniBut.setCheckable(True)
        self.UniBut.setDefaultAction(self.actionUni_Mode)
        self.ModeButtonGroup.addButton(self.UniBut)

    def setMinimalistView(self):
        if self.isFullScreen() or self.isMaximized():
            self.setWindowFlags(self._flags)
            self.showNormal()
        self.ExScoreInfo.hide()
        self.Eq_Settings.hide()
        self.SupportProject.hide()
        self.TransportPanel.hide()
        av_geom = definitions.app.primaryScreen().availableGeometry()
        width = min(self.width(), 1100, av_geom.width() - 10)
        height = min(self.height(), 700, av_geom.height() - 30)
        self.resize(width, height)

    def setMaximalistView(self):
        self.showMaximized()
        self.showFullScreen()
        self.ExScoreInfo.show()
        self.Eq_Settings.show()
        self.SupportProject.show()
        self.TransportPanel.show()

    def setActionNextExampleEnabled(self, arg):
        self.actionNext_Example.setEnabled(arg)
        self.actionNext_Example.setVisible(arg)

    def mousePressEvent(self, event):
        super(MainWindowView, self).mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            self.setFocus()

    def error_msg(self, message: str):
        error_message(self, message)

    def setEQStateIndicatorOn(self, arg: bool):
        self.EqOnOffLab.setVisible(True)
        self.status.EQStateLabel.setVisible(True)
        if arg:
            self.EqOnOffLab.setText('EQ On')
            self.EqOnOffLab.setStyleSheet('color: green; font-weight: bold')
        else:
            self.EqOnOffLab.setText('EQ Off')
            self.EqOnOffLab.setStyleSheet('color: gray; font-weight: bold')
        self.status.EQStateLabel.update(isOn=arg)

    def closeEvent(self, ev):
        self.signals.appClose.emit()
        super(MainWindowView, self).closeEvent(ev)

    def onActionSequentialPlaybackTriggered(self):
        self.actionLoop_Sequence.setEnabled(self.actionSequential_Playback.isChecked())

    def storeWindowView(self):
        Settings.setValue('MainWindow/Geometry', self.geometry())
        self._saveDockWidgets(self.dockWidgets)

    def restoreWindowView(self):
        geometry = Settings.value('MainWindow/Geometry', None)
        if geometry is None:
            self.setMinimalistView()
            return
        self.setGeometry(geometry)
        self._restoreDockWidgets(self.dockWidgets)

    @property
    def dockWidgets(self):
        return self.findChildren(QDockWidget)

    def _saveDockWidgets(self, objects: list[QDockWidget] or tuple[QDockWidget]):
        for obj in objects:
            self._saveDockWidget(obj)

    def _restoreDockWidgets(self, objects: list[QDockWidget] or tuple[QDockWidget]):
        for obj in objects:
            self._restoreDockWidget(obj)

    def minimizeAllWindows(self):
        self.showMinimized()
        DockWidgets = self.findChildren(QDockWidget)
        for W in DockWidgets:
            if W.isFloating():
                W.setHidden(True)

    @staticmethod
    def _saveDockWidget(obj: QDockWidget):
        Settings.beginGroup('MainWindow')
        Settings.setValue(obj.objectName(), {'Visible': obj.isVisible(),
                                             'Floating': obj.isFloating(),
                                             'Geometry': obj.geometry()})
        Settings.endGroup()

    @staticmethod
    def _restoreDockWidget(obj: QDockWidget):
        Settings.beginGroup('MainWindow')
        with contextlib.suppress(TypeError, KeyError):
            obj.setVisible(Settings.value(obj.objectName())['Visible'])
            obj.setFloating(Settings.value(obj.objectName())['Floating'])
            obj.setGeometry(Settings.value(obj.objectName())['Geometry'])
        Settings.endGroup()

    def _restoreActionsState(self):
        self.loadActionState(self.actionStartPlayingAfterLoading, default=True)
        self.loadActionState(self.actionSkip_Unavailable_Tracks, default=True)
        self.loadActionState(self.actionLoop_Playback, default=True)
        self.loadActionState(self.actionShuffle_Playback, default=False)
        self.loadActionState(self.actionRepeat_Playlist, default=True)
        self.loadActionState(self.actionSequential_Playback, default=False)
        self.loadActionState(self.actionLoop_Sequence, default=False)
        self.loadActionState(self.actionAscendingEQ, default=True)
        self.loadActionState(self.actionDescendingEQ, default=False)
        self.loadActionState(self.actionShuffleEQ, default=False)
        self.loadActionState(self.actionEach_Band_Boosted_then_Cut, default=True)
        self.loadActionState(self.actionAll_Bands_Boosted_then_All_Bands_Cut, default=False)

    def _connectActionsToSaver(self):
        controlActions = [self.actionStartPlayingAfterLoading, self.actionSkip_Unavailable_Tracks,
                          self.actionLoop_Playback, self.actionShuffle_Playback, self.actionRepeat_Playlist,
                          self.actionSequential_Playback, self.actionLoop_Sequence,
                          self.actionAscendingEQ, self.actionDescendingEQ, self.actionShuffleEQ,
                          self.actionEach_Band_Boosted_then_Cut, self.actionAll_Bands_Boosted_then_All_Bands_Cut]
        for act in controlActions:
            act.toggled.connect(partial(self.saveActionState, act))

    @staticmethod
    def loadActionState(obj: QAction, default=None):
        value = Settings.value(f'Actions/{obj.objectName()}', default)
        if value is not None:
            obj.setChecked(str2bool(value))

    @staticmethod
    def saveActionState(obj: QAction):
        Settings.setValue(f'Actions/{obj.objectName()}', obj.isChecked())

    def onSupportProjectVisibilityChanged(self, arg: bool):
        if arg:
            return
        Settings.setValue(f'MainWindow/{self.SupportProject.objectName()}_LastClosed', datetime.datetime.now())
