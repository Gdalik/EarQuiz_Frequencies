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

import contextlib
import mimetypes
from pathlib import Path
from PyQt6.QtCore import QObject, Qt, QModelIndex, QUrl
from PyQt6.QtWidgets import QFileDialog, QWidget
from PyQt6.QtGui import QAction, QKeySequence
from GUI.FileMaker.make_playlist import saveCurrentPlaylist
from GUI.Misc.error_message import error_message
from GUI.Playlist.ContextMenu import PLContextMenu
from GUI.Playlist.PLLoadDialog import PLProcDialog
from GUI.Playlist.PlaylistNavigation import PlNavi
from GUI.Playlist.playlistmodel import PlaylistData, PlaylistModel, PLSortFilterProxyModel
from GUI.Playlist.plsong import PlSong
from Model.FileLinksParser import parseLinksFrom_M3U, AudioMimes
from definitions import USER_DOCS_DIR, CURRENT_PLAYLIST_PATH, PN
from application import app, launch_files_onstart, Settings


class PlaylistContr(QObject):
    """@DynamicAttrs"""

    def __init__(self, parent):
        super().__init__()
        self.mw_view = parent.mw_view
        self.mw_contr = parent
        for W in self.mw_view.AudioSource.findChildren(QWidget):
            self.__setattr__(W.objectName(), W)
        self.playlistData = PlaylistData
        self.playlistModel = PlaylistModel(playlistdata=self.playlistData)
        self.proxyModel = PLSortFilterProxyModel(self)
        self.PlaylistView.setModel(self.proxyModel)
        self.PlNavi = PlNavi(self.playlistModel.playlistdata, shuffle=self.mw_view.actionShuffle_Playback.isChecked())
        self.selModel = self.PlaylistView.selectionModel()
        self._setUpActions()
        self.PlaylistView.customContextMenuRequested.connect(self._onCustomContextMenuRequested)
        self.plStatsLabUpd()
        self.launch_files_onstart = launch_files_onstart

    def _setUpActions(self):
        self.selModel.selectionChanged.connect(self.onSelectionChanged)
        self.SearchAudio.textChanged.connect(self.proxyModel.setFilter)
        self.PlaylistView.signals.urlsDropped.connect(self.addTracks)
        self.PlaylistView.signals.dragDropFromPLFinished.connect(self.ondragDropFromPLFinished)
        self.ClearFilesBut.clicked.connect(self.clearPL)
        self.MinusFilesBut.clicked.connect(self.removeTracks)
        self.PlusFilesBut.clicked.connect(lambda x: self.openFiles(mode='files'))
        self.PlaylistView.doubleClicked.connect(self.onDoubleClicked)
        self.playlistModel.layoutChanged.connect(self.onLayoutChanged)
        self.mw_view.actionPrevious_Track.triggered.connect(self.onPreviousTrack_trig)
        self.mw_view.actionNext_Track.triggered.connect(self.onNextTrack_trig)
        self.mw_view.actionShuffle_Playback.triggered.connect(self.onShufflePlayback_trig)
        self.mw_view.actionRepeat_Playlist.triggered.connect(self.onRepeatPlaylist_trig)
        self.PlaylistView.signals.keyPressed.connect(self.onKeyPressed)
        self.onPlFullEmpty()
        self.mw_view.PreviewNextBut.clicked.connect(self.onPreviewNextBut_clicked)
        self.mw_view.PreviewPreviousBut.clicked.connect(self.onPreviewPreviousBut_clicked)
        self._setupSearchActions()

    def _setupSearchActions(self):
        searchActivateAction = QAction(self.PlaylistView)
        searchDeactivateAction = QAction(self.PlaylistView)
        self.PlaylistView.addActions((searchActivateAction, searchDeactivateAction))
        searchActivateAction.setShortcut(QKeySequence.StandardKey.Find)
        searchDeactivateAction.setShortcut(Qt.Key.Key_Escape)
        searchActivateAction.triggered.connect(self.SearchAudio.setFocus)
        searchDeactivateAction.triggered.connect(self._onSearchDeactivateActionTriggered)

    def _onSearchDeactivateActionTriggered(self):
        self.SearchAudio.clear()
        self.PlaylistView.setFocus()

    def _onCustomContextMenuRequested(self, pos):
        contextMenu = PLContextMenu(self)
        if not contextMenu.menuCreated:
            return True
        sel_ind = self.PlaylistView.selectedIndexes()
        contextMenu.actionLoad.triggered.connect(lambda x: self.loadSongFromIndex(sel_ind[0]))
        contextMenu.actionConvertAudio.triggered.connect(self.mw_contr.FileMaker.onActionConvertFilesTriggered)
        contextMenu.actionRemove.triggered.connect(self.removeTracks)
        contextMenu.actionRemoveUnavailable.triggered.connect(self.removeUnavaliable)
        contextMenu.exec(self.PlaylistView.mapToGlobal(pos))

    def addTracks(self, URLs: list[QUrl], index=-1):
        if not URLs:
            return
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
            self.onSelectionChanged()  # onSelectionChanged signal is not emitted after layoutChange
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
            if len(self.playlistModel.lastInsertedRows) != 0:
                self.PlaylistView.selectRows(self.playlistModel.lastInsertedRows[0],
                                             self.playlistModel.lastInsertedRows[-1])

    def onSelectionChanged(self):
        rows = self.PlaylistView.selectionModel().selectedRows()
        self.mw_view.actionConvert_Selected_Files.setEnabled(len(rows) != 0)
        self.PlaylistView.selectedItems = []
        self.playlistModel.SelectedRows = []
        for row in rows:
            cur_row = self.PlaylistView.model().mapToSource(row).row()
            self.playlistModel.SelectedRows.append(cur_row)
            self.PlaylistView.selectedItems.append(self.PlaylistView.Model.playlistdata[cur_row])
        return zip(self.playlistModel.SelectedRows, self.PlaylistView.selectedItems)

    def error_msg(self, message: str):
        error_message(self.mw_view, message)

    def openFiles(self, mode='files'):
        dialog = QFileDialog(self.mw_view)
        if mode == 'files':
            self._setFileDialogToFileMode(dialog)
        else:
            self._setFileDialogToFolderMode(dialog)
        dialog.setDirectory(USER_DOCS_DIR)
        if dialog.exec():
            filenames = list(map(QUrl.fromLocalFile, dialog.selectedFiles()))
            index = self.PlaylistView.selectedIndexes()[0].row() if self.PlaylistView.selectedIndexes() else -1
            self.addTracks(filenames, index)

    def onDoubleClicked(self, index):
        if self.PlaylistView.MouseButtonPressed != Qt.MouseButton.LeftButton:
            return
        self.loadSongFromIndex(index)

    def onKeyPressed(self, key: int):
        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            with contextlib.suppress(IndexError):
                self.loadSongFromIndex(self.PlaylistView.selectedIndexes()[0])
        elif key in (Qt.Key.Key_Backspace, Qt.Key.Key_Delete):
            self.removeTracks()

    def loadSongFromIndex(self, index):
        self.mw_view.AudiofileRBut.setChecked(True)
        source_ind = self.proxyModel.mapToSource(index).row()
        song2load = self.playlistModel.playlistdata[source_ind]
        self.mw_contr.AL.load_song(song2load)

    def loadAndSelectSong(self, Song: PlSong, forcePlayAfter=False, forceNotPlayAfter=False):
        self.mw_contr.AL.load_song(Song, forcePlayAfter=forcePlayAfter, forceNotPlayAfter=forceNotPlayAfter)
        self.selectCurrentSong()

    def restoreLastAudioSource(self):
        _launched_file_onstart = self.launch_files_onstart[0] \
            if self.launch_files_onstart is not None and Path(self.launch_files_onstart[0]).is_file() \
               and mimetypes.guess_type(self.launch_files_onstart[0])[0] in AudioMimes else None
        last_source = _launched_file_onstart or Settings.value('LastStuff/AudioSource', PN)
        if last_source == PN or last_source not in self.PlNavi.playlist_paths \
                or not Path(last_source).is_file():
            self.mw_view.PinkNoiseRBut.setChecked(True)
            return
        self.mw_view.AudiofileRBut.setChecked(True)
        ind = Settings.value('LastStuff/PlaylistIndex', None) if _launched_file_onstart is None else 0
        ind = int(ind) if ind is not None else ind
        if ind is None or not Path(self.playlistModel.playlistdata[ind].path).samefile(last_source):
            return
        self.loadAndSelectSong(self.playlistModel.playlistdata[ind], forceNotPlayAfter=True)

    def setCurrentSongToPlaylistModel(self):
        rows = []
        if self.playlistModel.currentSong in self.playlistModel.playlistdata:
            rows.append(self.playlistModel.playlistdata.index(self.playlistModel.currentSong))
        self.playlistModel.currentSong = self.mw_contr.SourceAudio
        rows.append(self.playlistModel.playlistdata.index(self.mw_contr.SourceAudio))
        rows.sort()
        self.playlistModel.dataChanged.emit(self.playlistModel.index(rows[0], 0),
                                            self.playlistModel.index(rows[-1], 0))

    def onPreviousTrack_trig(self):
        prev_song = self.PlNavi.prev()
        if prev_song is None:
            return
        _currentSong = self.PlNavi.currentSong()
        if self.mw_view.actionSkip_Unavailable_Tracks.isChecked():
            while prev_song is not None and not prev_song.available:
                self.PlNavi.setCurrentSong(prev_song)
                prev_song = self.PlNavi.prev()
                if prev_song == self.PlNavi.currentSong():
                    self.PlNavi.setCurrentSong(_currentSong)
                    return
        if prev_song is not None:
            self.loadAndSelectSong(prev_song)

    def onNextTrack_trig(self):
        next_song = self.PlNavi.next()
        if next_song is None:
            return
        _currentSong = self.PlNavi.currentSong()
        if self.mw_view.actionSkip_Unavailable_Tracks.isChecked():
            if any(S.available for S in self.playlistModel.playlistdata):
                while next_song is not None and not next_song.available:
                    self.PlNavi.setCurrentSong(next_song)
                    next_song = self.PlNavi.next()
            else:
                next_song = None
        self.PlNavi.setCurrentSong(_currentSong)
        if next_song is not None:
            self.loadAndSelectSong(next_song)

    def onPreviewNextBut_clicked(self):
        _next = self.PlNavi.next()
        if _next is None or (_next == self.mw_contr.SourceAudio and self.mw_contr.CurrentMode.name != 'Preview'):
            return
        self.mw_view.actionPreview_Mode.setChecked(True)
        self.onNextTrack_trig()

    def onPreviewPreviousBut_clicked(self):
        _prev = self.PlNavi.prev()
        if _prev is None or (_prev == self.mw_contr.SourceAudio and self.mw_contr.CurrentMode.name != 'Preview'):
            return
        self.mw_view.actionPreview_Mode.setChecked(True)
        self.onPreviousTrack_trig()

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

    def onLayoutChanged(self):
        self.PlNavi.dataSync(self.playlistModel.playlistdata)
        self.plStatsLabUpd()
        self.onPlFullEmpty()

    def plStatsLabUpd(self):
        self.mw_view.PL_Stats_Lab.setText(self.PlaylistView.plStatsLabText(self.playlistModel.rowCount(QModelIndex)))

    def onPlFullEmpty(self):
        pl_not_empty = len(self.playlistModel.playlistdata) > 0
        self.mw_view.menuExport_Playlist.setEnabled(pl_not_empty)
        self.MinusFilesBut.setEnabled(pl_not_empty)
        self.ClearFilesBut.setEnabled(pl_not_empty)
        PreviewNextPrevButEnabled = pl_not_empty if self.mw_view.AudiofileRBut.isChecked() else False
        self.mw_view.PreviewPreviousBut.setEnabled(PreviewNextPrevButEnabled)
        self.mw_view.PreviewNextBut.setEnabled(PreviewNextPrevButEnabled)

    def onRepeatPlaylist_trig(self):
        self.PlNavi.setRepeatPlaylist(self.mw_view.actionRepeat_Playlist.isChecked())

    @staticmethod
    def _setFileDialogToFileMode(dialog: QFileDialog):
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        af_ext = '*.wav *.aiff *.mp3 *.flac *.ogg'
        pl_ext = '*.m3u *.m3u8 *.pls *.xspf'
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

    def saveCurrentPlaylist(self):
        saveCurrentPlaylist(self.playlistModel.playlistdata)

    def loadCurrentPlaylist(self):
        if not Path(CURRENT_PLAYLIST_PATH).is_file():
            return
        with contextlib.suppress(Exception):
            urls = [QUrl.fromLocalFile(link) for link in parseLinksFrom_M3U(CURRENT_PLAYLIST_PATH, encoding='utf-8')]
            urls_to_ins = [QUrl.fromLocalFile(link) for link in self.launch_files_onstart] if self.launch_files_onstart is not None else None
            if urls_to_ins is not None:
                urls = urls_to_ins + urls
            if urls:
                self.addTracks(urls)

    def removeUnavaliable(self):
        new_pl = [S for S in self.playlistModel.playlistdata if S.available]
        self.playlistModel.layoutAboutToBeChanged.emit()
        self.playlistModel.playlistdata = new_pl
        self.playlistModel.layoutChanged.emit()
        self.PlaylistView.clearSelection()

    def handle_open_file_request(self, url):
        if self.launch_files_onstart is None:
            self.launch_files_onstart = []
        self.launch_files_onstart.append(url.toLocalFile())
