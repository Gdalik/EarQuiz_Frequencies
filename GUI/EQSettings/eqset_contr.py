import json
from pathlib import PurePath
import definitions


class EQSetContr:
    def __init__(self, parent):
        self.parent = parent
        self.EQSetView = parent.mw_view.EQSetView
        self.EQSetView.loadBWQList(self.getPresetNames())

    def refreshSet(self):
        EQpattern = self.parent.EQContr.EQpattern
        if EQpattern is None:
            return
        Gain = EQpattern['Gain_depth']
        BW_Q = EQpattern['BW_Q']
        self.EQSetView.update(Gain, BW_Q)

    def getPresetNames(self):
        with open(PurePath(definitions.ROOT_DIR, 'Model', 'Data', 'bw_q_patterns.json')) as f:
            list = json.load(f)
        return list

