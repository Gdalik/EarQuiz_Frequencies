from GUI.Modes.UniMode import UniMode


class PreviewMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Preview'
        self.view.AudiofileRBut.setChecked(True)
        self.playPause_toggleable = True
        self.parent.EQContr.resetEQ()
        self.view.TransportPanel.show()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.hide()
        self.parent.ExScore.view.init_texts(onlyLastExcInfo=True)
        if self.parent.SourceAudio is not None:
            self.enableTimeSettingsChanges(True)
        if self.updateCurrentAudio():
            self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=self.parent.playAudioOnPreview)
        if not self.parent.playAudioOnPreview:
            self.parent.TransportContr.TransportView.AudioSliderView.Cursor.setPos(self.currentAudioStartTime)
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
        self.view.actionSkip_Unavailable_Tracks.setEnabled(True)
        self.view.actionLoop_Playback.setEnabled(True)
        self.view.actionLoop_Playback.setChecked(True)
        self.view.actionShuffle_Playback.setChecked(self.parent.PlaylistContr.PlNavi.shuffle())
        self.view.actionShuffle_Playback.setEnabled(True)

    def updateCurrentAudio(self):
        old_value = self.parent.CurrentAudio
        self.parent.CurrentAudio = self.parent.SourceAudio.path if self.parent.SourceAudio else None
        return self.parent.CurrentAudio != old_value

    def oncePlayingStarted(self):
        pass

    def whilePlaying(self):
        pass

