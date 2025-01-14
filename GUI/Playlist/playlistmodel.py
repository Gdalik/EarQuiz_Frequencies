#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from pathlib import Path
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QSortFilterProxyModel, QModelIndex, QRegularExpression
from PyQt6.QtGui import QImage
from GUI.Playlist.plsong import PlSong
from GUI.MainWindow.View.dark_theme import playlist_even_background_color
from Model.globals import MinAudioDuration

PlaylistData = []


class PlaylistModel(QtCore.QAbstractTableModel):
    def __init__(self, playlistdata=None):
        super().__init__()
        self.playlistdata = playlistdata or []
        self.nonLoadedSong_paths = set()
        self.CurName = None
        self.currentSong = None
        self.MimeTypes = 'text/uri-list'
        self.filtered = False
        self.SelectedRows = []
        self.lastInsertedRows = []

    def data(self, index, role: int):
        CurData = self.playlistdata[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return [CurData.name, CurData.duration_str, CurData.dirPath][index.column()]
        if role == Qt.ItemDataRole.ForegroundRole:
            if not CurData.exists:
                return QtGui.QColor('red')
            elif index.column() == 1 and (not CurData.duration or
                                        (CurData.duration and CurData.duration < MinAudioDuration)):
                return QtGui.QColor('red')
            elif not CurData.available:
                return QtGui.QColor('gray')
        if role == Qt.ItemDataRole.BackgroundRole and index.row() % 2 != 0:
            return playlist_even_background_color()
        if (
                role == Qt.ItemDataRole.DecorationRole
                and index.column() == 0
                and self.currentSong == CurData
        ):
            return QImage(':/Player/Icons/Player/CurrentSong.png')

    def rowCount(self, index):
        return len(self.playlistdata)

    def columnCount(self, index):
        return 3 if self.playlistdata else 0

    def mimeTypes(self):
        return [self.MimeTypes]

    def flags(self, index):
        flags = super().flags(index)
        if index.isValid():
            flags |= Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsDragEnabled
        else:
            flags |= Qt.ItemFlag.ItemIsDropEnabled
        return flags

    def canDropMimeData(self, data, action, row, col, parent):
        return data.hasFormat(self.MimeTypes) and not self.filtered

    def dropMimeData(self, data, action, row, column, parent):
        if self.canDropMimeData(data, action, row, column, parent) is False:
            return False
        if row == -1:
            row = len(self.playlistdata)
        # urls = validUrls(data.urls())
        urls = data.urls()
        if not urls:
            return False
        selected_songs = [self.playlistdata[ind] for ind in self.SelectedRows]
        rows_count = len(urls)
        self.insertRows(row, rows_count, parent)
        for r in range(rows_count):
            CurData = next(self.plSongsYielder(selected_songs, str(Path(urls[r].toLocalFile()).absolute())))
            self.setData(self.index(row + r, 0, parent), CurData)

        return True

    @staticmethod
    def plSongsYielder(song_list: list[PlSong], song_path: str):
        for ind, S in enumerate(song_list):
            if S.path == song_path:
                yield song_list.pop(ind)

    def supportedDropActions(self):
        return Qt.DropAction.MoveAction

    def setData(self, index, value, role=Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return False
        self.playlistdata[index.row()] = value
        return True

    def insertRows(self, row: int, count: int, parent):
        if parent.isValid():
            return False
        if row < 0:
            return False
        self.lastInsertedRows.clear()
        self.beginInsertRows(parent, row, row + count - 1)
        for i in range(count):
            row_ind = row + i
            self.playlistdata.insert(row_ind, PlSong(''))
            self.lastInsertedRows.append(row_ind)
        self.endInsertRows()
        return True

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        if parent.isValid():
            return False
        if row < 0:
            return False
        self.SelectedRows.sort()
        for R in reversed(self.SelectedRows):
            self.beginRemoveRows(parent, R, R)
            self.playlistdata.pop(R)
            self.endRemoveRows()
        if len(self.lastInsertedRows) != 0 and row < self.lastInsertedRows[0]:
            self.lastInsertedRows = list(map(lambda x: x - count, self.lastInsertedRows))
        return True

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ['Filename', 'Duration', 'Folder Path'][section]

    def updCanLoadData(self, changeLayout=True):
        if changeLayout:
            self.layoutAboutToBeChanged.emit()
        for S in self.playlistdata:
            S.canLoad = S.path not in self.nonLoadedSong_paths
        if changeLayout:
            self.layoutChanged.emit()


class PLSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent):
        super().__init__()
        self.setSourceModel(parent.playlistModel)
        self._filter_string = ''

    def setFilter(self, pattern: str):
        self._filter_string = pattern
        self.setFilterWildcard(None)
        self.sourceModel().filtered = bool(pattern)

    def filterAcceptsRow(self, source_row: int, source_parent) -> bool:
        index0 = self.sourceModel().index(source_row, 0, source_parent)
        index2 = self.sourceModel().index(source_row, 2, source_parent)
        return (self._wcMatch(self._filter_string, self.sourceModel().data(index0, role=Qt.ItemDataRole.DisplayRole)) or
                self._wcMatch(self._filter_string, self.sourceModel().data(index2, role=Qt.ItemDataRole.DisplayRole)))

    @staticmethod
    def _wcMatch(wc_pattern: str, string: str) -> bool:
        re_pattern = QtCore.QRegularExpression.fromWildcard(wc_pattern, Qt.CaseSensitivity.CaseInsensitive,
                                                            QRegularExpression.WildcardConversionOption.UnanchoredWildcardConversion)
        return re_pattern.match(string).hasMatch()
