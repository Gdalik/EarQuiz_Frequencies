


class EQSetContr:
    def __init__(self, parent):
        self.parent = parent
        self.EQSetView = parent.mw_view.EQSetView

    def refreshSet(self):
        EQpattern = self.parent.EQContr.EQpattern
        if EQpattern is None:
            return
        Gain = EQpattern['Gain_depth']
        BW_Q = EQpattern['BW_Q']
        self.EQSetView.update(Gain, BW_Q)

