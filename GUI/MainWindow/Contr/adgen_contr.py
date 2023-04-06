from GUI.Misc.tracked_proc import ProcTrackControl
from Model.audiodrill_gen import AudioDrillGen
from Utilities.Q_extract import Qextr


class ADGenContr:
    def __init__(self, parent):     # parent: MainWindowContr
        self.parent = parent

    def setAudioDrillGen(self, resetExGen=True):
        if self.parent.ADGen is None and self.parent.SourceAudio is not None \
                and (self.parent.SourceAudio.name == 'Pink noise' or self.parent.LoadedFileHash):
            self._createADGen()
            self._adjustADGenOrderToMode()
        elif self.parent.ADGen is not None:
            self._adjustADGenCropRange()
            if resetExGen:
                self.parent.PatternBoxContr.setExGenToPattern()

    def _createADGen(self):
        EQP = self.parent.EQContr.EQpattern
        SR = self.parent.SourceRange
        SA = self.parent.SourceAudio
        ADG = ProcTrackControl(AudioDrillGen, args=[self.parent.EQContr.getAvailableFreq()],
                               kwargs={'boost_cut': EQP['EQ_boost_cut'],
                                       'DualBandMode': EQP['DualBandMode'],
                                       'audio_source_path': SA.path,
                                       'starttime': SR.starttime,
                                       'endtime': SR.endtime,
                                       'drill_length': SR.slice_length,
                                       'gain_depth': self.parent.EQSetContr.EQSetView.GainRangeSpin.value(),
                                       'Q': Qextr(self.parent.EQSetContr.EQSetView.BWBox.currentText()),
                                       'order': self.parent.freqOrder(),
                                       'boost_cut_priority': self.parent.boostCutPriority,
                                       'disableAdjacent': EQP['DisableAdjacentFiltersMode']})
        ADG.exec()
        self.parent.isErrorInProcess(ADG)
        self.parent.ADGen = ADG.return_obj or None
        if self.parent.ADGen is not None:
            self.parent.ADGen.audiochunk.signals.showNormalizationLevel.connect(self.parent.mw_view.status.showNormalization)
        self.parent.isErrorInProcess(ADG)

    def _adjustADGenCropRange(self):
        SR = self.parent.SourceRange
        self.parent.ADGen.audiochunk.setStrictModeActive(True)
        self.parent.ADGen.audiochunk.starttime = SR.starttime
        self.parent.ADGen.audiochunk.endtime = SR.endtime
        self.parent.ADGen.audiochunk.slice_length = SR.slice_length
        self.parent.ADGen.audiochunk.setStrictModeActive(False)
        action = self.parent.ADGen.audiochunk.checkActionNeeded()
        if action is None:
            return
        if action == 'reset':
            self.parent.ADGen.setGain_depth(self.parent.EQSetContr.EQSetView.GainRangeSpin.value(),
                                            normalize_audio=False)
            ADG_upd = ProcTrackControl(self.parent.ADGen.audiochunk.update, args=[action])
            if not ADG_upd.exec():
                self.parent.ADGen = None
            if ADG_upd.error:
                self.parent.mw_view.error_msg(ADG_upd.error)
                self.parent.ADGen = None
        else:
            self.parent.ADGen.audiochunk.update(mode=action)

    def _adjustADGenOrderToMode(self):
        if self.parent.ADGen is None:
            return
        self.parent.ADGen.order = self.parent.freqOrder()
