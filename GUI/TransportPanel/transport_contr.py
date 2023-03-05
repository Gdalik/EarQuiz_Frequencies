from PyQt6.QtCore import QObject, Qt
from GUI.TransportPanel.player_contr import PlayerContr
from Utilities.common_calcs import hhmmss
import math
from Model.calc import proc_unproc_len


class TransportContr(QObject):
    def __init__(self, parent):     # parent: MainWindowContr
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

    @property
    def SourceRange(self):
        return self.parent.SourceRange

    @property
    def currentAudio(self):
        return self.parent.CurrentMode.CurrentAudio

    def _setCropRegionActions(self):
        self.TransportView.AudioSliderView.CropRegion.sigRegionChanged.connect(self.onCropRegionChanged)
        self.TransportView.AudioSliderView.CropRegion.sigRegionChangeFinished.connect(self.onCropRegionChangeFinished)
        self.TransportView.StartTimeEdit.timeChanged.connect(self.onCropRegionTstrChanged)
        self.TransportView.EndTimeEdit.timeChanged.connect(self.onCropRegionTstrChanged)
        self.TransportView.StartPointBut.clicked.connect(self.onStartPointButClicked)
        self.TransportView.EndPointBut.clicked.connect(self.onEndPointButClicked)
        self.TransportView.RangeToStart.clicked.connect(self.onRangeToStartClicked)
        self.TransportView.RangeToEnd.clicked.connect(self.onRangeToEndClicked)
        self.TransportView.ClearRangeBut.clicked.connect(lambda x: self.parent.setOptimalSourceRange(reset=False))

    def _setCursorActions(self):
        self.TransportView.AudioSliderView.Cursor.sigPositionChanged.connect(self.onCursorPositionChanged)
        self.TransportView.AudioSliderView.Cursor.sigPositionChangeFinished.connect(self.onCursorPositionChangeFinished)
        self.TransportView.AudioSliderView.GScene.sigMouseClicked.connect(self.onASMouseClicked)

    def onCropRegionChanged(self):
        self.CropRegionBeingChanged = True
        if self.SourceRange is None:
            return
        region = self.TransportView.AudioSliderView.CropRegion.getRegion()
        _range = (region[0] / 1000, region[1] / 1000)    # ms -> s
        self._resetSourceRange(_range)

    def onCropRegionChangeFinished(self):
        self.CropRegionBeingChanged = False
        self._checkPlaybackRange()

    def onCursorPositionChanged(self, pos):
        self.CursorBeingDragged = True
        position = pos.x()
        self.TransportView.Position_Lab.setText(hhmmss(position / 1000))
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
        self.PlayerContr.setPosition(pos.x())

    def onASMouseClicked(self, ev):
        if ev.button() != Qt.MouseButton.LeftButton or self.parent.CurrentMode.name != 'Preview':
            return
        if self.SourceRange is None:
            return
        mouse_x = self.TransportView.AudioSliderView.ViewBox.mapSceneToView(ev.scenePos()).toPoint().x()
        if mouse_x < self.SourceRange.starttime * 1000 or mouse_x > self.SourceRange.endtime * 1000:
            return
        self.PlayerContr.setPosition(mouse_x)

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

    def _resetSourceRange(self, _range: list or tuple):
        self.SourceRange.blockSignals(True)
        self.SourceRange.starttime = int(_range[0] * 1000) / 1000
        self.SourceRange.endtime = math.ceil(_range[1] * 1000) / 1000
        self.SourceRange.blockSignals(False)
        self.onSourceRangeChanged()

    def onLoadSourceAudio(self):
        if self.parent.CurrentMode.name != 'Preview':
            return
        self.TransportView.setHeader(self.PlayerContr.sourceAudioData())
        # duration_s = self.PlayerContr.duration() / 1000
        duration_s = self.parent.SourceAudio.duration
        self.TransportView.Duration_Lab.setText(hhmmss(duration_s))
        self.TransportView.AudioSliderView.setNewDataLength(duration_s)
        if not self.parent.CurrentMode.TimeSettingsChangesEnabled:
            self.parent.CurrentMode.enableTimeSettingsChanges(True)
        if self.parent.SourceAudio != self.parent.LastSourceAudio:
            self.parent.setInitSourceRangeView()
            self.setInitCropRegionView()
            self.TransportView.AudioSliderView.Cursor.show()
        self.CursorBeingDragged = False
        self.CropRegionBeingChanged = False
        self.parent.LastSourceAudio = self.parent.SourceAudio

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
        self.TransportView.SliceLenSpin.setValue(self.SourceRange.slice_length)
        self.TransportView.setSlicesNum(self.SourceRange.slices_num)

    def updAudioToEqSettings(self, refreshAfter=True):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or not self.parent.eqSetChanged:
            return
        refresh_needed = False
        if self.parent.gainDepthChanged and \
                self.parent.EQSetContr.setGainDepth(self.parent.EQSetContr.EQSetView.GainRangeSpin.value()):
            refresh_needed = True
        if self.parent.qChanged:
            # print('qChanged')
            self.parent.EQSetContr.updADGenQ()
            refresh_needed = True
        if refresh_needed and refreshAfter:
            self.refreshAudio()
        return refresh_needed

    def refreshAudio(self):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or self.parent.ADGen is None:
            return
        self.parent.CurrentMode.updateCurrentAudio()
        self.parent.ADGen.refresh_audio(filepath=self.parent.CurrentMode.CurrentAudio)
        self.PlayerContr.loadCurrentAudio(play_after=False)

    def setInitCropRegionView(self):
        self.onSourceRangeChanged()
        self.TransportView.AudioSliderView.CropRegion.show()

    def onPlaybackPosChanged(self):
        if not self.CursorBeingDragged:
            CursorPos = self.parent.CurrentMode.proxyCursorPos
            self.TransportView.AudioSliderView.Cursor.update_pos(CursorPos)
            self.TransportView.Position_Lab.setText(hhmmss(CursorPos))
        self._checkPlaybackRange()
        if self.PlayerContr.playbackState() == self.PlayerContr.PlaybackState.PlayingState:
            self.parent.CurrentMode.whilePlaying()

    def eqStateOnOff(self):
        if self.parent.CurrentMode.name not in ('Learn', 'Test') or self.parent.ADGen is None:
            return False
        slice_len = self.parent.ADGen.audiochunk.slice_length
        proc_unproc = proc_unproc_len(slice_len, self.parent.ADGen.proc_t_perc)
        eq_range = (proc_unproc[1], proc_unproc[0] + proc_unproc[1])
        pos_s = self.PlayerContr.position() / 1000
        return eq_range[0] <= pos_s <= eq_range[1]

    def _checkPlaybackRange(self):
        if self.CropRegionBeingChanged or self.parent.CurrentMode.name != 'Preview':
            return
        pos = self.PlayerContr.position() / 1000    # ms -> s
        if pos < int(self.SourceRange.starttime) or pos > self.SourceRange.endtime:
            if not self.parent.mw_view.actionLoop_Playback.isChecked():
                self.PlayerContr.onStopTriggered()
            else:
                self.PlayerContr.loopPlayback()
