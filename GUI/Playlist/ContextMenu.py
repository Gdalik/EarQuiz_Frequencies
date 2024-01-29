#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
        self.menuCreated = False
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
            remove_sep = True
            self._createMultipleSelectedTrackMenu()
        if not remove_sep:
            self.addSeparator()
        unavailable_present = any((not S.available for S in self.playlistdata))
        self.actionRemoveUnavailable.setEnabled(unavailable_present)
        if unavailable_present or len(self.selected_tracks) > 0:
            self.addAction(self.actionRemoveUnavailable)
            self.menuCreated = True

    def _createSingleSelectedTrackMenu(self):
        self.addAction(self.actionLoad)
        self.addSeparator()
        self.addAction(self.actionShowFile)
        exists = self.selected_tracks[0].exists
        self.actionLoad.setEnabled(exists)
        self.actionShowFile.setEnabled(exists)
        self.menuCreated = True

    def _createMultipleSelectedTrackMenu(self):
        self.actionConvertAudio.setEnabled(any((P.exists for P in self.selected_tracks)))
        self.addAction(self.actionConvertAudio)
        self.addSeparator()
        self.addAction(self.actionRemove)
        self.menuCreated = True

    def showSelectedFile(self):
        filepath = self.selected_tracks[0].path
        selectFile(filepath)
