from Model.AudioEngine.sine_wav_gen import generateCalibrationSineTones
from Model.AudioEngine.convert_audio import convert_audio
from GUI.ConvertToWAV_AIFF.convert_dialog_contr import ConvertFilesDialogContr
from GUI.Misc.tracked_proc import ProcTrackControl
from PyQt6.QtCore import QUrl, QItemSelection, QItemSelectionModel
from GUI.Playlist.plsong import PlSong


class AudioFileMaker:
    def __init__(self, parent):     # parent -- MainWindowContr
        self.parent = parent

    def makeAndImportCalibrationSineTones(self):
        file = generateCalibrationSineTones()
        if file:
            self.parent.PlaylistContr.addTracks([QUrl.fromLocalFile(file)])

    def onActionConvertFilesTriggered(self):
        Dialog = ConvertFilesDialogContr()
        if not Dialog.exec():
            return
        proc_list = []
        for ind, S in enumerate(self.parent.mw_view.PlaylistView.selectedItems):
            Proc = ProcTrackControl(convert_audio, [S.path, S.samplerate],
                                    {'target_samplerate_mode': Dialog.target_samplerate_mode,
                                     'audio_format': Dialog.audio_format})
            cur_row = self.parent.mw_view.PlaylistView.selectionModel().selectedRows()[ind]
            Proc.track_ind = self.parent.mw_view.PlaylistView.model().mapToSource(cur_row).row()
            if not Proc.exec():
                break
            if Proc.return_obj is not None:
                proc_list.append(Proc)
        self._addConvertedFilesToPlaylist(proc_list)

    def _addConvertedFilesToPlaylist(self, proc_list):
        self.parent.mw_view.PlaylistView.clearSelection()
        pl_model = self.parent.PlaylistContr.playlistModel
        selection = QItemSelection()
        pl_model.layoutAboutToBeChanged.emit()
        for ind, P in enumerate(proc_list):
            ins_ind = P.track_ind + ind + 1
            pl_model.playlistdata[ins_ind:ins_ind] = [PlSong(P.return_obj)]
            selection.select(pl_model.index(ins_ind, 0),
                             pl_model.index(ins_ind, 0))
        pl_model.updCanLoadData(changeLayout=False)
        pl_model.layoutChanged.emit()
        self.parent.mw_view.PlaylistView.selectionModel().select(selection, QItemSelectionModel.SelectionFlag.Select |
                                                                 QItemSelectionModel.SelectionFlag.Rows)
