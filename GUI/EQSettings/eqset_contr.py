import json
from pathlib import PurePath
import definitions
from Utilities.Q_extract import Qextr


class EQSetContr:   # parent: MainWindowContr
    def __init__(self, parent):
        self.parent = parent
        self.EQSetView = parent.mw_view.EQSetView
        self.BWQPresets = self.getPresetNames()
        self.EQSetView.refreshBWQList(self.BWQPresets)
        self.ResetEQBut = parent.mw_view.ResetEQBut
        self.ResetEQBut.clicked.connect(self.on_ResetClicked)

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
