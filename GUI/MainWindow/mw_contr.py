import contextlib
from definitions import app, SineWaveCalibrationFilename
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
from GUI.Misc.tracked_proc import ProcTrackControl
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from Model.audiodrill_gen import AudioDrillGen
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QActionGroup
import platform
from Model.calc import optimal_range_length
from filehash import FileHash
from Utilities.Q_extract import Qextr
from Utilities.exceptions import InterruptedException


class MainWindowContr(QObject):
    modesActionGroup: Union[QActionGroup, QActionGroup]
    LearnFreqOrderActionGroup: Union[QActionGroup, QActionGroup]
    BoostCutOrderActionGroup: Union[QActionGroup, QActionGroup]
    SourceAudio: PlSong or None
    SourceRange: PreviewAudioCrop or None
    ADGen: AudioDrillGen or None
    LoadedFileHash: str or None
    LoadedFilePath: str or None
    CurrentSourceMode: PinkNoiseMode or AudioFileMode

    def __init__(self):
        super().__init__()
        self.mw_view = MainWindowView()
        if platform.system() == 'Windows':
            self.mw_view.win_os_settings()
        self.CurrentAudio = None
        self.LoadedFilePath = None
        self.LastSourceAudio = None
        self.EQContr = EQContr(self)
        self.EQSetContr = EQSetContr(self)
        self.setShufflePBMode()
        self.PlaylistContr = PlaylistContr(self)
        self.PatternBoxContr = PatternBoxContr(self)
        self.TransportContr = TransportContr(self)
        self.ExScore = ExScoreInfoContr(self)
        self.CurrentMode = self.LastMode = UniMode(self)
        self.CurrentSourceMode = PinkNoiseMode(self)
        self.setNoAudio()
        self.setFileMenuActions()
        self.setModesActions()
        self.setModesButtons()
        self.setLearnFreqOrderAG()
        self.setBoostCutOrderAG()
        self.setPlaybackButtons()
        self.mw_view.NextExample.setDefaultAction(self.mw_view.actionNext_Example)
        self.mw_view.actionNext_Example.triggered.connect(self.onNextExampleTriggered)
        self.mw_view.actionClose.triggered.connect(self.onCloseTriggered)
        self.mw_view.show()
        self.setSourceButtons()
        self.mw_view.VolumeSlider.setValue(60)
        self.playAudioOnPreview = False

    def setFileMenuActions(self):
        self.mw_view.actionOpen.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='files'))
        self.mw_view.actionOpen_Folder.triggered.connect(lambda x: self.PlaylistContr.openFiles(mode='folder'))

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
        self.ADGen.order = self.freqOrder

    def onBoostCutOrderActionChanged(self):
        if self.ADGen is None:
            return
        self.ADGen.boost_cut_priority = self.boostCutPriority

    def onNextExampleTriggered(self):
        if self.CurrentMode is not None:
            self.CurrentMode.nextDrill(raiseInterruptedException=False)

    def onmodesActionGroupTriggered(self):
        player = self.TransportContr.PlayerContr
        player.onStopTriggered(checkPlaybackState=True)

    @property
    def freqOrder(self):
        if self.CurrentMode.name == 'Test':
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

    def endTest(self):
        if self.CurrentMode.name != 'Test':
            return
        self.mw_view.actionUni_Mode.setChecked(True)
        self.mw_view.ExScoreInfo.show()
        if 'passed' in self.ExScore.test_status:
            self.mw_view.SupportProject.show()

    def _pushBackToPreview(self):
        if self.ADGen is None and self.CurrentSourceMode.name == 'Audiofile' \
                and self.CurrentMode.name not in ('Preview', 'Uni'):
            self.mw_view.actionPreview_Mode.setChecked(True)

    def setNoAudio(self):
        self.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.SourceAudio = self.LastSourceAudio = None
        self.ADGen = None
        self.CurrentAudio = None
        self.LoadedFileHash = None
        self.disconnectSourceRangeSig()
        self.TransportContr.PlayerContr.clearSource()
        self.CurrentMode.cleanTempAudio()
        self.LoadedFilePath = None
        self.mw_view.TransportPanelView.noSongState()
        self.SourceRange = None

    def hashAudioFile(self):
        if self.SourceAudio is None:
            return
        md5hasher = FileHash('md5')
        hash = md5hasher.hash_file(self.SourceAudio.path)
        self.LoadedFileHash = hash
        return hash

    def setPlaybackButtons(self):
        self.mw_view.MW_PlayPause.setDefaultAction(self.mw_view.actionPlayPause)
        self.mw_view.MW_Stop.setDefaultAction(self.mw_view.actionStop)

    def setShufflePBMode(self):
        self.mw_view.actionShuffle_Playback.setChecked(False)
        self.mw_view.ShufflePlaybackBut.setDefaultAction(self.mw_view.actionShuffle_Playback)

    def load_song(self, Song: PlSong):
        if self.CurrentSourceMode.name != 'Audiofile':
            return
        if hasattr(Song, 'file_properties'):
            Song.__delattr__('file_properties')
        if Song.duration < 30 or not Song.exists:
            return
        self.SourceAudio = Song
        self.PlaylistContr.PlNavi.setCurrentSong(Song)
        if self.CurrentMode.name == 'Preview':
            self.CurrentMode.updateCurrentAudio()
        else:
            self.playAudioOnPreview = True
            self.mw_view.actionPreview_Mode.setChecked(True)

        if self.LoadedFilePath is not None and Song.path == self.LoadedFilePath:
            self.TransportContr.PlayerContr.onStopTriggered()
            self.TransportContr.PlayerContr.play()
            return
        if self.SourceAudio == self.LastSourceAudio:
            return
        self.ADGen = None
        self.TransportContr.PlayerContr.loadCurrentAudio()

    def load_pinknoise(self):
        self.SourceAudio = PlSong('pinknoise')
        self.TransportContr.TransportView.setHeader('Pink noise')
        dur = self.SourceAudio.duration
        self.SourceRange = PreviewAudioCrop(dur, 0, dur, self.TransportContr.TransportView.SliceLenSpin.value())
        self.TransportContr.setInitCropRegionView()
        self.TransportContr.TransportView.setDurationLabValue(dur)
        self.TransportContr.TransportView.AudioSliderView.setNewDataLength(dur)
        # self.setAudioDrillGen()

    def setInitSourceRangeView(self):
        self.disconnectSourceRangeSig()
        self.setOptimalSourceRange()
        self.mw_view.TransportPanelView.CropRegionTstr.noAudioState(False)
        self.SourceRange.rangeChanged.connect(self.TransportContr.onSourceRangeChanged)

    def setOptimalSourceRange(self, reset=True):
        range_params = self._getSourceRangeParameters(reset=reset)
        if reset:
            self.SourceRange = PreviewAudioCrop(self.SourceAudio.duration, range_params[0], range_params[1],
                                                range_params[2])
        elif self.SourceRange is not None:
            self.SourceRange.setStrictModeActive(True)
            self.SourceRange.starttime = 0
            self.SourceRange.endtime = range_params[1]
            self.SourceRange.setStrictModeActive(False)
        self.mw_view.TransportPanelView.SliceLenSpin.setValue(range_params[2])

    def _getSourceRangeParameters(self, reset=True):
        if self.SourceAudio.name == SineWaveCalibrationFilename:
            slice_length = 10
        elif reset:
            slice_length = self.CurrentSourceMode.default_slice_length
        else:
            slice_length = self.mw_view.TransportPanelView.SliceLenSpin.value()
        duration = self.SourceAudio.duration
        opt_length = optimal_range_length(duration, slice_length)
        return (0, opt_length, slice_length)

    def disconnectSourceRangeSig(self):
        with contextlib.suppress(AttributeError, TypeError):
            self.SourceRange.rangeChanged.disconnect(self.TransportContr.onSourceRangeChanged)

    def onCloseTriggered(self):
        app.quit()

    def setAudioDrillGen(self):
        # print(self.SourceAudio)
        if self.ADGen is None and self.SourceAudio is not None and (self.SourceAudio.name == 'pinknoise' or self.LoadedFileHash):
            self._createADGen()
            self._adjustADGenOrderToMode()
        elif self.ADGen is not None:
            self._adjustADGenCropRange()
            self.PatternBoxContr.setExGenToPattern()

    def _createADGen(self):
        EQP = self.EQContr.EQpattern
        SR = self.SourceRange
        SA = self.SourceAudio
        ADG = ProcTrackControl(AudioDrillGen, args=[self.EQContr.getAvailableFreq()],
                               kwargs={'boost_cut': EQP['EQ_boost_cut'],
                                       'DualBandMode': EQP['DualBandMode'],
                                       'audio_source_path': SA.path,
                                       'starttime': SR.starttime,
                                       'endtime': SR.endtime,
                                       'drill_length': SR.slice_length,
                                       'gain_depth': self.EQSetContr.EQSetView.GainRangeSpin.value(),
                                       'Q': Qextr(self.EQSetContr.EQSetView.BWBox.currentText()),
                                       'order': self.freqOrder,
                                       'boost_cut_priority': self.boostCutPriority,
                                       'disableAdjacent': EQP['DisableAdjacentFiltersMode']})
        ADG.exec()
        self.ADGen = ADG.return_obj or None
        if ADG.error:
            self.mw_view.error_msg(ADG.error)

    def _adjustADGenCropRange(self):
        SR = self.SourceRange
        # print(f'{self.SourceRange.starttime=} {self.SourceRange.endtime=}')
        self.ADGen.audiochunk.setStrictModeActive(True)
        self.ADGen.audiochunk.starttime = SR.starttime
        self.ADGen.audiochunk.endtime = SR.endtime
        self.ADGen.audiochunk.slice_length = SR.slice_length
        self.ADGen.audiochunk.setStrictModeActive(False)
        action = self.ADGen.audiochunk.checkActionNeeded()
        if action is None:
            return
        if action == 'reset':
            self.ADGen.setGain_depth(self.EQSetContr.EQSetView.GainRangeSpin.value(), normalize_audio=False)
            ADG_upd = ProcTrackControl(self.ADGen.audiochunk.update, args=[action])
            if not ADG_upd.exec():
                self.ADGen = None
            if ADG_upd.error:
                self.mw_view.error_msg(ADG_upd.error)
                self.ADGen = None
        else:
            self.ADGen.audiochunk.update(mode=action)

    def _adjustADGenOrderToMode(self):
        if self.ADGen is None:
            return
        self.ADGen.order = self.freqOrder

    @property
    def normHeadroomChanged(self):
        gain_range_gui = self.EQSetContr.EQSetView.GainRangeSpin.value()
        DualBand_pattern = self.EQContr.EQpattern['DualBandMode']
        # print(f'{self.ADGen.gain_headroom_calc(gain_range_gui, DualBand_pattern)=} {self.ADGen.audiochunk.last_norm_level=}')
        return self.ADGen.gain_headroom_calc(gain_range_gui, DualBand_pattern) != self.ADGen.audiochunk.last_norm_level \
            if self.ADGen is not None else False

    @property
    def qChanged(self):
        return Qextr(self.EQSetContr.EQSetView.BWBox.currentText()) != self.ADGen.Q if self.ADGen is not None else False

    @property
    def eqSetChanged(self):
        return bool(self.normHeadroomChanged or self.qChanged)