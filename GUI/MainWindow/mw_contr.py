from GUI.MainWindow.View.mw_view import MainWindowView
from GUI.EQ.eq_contr import EQContr
from GUI.EQSettings.eqset_contr import EQSetContr
from GUI.PatternBox.patternbox_contr import PatternBoxContr
from GUI.Playlist.playlistcontr import PlaylistContr
from PySide6.QtCore import QObject
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
        self.mw_view.show()
        self.setFileMenuActions()

    def setFileMenuActions(self):
        self.mw_view.actionOpen.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='files'))
        self.mw_view.actionOpen_Folder.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='folder'))


