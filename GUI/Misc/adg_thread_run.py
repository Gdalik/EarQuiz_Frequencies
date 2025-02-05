from PySide6.QtCore import QRunnable, Signal, Slot, QObject
import numpy as np


class ADGProcSig(QObject):
    drillGenerated = Signal(object, np.ndarray)
    audioRefreshed = Signal(bool)


class ADGProc(QRunnable):
    signals = ADGProcSig()

    def __init__(self, gen_func, **kwargs):
        super().__init__()
        self.gen_func = gen_func
        self.kwargs = kwargs

    @Slot(int or tuple, np.ndarray)
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

    @Slot()
    def run(self):
        self.refresh_func(filepath=self.filepath)
        self.signals.audioRefreshed.emit(self.play_after)
