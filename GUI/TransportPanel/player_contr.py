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
        self.mediaStatusChanged.connect(self.onPlayerStatusChanged)
        self.playbackStateChanged.connect(self.onPlaybackStateChanged)
        MediaDevices.audioOutputsChanged.connect(self.onAudioOutputsChanged)
        self._setupAudioOutput()
        self.mw_view.actionPlayPause.triggered.connect(self.onPlayPause_triggered)
        self.mw_view.actionStop.triggered.connect(self.onStopTriggered)
        self.mw_view.actionIncrease_Volume.triggered.connect(self.increaseVolume)
        self.mw_view.actionDecrease_Volume.triggered.connect(self.decreaseVolume)
        self.mw_view.AudioDevicesGroup.triggered.connect(self.onAudioDeviceChecked)
        self.mw_view.VolumeSlider.valueChanged.connect(self.applyVolume)
        self.playAfterAudioLoaded = False
        self.onceAudioLoaded = False
        self.__positions = []
        self.__inf_loop_repos = None

    def loadCurrentAudio(self, play_after=True):
        self.setSource(QUrl())
        self.setSource(QUrl.fromLocalFile(self.parent.currentAudio))
        self.playAfterAudioLoaded = play_after
        self.onceAudioLoaded = True

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
        position = self.startPos
        self.setPosition(position)
        # self.__infLoopResolve(position)

    def __infLoopResolve(self, position: int or float):
        # This is a workaround to prevent infinite loop due to QMediaPlayer.setPosition behavior.
        inf_loop: bool = self.__infLoopDetect((position, self.position()))
        print(f'{inf_loop=}')
        if inf_loop:
            if self.__inf_loop_repos is None:
                self.__inf_loop_repos = self.startPos
            self.__inf_loop_repos += 1
            # print(f'{self.__inf_loop_repos=}')
            self.setPosition(self.__inf_loop_repos)
            self.__infLoopDetect((self.__inf_loop_repos, self.position()))

    def __infLoopDetect(self, cur_positions: tuple):
        print(self.__positions)
        if cur_positions in self.__positions:
            self.__positions.append(cur_positions)
        else:
            # self.infLoopClear()
            self.__positions = [cur_positions]
            self.__inf_loop_repos = cur_positions[0]
            # print(self.__positions)
        return len(self.__positions) >= 5

    def infLoopClear(self):
        self.__positions.clear()
        self.__inf_loop_repos = None

    def sourceAudioData(self):
        def hzTokHz(value: int or float):
            res = value / 1000
            return int(res) if value % 1000 == 0 else round(res, 1)

        metadata = self.loadMetaData()
        SourceAudio = self.mw_contr.SourceAudio
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
            self.parent.onLoadSourceAudio()
            self._refreshAudioOutput_mac()
            self.onceAudioLoaded = False
        self._playLoadedAudio()

    def _onEndofMedia(self):
        self.setPosition(self.startPos)
        if self.mw_view.actionLoop_Playback.isChecked():
            self.play()

    def onStopTriggered(self):
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
        if platform.system() == 'Windows' or anyplatform:
            self.audioOutput.setDevice(self.mw_view.AudioDevicesView.selectedOutput())
            self.setAudioOutput(self.audioOutput)
        self.applyVolume(self.mw_view.VolumeSlider.value())

    def _playLoadedAudio(self):
        if self.playAfterAudioLoaded:
            self.play()
            self.playAfterAudioLoaded = False

    def onPlaybackStateChanged(self, state):
        if state == self.PlaybackState.PlayingState:
            if self.mw_contr.CurrentMode.playPause_toggleable:
                self.PlayerView.setPlayPause2Pause()
        elif state in [self.PlaybackState.PausedState, self.PlaybackState.StoppedState]:
            self.PlayerView.setPlayPause2Play()

    def onPlayPause_triggered(self):
        if self.playbackState() == self.PlaybackState.PlayingState and self.mw_contr.CurrentMode.playPause_toggleable:
            self.pause()
        else:
            self.play()

    def onAudioDeviceChecked(self):
        selected_out = self.mw_view.AudioDevicesView.selectedOutput()
        if selected_out != self.audioOutput.device():
            self.audioOutput.setDevice(selected_out)

    def onAudioOutputsChanged(self):
        checked_item = self.mw_view.AudioDevicesGroup.checkedAction()
        if not checked_item:
            self.mw_view.AudioDevicesView.selectOutput(self.mw_view.AudioDevicesView.default_name)
        self.onAudioDeviceChecked()

    def onError(self, err, string):
        print(err)
        print(string)

    def applyVolume(self, volumeSliderValue):
        linearVolume = QAudio.convertVolume(volumeSliderValue / 100,
                                            QAudio.VolumeScale.LogarithmicVolumeScale,
                                            QAudio.VolumeScale.LinearVolumeScale)
        self.audioOutput.setVolume(linearVolume)
