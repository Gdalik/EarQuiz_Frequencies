from GUI.Playlist.playlistmodel import PlaylistData, PlaylistModel, PLSortFilterProxyModel
from GUI.Playlist.plsong import PlSong
from PySide6.QtCore import QObject, Qt, QModelIndex
from definitions import app
from GUI.Playlist.FileLinksParser import pathsResolve


class PlaylistContr(QObject):
    def __init__(self, parent):
        super().__init__()
        self.playlistData = PlaylistData
        self.playlistModel = PlaylistModel(playlistdata=self.playlistData)
        self.mw_view = parent.mw_view
        self.playlistView = self.mw_view.PlaylistView
        self.proxyModel = PLSortFilterProxyModel(self)
        self.playlistView.setModel(self.proxyModel)
        self.selModel = self.playlistView.selectionModel()
        self.selModel.selectionChanged.connect(self.playlistView.onSelectionChanged)
        self.Search = self.mw_view.SearchAudio
        self.Search.textChanged.connect(self.proxyModel.setFilter)
        self.playlistView.signals.urlsDropped.connect(self.addTracks)
        self.playlistView.signals.dragDropFromPLFinished.connect(self.ondragDropFromPLFinished)

    def addTracks(self, URLs: list, index=-1):
        app.setOverrideCursor(Qt.CursorShape.BusyCursor)
        paths = [url.path() for url in URLs]
        paths = pathsResolve(paths)
        tracklist = list(map(lambda p: PlSong(p), paths))
        _index = len(self.playlistModel.playlistdata) if index == -1 else index
        self.playlistModel.layoutAboutToBeChanged.emit()
        self.playlistModel.playlistdata[_index:_index] = tracklist
        self.playlistModel.layoutChanged.emit()
        if len(self.playlistModel.playlistdata) != len(paths):
            self.playlistView.selectRows(_index, _index + len(paths) - 1)
            self.playlistView.onSelectionChanged()  # onSelectionChanged signal is not emitted after layoutChange
        app.restoreOverrideCursor()

    def ondragDropFromPLFinished(self, action):
        if action == Qt.DropAction.MoveAction and self.playlistView.selectedIndexes():
            self.playlistModel.removeRows(self.selModel.selectedRows()[0].row(),
                                          len(self.selModel.selectedRows()), QModelIndex())
            self.playlistView.selectRows(self.playlistModel.lastInsertedRows[0],
                                         self.playlistModel.lastInsertedRows[-1])
