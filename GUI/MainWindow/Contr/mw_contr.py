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

import datetime
import platform
from PyQt6.QtCore import QObject, QTimer, QThreadPool
from GUI.MainWindow.Contr.app_modes_handler import AppModesHandler
from GUI.MainWindow.Contr.learn_freq_order_handler import LearnFreqOrderHandler
from GUI.MainWindow.View import dark_theme
from GUI.UpdateChecker.update_checker_contr import UpdCheckContr
from GUI.EQ.eq_contr import EQContr
from GUI.EQSettings.eqset_contr import EQSetContr
from GUI.ExScoreInfo.exscoreinfo_contr import ExScoreInfoContr
from GUI.FileMaker.audiofilemaker import AudioFileMaker
from GUI.FileMaker.make_playlist import exportPlaylist, exportPlaylistWithRelPaths
from GUI.MainWindow.Contr.adgen_contr import ADGenContr
from GUI.MainWindow.Contr.audio_loader import AudioLoad
from GUI.MainWindow.Contr.sourcerange_contr import SourceRangeContr
from GUI.MainWindow.View.mw_view import MainWindowView
from GUI.Misc.tracked_proc import ProcTrackControl
from GUI.Modes.UniMode import UniMode
from GUI.Modes.audiosource_modes import PinkNoiseMode, AudioFileMode
from GUI.PatternBox.patternbox_contr import PatternBoxContr
from GUI.Playlist.playlistcontr import PlaylistContr
from GUI.Playlist.plsong import PlSong
from GUI.Misc.StartScreen import StartLogoTime
from GUI.TransportPanel.transport_contr import TransportContr
from GUI.AudioProcSettings.audio_proc_settings_contr import AudioProcSettingsContr
from GUI.Help.HelpActions import HelpActions
from GUI.SupportApp.supportapp_contr import SupportAppContr
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from Model.audiodrill_gen import AudioDrillGen
from Model.file_hash import filehash
from Utilities.Q_extract import Qextr
from definitions import PN
from application import app, Settings, IsWin11


