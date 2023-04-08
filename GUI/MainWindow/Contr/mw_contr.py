from definitions import app
from typing import Union
from GUI.MainWindow.View.mw_view import MainWindowView
from GUI.EQ.eq_contr import EQContr
from GUI.EQSettings.eqset_contr import EQSetContr
from GUI.PatternBox.patternbox_contr import PatternBoxContr
from GUI.Playlist.playlistcontr import PlaylistContr
from GUI.ExScoreInfo.exscoreinfo_contr import ExScoreInfoContr
from GUI.Modes.PreviewMode import PreviewMode
from GUI.Modes.LearnMode import LearnMode
from GUI.Modes.TestMode import TestMode
from GUI.Modes.UniMode import UniMode
from GUI.Modes.audiosource_modes import PinkNoiseMode, AudioFileMode
from GUI.Playlist.plsong import PlSong
from GUI.TransportPanel.transport_contr import TransportContr
from GUI.FileMaker.audiofilemaker import AudioFileMaker
from GUI.MainWindow.Contr.audio_loader import AudioLoad
from GUI.MainWindow.Contr.adgen_contr import ADGenContr
from GUI.MainWindow.Contr.sourcerange_contr import SourceRangeContr
from GUI.Misc.tracked_proc import ProcTrackControl
from GUI.StartScreen import StartLogo
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from Model.audiodrill_gen import AudioDrillGen
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QActionGroup
import platform
from Model.file_hash import filehash
from Utilities.Q_extract import Qextr
from Utilities.exceptions import InterruptedException
from GUI.FileMaker.make_playlist import exportPlaylist, exportPlaylistWithRelPaths


