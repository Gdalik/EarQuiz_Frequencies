from GUI.Modes.UniMode import UniMode


class TestMode(UniMode):
    def __init__(self, parent):     # parent: MainWindowContr
        super().__init__(parent)
        self.name = 'Test'
        self.parent.EQContr.resetEQ()
        self.view.setActionNextExerciseEnabled(True)
        self.view.menuEQ_Bands_Playback_Order.setEnabled(False)
        self.parent.setAudioDrillGen()

    @property
    def currentAudioCursorStartPos(self):   # in sec
        if self.parent.ADGen is None or self.parent.ADGen.audiochunk.currentSliceRange is None:
            return self.sourceRangeStartTime or 0
        return self.parent.ADGen.audiochunk.currentSliceRange[0]

    @property
    def proxyCursorPos(self):   # in sec
        return self.parent.TransportContr.PlayerContr.position() / 1000 + self.currentAudioCursorStartPos \
            if self.parent.SourceAudio is not None else 0