class MainWindowContr(QObject):
    SourceAudio: PlSong or None
    SourceRange: PreviewAudioCrop or None
    ADGen: AudioDrillGen or None
    CurrentSourceMode: PinkNoiseMode or AudioFileMode

    def __init__(self):
        super().__init__()
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows' and not IsWin11:
            self.mw_view.win_os_settings()
        elif platform.system() == 'Linux' or IsWin11:
            self.mw_view.fusion_style_settings()
        self.CurrentAudio = None
        self.LoadedFileHash = None
        self.LoadedFilePath = None
        self.LastSourceAudio = None
        self.UpdCheckContr = UpdCheckContr(self)
        self.EQContr = EQContr(self)
        self.EQSetContr = EQSetContr(self)
        self.setShufflePBMode()
        self.PlaylistContr = PlaylistContr(self)
        self.PatternBoxContr = PatternBoxContr(self)
        self.TransportContr = TransportContr(self)
        self.FileMaker = AudioFileMaker(self)
        self.ExScore = ExScoreInfoContr(self)
        self.CurrentMode = self.LastMode = UniMode(self)
        self.AL = AudioLoad(self)
        self.SRC = SourceRangeContr(self)
        self.CurrentSourceMode = PinkNoiseMode(self) if Settings.value('LastStuff/AudioSource', PN) == PN \
            else AudioFileMode(self)
        self.AL.setNoAudio()
        self.ADGC = ADGenContr(self)
        self.setFileMenuActions()
        self.AudioProcSettingsContr = AudioProcSettingsContr(self)
        self.HelpActions = HelpActions(self)
        self.SupportAppContr = SupportAppContr(self)
        self.ModesHandler = AppModesHandler(self)
        self.LFOH = LearnFreqOrderHandler(self)
        self.setPlaybackButtons()
        self.setNextExampleBut()
        self.mw_view.signals.appClose.connect(self.onAppClose)
        QTimer.singleShot(StartLogoTime, self.mw_view.show)
        self.mw_view.VolumeSlider.setValue(60)
        dark_theme.change_theme(self.mw_view)
        self.playAudioOnPreview = False
        QTimer.singleShot(0, self._restoreAudioSource)

    def _restoreAudioSource(self):
        self.PlaylistContr.loadCurrentPlaylist()
        self.PlaylistContr.restoreLastAudioSource()

    def setFileMenuActions(self):
        self.mw_view.actionOpen.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='files'))
        self.mw_view.actionOpen_Folder.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='folder'))
        self.mw_view.actionMake_and_Open_Calibration_Sine_Wave_File.triggered.connect \
            (self.FileMaker.makeAndImportCalibrationSineTones)
        self.mw_view.actionMake_Test_Files.triggered.connect(self.FileMaker.onActionMakeTestFilesTrig)
        self.mw_view.actionMake_Learning_Files.triggered.connect(self.FileMaker.onActionMakeLearningFilesTrig)
        self.mw_view.actionConvert_Selected_Files.triggered.connect(self.FileMaker.onActionConvertFilesTriggered)
        self.mw_view.actionClose.triggered.connect(self.onActionCloseTriggered)
        self.mw_view.actionExportPlaylistAbsolute.triggered.connect \
            (lambda x: exportPlaylist(self.mw_view, self.PlaylistContr.playlistModel.playlistdata))
        self.mw_view.actionExportPlaylistRelative.triggered.connect \
            (lambda x: exportPlaylistWithRelPaths(self.mw_view, self.PlaylistContr.playlistModel.playlistdata))

    def setNextExampleBut(self):
        self.mw_view.NextExample.setDefaultAction(self.mw_view.actionNext_Example)
        self.mw_view.NextExample_TP.setDefaultAction(self.mw_view.actionNext_Example)
        self.mw_view.actionNext_Example.triggered.connect(self.onNextExampleTriggered)

    def onNextExampleTriggered(self):
        if self.CurrentMode is not None:
            self.CurrentMode.nextDrill(raiseInterruptedException=False)

    def freqOrder(self, audioFileGeneratorMode=False):
        if self.CurrentMode.name == 'Test' and not audioFileGeneratorMode:
            return 'random'
        if self.LFOH.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionAscendingEQ:
            return 'asc'
        if self.LFOH.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionDescendingEQ:
            return 'desc'
        if self.LFOH.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionShuffleEQ:
            return 'shuffle'

    @property
    def boostCutPriority(self):
        if self.LFOH.BoostCutOrderActionGroup.checkedAction() == self.mw_view.actionEach_Band_Boosted_then_Cut:
            return 1
        if self.LFOH.BoostCutOrderActionGroup.checkedAction() == self.mw_view.actionAll_Bands_Boosted_then_All_Bands_Cut:
            return 2

    def isErrorInProcess(self, process: ProcTrackControl):
        if process.error is not None:
            self.mw_view.error_msg(process.error)
            return True
        return False

    def endTest(self):
        if self.CurrentMode.name != 'Test':
            return
        self.mw_view.actionUni_Mode.setChecked(True)
        self.mw_view.ExScoreInfo.show()
        days_passed = self._daysSinceBeggingWinWasClosed()
        if 'passed' in self.ExScore.test_status and (days_passed is None or days_passed >= 7):
            self.mw_view.SupportProject.show()

    def _daysSinceBeggingWinWasClosed(self):
        last_closed = Settings.value(f'MainWindow/{self.mw_view.SupportProject.objectName()}_LastClosed', None)
        if last_closed is None:
            return None
        timedelta = datetime.datetime.now() - last_closed
        return timedelta.days

    def hashAudioFile(self):
        if self.SourceAudio is None:
            return
        _hash = filehash(self.SourceAudio.path)
        self.LoadedFileHash = _hash
        return _hash

    def setPlaybackButtons(self):
        self.mw_view.MW_PlayPause.setDefaultAction(self.mw_view.actionPlayPause)
        self.mw_view.MW_Stop.setDefaultAction(self.mw_view.actionStop)

    def setShufflePBMode(self):
        self.mw_view.ShufflePlaybackBut.setDefaultAction(self.mw_view.actionShuffle_Playback)

    def setMakeAudioActionsEnabled(self, arg: bool):
        self.mw_view.actionMake_Learning_Files.setEnabled(arg)
        self.mw_view.actionMake_Test_Files.setEnabled(arg)

    def setTrainingActionsEnabled(self, arg: bool):
        self.mw_view.actionLearn_Mode.setEnabled(arg)
        self.mw_view.actionTest_Mode.setEnabled(arg)

    @staticmethod
    def onActionCloseTriggered():
        app.quit()

    def onAppClose(self):
        self.SRC.savePrevSourceAudioRange()
        self.EQSetContr.saveEQSettings()
        self.PlaylistContr.saveCurrentPlaylist()
        self.mw_view.storeWindowView()

    @property
    def normHeadroomChanged(self):
        gain_range_gui = self.EQSetContr.EQSetView.GainRangeSpin.value()
        DualBand_pattern = self.EQContr.EQpattern['DualBandMode']
        return self.ADGen.gain_headroom_calc(gain_range_gui, DualBand_pattern) != self.ADGen.audiochunk.last_norm_level \
            if self.ADGen is not None else False

    @property
    def qChanged(self):
        return Qextr(self.EQSetContr.EQSetView.BWBox.currentText()) != self.ADGen.Q if self.ADGen is not None else False

    @property
    def eqSetChanged(self):
        return bool(self.normHeadroomChanged or self.qChanged or self.eqOnTimePercChanged)

    @property
    def eqOnTimePercChanged(self):
        return self.AudioProcSettingsContr.sit_proc_t_perc != self.ADGen.proc_t_perc \
            if self.ADGen is not None else False
