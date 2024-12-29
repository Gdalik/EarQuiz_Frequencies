from PyQt6.QtCore import QRunnable, pyqtSignal, pyqtSlot, QObject
import numpy as np


class ADGProcSig(QObject):
    drillGenerated = pyqtSignal(object, np.ndarray)
    audioRefreshed = pyqtSignal(bool)


class ADGProc(QRunnable):
    signals = ADGProcSig()

    def __init__(self, gen_func, **kwargs):
        super().__init__()
        self.gen_func = gen_func
        self.kwargs = kwargs

    @pyqtSlot(int or tuple, np.ndarray)
    def run(self):
        freq, audio = self.gen_func(**self.kwargs)
        self.signals.drillGenerated.emit(freq, audio)
        return


class ADGRefresh(QRunnable):
    signals = ADGProcSig()

    def __init__(self, refresh_func, filepath=None, play_after=False):
        super().__init__()
        self.refresh_func = refresh_func
        self.filepath = filepath
        self.play_after = play_after

    @pyqtSlot()
    def run(self):
        self.refresh_func(filepath=self.filepath)
        self.signals.audioRefreshed.emit(self.play_after)
