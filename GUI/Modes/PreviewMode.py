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

from definitions import PN
from GUI.Modes.UniMode import UniMode


class PreviewMode(UniMode):
    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__(parent, setPlayerContr=False)
        self.name = 'Preview'
        self.parent.EQContr.resetEQ()
        self.view.TransportPanelView.AudioSliderView.SliceRegion.hide()
        self.hideSequentialPlayContr()
        self.parent.ExScore.view.init_texts(onlyLastExcInfo=True)
        self.view.status.clearNormalization()
        if not self.parent.CurrentSourceMode.name == 'Audiofile':
            self._pinkNoiseModeView()
            return
        self.setPlayerControls()
        self.playPause_toggleable = True
        if self.parent.SourceAudio is not None:
            self.enableTimeSettingsChanges(True)
        if self.updateCurrentAudio():
            self.parent.TransportContr.PlayerContr.loadCurrentAudio(play_after=self.parent.playAudioOnPreview)
        self.parent.playAudioOnPreview = False

    @property
    def proxyCursorPos(self):  # in sec
        player_pos_s = self.parent.TransportContr.PlayerContr.position() / 1000
        if self.sourceRangeStartTime is not None and player_pos_s < self.sourceRangeStartTime:
            return self.sourceRangeStartTime
        return player_pos_s if self.parent.SourceAudio is not None else 0

    @property
    def currentAudioStartTime(self):  # in sec
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
        self.view.actionLoop_Playback.setVisible(True)
        self.view.actionRepeat_Playlist.setVisible(True)
        self.view.actionShuffle_Playback.setEnabled(True)
        self.view.actionShuffle_Playback.setVisible(True)
        self.view.actionStartPlayingAfterLoading.setVisible(True)
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
        if self.parent.SourceAudio.path == PN:
            self.parent.TransportContr.PlayerContr.onStopTriggered()
            self.parent.TransportContr.PlayerContr.clearSource()

    def whilePlaying(self):
        pass

    def ensureCursorGotoStart(self):
        if not self.parent.playAudioOnPreview and self.currentAudioStartTime is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.setPos(self.currentAudioStartTime)
            self.parent.TransportContr.CursorBeingDragged = False

    def _pinkNoiseModeView(self):
        self.enableTimeSettingsChanges(False)
        self.view.actionPlayPause.setEnabled(False)
        self.view.actionStop.setEnabled(False)
        self.view.actionPrevious_Track.setVisible(False)
        self.view.actionNext_Track.setVisible(False)
        self.view.actionSkip_Unavailable_Tracks.setVisible(False)
        self.view.actionLoop_Playback.setVisible(False)
        self.view.actionRepeat_Playlist.setVisible(False)
        self.view.actionShuffle_Playback.setEnabled(False)
        self.view.actionShuffle_Playback.setVisible(False)
        self.view.actionStartPlayingAfterLoading.setVisible(False)
        self.view.PreviewPreviousBut.setEnabled(False)
        self.view.PreviewNextBut.setEnabled(False)
        self.view.LoopButton.setVisible(False)
        self.view.Player_SkipBackw.setVisible(False)
        self.view.Player_SkipForw.setVisible(False)
        self.view.TransportPanelView.AudioSliderView.Cursor.hide()
        self.view.TransportPanelView.AudioSliderView.Cursor.setPos(self.currentAudioStartTime)
        self.parent.TransportContr.CursorBeingDragged = False
