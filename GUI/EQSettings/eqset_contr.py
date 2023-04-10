import json
from pathlib import PurePath
from Utilities.exceptions import InterruptedException
import definitions
from definitions import Settings
from Utilities.Q_extract import Qextr
from GUI.Misc.tracked_proc import ProcTrackControl


class EQSetContr:   # parent: MainWindowContr
    def __init__(self, parent):
        self.parent = parent
        self.EQSetView = parent.mw_view.EQSetView
        self.BWQPresets = self.getPresetNames()
        self.EQSetView.refreshBWQList(self.BWQPresets)
        self.ResetEQBut = parent.mw_view.ResetEQBut
        self.ResetEQBut.clicked.connect(self.on_ResetClicked)
        self.parent.mw_view.actionLockEQSettings.triggered.connect(self.onActionLockEQSettings_trig)
        self.restoreEQSettings()

    @property
    def EQpattern(self):
        return self.parent.EQContr.EQpattern

    def refreshSet(self):
        EQpattern = self.EQpattern
        if EQpattern is None:
            return
        BW_Q = EQpattern['BW_Q']
        self.BWQPresets = self.getPresetNames()
        if BW_Q not in self.BWQPresets:
            self._addCustomBWQPreset(BW_Q)
        self.EQSetView.refreshBWQList(self.BWQPresets)
        self.EQSetView.update(EQpattern['Gain_depth'], BW_Q)

    @staticmethod
    def getPresetNames():
        with open(PurePath(definitions.ROOT_DIR, 'Model', 'Data', 'bw_q_patterns.json')) as f:
            preset_list = json.load(f)
        return preset_list

    def _addCustomBWQPreset(self, BW_Q: str):
        self.BWQPresets.append(BW_Q)
        self.BWQPresets.sort(key=lambda Q: Qextr(Q))

    def on_ResetClicked(self):
        self.EQSetView.update(self.EQpattern['Gain_depth'], self.EQpattern['BW_Q'])

    def setGainDepth(self, value: int, raiseInterruptedException=True):
        if self.parent.ADGen is None:
            return
        old_ADGen_gain_depth = self.parent.ADGen.gain_depth()
        ADG_gain_upd = ProcTrackControl(self.parent.ADGen.setGain_depth, args=[value])
        if not ADG_gain_upd.exec():
            self.parent.isErrorInProcess(ADG_gain_upd)
            self.parent.ADGen.setGain_depth(old_ADGen_gain_depth, normalize_audio=False)
            if raiseInterruptedException:
                raise InterruptedException
            self.EQSetView.update_gain_depth(self.parent.ADGen.gain_depth())
            return False
        return True

    def updADGenQ(self):
        if self.parent.ADGen is None:
            return
        self.parent.ADGen.Q = Qextr(self.EQSetView.BWBox.currentText())

    def onActionLockEQSettings_trig(self):
        self.saveEQSettings()

    def saveEQSettings(self):
        if self.parent.mw_view.actionLockEQSettings.isChecked():
            Settings.setValue('LastStuff/EQSettingsLocked', {'GainDepth': self.EQSetView.GainRangeSpin.value(),
                                                    'BW': self.EQSetView.BWBox.currentText()})
        else:
            Settings.setValue('LastStuff/EQSettingsLocked', None)

    def restoreEQSettings(self):
        values = Settings.value('LastStuff/EQSettingsLocked', None)
        if values is None:
            self.parent.mw_view.actionLockEQSettings.setChecked(False)
            return
        self.parent.mw_view.actionLockEQSettings.setChecked(True)
        self.EQSetView.update(int(values['GainDepth']), values['BW'])
