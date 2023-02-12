from GUI.Modes.UniMode import UniMode


class LearnMode(UniMode):
    def __init__(self, parent):
        super().__init__(parent)
        self.name = 'Learn'
        if self.parent.LastMode.name not in ['Preview', 'Uni']:
            self.parent.PatternBoxContr.onPatternBoxIndexChanged()
        self.view.NextExercise.show()
