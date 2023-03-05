class EQSetView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.GainRangeSpin = self.mw_view.GainRangeSpin
        self.BWBox = self.mw_view.BWBox

    def refreshBWQList(self, items: list):
        self.BWBox.clear()
        for item in items:
            self.BWBox.addItem(item)

    def update(self, gain_depth: int, BW: str):
        self.update_gain_depth(gain_depth)
        self.update_BW(BW)

    def update_gain_depth(self, gain_depth: int):
        self.GainRangeSpin.blockSignals(True)
        self.GainRangeSpin.setValue(gain_depth)
        self.GainRangeSpin.blockSignals(False)

    def update_BW(self, BW: str):
        self.BWBox.blockSignals(True)
        self.BWBox.setCurrentText(BW)
        self.BWBox.blockSignals(False)

