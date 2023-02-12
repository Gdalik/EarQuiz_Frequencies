from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Test'
        self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.view.NextExercise.show()
