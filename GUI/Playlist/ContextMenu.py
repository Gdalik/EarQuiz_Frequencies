from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction
from Utilities.selectFileInSysExplorer import selectFile
import platform


class PLContextMenu(QMenu):
    actionLoad: QAction
    actionShowFile: QAction
    actionConvertAudio: QAction
    actionRemove: QAction

    def __init__(self, parent):     # parent: PlaylistContr
        super().__init__()
        self.parent = parent
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
        self.actionRemove = QAction('Remove')

    def createMenu(self):
        if len(self.selected_tracks) == 0:
            return
        if len(self.selected_tracks) == 1:
            self.addActions((self.actionLoad, self.actionShowFile))
            exists = self.selected_tracks[0].exists
            self.actionLoad.setEnabled(exists)
            self.actionShowFile.setEnabled(exists)
        self.actionConvertAudio.setEnabled(any((P.exists for P in self.selected_tracks)))
        self.addActions((self.actionConvertAudio, self.actionRemove))

    def showSelectedFile(self):
        filepath = self.selected_tracks[0].path
        selectFile(filepath)
