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

from PySide6.QtCore import QTimer, QObject, QThread
from application import app


class UniMode(QObject):
    def __init__(self, parent, contrEnabled=True, setPlayerContr=True):  # parent: MainWindowContr
        super().__init__()
        self.TimeSettingsChangesEnabled = None
        self.name = 'Uni'
        self.view = parent.mw_view
        QThread.currentThread().msleep(50)
        self.view.status.clearMessage()
        self.parent = parent
        self.parent.CurrentMode = self
        self.playPause_toggleable = False
        self.parent.TransportContr.CursorBeingDragged = False
        # True CursorBeingDragged value, caused by previous Audio Cursor position change, may result in further
        # glitches.
        self.view.setActionNextExampleEnabled(False)
        self.setNextExampleVisible(False)
        self.enableTimeSettingsChanges(False)
        self.hideEQState()
        self.setEQBandsOrderMenuEnabled(True)
        if setPlayerContr:
            self.setPlayerControls()
        self.view.SliceLenSpin.setEnabled(contrEnabled)
        self.view.EQSetView.setEnabled(contrEnabled)
        self.parent.ExScore.showTestStatus(reset_mark=False)

    @property
    def currentAudioCursorStartPos(self):  # in sec
        if self.parent.ADGen is None or self.parent.ADGen.audiochunk.currentSliceRange is None:
            return self.sourceRangeStartTime or 0
        return self.parent.ADGen.audiochunk.currentSliceRange[0]

    @property
    def proxyCursorPos(self):  # in sec
        return self.parent.TransportContr.PlayerContr.position() / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0

    @property
    def sourceRangeStartTime(self):  # in sec
        return self.parent.SourceRange.starttime if self.parent.SourceRange else None

    @property
    def sourceRangeEndTime(self):  # in sec
        return self.parent.SourceRange.endtime if self.parent.SourceRange else None

    @property
    def currentAudioStartTime(self):  # in sec
        return 0

    @property
    def currentAudioEndTime(self):  # in sec
        return 0

    def setPlayerControls(self):
        self.view.actionPlayPause.setEnabled(True)
        self.view.actionStop.setEnabled(True)
        self.view.actionPrevious_Track.setEnabled(False)
        self.view.actionPrevious_Track.setVisible(False)
        self.view.actionNext_Track.setEnabled(False)
        self.view.actionNext_Track.setVisible(False)
        self.view.actionSkip_Unavailable_Tracks.setVisible(False)
        self.view.actionLoop_Playback.setVisible(False)
        self.parent.PlaylistContr.onPlFullEmpty()
        self.view.LoopButton.setVisible(False)
        self.view.Player_SkipBackw.setVisible(False)
        self.view.Player_SkipForw.setVisible(False)
        self.view.actionSequential_Playback.setVisible(False)
        self.view.SequencePlayBut.setVisible(False)
        self.view.actionLoop_Sequence.setVisible(False)

    def updateCurrentAudio(self):
        pass

    def enableTimeSettingsChanges(self, arg: bool):
        self.view.TransportPanelView.AudioSliderView.Cursor.setMovable(arg)
        self.view.TransportPanelView.AudioSliderView.Cursor.showEnabled(arg)
        self.view.TransportPanelView.AudioSliderView.CropRegion.setMovable(arg)
        self.view.TransportPanelView.CropRegionTstr.setChangesEnabled(arg)
        self.TimeSettingsChangesEnabled = arg

    def generateDrill(self, **kwargs):
        pass

    def nextDrill(self, **kwargs):
        pass

    def playbackStoppedEnded(self):
        self.hideEQState()

    def playbackEnded(self):
        pass

    def oncePlayingStarted(self):
        self.view.setEQStateIndicatorOn(self.parent.TransportContr.eqStateOnOff())
        self.view.EqOnOffLab.setVisible(True)
        QTimer.singleShot(200, self.updateSliceRegion)

    def whilePlaying(self):
        self.view.setEQStateIndicatorOn(self.parent.TransportContr.eqStateOnOff())

    def acceptAnswer(self):
        pass

    def restart_test(self):
        pass

    def showAudioCursor(self):
        if self.parent.CurrentAudio is not None:
            self.view.TransportPanelView.AudioSliderView.Cursor.show()

    def _updateSliceRegion(self):
        if self.parent.ADGen is None:
            return
        slicerange = self.parent.ADGen.audiochunk.currentSliceRange
        self.view.TransportPanelView.AudioSliderView.SliceRegion.setValues(slicerange[0], slicerange[1])

    def updateSliceRegion(self):
        pass

    def setEQBandsOrderMenuEnabled(self, arg: bool):
        self.view.menuEQ_Bands_Playback_Order.setEnabled(arg)

    def showProcessingSourceMessage(self):
        self.view.status.showMessage(f'{self.parent.SourceAudio.name}: Processing/Loading...', 0)

    def procEvents(self):
        app.processEvents()

    def hideEQState(self):
        self.view.EqOnOffLab.setVisible(False)
        self.view.status.EQStateLabel.setVisible(False)

    def setNextExampleVisible(self, arg: bool):
        self.view.NextExample.setVisible(arg)
        self.view.NextExample_TP.setVisible(arg)
