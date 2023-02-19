from PyQt6.QtCore import pyqtSignal, QObject
from Utilities.common_calcs import round_s


class PreviewAudioCrop(QObject):
    min_slice_length = 10
    max_slice_length = 30
    rangeChanged = pyqtSignal()

    def __init__(self, audiofile_length: int or float, starttime: int or float, endtime: int or float,
                 slice_length=15):
        super().__init__()
        self.source_length = audiofile_length
        self._starttime = max(0, starttime)
        self._endtime = max(0, endtime)
        self._starttime = min(self.starttime, self.endtime)
        self._endtime = max(self.starttime + self.min_slice_length, self.endtime)
        self._endtime = min(self._endtime, self.source_length)
        self._slice_length = max(slice_length, self.min_slice_length)
        self._slice_length = min(self._slice_length, self._endtime - self._starttime, self.max_slice_length)

    @property
    def starttime(self):
        return self._starttime

    @starttime.setter
    def starttime(self, value):
        old_value = self._starttime
        self._starttime = max(value, 0)
        self._starttime = min(self._starttime, self.endtime - self.slice_length)
        # print(f'{old_value=} {self._starttime=}')
        if old_value != self._starttime:
            self.rangeChanged.emit()

    @property
    def endtime(self):
        return self._endtime

    @endtime.setter
    def endtime(self, value):
        old_value = self._endtime
        self._endtime = max(self.starttime + self.slice_length, value)
        self._endtime = min(self._endtime, self.source_length)
        # print(f'{old_value=} {self._starttime=}')
        if old_value != self._endtime:
            self.rangeChanged.emit()

    @property
    def slice_length(self):
        return self._slice_length

    @slice_length.setter
    def slice_length(self, value):
        self._slice_length = min(value, self.chunk_length, self.max_slice_length)
        self._slice_length = max(self._slice_length, self.min_slice_length)

    @property
    def chunk_length(self):
        return self.endtime - self.starttime

    @property
    def slices_num(self):
        # print(f'No rounding slices num: {(self.endtime - self.starttime) // self.slice_length}')
        return int(round_s(self.chunk_length) // self.slice_length)

    @property
    def range(self):
        return self.starttime, self.endtime
