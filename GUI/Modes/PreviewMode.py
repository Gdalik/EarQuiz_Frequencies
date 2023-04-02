from GUI.Modes.UniMode import UniMode


class PreviewMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent, setPlayerContr=False)
        self.name = 'Preview'
        self.parent.EQContr.resetEQ()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.hide()
        self.hideSequentialPlayContr()
        self.parent.ExScore.view.init_texts(onlyLastExcInfo=True)
        if not self.isAudioSourceMode():
            return
        self.setPlayerControls()
        self.playPause_toggleable = True
        if self.parent.SourceAudio is not None:
            self.enableTimeSettingsChanges(True)
        if self.updateCurrentAudio():
            self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=self.parent.playAudioOnPreview)
        self.parent.playAudioOnPreview = False

    @property
    def proxyCursorPos(self):   # in sec
        player_pos_s = self.parent.TransportContr.PlayerContr.position() / 1000
        if self.sourceRangeStartTime is not None and player_pos_s < self.sourceRangeStartTime:
            return self.sourceRangeStartTime
        return player_pos_s if self.parent.SourceAudio is not None else 0

    @property
    def currentAudioStartTime(self):    # in sec
        return self.sourceRangeStartTime or 0

    @property
    def currentAudioEndTime(self):  # in sec
        return self.parent.SourceRange.endtime or 0

    def setPlayerControls(self):
        self.view.actionPlayPause.setEnabled(True)
        self.view.actionStop.setEnabled(True)
        self.view.actionPrevious_Track.setEnabled(True)
        self.view.actionNext_Track.setEnabled(True)
        self.view.actionPrevious_Track.setVisible(True)
        self.view.actionNext_Track.setVisible(True)
        self.view.actionSkip_Unavailable_Tracks.setVisible(True)
        self.view.actionLoop_Playback.setEnabled(True)
        self.view.actionLoop_Playback.setChecked(True)
        self.view.actionLoop_Playback.setVisible(True)
        self.view.actionRepeat_Playlist.setVisible(True)
        self.view.actionRepeat_Playlist.setChecked(self.parent.PlaylistContr.PlNavi.repeat_playlist())
        self.view.actionShuffle_Playback.setChecked(self.parent.PlaylistContr.PlNavi.shuffle())
        self.view.actionShuffle_Playback.setEnabled(True)
        self.view.actionShuffle_Playback.setVisible(True)
        self.parent.PlaylistContr.onPlFullEmpty()
        self.view.LoopButton.setVisible(True)
        self.view.Player_SkipBackw.setVisible(True)
        self.view.Player_SkipForw.setVisible(True)

    def hideSequentialPlayContr(self):
        self.view.actionSequential_Playback.setVisible(False)
        self.view.SequencePlayBut.setVisible(False)
        self.view.actionLoop_Sequence.setVisible(False)

    def updateCurrentAudio(self):
        old_value = self.parent.CurrentAudio
        self.parent.CurrentAudio = self.parent.SourceAudio.path if self.parent.SourceAudio else None
        return self.parent.CurrentAudio != old_value

    def nextDrill(self, **kwargs):
        pass

    def oncePlayingStarted(self):
        pass

    def whilePlaying(self):
        pass

    def ensureCursorGotoStart(self):
        if not self.parent.playAudioOnPreview and self.currentAudioStartTime is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.setPos(self.currentAudioStartTime)
            self.parent.TransportContr.CursorBeingDragged = False

    def isAudioSourceMode(self):
        if self.parent.CurrentSourceMode.name == 'Audiofile':
            return True
        self.enableTimeSettingsChanges(False)
        self.view.actionPlayPause.setEnabled(False)
        self.view.actionStop.setEnabled(False)
        self.view.actionPrevious_Track.setVisible(False)
        self.view.actionNext_Track.setVisible(False)
        self.view.actionSkip_Unavailable_Tracks.setVisible(False)
        self.view.actionLoop_Playback.setVisible(False)
        self.view.actionRepeat_Playlist.setVisible(False)
        self.view.actionShuffle_Playback.setChecked(False)
        self.view.actionShuffle_Playback.setEnabled(False)
        self.view.actionShuffle_Playback.setVisible(False)
        self.view.PreviewPreviousBut.setEnabled(False)
        self.view.PreviewNextBut.setEnabled(False)
        self.view.LoopButton.setVisible(False)
        self.view.Player_SkipBackw.setVisible(False)
        self.view.Player_SkipForw.setVisible(False)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.view.TransportPanelView.AudioSliderView.Cursor.setPos(self.currentAudioStartTime)
        self.parent.TransportContr.CursorBeingDragged = False
        return False
