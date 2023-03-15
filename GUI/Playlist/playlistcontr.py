from GUI.Playlist.playlistmodel import PlaylistData, PlaylistModel, PLSortFilterProxyModel
from GUI.Playlist.plsong import PlSong
from GUI.Playlist.PLLoadDialog import PLProcDialog
from GUI.Playlist.PlaylistNavigation import PlNavi
from GUI.Misc.error_message import error_message
from PyQt6.QtCore import QObject, Qt, QModelIndex, QUrl
from PyQt6.QtWidgets import QFileDialog, QWidget
from definitions import app


class PlaylistContr(QObject):
    """@DynamicAttrs"""
    def __init__(self, parent):
        super().__init__()
        self.mw_view = parent.mw_view
        self.mw_contr = parent
        for W in self.mw_view.SourceBox.findChildren(QWidget):
            self.__setattr__(W.objectName(), W)
        self.playlistData = PlaylistData
        self.playlistModel = PlaylistModel(playlistdata=self.playlistData)
        self.proxyModel = PLSortFilterProxyModel(self)
        self.PlaylistView.setModel(self.proxyModel)
        self.PlNavi = PlNavi(self.playlistModel.playlistdata, shuffle=self.mw_view.actionShuffle_Playback.isChecked())
        self.selModel = self.PlaylistView.selectionModel()
        self.selModel.selectionChanged.connect(self.PlaylistView.onSelectionChanged)
        self.SearchAudio.textChanged.connect(self.proxyModel.setFilter)
        self.PlaylistView.signals.urlsDropped.connect(self.addTracks)
        self.PlaylistView.signals.dragDropFromPLFinished.connect(self.ondragDropFromPLFinished)
        self.ClearFilesBut.clicked.connect(self.clearPL)
        self.MinusFilesBut.clicked.connect(self.removeTracks)
        self.PlusFilesBut.clicked.connect(lambda x: self.openFiles(mode='files'))
        self.PlaylistView.doubleClicked.connect(self.onDoubleClicked)
        self.playlistModel.layoutChanged.connect(lambda x: self.PlNavi.dataSync(self.playlistModel.playlistdata))
        self.mw_view.actionPrevious_Track.triggered.connect(self.onPreviousTrack_trig)
        self.mw_view.actionNext_Track.triggered.connect(self.onNextTrack_trig)
        self.mw_view.actionShuffle_Playback.triggered.connect(self.onShufflePlayback_trig)

    def addTracks(self, URLs: list[QUrl], index=-1):
        app.setOverrideCursor(Qt.CursorShape.BusyCursor)

        paths = [url.toLocalFile() for url in URLs]

        pl_audio_adding_dialog = PLProcDialog(paths)
        paths = pl_audio_adding_dialog.return_dict['Paths'] if pl_audio_adding_dialog.exec() else []
        if 'Errors' in pl_audio_adding_dialog.return_dict:
            self.mw_view.error_msg(';\n'.join(pl_audio_adding_dialog.return_dict['Errors']))

        if not paths:
            app.restoreOverrideCursor()
            return
        tracklist = list(map(lambda p: PlSong(p), paths))
        _index = len(self.playlistModel.playlistdata) if index == -1 else index
        self.playlistModel.layoutAboutToBeChanged.emit()
        self.playlistModel.playlistdata[_index:_index] = tracklist
        self.playlistModel.updCanLoadData(changeLayout=False)
        self.playlistModel.layoutChanged.emit()
        if len(self.playlistModel.playlistdata) != len(paths):
            self.PlaylistView.selectRows(_index, _index + len(paths) - 1)
            self.PlaylistView.onSelectionChanged()  # onSelectionChanged signal is not emitted after layoutChange
        app.restoreOverrideCursor()

    def removeTracks(self):
        sel_items = self.PlaylistView.selectedItems
        if not self.selModel.selectedRows():
            return
        self.playlistModel.layoutAboutToBeChanged.emit()
        for item in sel_items:
            self.playlistModel.playlistdata.remove(item)
        self.playlistModel.layoutChanged.emit()
        self.PlaylistView.clearSelection()

    def clearPL(self):
        self.playlistModel.layoutAboutToBeChanged.emit()
        self.playlistModel.playlistdata.clear()
        self.playlistModel.layoutChanged.emit()

    def ondragDropFromPLFinished(self, action):
        if action == Qt.DropAction.MoveAction and self.PlaylistView.selectedIndexes():
            self.playlistModel.removeRows(self.selModel.selectedRows()[0].row(),
                                          len(self.selModel.selectedRows()), QModelIndex())
            self.PlaylistView.selectRows(self.playlistModel.lastInsertedRows[0],
                                         self.playlistModel.lastInsertedRows[-1])

    def error_msg(self, message: str):
        error_message(self.mw_view, message)

    def openFiles(self, mode='files'):
        dialog = QFileDialog(self.mw_view)
        if mode == 'files':
            self._setFileDialogToFileMode(dialog)
        else:
            self._setFileDialogToFolderMode(dialog)
        if dialog.exec():
            filenames = list(map(QUrl.fromLocalFile, dialog.selectedFiles()))
            index = self.PlaylistView.selectedIndexes()[0].row() if self.PlaylistView.selectedIndexes() else -1
            self.addTracks(filenames, index)

    def onDoubleClicked(self, index):
        self.mw_view.AudiofileRBut.setChecked(True)
        source_ind = self.proxyModel.mapToSource(index).row()
        song2load = self.playlistModel.playlistdata[source_ind]
        self.mw_contr.load_song(song2load)

    def onPreviousTrack_trig(self):
        prev_song = self.PlNavi.prev()
        _currentSong = self.PlNavi.currentSong()
        if self.mw_view.actionSkip_Unavailable_Tracks.isChecked():
            while prev_song is not None and not prev_song.available:
                self.PlNavi.setCurrentSong(prev_song)
                prev_song = self.PlNavi.prev()
                if prev_song == self.PlNavi.currentSong():
                    self.PlNavi.setCurrentSong(_currentSong)
                    return
        if prev_song is not None:
            self.mw_contr.load_song(prev_song)
            self.selectCurrentSong()

    def onNextTrack_trig(self):
        next_song = self.PlNavi.next()
        _currentSong = self.PlNavi.currentSong()
        if self.mw_view.actionSkip_Unavailable_Tracks.isChecked():
            while next_song is not None and not next_song.available:
                self.PlNavi.setCurrentSong(next_song)
                next_song = self.PlNavi.next()
        self.PlNavi.setCurrentSong(_currentSong)
        if next_song is not None:
            self.mw_contr.load_song(next_song)
            self.selectCurrentSong()

    def selectCurrentSong(self):
        if self.PlNavi.currentSong() is None:
            return
        abs_ind = 0
        try:
            abs_ind = self.playlistModel.playlistdata.index(self.PlNavi.currentSong())
        except ValueError:
            for ind, S in enumerate(self.playlistModel.playlistdata):
                if self.PlNavi.currentSong().path == S.path:
                    abs_ind = ind
                    break
        rel_ind = self.proxyModel.mapFromSource(self.playlistModel.index(abs_ind, 0, QModelIndex())).row()
        self.PlaylistView.selectRows(rel_ind, rel_ind, scrolling=True)

    def onShufflePlayback_trig(self):
        self.PlNavi.setShuffle(self.mw_view.actionShuffle_Playback.isChecked())

    @staticmethod
    def _setFileDialogToFileMode(dialog: QFileDialog):
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        af_ext = '*.wav *.aiff *.mp3 *.flac *.ogg'
        pl_ext = '*.m3u *.pls *.xspf'
        audiofile_filters = f'Audio files ({af_ext})'
        playlist_filters = f'Playlist files ({pl_ext})'
        all_filters = f'All supported ({af_ext} {pl_ext})'
        dialog.setNameFilters({audiofile_filters, playlist_filters, all_filters})
        dialog.selectNameFilter(all_filters)
        dialog.setWindowTitle('Open Files...')
        return dialog

    @staticmethod
    def _setFileDialogToFolderMode(dialog: QFileDialog):
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setWindowTitle('Open Folder...')
        return dialog
