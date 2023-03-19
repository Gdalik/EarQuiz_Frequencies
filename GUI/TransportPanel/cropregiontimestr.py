from Utilities.common_calcs import hhmmss, get_sec
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QPushButton


class CropRegionTimestr:
    def __init__(self, parent):     # parent: TransportView
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
        self.setStartEndButEnabled(self.parent.StartPointBut, arg)
        self.setStartEndButEnabled(self.parent.EndPointBut, arg)
        self.setStartEndButEnabled(self.parent.RangeToStart, arg)
        self.setStartEndButEnabled(self.parent.RangeToEnd, arg)
        self.parent.ClearRangeBut.setEnabled(arg)
        self.setReadOnly(not arg)

    @staticmethod
    def setStartEndButEnabled(button: QPushButton, arg: bool):
        if arg:
            style = 'QPushButton{border: none; color: blue}' \
                    '\nQPushButton:hover{font-weight: bold;}' \
                    '\nQPushButton:pressed{color: green;}'
        else:
            style = 'QPushButton{border: none; color: black}'
        button.setStyleSheet(style)
        button.setEnabled(arg)


