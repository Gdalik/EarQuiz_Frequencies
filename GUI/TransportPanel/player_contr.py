from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from definitions import MediaDevices


class PlayerContr(QMediaPlayer):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.mw_contr = parent.parent
        self.mw_view = self.mw_contr.mw_view
        self.TransportView = parent.TransportView
        self.PlayerView = self.TransportView.PlayerView
        self.mediaStatusChanged.connect(self.onPlayerStatusChanged)
        self.playbackStateChanged.connect(self.onPlaybackStateChanged)
        MediaDevices.audioOutputsChanged.connect(self.onAudioOutputsChanged)
        self.audioOutput = QAudioOutput()
        self.audioOutput.deviceChanged.connect(self.onDeviceChanged)
        self.mw_view.actionPlayPause.triggered.connect(self.onPlayPause_triggered)
        self.mw_view.actionStop.triggered.connect(self.stop)
        self.mw_view.AudioDevicesGroup.triggered.connect(self.onAudioDeviceChecked)
        self.playAfterAudioLoaded = False

    def loadCurrentAudio(self, play_after=True):
        self.setSource(QUrl())
        self.setSource(QUrl.fromLocalFile(self.parent.currentAudio))
        self.playAfterAudioLoaded = play_after

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

    def _sourceAudioData(self):
        metadata = self.loadMetaData()
        displ_data = [f'"{self.mw_contr.SourceAudio.name}"']
        if metadata:
            displ_data.append(f'({metadata})')
        displ_data.append(f'[{self.mw_contr.SourceAudio.samplerate} Hz {self.mw_contr.SourceAudio.num_channels}]')
        return ' '.join(displ_data)

    def onPlayerStatusChanged(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            if self.mw_contr.CurrentMode.name == 'Preview':
                self.TransportView.setHeader(self._sourceAudioData())
            self.audioOutput = QAudioOutput()
            self.audioOutput.setDevice(self.mw_view.AudioDevicesView.selectedOutput())
            self.setAudioOutput(self.audioOutput)
            if self.playAfterAudioLoaded:
                self.play()
                self.playAfterAudioLoaded = False

    def onPlaybackStateChanged(self, state):
        if state == self.PlaybackState.PlayingState:
            if self.mw_contr.CurrentMode.playPause_toggleable:
                self.PlayerView.setPlayPause2Pause()
        elif state in [self.PlaybackState.PausedState, self.PlaybackState.StoppedState]:
            self.PlayerView.setPlayPause2Play()

    def onDeviceChanged(self):
        self.mw_view.AudioDevicesView.selectOutput(self.audioOutput.device().description())

    def onPlayPause_triggered(self):
        if self.playbackState() == self.PlaybackState.PlayingState and self.mw_contr.CurrentMode.playPause_toggleable:
            self.pause()
        else:
            self.play()

    def onAudioDeviceChecked(self):
        selected_out = self.mw_view.AudioDevicesView.selectedOutput()
        if self.playbackState() == self.PlaybackState.PlayingState and selected_out != self.audioOutput.device():
            self.audioOutput.setDevice(selected_out)

    def onAudioOutputsChanged(self):
        checked_item = self.mw_view.AudioDevicesGroup.checkedAction()
        if not checked_item:
            self.mw_view.AudioDevicesView.selectOutput(self.mw_view.AudioDevicesView.default_name)
        self.onAudioDeviceChecked()
