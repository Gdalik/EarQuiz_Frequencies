from GUI.MainWindow.View.mw_view import MainWindowView
from GUI.EQ.eq_contr import EQContr
from GUI.EQSettings.eqset_contr import EQSetContr
from GUI.PatternBox.patternbox_contr import PatternBoxContr
from GUI.Playlist.playlistcontr import PlaylistContr
from GUI.Modes.PreviewMode import PreviewMode
from GUI.Modes.LearnMode import LearnMode
from GUI.Modes.TestMode import TestMode
from GUI.Playlist.plsong import PlSong
from GUI.TransportPanel.transport_contr import TransportContr
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QActionGroup
from PyQt6.QtMultimedia import QMediaDevices
import platform


class MainWindowContr(QObject):
    def __init__(self):
        super().__init__()
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.EQContr = EQContr(self)
        self.EQSetContr = EQSetContr(self)
        self.PlaylistContr = PlaylistContr(self)
        self.PatternBoxContr = PatternBoxContr(self)
        self.TransportContr = TransportContr(self)
        self.mw_view.show()
        self.setFileMenuActions()
        self.setModesActions()
        self.setModesButtons()
        self.setPlaybackButtons()
        self.setShufflePBMode()
        self.CurrentMode = self.LastMode = None
        self.setNoAudio()
        self.audio_devices = QMediaDevices()


    def setFileMenuActions(self):
        self.mw_view.actionOpen.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='files'))
        self.mw_view.actionOpen_Folder.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='folder'))

    def setModesButtons(self):
        self.mw_view.PreviewBut.setDefaultAction(self.mw_view.actionPreview_Mode)
        self.mw_view.LearnBut.setDefaultAction(self.mw_view.actionLearn_Mode)
        self.mw_view.TestBut.setDefaultAction(self.mw_view.actionTest_Mode)

    def setModesActions(self):
        self.modesActionGroup = QActionGroup(self)
        self.modesActionGroup.addAction(self.mw_view.actionPreview_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionLearn_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionTest_Mode)
        self.modesActionGroup.setExclusive(True)
        self.mw_view.actionPreview_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionLearn_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionTest_Mode.toggled.connect(self.setCurrentMode)

    def setCurrentMode(self):
        if self.modesActionGroup.checkedAction() == self.mw_view.actionPreview_Mode:
            self.CurrentMode = PreviewMode(self)
        elif self.modesActionGroup.checkedAction() == self.mw_view.actionLearn_Mode:
            self.CurrentMode = LearnMode(self)
        elif self.modesActionGroup.checkedAction() == self.mw_view.actionTest_Mode:
            self.CurrentMode = TestMode(self)
        self.LastMode = self.CurrentMode

    def setNoAudio(self):
        self.SourceAudio = None
        self.TransportContr.noSongState()

    def setPlaybackButtons(self):
        self.mw_view.MW_PlayPause.setDefaultAction(self.mw_view.actionPlayPause)
        self.mw_view.MW_Stop.setDefaultAction(self.mw_view.actionStop)

    def setShufflePBMode(self):
        self.mw_view.actionShuffle_Playback.setChecked(False)
        self.mw_view.ShufflePlaybackBut.setDefaultAction(self.mw_view.actionShuffle_Playback)

    def load_song(self, Song: PlSong):
        if hasattr(Song, 'file_properties'):
            Song.__delattr__('file_properties')
        if Song.duration < 30 or not Song.exists:
            return
        self.SourceAudio = Song
        if self.CurrentMode is None or self.CurrentMode.name != 'Preview':
            self.mw_view.actionPreview_Mode.toggle()
        else:
            self.CurrentMode.updateCurrentAudio()
        self.TransportContr.PlayerContr.loadCurrentAudio()


