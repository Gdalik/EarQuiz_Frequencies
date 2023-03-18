from Model.AudioEngine.sine_wav_gen import generateCalibrationSineTones
from PyQt6.QtCore import QUrl


class AudioFileMaker:
    def __init__(self, parent):     # parent -- MainWindowContr
        self.parent = parent

    def makeAndImportCalibrationSineTones(self):
        file = generateCalibrationSineTones()
        if file:
            self.parent.PlaylistContr.addTracks([QUrl.fromLocalFile(file)])
