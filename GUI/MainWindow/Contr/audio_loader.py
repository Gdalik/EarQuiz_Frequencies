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

from GUI.Modes.PreviewMode import PreviewMode
from GUI.Playlist.plsong import PlSong
from PyQt6.QtCore import QTimer, QThread
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from Model.globals import MinAudioDuration
from definitions import PN
from application import Settings
from pathlib import Path


class AudioLoad:
    def __init__(self, parent):  # parent: MainWindowContr
        self.parent = parent
        self.mw_view = self.parent.mw_view
        self.TransportContr = self.parent.TransportContr

    def _songCanBeLoaded(self, Song: PlSong):
        if self.parent.CurrentSourceMode.name != 'Audiofile':
            return False
        if hasattr(Song, 'file_properties'):
            Song.__delattr__('file_properties')
        self._showNoLoadReasons(Song)
        return bool(
            Song.duration >= MinAudioDuration
            and Song.exists
            and Song.samplerate >= 44100
        )

    def _showNoLoadReasons(self, Song: PlSong):
        if not Song.exists:
            return
        if Song.duration < MinAudioDuration:
            self.mw_view.status.WarnLabel.update(shown_text=f'Audio file duration cannot be less than '
                                                            f'{MinAudioDuration}sec!')
        elif Song.samplerate < 44100:
            self.mw_view.status.WarnLabel.update(
                shown_text='Audio file sampling rate cannot be less than 44.1kHz!')

    def _switchToPreview(self):
        if self.parent.CurrentMode.name == 'Preview':
            self.parent.CurrentMode.updateCurrentAudio()
        elif self.mw_view.actionPreview_Mode.isChecked():
            self.parent.CurrentMode = PreviewMode(self.parent)
        else:
            self.mw_view.actionPreview_Mode.setChecked(True)
            return True
        return False

    def load_song(self, Song: PlSong, forcePlayAfter=False, forceNotPlayAfter=False):
        if not self._songCanBeLoaded(Song):
            return
        reloaded_same = (self.parent.SourceAudio is not None and self.parent.SourceAudio == Song)
        try:
            reloaded_same_path = (self.parent.SourceAudio is not None and
                                  Path(self.parent.SourceAudio.path).samefile(Song.path))
        except FileNotFoundError:
            reloaded_same_path = False
        if not reloaded_same_path:
            self.parent.SRC.savePrevSourceAudioRange()
        self.parent.SourceAudio = Song
        self.parent.PlaylistContr.PlNavi.setCurrentSong(Song)
        self.parent.playAudioOnPreview = True if reloaded_same \
            else self.mw_view.actionStartPlayingAfterLoading.isChecked()
        self.parent.playAudioOnPreview = False if forceNotPlayAfter else self.parent.playAudioOnPreview
        self.TransportContr.PlayerContr.onStopTriggered()
        if not self._switchToPreview() and reloaded_same_path and not forceNotPlayAfter:
            # play the same audio file without leaving the Preview mode
            if not reloaded_same:
                self.parent.PlaylistContr.setCurrentSongToPlaylistModel()
            QThread.msleep(50)
            self.TransportContr.PlayerContr.play()
            return
        elif not reloaded_same_path:
            self.parent.ADGen = None
        self.parent.PlaylistContr.setCurrentSongToPlaylistModel()
        self.TransportContr.PlayerContr.t_loadCurrentAudio(play_after=self.parent.playAudioOnPreview or forcePlayAfter)

    def load_pinknoise(self):
        self.parent.SourceAudio = PlSong(PN)
        self.parent.CurrentAudio = PN
        self.TransportContr.TransportView.setHeader(PN)
        dur = self.parent.SourceAudio.duration
        self.parent.SourceRange = PreviewAudioCrop(dur, 0, dur, self.TransportContr.TransportView.SliceLenSpin.value())
        self.TransportContr.setInitCropRegionView()
        self.TransportContr.TransportView.setDurationLabValue(dur)
        self.TransportContr.TransportView.AudioSliderView.setNewDataLength(dur)
        self.saveLoadedSourceInfo()
        self.parent.setTrainingActionsEnabled(True)

    def setNoAudio(self):
        self.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.parent.SourceAudio = self.parent.LastSourceAudio = None
        self.parent.ADGen = None
        self.parent.CurrentAudio = None
        self.parent.LoadedFileHash = None
        self.parent.SRC.disconnectSourceRangeSig()
        #self.TransportContr.PlayerContr.clearSource()
        QTimer.singleShot(0, self.TransportContr.PlayerContr.clearSource)
        self.parent.LoadedFilePath = None
        self.mw_view.TransportPanelView.noSongState()
        self.parent.SourceRange = None
        self.parent.setMakeAudioActionsEnabled(False)
        self.parent.setTrainingActionsEnabled(False)
        self.mw_view.status.clearMessage()
        #self.parent.pushBackToPreview()

    def saveLoadedSourceInfo(self):
        if self.parent.SourceAudio.isPinkNoise:
            Settings.setValue('LastStuff/AudioSource', self.parent.SourceAudio.name)
            Settings.setValue('LastStuff/PlaylistIndex', None)
        else:
            Settings.setValue('LastStuff/AudioSource', self.parent.SourceAudio.path)
            if self.parent.SourceAudio in self.parent.PlaylistContr.playlistModel.playlistdata:
                ind = self.parent.PlaylistContr.playlistModel.playlistdata.index(self.parent.SourceAudio)
                Settings.setValue('LastStuff/PlaylistIndex', ind)
            else:
                Settings.setValue('LastStuff/PlaylistIndex', None)
