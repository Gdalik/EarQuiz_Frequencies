from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QSortFilterProxyModel, QModelIndex
from GUI.Playlist.plsong import PlSong
from pathlib import Path
from Utilities.urlcheck import validUrls
import copy

PlaylistData = []


class PlaylistModel(QtCore.QAbstractTableModel):
    def __init__(self, playlistdata=None):
        super().__init__()
        self.playlistdata = playlistdata or []
        self.nonLoadedSong_paths = set()
        self.CurName = None
        self.MimeTypes = 'text/uri-list'
        self.filtered = False
        self.SelectedRows = []
        self.lastInsertedRows = []

    def data(self, index, role: int):
        CurData = self.playlistdata[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return [CurData.name, CurData.duration_str, CurData.dirPath][index.column()]
        if role == Qt.ItemDataRole.ForegroundRole and not CurData.exists:
            return QtGui.QColor('red')
        elif role == Qt.ItemDataRole.ForegroundRole and not CurData.available:
            return QtGui.QColor('gray')

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
        urls = validUrls(data.urls())
        if not urls:
            return False
        rows_count = len(urls)
        self.insertRows(row, rows_count, parent)

        for r in range(rows_count):
            CurData = PlSong(str(Path(urls[r].toLocalFile()).absolute()))
            CurData.canLoad = CurData.path not in self.nonLoadedSong_paths
            self.setData(self.index(row + r, 0, parent), CurData)

        return True

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
        self.beginInsertRows(parent, row, row + count - 1)
        self.lastInsertedRows.clear()
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
    def __init__(self, parent, **kwargs):
        super().__init__()
        self.setSourceModel(parent.playlistModel)
        self._filter_string = ''

    def setFilter(self, pattern: str):
        self._filter_string = pattern.lower()
        self.setFilterFixedString(self._filter_string)
        self.sourceModel().filtered = bool(pattern)

    def filterAcceptsRow(self, source_row: int, source_parent):
        index0 = self.sourceModel().index(source_row, 0, source_parent)
        index2 = self.sourceModel().index(source_row, 2, source_parent)
        return self._filter_string in self.sourceModel().data(index0, role=Qt.ItemDataRole.DisplayRole).lower() or \
               self._filter_string in self.sourceModel().data(index2, role=Qt.ItemDataRole.DisplayRole).lower()
