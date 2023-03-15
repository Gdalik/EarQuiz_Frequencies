class PatternBoxView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.Widget = mw_view.PatternBox
        self.NextButton = mw_view.NextPatternBut

    def loadItems(self, mode_names: list[str]):
        for ind, N in enumerate(mode_names):
            self.Widget.addItem(f'{ind + 1}. {N}')

    def setEnabled(self, arg: bool):
        self.Widget.setEnabled(arg)
        self.NextButton.setEnabled(arg)
