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

from PyQt6.QtCore import QUrl, QItemSelection, QItemSelectionModel, QObject, QTimer
from GUI.AudioConvertDialog.convert_dialog_contr import ConvertFilesDialogContr
from GUI.FileMaker.FileCreationSuccessDialog import SuccessDialog
from GUI.MakeLearnTestFiles.make_learn_test_dialog_contr import MakeLearnTestDialogContr
from GUI.Misc.tracked_proc import ProcTrackControl
from GUI.Playlist.plsong import PlSong
from Model.AudioEngine.convert_audio import convert_audio
from Model.AudioEngine.sine_wav_gen import generateCalibrationSineTones
from Model.make_learntest_files import makeLearnFiles, makeTestFiles
import Model.AudioEngine.audio_proc_settings as APS
from Utilities.Q_extract import Qextr
from Utilities.exceptions import InterruptedException


class AudioFileMaker(QObject):
    def __init__(self, parent):  # parent -- MainWindowContr
        super().__init__()
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
            if not S.exists or not S.samplerate or not S.duration:
                continue
            Proc = ProcTrackControl(convert_audio, [S.path, S.samplerate],
                                    {'target_samplerate_mode': Dialog.target_samplerate_mode,
                                     'audio_format': Dialog.audio_format})
            cur_row = self.parent.mw_view.PlaylistView.selectionModel().selectedRows()[ind]
            Proc.track_ind = self.parent.mw_view.PlaylistView.model().mapToSource(cur_row).row()
            if not Proc.exec():
                self.parent.isErrorInProcess(Proc)
                break
            if Proc.return_obj is not None:
                proc_list.append(Proc)
        self._addConvertedFilesToPlaylist(proc_list)

    def _addConvertedFilesToPlaylist(self, proc_list):
        if len(proc_list) == 0:
            return
        self.parent.mw_view.PlaylistView.clearSelection()
        pl_model = self.parent.PlaylistContr.playlistModel
        selection = QItemSelection()
        proxy_model = self.parent.PlaylistContr.proxyModel
        pl_model.layoutAboutToBeChanged.emit()
        for ind, P in enumerate(proc_list):
            ins_ind = P.track_ind + ind + 1
            pl_model.playlistdata[ins_ind:ins_ind] = [PlSong(P.return_obj)]
            selection.select(pl_model.index(ins_ind, 0),
                             pl_model.index(ins_ind, 0))
        pl_model.updCanLoadData(changeLayout=False)
        pl_model.layoutChanged.emit()
        self.parent.mw_view.PlaylistView.selectionModel().select(proxy_model.mapSelectionFromSource(selection),
                                                                 QItemSelectionModel.SelectionFlag.Select |
                                                                 QItemSelectionModel.SelectionFlag.Rows)

    def onActionMakeTestFilesTrig(self):
        Dialog = MakeLearnTestDialogContr(self.parent)
        Dialog.TestBut.setChecked(True)
        if Dialog.exec():
            self._makeLearnTestFiles(Dialog)

    def onActionMakeLearningFilesTrig(self):
        Dialog = MakeLearnTestDialogContr(self.parent)
        Dialog.LearnBut.setChecked(True)
        if Dialog.exec():
            self._makeLearnTestFiles(Dialog)

    def _makeLearnTestFiles(self, Dialog):
        action = makeLearnFiles if Dialog.LearnBut.isChecked() else makeTestFiles
        EQOnTimePerc = 100 if APS.getEQAlwaysOnInTest() and action == makeTestFiles else APS.getEQOnTimePerc()
        EQP = self.parent.EQContr.EQpattern
        SR = self.parent.SourceRange
        SA = self.parent.SourceAudio
        self.parent.ADGC.setAudioDrillGen(resetExGen=False)
        if self.parent.ADGen is None:
            return
        try:
            self._checkAudioNormalization()
        except InterruptedException:
            return
        cropped = self.parent.ADGen.audiochunk.cropped
        cropped_normalized = self.parent.ADGen.audiochunk.cropped_normalized
        kwargs = {'audiodata': self.parent.TransportContr.PlayerContr.sourceAudioData(),
                  'EQPattern': self.parent.PatternBoxContr.PatternBox.currentText(),
                  'cropped': cropped,
                  'cropped_normalized': cropped_normalized,
                  'filename_prefix': Dialog.prefix,
                  'extension': Dialog.extension,
                  'bitrate': Dialog.bitrate,
                  'boost_cut': EQP['EQ_boost_cut'],
                  'DualBandMode': EQP['DualBandMode'],
                  'starttime': SR.starttime,
                  'endtime': SR.endtime,
                  'drill_length': SR.slice_length,
                  'proc_t_perc': EQOnTimePerc,
                  'gain_depth': self.parent.EQSetContr.EQSetView.GainRangeSpin.value(),
                  'Q': Qextr(self.parent.EQSetContr.EQSetView.BWBox.currentText()),
                  'disableAdjacent': EQP['DisableAdjacentFiltersMode']}
        if Dialog.LearnBut.isChecked():
            kwargs['order'] = self.parent.freqOrder(audioFileGeneratorMode=True)
            kwargs['enumerate_examples'] = Dialog.EnumLearningExBut.isChecked()
        Proc = ProcTrackControl(action, args=[SA.path, Dialog.ExerciseFolderLine.text(),
                                              self.parent.EQContr.getAvailableFreq()], kwargs=kwargs)
        if not Proc.exec():
            self.parent.isErrorInProcess(Proc)
            return
        QTimer.singleShot(100, lambda: SuccessDialog(self.parent.mw_view, Dialog.ExerciseFolderLine.text(),
                      mode_name='Learning' if Dialog.LearnBut.isChecked() else 'Test'))

    def _checkAudioNormalization(self):
        if self.parent.CurrentMode.name == 'Preview':
            Proc = ProcTrackControl(self.parent.ADGen.setGain_depth,
                                    args=[self.parent.EQSetContr.EQSetView.GainRangeSpin.value()])
            if not Proc.exec():
                self.parent.isErrorInProcess(Proc)
                raise InterruptedException
        else:
            self.parent.TransportContr.updAudioToEqSettings(play_after=False, raiseInterruptedException=True)
