from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Test'
        self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.view.setActionNextExerciseEnabled(True)
