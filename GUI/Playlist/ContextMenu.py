import platform

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

from Utilities.selectFileInSysExplorer import selectFile


class PLContextMenu(QMenu):
    actionLoad: QAction
    actionShowFile: QAction
    actionConvertAudio: QAction
    actionRemove: QAction
    actionRemoveUnavailable: QAction

    def __init__(self, parent):  # parent: PlaylistContr
        super().__init__()
        self.parent = parent
        self.playlistdata = self.parent.playlistModel.playlistdata
        self.selected_tracks = self.parent.PlaylistView.selectedItems
        self.createActions()
        self.createMenu()

    def createActions(self):
        self.actionLoad = QAction('Load in Preview Mode', self)
        filemanager = 'Finder' if platform.system() == 'Darwin' else 'Explorer'
        self.actionShowFile = QAction(f'Show in {filemanager}')
        self.actionShowFile.triggered.connect(self.showSelectedFile)
        file_word = 'File' if len(self.selected_tracks) == 1 else 'Files'
        self.actionConvertAudio = QAction(f'Convert Selected {file_word}...')
        self.actionRemove = QAction('Remove Selected')
        self.actionRemoveUnavailable = QAction('Remove Unavailable')

    def createMenu(self):
        if len(self.playlistdata) == 0:
            return
        if len(self.selected_tracks) == 1:
            self._createSingleSelectedTrackMenu()
        remove_sep = False
        if len(self.selected_tracks) >= 1:
            self.actionConvertAudio.setEnabled(any((P.exists for P in self.selected_tracks)))
            self.addAction(self.actionConvertAudio)
            self.addSeparator()
            remove_sep = True
            self.addAction(self.actionRemove)
        if not remove_sep:
            self.addSeparator()
        unavailable_present = any((not S.available for S in self.playlistdata))
        self.actionRemoveUnavailable.setEnabled(unavailable_present)
        if unavailable_present or len(self.selected_tracks) > 0:
            self.addAction(self.actionRemoveUnavailable)

    def _createSingleSelectedTrackMenu(self):
        self.addAction(self.actionLoad)
        self.addSeparator()
        self.addAction(self.actionShowFile)
        exists = self.selected_tracks[0].exists
        self.actionLoad.setEnabled(exists)
        self.actionShowFile.setEnabled(exists)

    def showSelectedFile(self):
        filepath = self.selected_tracks[0].path
        selectFile(filepath)
