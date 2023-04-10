from PyQt6.QtCore import QTime
from Utilities.common_calcs import hhmmss, get_sec


class CropRegionTimestr:
    def __init__(self, parent):  # parent: TransportView
        self.parent = parent
        self.StartTimeEdit = parent.StartTimeEdit
        self.EndTimeEdit = parent.EndTimeEdit

    def setValues(self, starttime_s: int or float, endtime_s: int or float):
        starttime = QTime(*hhmmss(starttime_s, string=False))
        endtime = QTime(*hhmmss(endtime_s, string=False))
        self.StartTimeEdit.blockSignals(True)
        self.StartTimeEdit.setTime(starttime)
        self.StartTimeEdit.blockSignals(False)
        self.EndTimeEdit.blockSignals(True)
        self.EndTimeEdit.setTime(endtime)
        self.EndTimeEdit.blockSignals(False)

    def getValues(self):
        return get_sec(self.StartTimeEdit.time().toString('HH:mm:ss.zzz')), \
               get_sec(self.EndTimeEdit.time().toString('HH:mm:ss.zzz'))

    def noAudioState(self, arg: bool):
        if arg:
            self.setValues(0, 0)
        self.setChangesEnabled(not arg)

    def setReadOnly(self, arg: bool):
        self.StartTimeEdit.setReadOnly(arg)
        self.EndTimeEdit.setReadOnly(arg)

    def setChangesEnabled(self, arg: bool):
        self.parent.StartPointBut.setEnabled(arg)
        self.parent.EndPointBut.setEnabled(arg)
        self.parent.RangeToStart.setEnabled(arg)
        self.parent.RangeToEnd.setEnabled(arg)
        self.parent.ClearRangeBut.setEnabled(arg)
        self.setReadOnly(not arg)