class MainWindowContr(QObject):
    modesActionGroup: Union[QActionGroup, QActionGroup]
    LearnFreqOrderActionGroup: Union[QActionGroup, QActionGroup]
    BoostCutOrderActionGroup: Union[QActionGroup, QActionGroup]
    SourceAudio: PlSong or None
    SourceRange: PreviewAudioCrop or None
    ADGen: AudioDrillGen or None
    CurrentSourceMode: PinkNoiseMode or AudioFileMode

    def __init__(self):
        super().__init__()
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.CurrentAudio = None
        self.LoadedFileHash = None
        self.LoadedFilePath = None
        self.LastSourceAudio = None
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
        self.CurrentSourceMode = PinkNoiseMode(self)
        self.AL.setNoAudio()
        self.ADGC = ADGenContr(self)
        self.setFileMenuActions()
        self.setModesActions()
        self.setModesButtons()
        self.setLearnFreqOrderAG()
        self.setBoostCutOrderAG()
        self.setPlaybackButtons()
        self.setNextExampleBut()
        self.mw_view.signals.appClose.connect(self.onAppClose)
        self.mw_view.show()
        self.setSourceButtons()
        self.mw_view.VolumeSlider.setValue(60)
        self.playAudioOnPreview = False
        StartLogo.hide()
        self.PlaylistContr.loadCurrentPlaylist()

    def setFileMenuActions(self):
        self.mw_view.actionOpen.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='files'))
        self.mw_view.actionOpen_Folder.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='folder'))
        self.mw_view.actionMake_and_Open_Calibration_Sine_Wave_File.triggered.connect \
            (self.FileMaker.makeAndImportCalibrationSineTones)
        self.mw_view.actionMake_Test_Files.triggered.connect(self.FileMaker.onActionMakeTestFilesTrig)
        self.mw_view.actionMake_Learning_Files.triggered.connect(self.FileMaker.onActionMakeLearningFilesTrig)
        self.mw_view.actionConvert_Selected_Files.triggered.connect(self.FileMaker.onActionConvertFilesTriggered)
        self.mw_view.actionClose.triggered.connect(self.onActionCloseTriggered)
        self.mw_view.actionExportPlaylistAbsolute.triggered.connect\
            (lambda x: exportPlaylist(self.mw_view, self.PlaylistContr.playlistModel.playlistdata))
        self.mw_view.actionExportPlaylistRelative.triggered.connect\
            (lambda x: exportPlaylistWithRelPaths(self.mw_view, self.PlaylistContr.playlistModel.playlistdata))

    def setModesButtons(self):
        self.mw_view.PreviewBut.setDefaultAction(self.mw_view.actionPreview_Mode)
        self.mw_view.LearnBut.setDefaultAction(self.mw_view.actionLearn_Mode)
        self.mw_view.TestBut.setDefaultAction(self.mw_view.actionTest_Mode)

    def setSourceButtons(self):
        self.mw_view.PinkNoiseRBut.toggled.connect(self.setAudioSourceMode)
        self.mw_view.AudiofileRBut.toggled.connect(self.setAudioSourceMode)
        self.mw_view.PinkNoiseRBut.setChecked(True)

    def setAudioSourceMode(self, value):
        if not value:
            return
        if self.mw_view.PinkNoiseRBut.isChecked():
            self.CurrentSourceMode = PinkNoiseMode(self)
        elif self.mw_view.AudiofileRBut.isChecked():
            self.CurrentSourceMode = AudioFileMode(self)
        if self.mw_view.actionPreview_Mode.isChecked():
            self.CurrentMode = PreviewMode(self)
        else:
            self.mw_view.actionPreview_Mode.setChecked(True)

    def setModesActions(self):
        self.modesActionGroup = QActionGroup(self)
        self.modesActionGroup.setExclusive(True)
        self.modesActionGroup.addAction(self.mw_view.actionPreview_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionLearn_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionTest_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionUni_Mode)
        self.mw_view.actionPreview_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionLearn_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionTest_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionUni_Mode.toggled.connect(self.setCurrentMode)
        self.modesActionGroup.triggered.connect(self.onmodesActionGroupTriggered)

    def setLearnFreqOrderAG(self):
        self.LearnFreqOrderActionGroup = QActionGroup(self)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionAscendingEQ)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionDescendingEQ)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionShuffleEQ)
        self.LearnFreqOrderActionGroup.triggered.connect(self.onLearnFreqOrderActionChanged)

    def setBoostCutOrderAG(self):
        self.BoostCutOrderActionGroup = QActionGroup(self)
        self.BoostCutOrderActionGroup.addAction(self.mw_view.actionEach_Band_Boosted_then_Cut)
        self.BoostCutOrderActionGroup.addAction(self.mw_view.actionAll_Bands_Boosted_then_All_Bands_Cut)
        self.BoostCutOrderActionGroup.triggered.connect(self.onBoostCutOrderActionChanged)

    def onLearnFreqOrderActionChanged(self):
        if self.ADGen is None:
            return
        self.ADGen.order = self.freqOrder()

    def onBoostCutOrderActionChanged(self):
        if self.ADGen is None:
            return
        self.ADGen.boost_cut_priority = self.boostCutPriority

    def setNextExampleBut(self):
        self.mw_view.NextExample.setDefaultAction(self.mw_view.actionNext_Example)
        self.mw_view.actionNext_Example.triggered.connect(self.onNextExampleTriggered)

    def onNextExampleTriggered(self):
        if self.CurrentMode is not None:
            self.CurrentMode.nextDrill(raiseInterruptedException=False)

    def onmodesActionGroupTriggered(self):
        player = self.TransportContr.PlayerContr
        player.onStopTriggered(checkPlaybackState=True)

    def freqOrder(self, audioFileGeneratorMode=False):
        if self.CurrentMode.name == 'Test' and not audioFileGeneratorMode:
            return 'random'
        if self.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionAscendingEQ:
            return 'asc'
        if self.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionDescendingEQ:
            return 'desc'
        if self.LearnFreqOrderActionGroup.checkedAction() == self.mw_view.actionShuffleEQ:
            return 'shuffle'

    @property
    def boostCutPriority(self):
        if self.BoostCutOrderActionGroup.checkedAction() == self.mw_view.actionEach_Band_Boosted_then_Cut:
            return 1
        if self.BoostCutOrderActionGroup.checkedAction() == self.mw_view.actionAll_Bands_Boosted_then_All_Bands_Cut:
            return 2

    def setCurrentMode(self, value):
        if not value:
            return
        self.CurrentMode.cleanTempAudio()
        try:
            if self.modesActionGroup.checkedAction() == self.mw_view.actionPreview_Mode:
                self.CurrentMode = PreviewMode(self)
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionLearn_Mode:
                self.CurrentMode = LearnMode(self)
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionTest_Mode:
                self.CurrentMode = TestMode(self)
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionUni_Mode:
                self.CurrentMode = UniMode(self, contrEnabled=self.LastMode.name != 'Test')
        except InterruptedException:
            self.mw_view.actionPreview_Mode.setChecked(True)
        self._pushBackToPreview()
        self.LastMode = self.CurrentMode

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
        if 'passed' in self.ExScore.test_status:
            self.mw_view.SupportProject.show()

    def _pushBackToPreview(self):
        if self.ADGen is None and self.CurrentMode.name not in ('Preview', 'Uni'):
            self.mw_view.actionPreview_Mode.setChecked(True)

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
        self.mw_view.actionShuffle_Playback.setChecked(False)
        self.mw_view.ShufflePlaybackBut.setDefaultAction(self.mw_view.actionShuffle_Playback)

    def setMakeAudioActionsEnabled(self, arg: bool):
        self.mw_view.actionMake_Learning_Files.setEnabled(arg)
        self.mw_view.actionMake_Test_Files.setEnabled(arg)

    @staticmethod
    def onActionCloseTriggered():
        app.quit()

    def onAppClose(self):
        self.SRC.savePrevSourceAudioRange()
        self.PlaylistContr.saveCurrentPlaylist()

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
        return bool(self.normHeadroomChanged or self.qChanged)
