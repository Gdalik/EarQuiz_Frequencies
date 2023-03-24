from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData, QAudio
from definitions import MediaDevices
import platform

class PlayerContr(QMediaPlayer):
    def __init__(self, parent):  # parent: TransportContr
        super().__init__()
        self.parent = parent
        self.mw_contr = parent.parent
        self.mw_view = self.mw_contr.mw_view
        self.TransportView = parent.TransportView
        self.PlayerView = self.TransportView.PlayerView
        self._setupAudioOutput()
        self._connectSignals()
        self.playAfterAudioLoaded = False
        self.onceAudioLoaded = False
        self.PlModel = self.mw_contr.PlaylistContr.playlistModel

    def _connectSignals(self):
        self.mediaStatusChanged.connect(self.onPlayerStatusChanged)
        self.playbackStateChanged.connect(self.onPlaybackStateChanged)
        self.errorOccurred.connect(self.onError)
        MediaDevices.audioOutputsChanged.connect(self.onAudioOutputsChanged)
        self.mw_view.actionPlayPause.triggered.connect(self.onPlayPause_triggered)
        self.mw_view.actionStop.triggered.connect(self.onStopTriggered)
        self.mw_view.actionIncrease_Volume.triggered.connect(self.increaseVolume)
        self.mw_view.actionDecrease_Volume.triggered.connect(self.decreaseVolume)
        self.mw_view.AudioDevicesGroup.triggered.connect(self.onAudioDeviceChecked)
        self.mw_view.VolumeSlider.valueChanged.connect(self.applyVolume)

    def loadCurrentAudio(self, play_after=True):
        AudioToLoad = QUrl.fromLocalFile(self.mw_contr.CurrentAudio)
        if self.source() == AudioToLoad:
            return
        self.clearSource()
        self.setSource(AudioToLoad)
        self.onceAudioLoaded = True
        self.playAfterAudioLoaded = play_after

    def clearSource(self):
        self.setSource(QUrl())

    def loadMetaData(self):
        if not self.metaData():
            return ''
        title = self.metaData().stringValue(QMediaMetaData.Key.Title)
        author = self.metaData().stringValue(QMediaMetaData.Key.Author)
        albumTitle = self.metaData().stringValue(QMediaMetaData.Key.AlbumTitle)
        albumArtist = self.metaData().stringValue(QMediaMetaData.Key.AlbumArtist)
        displ_data = []
        if title or albumTitle:
            displ_data.append(title or albumTitle)
        if author or albumArtist:
            displ_data.append(author or albumArtist)
        return f'{" - ".join(displ_data)}' if displ_data else ''

    @property
    def startPos(self):     # in ms
        try:
            return self.mw_contr.CurrentMode.currentAudioStartTime * 1000
        except AttributeError:
            return 0

    def loopPlayback(self):
        self.setPosition(self.startPos)

    def sourceAudioData(self):
        def hzTokHz(value: int or float):
            res = value / 1000
            return int(res) if value % 1000 == 0 else round(res, 1)

        SourceAudio = self.mw_contr.SourceAudio
        metadata = self.loadMetaData() if SourceAudio.name != 'pinknoise' else ''
        displ_data = [f'"{SourceAudio.name}"']
        if metadata:
            displ_data.append(f'({metadata})')
        displ_data.append(f'[{hzTokHz(SourceAudio.samplerate)} kHz | {SourceAudio.num_channels}]')
        return ' '.join(displ_data)

    def onPlayerStatusChanged(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self._onLoadedMedia()
        elif status == QMediaPlayer.MediaStatus.EndOfMedia:
            self._onEndofMedia()

    def _onLoadedMedia(self):
        if self.onceAudioLoaded:
            self.mw_contr.CurrentMode.cleanTempAudio()
            # self.parent.onLoadSourceAudio()
            self._refreshAudioOutput_mac()
            self.mw_contr.LoadedFilePath = self.mw_contr.CurrentAudio
            if self.mw_contr.CurrentMode.name == 'Preview' and self.mw_contr.CurrentSourceMode.name == 'Audiofile':
                self.mw_contr.hashAudioFile()
                if self.mw_contr.LoadedFilePath in self.PlModel.nonLoadedSong_paths:
                    self.PlModel.nonLoadedSong_paths.remove(self.mw_contr.LoadedFilePath)
                    self.PlModel.updCanLoadData()
            self.parent.onLoadSourceAudio()
            self.checkPreviewStartTime()
            self.onceAudioLoaded = False
        self._playLoadedAudio()

    def _onEndofMedia(self):
        self.setPosition(self.startPos)
        if self.mw_view.actionLoop_Playback.isChecked():
            self.play()
        self.mw_contr.CurrentMode.playbackStoppedEnded()
        self.mw_contr.CurrentMode.playbackEnded()

    def onPlayTriggered(self):
        if self.playbackState() == self.PlaybackState.PlayingState:
            return
        noPreviewSource = (self.mw_contr.CurrentMode.name == 'Preview' and self.mw_contr.SourceAudio is None)
        if noPreviewSource and self.mw_contr.PlaylistContr.PlNavi.currentSongInside() is not None:
            self.mw_contr.PlaylistContr.loadAndSelectSong(self.mw_contr.PlaylistContr.PlNavi.currentSongInside(),
                                                          forcePlayAfter=True)
        elif noPreviewSource and self.mw_contr.PlaylistContr.PlNavi.firstAvailable() is not None:
            self.mw_contr.PlaylistContr.loadAndSelectSong(self.mw_contr.PlaylistContr.PlNavi.firstAvailable(),
                                                          forcePlayAfter=True)
        elif noPreviewSource and self.mw_contr.PlaylistContr.PlNavi.firstAvailable() is None:
            self.mw_contr.PlaylistContr.openFiles()
        elif not self.parent.updAudioToEqSettings(play_after=True, raiseInterruptedException=False):
            self.play()

    def onStopTriggered(self, checkPlaybackState=False):
        if checkPlaybackState and self.playbackState() != self.PlaybackState.PlayingState:
            return
        self.stop()
        try:
            starttime = self.startPos
        except AttributeError:
            starttime = 0
        if self.position() != starttime:
            self.setPosition(starttime)

    def increaseVolume(self):
        self.mw_view.VolumeSlider.setValue(self.mw_view.VolumeSlider.value() + 5)

    def decreaseVolume(self):
        self.mw_view.VolumeSlider.setValue(self.mw_view.VolumeSlider.value() - 5)

    def _refreshAudioOutput_mac(self):
        if platform.system() == 'Darwin':
            self._setupAudioOutput(anyplatform=True)

    def _setupAudioOutput(self, anyplatform=False):
        self.audioOutput = QAudioOutput()
        self.audioOutput.volumeChanged.connect(self.PlayerView.upd_VolumeLevelLab)
        if platform.system() == 'Windows' or anyplatform:
            self.audioOutput.setDevice(self.mw_view.AudioDevicesView.selectedOutput())
            self.setAudioOutput(self.audioOutput)
        self.applyVolume(self.mw_view.VolumeSlider.value())

    def _playLoadedAudio(self):
        if self.playAfterAudioLoaded:
            self.onPlayTriggered()
            self.playAfterAudioLoaded = False

    def checkPreviewStartTime(self):
        curMode = self.mw_contr.CurrentMode
        if curMode.name != 'Preview':
            return
        starttime = curMode.currentAudioStartTime * 1000
        if self.position() != starttime:
            self.setPosition(starttime)

    def onPlaybackStateChanged(self, state):
        self._translatePBStateToStatusBar(state)
        if state == self.PlaybackState.PlayingState:
            if self.mw_contr.CurrentMode.playPause_toggleable:
                self.PlayerView.setPlayPause2Pause()
            self.mw_contr.CurrentMode.oncePlayingStarted()
        elif state in (self.PlaybackState.PausedState, self.PlaybackState.StoppedState):
            self.PlayerView.setPlayPause2Play()
        if state == self.PlaybackState.StoppedState:
            self.mw_contr.CurrentMode.playbackStoppedEnded()

    def _translatePBStateToStatusBar(self, state):
        if self.mw_contr.SourceAudio is None:
            return
        source = 'Pink noise' if self.mw_contr.SourceAudio.name == 'pinknoise' else self.mw_contr.SourceAudio.name
        self.mw_view.status.showMessage(f'{source}: {self.PlayerView.pb_state2str(state)}')

    def onPlayPause_triggered(self):
        if self.playbackState() == self.PlaybackState.PlayingState and self.mw_contr.CurrentMode.playPause_toggleable:
            self.pause()
        else:
            self.onPlayTriggered()

    def onAudioDeviceChecked(self):
        selected_out = self.mw_view.AudioDevicesView.selectedOutput()
        if selected_out != self.audioOutput.device():
            self.audioOutput.setDevice(selected_out)
            self._translatePBStateToStatusBar(self.playbackState())

    def onAudioOutputsChanged(self):
        checked_item = self.mw_view.AudioDevicesGroup.checkedAction()
        if not checked_item:
            self.mw_view.AudioDevicesView.selectOutput(self.mw_view.AudioDevicesView.default_name)
        self.onAudioDeviceChecked()

    def onError(self, err, string):
        self.PlModel.nonLoadedSong_paths.add(self.mw_contr.SourceAudio.path)
        self.PlModel.updCanLoadData()
        self.mw_contr.AL.setNoAudio()
        print(err)
        print(string)

    def applyVolume(self, volumeSliderValue):
        linearVolume = QAudio.convertVolume(volumeSliderValue / 100,
                                            QAudio.VolumeScale.LogarithmicVolumeScale,
                                            QAudio.VolumeScale.LinearVolumeScale)
        self.audioOutput.setVolume(linearVolume)
