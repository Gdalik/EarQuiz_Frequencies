from GUI.Playlist.plsong import PlSong
from definitions import MinAudioDuration
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from GUI.Modes.PreviewMode import PreviewMode


class AudioLoad:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent
        self.mw_view = self.parent.mw_view
        self.TransportContr = self.parent.TransportContr

    def load_song(self, Song: PlSong, forcePlayAfter=False):
        if self.parent.CurrentSourceMode.name != 'Audiofile':
            return
        if hasattr(Song, 'file_properties'):
            Song.__delattr__('file_properties')
        if Song.duration < MinAudioDuration or not Song.exists or Song.samplerate < 44100:
            return
        self.parent.SRC.savePrevSourceAudioRange()
        reloaded_same = (self.parent.SourceAudio is not None and self.parent.SourceAudio == Song)
        self.parent.SourceAudio = Song
        self.parent.PlaylistContr.PlNavi.setCurrentSong(Song)
        self.parent.playAudioOnPreview = True if reloaded_same \
            else self.mw_view.actionStartPlayingAfterLoading.isChecked()
        if self.parent.CurrentMode.name == 'Preview':
            self.parent.CurrentMode.updateCurrentAudio()
        elif self.mw_view.actionPreview_Mode.isChecked():
            self.parent.CurrentMode = PreviewMode(self.parent)
        else:
            self.mw_view.actionPreview_Mode.setChecked(True)
        if reloaded_same:
            self.TransportContr.PlayerContr.onStopTriggered()
            self.TransportContr.PlayerContr.play()
            return
        if self.parent.SourceAudio == self.parent.LastSourceAudio:
            return
        self.parent.ADGen = None
        self.TransportContr.PlayerContr.loadCurrentAudio(play_after=self.parent.playAudioOnPreview or forcePlayAfter)

    def load_pinknoise(self):
        self.parent.SourceAudio = PlSong('pinknoise')
        self.TransportContr.TransportView.setHeader('Pink noise')
        dur = self.parent.SourceAudio.duration
        self.parent.SourceRange = PreviewAudioCrop(dur, 0, dur, self.TransportContr.TransportView.SliceLenSpin.value())
        self.TransportContr.setInitCropRegionView()
        self.TransportContr.TransportView.setDurationLabValue(dur)
        self.TransportContr.TransportView.AudioSliderView.setNewDataLength(dur)

    def setNoAudio(self):
        self.TransportContr.PlayerContr.onStopTriggered(checkPlaybackState=True)
        self.parent.SourceAudio = self.parent.LastSourceAudio = None
        self.parent.ADGen = None
        self.parent.CurrentAudio = None
        self.parent.LoadedFileHash = None
        self.parent.SRC.disconnectSourceRangeSig()
        self.TransportContr.PlayerContr.clearSource()
        self.parent.CurrentMode.cleanTempAudio()
        self.parent.LoadedFilePath = None
        self.mw_view.TransportPanelView.noSongState()
        self.parent.SourceRange = None
        self.parent.setMakeAudioActionsEnabled(False)
        self.mw_view.statusbar.clearMessage()
