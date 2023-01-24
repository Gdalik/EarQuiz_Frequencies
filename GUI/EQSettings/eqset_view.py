class EQSetView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.GainRangeSpin = self.mw_view.GainRangeSpin
        self.BWBox = self.mw_view.BWBox

    def update(self, gain_depth: int, BW: str):
        self.GainRangeSpin.setValue(gain_depth)
        self.BWBox.setCurrentText(BW)