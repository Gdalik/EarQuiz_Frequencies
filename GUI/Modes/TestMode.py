from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Test'
        self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(True)
        self.view.menuEQ_Bands_Playback_Order.setEnabled(False)
        self.parent.setAudioDrillGen()