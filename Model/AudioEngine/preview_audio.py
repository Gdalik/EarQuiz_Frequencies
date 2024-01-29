#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt6.QtCore import pyqtSignal, QObject


class PreviewAudioCrop(QObject):
    min_slice_length = 10
    max_slice_length = 30
    rangeChanged = pyqtSignal()
    sliceLengthChanged = pyqtSignal(int)

    def __init__(self, audiofile_length: int or float, starttime: int or float, endtime: int or float,
                 slice_length=15, strictMode=False):
        super().__init__()
        self.source_length = audiofile_length
        self._strictMode = strictMode
        if strictMode:
            self._starttime = starttime
            self._endtime = endtime
            self._slice_length = slice_length
        else:
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
        if self._strictMode:
            self._starttime = value
        else:
            self._starttime = max(value, 0)
            self._starttime = min(self._starttime, self.endtime - self.slice_length)
        if old_value != self._starttime:
            self.rangeChanged.emit()

    @property
    def endtime(self):
        return self._endtime

    @endtime.setter
    def endtime(self, value):
        old_value = self._endtime
        if self._strictMode:
            self._endtime = value
        else:
            self._endtime = max(self.starttime + self.slice_length, value)
            self._endtime = min(self._endtime, self.source_length)
        if old_value != self._endtime:
            self.rangeChanged.emit()
        self.slice_length = self.slice_length

    @property
    def slice_length(self):
        return self._slice_length

    @slice_length.setter
    def slice_length(self, value):
        old_value = self._slice_length
        if self._strictMode:
            self._slice_length = value
        self._slice_length = min(value, self.chunk_length, self.max_slice_length)
        self._slice_length = max(self._slice_length, self.min_slice_length)
        if old_value != self._slice_length:
            self.sliceLengthChanged.emit(self._slice_length)

    @property
    def chunk_length(self):
        return self.endtime - self.starttime

    @property
    def slices_num(self):
        return int(self.chunk_length // self.slice_length)

    @property
    def range(self):
        return self.starttime, self.endtime

    def setStrictModeActive(self, arg: bool):
        self._strictMode = arg
