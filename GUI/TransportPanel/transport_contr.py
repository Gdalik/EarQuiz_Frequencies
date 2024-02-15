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

import math
from PyQt6.QtCore import QObject, Qt
from GUI.TransportPanel.player_contr import PlayerContr
from GUI.globals import defaultSliceLenUpd
from Model.calc import proc_unproc_len
from definitions import Settings


class TransportContr(QObject):
    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__()
        self.CursorBeingDragged = None
        self.CropRegionBeingChanged = None
        self.parent = parent
        self.TransportView = parent.mw_view.TransportPanelView
        self.PlayerContr = PlayerContr(self)
        self.PlayerContr.positionChanged.connect(self.onPlaybackPosChanged)
        self._setCropRegionActions()
        self._setCursorActions()
        self.TransportView.SliceLenSpin.valueChanged.connect(self.onSliceLenChanged)
        self.TransportView.SaveSliceLengthAsDefault.clicked.connect(self.onSaveSliceLengthAsDefaultClicked)

    @property
    def SourceRange(self):
        return self.parent.SourceRange

    def _setCropRegionActions(self):
        self.TransportView.AudioSliderView.CropRegion.sigRegionChanged.connect(self.onCropRegionChanged)
        self.TransportView.AudioSliderView.CropRegion.sigRegionChangeFinished.connect(self.onCropRegionChangeFinished)
        self.TransportView.StartTimeEdit.timeChanged.connect(self.onCropRegionTstrChanged)
        self.TransportView.EndTimeEdit.timeChanged.connect(self.onCropRegionTstrChanged)
        self.TransportView.StartPointBut.clicked.connect(self.onStartPointButClicked)
        self.TransportView.EndPointBut.clicked.connect(self.onEndPointButClicked)
        self.TransportView.RangeToStart.clicked.connect(self.onRangeToStartClicked)
        self.TransportView.RangeToEnd.clicked.connect(self.onRangeToEndClicked)
        self.TransportView.ClearRangeBut.clicked.connect(self.onClearRangeButClicked)

    def _setCursorActions(self):
        self.TransportView.AudioSliderView.Cursor.sigPositionChanged.connect(self.onCursorPositionChanged)
        self.TransportView.AudioSliderView.Cursor.sigPositionChangeFinished.connect(self.onCursorPositionChangeFinished)
        self.TransportView.AudioSliderView.GScene.sigMouseClicked.connect(self.onASMouseClicked)

    def onCropRegionChanged(self):
        self.CropRegionBeingChanged = True
        if self.SourceRange is None:
            return
        region = self.TransportView.AudioSliderView.CropRegion.getRegion()
        _range = (region[0] / 1000, region[1] / 1000)  # ms -> s
        self._resetSourceRange(_range)

    def onCropRegionChangeFinished(self):
        self.CropRegionBeingChanged = False
        self._checkPlaybackRange()

    def onCursorPositionChanged(self, pos):
        self.CursorBeingDragged = True
        position = pos.x()
        self.TransportView.setPositionLabValue(position / 1000)
        if self.SourceRange is None:
            return
        range_start = self.SourceRange.starttime * 1000
        range_end = self.SourceRange.endtime * 1000
        if position < range_start:
            position = range_start
        elif position > range_end:
            position = range_end
        if position != pos.x():
            self.TransportView.AudioSliderView.Cursor.setPos(position)

    def onCursorPositionChangeFinished(self, pos):
        self.CursorBeingDragged = False
        self.PlayerContr.setPosition(int(pos.x()))

    def onASMouseClicked(self, ev):
        if ev.button() != Qt.MouseButton.LeftButton or self.parent.CurrentMode.name != 'Preview':
            return
        if self.SourceRange is None:
            return
        mouse_x = self.TransportView.AudioSliderView.ViewBox.mapSceneToView(ev.scenePos()).toPoint().x()
        if mouse_x < self.SourceRange.starttime * 1000 or mouse_x > self.SourceRange.endtime * 1000:
            return
        self.PlayerContr.setPosition(int(mouse_x))

    def onCropRegionTstrChanged(self):
        if self.SourceRange is None:
            return
        _range = self.TransportView.CropRegionTstr.getValues()
        self._resetSourceRange(_range)
        self._checkPlaybackRange()

    def onStartPointButClicked(self):
        self.SourceRange.starttime = self.parent.CurrentMode.proxyCursorPos

    def onEndPointButClicked(self):
        self.SourceRange.endtime = self.parent.CurrentMode.proxyCursorPos

    def onRangeToStartClicked(self):
        self.SourceRange.starttime = 0

    def onRangeToEndClicked(self):
        self.SourceRange.endtime = self.SourceRange.source_length

    def onClearRangeButClicked(self):
        self.parent.SRC.autoSetSourceRange(reset=False)
        self._checkPlaybackRange()

    def _resetSourceRange(self, _range: list or tuple):
        self.SourceRange.blockSignals(True)
        slices_num = self.SourceRange.slices_num
        k = 1000
        self.SourceRange.starttime = int(_range[0] * k) / k
        self.SourceRange.endtime = int(_range[1] * k) / k
        if self.SourceRange.slices_num < slices_num:  # Rounding error correction to maintain same number of slices
            self.SourceRange.endtime += 1 / k
        self.SourceRange.blockSignals(False)
        self.onSourceRangeChanged()

    def onLoadSourceAudio(self):
        if self.parent.CurrentMode.name != 'Preview' or self.parent.CurrentSourceMode.name != 'Audiofile':
            return
        self.TransportView.setHeader(self.PlayerContr.sourceAudioData())
        self.parent.setTrainingActionsEnabled(True)
        duration_s = self.parent.SourceAudio.duration
        self.TransportView.setDurationLabValue(duration_s)
        self.TransportView.AudioSliderView.setNewDataLength(duration_s)
        if not self.parent.CurrentMode.TimeSettingsChangesEnabled:
            self.parent.CurrentMode.enableTimeSettingsChanges(True)
        if self.parent.SourceAudio != self.parent.LastSourceAudio:
            self.parent.SRC.setInitSourceRangeView()
            self.setInitCropRegionView()
            self.TransportView.AudioSliderView.Cursor.show()
        self.CursorBeingDragged = False
        self.CropRegionBeingChanged = False
        self.parent.LastSourceAudio = self.parent.SourceAudio
        self.parent.AL.saveLoadedSourceInfo()
        self.parent.setMakeAudioActionsEnabled(True)

    def onSourceRangeChanged(self):
        self.TransportView.AudioSliderView.CropRegion.setValues(self.SourceRange.starttime,
                                                                self.SourceRange.endtime)
        self.TransportView.CropRegionTstr.setValues(self.SourceRange.starttime,
                                                    self.SourceRange.endtime)
        self.TransportView.setSlicesNum(self.SourceRange.slices_num)

    def onSliceLenChanged(self, value):
        if self.SourceRange is None:
            return
        self.SourceRange.slice_length = value
        self.TransportView.SliceLenSpin.setValue(int(self.SourceRange.slice_length))
        self.TransportView.setSlicesNum(self.SourceRange.slices_num)

    def onSaveSliceLengthAsDefaultClicked(self):
        value = self.TransportView.SliceLenSpin.value()
        if self.parent.CurrentSourceMode.name == 'Pinknoise':
            _key = 'PinknoiseSliceLength'
            self.parent.mw_view.status.TempLabel.update(f'Default slice length for pink noise set to {value} sec.')
        else:
            _key = 'ExtAudioSliceLength'
            self.parent.mw_view.status.TempLabel.update(f'Default slice length for external audio set to {value} sec.')
        Settings.setValue(f'GlobalVars/{_key}', value)
        defaultSliceLenUpd()

    def updAudioToEqSettings(self, refreshAfter=True, play_after=False, raiseInterruptedException=True):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or not self.parent.eqSetChanged:
            return
        refresh_needed = False
        if self.parent.normHeadroomChanged and \
                self.parent.EQSetContr.setGainDepth(self.parent.EQSetContr.EQSetView.GainRangeSpin.value(),
                                                    raiseInterruptedException=raiseInterruptedException):
            refresh_needed = True
        if self.parent.qChanged:
            self.parent.EQSetContr.updADGenQ()
            refresh_needed = True
        if refresh_needed and refreshAfter:
            self.refreshAudio(play_after=play_after)
        return refresh_needed

    def refreshAudio(self, play_after=False):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or self.parent.ADGen is None:
            return
        self.parent.CurrentMode.updateCurrentAudio()
        self.parent.ADGen.refresh_audio(filepath=self.parent.CurrentAudio)
        self.PlayerContr.loadCurrentAudio(play_after=play_after)
        self.parent.CurrentMode.cleanTempAudio()

    def setInitCropRegionView(self):
        self.onSourceRangeChanged()
        self.onSliceLenChanged(self.SourceRange.slice_length)
        self.TransportView.AudioSliderView.CropRegion.show()

    def onPlaybackPosChanged(self, pos):
        if not self.CursorBeingDragged:
            CursorPos = self.parent.CurrentMode.proxyCursorPos
            self.TransportView.AudioSliderView.Cursor.update_pos(CursorPos)
            self.TransportView.setPositionLabValue(CursorPos)
        self._checkPlaybackRange(excludeZeroPos=True)
        if self.PlayerContr.playbackState() == self.PlayerContr.PlaybackState.PlayingState:
            self.parent.CurrentMode.whilePlaying()

    def eqStateOnOff(self):
        if self.parent.CurrentMode.name == 'Preview' or self.parent.ADGen is None:
            return False
        slice_len = self.parent.ADGen.audiochunk.slice_length
        proc_unproc = proc_unproc_len(slice_len, self.parent.ADGen.proc_t_perc)
        eq_range = (proc_unproc[1], proc_unproc[0] + proc_unproc[1])
        pos_s = self.PlayerContr.position() / 1000
        return eq_range[0] <= pos_s <= eq_range[1]

    def _checkPlaybackRange(self, excludeZeroPos=False):
        if self.CropRegionBeingChanged or self.parent.CurrentMode.name != 'Preview':
            return
        pos = self.PlayerContr.position() / 1000  # ms -> s
        pos_cond = 0 < math.ceil(pos) < int(self.SourceRange.starttime) if excludeZeroPos else \
            math.ceil(pos) < int(self.SourceRange.starttime)
        if pos_cond or pos > self.SourceRange.endtime:
            if not self.parent.mw_view.actionLoop_Playback.isChecked():
                print('stopTriggered')
                self.PlayerContr.onStopTriggered()
            else:
                self.PlayerContr.loopPlayback()
