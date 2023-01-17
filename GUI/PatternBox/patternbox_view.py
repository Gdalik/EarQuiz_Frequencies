class PatternBoxView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.Widget = mw_view.PatternBox

    def loadItems(self, mode_names: list):
        for N in mode_names:
            self.Widget.addItem(N)