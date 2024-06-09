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

import platform
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PyQt6.QtWidgets import QMessageBox
from GUI.TransportPanel.volumeslider_contr import VolumeSliderContr
from GUI.Misc.error_message import reformat_message
from GUI.Misc.procEvents import procEvents
from definitions import PN
from application import MediaDevices, Settings
from pathlib import Path
from Model.AudioEngine.audio_backend import formatNotSupported


class PlayerContr(QMediaPlayer):
    def __init__(self, parent):  # parent: TransportContr
        super().__init__()
        self.parent = parent
        self.mw_contr = parent.parent
        self.mw_view = self.mw_contr.mw_view
        self.TransportView = parent.TransportView
        self.PlayerView = self.TransportView.PlayerView
        self.VolumeSlider = self.mw_view.VolumeSlider
        self.VolumeSliderContr = VolumeSliderContr(self)
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
        self.mw_view.actionSequential_Playback.triggered.connect(self.mw_view.onActionSequentialPlaybackTriggered)
        self.mw_view.AudioDevicesGroup.triggered.connect(self.onAudioDeviceChecked)

    def loadCurrentAudio(self, play_after=True):
        filepath = self.mw_contr.CurrentAudio

        # Workaround for PyQt6 QMediaPlayer issue with remote files' playback on Windows (native backend):
        # filepath = f'file:{filepath}' if platform.system() == 'Windows' else filepath

        AudioToLoad = QUrl.fromLocalFile(filepath)
        if self.source() == AudioToLoad:
            return
        self.clearSource()
        self.setSource(AudioToLoad)
        self.onceAudioLoaded = True
        self.playAfterAudioLoaded = play_after
        self.mw_contr.playAudioOnPreview = False

    def t_loadCurrentAudio(self, **kwargs):
        procEvents()
        QTimer.singleShot(0, lambda: self.loadCurrentAudio(**kwargs))

    def clearSource(self):
        self.setSource(QUrl())

    def loadMetaData(self):
        if not self.metaData():
            return ''
        title = self.metaData().stringValue(QMediaMetaData.Key.Title)
        title = f'"{title}"' if title else ''
        author = self.metaData().stringValue(QMediaMetaData.Key.Author)
        albumTitle = self.metaData().stringValue(QMediaMetaData.Key.AlbumTitle)
        albumTitle = f'"{albumTitle}"' if albumTitle else ''
        albumArtist = self.metaData().stringValue(QMediaMetaData.Key.AlbumArtist)
        track_data = [el for el in [title, author] if el]
        track_data_str = f"Track: {' - '.join(track_data)}" if track_data else ''
        album_data = [el for el in [albumTitle, albumArtist] if el]
        album_data_str = f"Album: {' - '.join(album_data)}" if album_data else ''
        displ_data = [track_data_str, album_data_str]
        return f'{"; ".join([el for el in displ_data if el])}' if displ_data else ''

    @property
    def startPos(self):  # in ms
        try:
            return self.mw_contr.CurrentMode.currentAudioStartTime * 1000
        except AttributeError:
            return 0

    def loopPlayback(self):
        self.setPosition(int(self.startPos))

    def sourceAudioData(self):
        def hzTokHz(value: int or float):
            res = value / 1000
            return int(res) if value % 1000 == 0 else round(res, 1)

        SourceAudio = self.mw_contr.SourceAudio
        metadata = self.loadMetaData() if SourceAudio.name != PN else ''
        displ_data = [f'"{SourceAudio.name}"'] if SourceAudio.name != PN else [SourceAudio.name]
        if metadata:
            displ_data.append(f'({metadata})')
        displ_data.append(f'[{hzTokHz(SourceAudio.samplerate)} kHz | {SourceAudio.num_channels}]')
        return ' '.join(displ_data)

    def onPlayerStatusChanged(self, status):
        if status == QMediaPlayer.MediaStatus.LoadedMedia:
            self._onLoadedMedia()
        elif status == QMediaPlayer.MediaStatus.LoadingMedia:
            self._onLoadingMedia()
        elif status == QMediaPlayer.MediaStatus.EndOfMedia:
            self._onEndofMedia()

    def _onLoadingMedia(self):
        self.mw_view.status.showMessage(f'{self.mw_contr.SourceAudio.name}: Loading...', 0)

    def _onLoadedMedia(self):
        if self.mw_contr.SourceAudio is None:
            return
        if self.onceAudioLoaded:
            self._onOnceAudioLoaded()
        self._playLoadedAudio()

    def _onOnceAudioLoaded(self):
        self.mw_contr.CurrentMode.cleanTempAudio()
        self._refreshAudioOutput_mac()
        self._hashAndRefreshLoadedAudioData()
        self.parent.onLoadSourceAudio()
        self.checkPreviewStartTime()
        self.mw_view.status.showMessage(f'{self.mw_contr.SourceAudio.name}{self._get_slice_number_str()}: Loaded', 0)
        self.onceAudioLoaded = False

    def _hashAndRefreshLoadedAudioData(self):
        self.mw_contr.LoadedFilePath = self.mw_contr.CurrentAudio
        if self.mw_contr.CurrentMode.name == 'Preview' and self.mw_contr.CurrentSourceMode.name == 'Audiofile':
            self.mw_contr.hashAudioFile()
            if self.mw_contr.LoadedFilePath in self.PlModel.nonLoadedSong_paths:
                self.PlModel.nonLoadedSong_paths.remove(self.mw_contr.LoadedFilePath)
                self.PlModel.updCanLoadData()

    def _onEndofMedia(self):
        self.setPosition(int(self.startPos))
        if self.mw_view.actionLoop_Playback.isChecked() and self.mw_contr.CurrentMode.name == 'Preview':
            self.play()
        self.mw_contr.CurrentMode.playbackStoppedEnded()
        self.mw_contr.CurrentMode.playbackEnded()

    def onPlayTriggered(self):
        procEvents()
        if self.playbackState() == self.PlaybackState.PlayingState:
            return
        noPreviewSource = (self.mw_contr.CurrentMode.name == 'Preview' and self.mw_contr.SourceAudio is None)
        if noPreviewSource:
            this_song = self.mw_contr.PlaylistContr.PlNavi.findCurrentSong \
                (availableOnly=self.mw_view.actionSkip_Unavailable_Tracks.isChecked())
            if this_song is not None:
                self.mw_contr.PlaylistContr.loadAndSelectSong(this_song, forcePlayAfter=True)
            elif not self.PlModel.playlistdata:
                self.mw_contr.PlaylistContr.openFiles()
        elif not self.parent.updAudioToEqSettings(play_after=True, raiseInterruptedException=False):
            self.play()

    def onStopTriggered(self, checkPlaybackState=False):
        if not checkPlaybackState:
            procEvents()
        elif self.playbackState() != self.PlaybackState.PlayingState:
            return
        self.stop()
        try:
            starttime = self.startPos
        except AttributeError:
            starttime = 0
        if self.position() != starttime:
            self.setPosition(int(starttime))

    def _refreshAudioOutput_mac(self):
        if platform.system() == 'Darwin':
            self._setupAudioOutput(anyplatform=True)

    def _setupAudioOutput(self, anyplatform=False):
        self.audioOutput = QAudioOutput()
        self.audioOutput.volumeChanged.connect(self.PlayerView.upd_VolumeLevelLab)
        if platform.system() != 'Darwin' or anyplatform:
            self.audioOutput.setDevice(self.mw_view.AudioDevicesView.selectedOutput())
            self.setAudioOutput(self.audioOutput)
        self.VolumeSliderContr.applyVolume(self.VolumeSlider.value())

    def _playLoadedAudio(self):
        if self.playAfterAudioLoaded:
            self.onPlayTriggered()
            self.playAfterAudioLoaded = False

    def checkPreviewStartTime(self):
        curMode = self.mw_contr.CurrentMode
        if curMode.name != 'Preview':
            return
        starttime = int(curMode.currentAudioStartTime * 1000)
        if self.position() != starttime:
            self.setPosition(starttime)
        curMode.ensureCursorGotoStart()

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

    def _get_slice_number_str(self):
        if self.mw_contr.ADGen is None or self.mw_contr.ADGen.audiochunk.cycle_id is None:
            return ''
        slice_number = self.mw_contr.ADGen.audiochunk.cycle_id + 1\
            if self.mw_contr.ADGen is not None and self.mw_contr.SourceAudio.name != PN and \
               self.mw_contr.CurrentMode.name != 'Preview' else None
        return f' [{slice_number}]' if slice_number is not None else ''

    def _translatePBStateToStatusBar(self, state):
        if self.mw_contr.SourceAudio is None:
            self.mw_view.status.clearMessage()
            return
        try:
            source = PN if self.mw_contr.SourceAudio.name == PN else self.mw_contr.LastSourceAudio.name
            self.mw_view.status.showMessage(f'{source}{self._get_slice_number_str()}: {self.PlayerView.pb_state2str(state)}', 0)
        except AttributeError:
            self.mw_view.status.clearMessage()

    def onPlayPause_triggered(self):
        if self.playbackState() == self.PlaybackState.PlayingState and self.mw_contr.CurrentMode.playPause_toggleable:
            self.pause()
        else:
            self.onPlayTriggered()

    def onAudioDeviceChecked(self):
        selected_out = self.mw_view.AudioDevicesView.selectedOutput()
        Settings.setValue('Actions/SelectedAudioOut', self.mw_view.AudioDevicesGroup.checkedAction().text())
        if selected_out != self.audioOutput.device():
            self.audioOutput.setDevice(selected_out)
            self._translatePBStateToStatusBar(self.playbackState())

    def onAudioOutputsChanged(self):
        checked_item = self.mw_view.AudioDevicesGroup.checkedAction()
        if not checked_item:
            self.mw_view.AudioDevicesView.selectOutput(self.mw_view.AudioDevicesView.default_name)
        self.onAudioDeviceChecked()

    def onError(self, err, string):
        sourcefile = self.mw_contr.SourceAudio
        self.PlModel.nonLoadedSong_paths.add(sourcefile.path)
        self.PlModel.updCanLoadData()
        self._stopTrainingOnError()
        message = f'{err}: {string}'
        if not sourcefile.exists:
            message = f'File "{sourcefile.path}" not found!'
        elif err == self.Error.FormatError and sourcefile.name != PN:
            message = f'The file "{sourcefile.name}" seems to be in a wrong format. Do you want to reformat it?'
            ext = Path(sourcefile.name).suffix
            if formatNotSupported(ext):
                message = f'{ext[1:].upper()} file format is not supported by the current audio playback backend. ' \
                              f'Do you want to reformat "{sourcefile.name}"?'
            if reformat_message(self.mw_view, msg=message) == QMessageBox.StandardButton.Yes:
                self.mw_contr.FileMaker.onActionConvertFilesTriggered()
            return
        self.mw_view.error_msg(message)

    def _stopTrainingOnError(self):
        if self.mw_contr.CurrentSourceMode.name == 'Audiofile':
            self.mw_contr.AL.setNoAudio()
        else:
            self.onStopTriggered(checkPlaybackState=True)
            self.mw_contr.ModesHandler.pushBackToPreview(ignoreADGen=True)
