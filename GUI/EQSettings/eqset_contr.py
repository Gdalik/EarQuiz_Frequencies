import json
from pathlib import PurePath
import definitions
from Utilities.Q_extract import Qextr


class EQSetContr:
    def __init__(self, parent):
        self.parent = parent
        self.EQSetView = parent.mw_view.EQSetView
        self.BWQPresets = self.getPresetNames()
        self.EQSetView.refreshBWQList(self.BWQPresets)

    def refreshSet(self):
        EQpattern = self.parent.EQContr.EQpattern
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
            list = json.load(f)
        return list

    def _addCustomBWQPreset(self, BW_Q: str):
        self.BWQPresets.append(BW_Q)
        self.BWQPresets.sort(key=lambda Q: Qextr(Q))


