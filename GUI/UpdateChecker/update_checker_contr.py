#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from PyQt6.QtCore import QObject, QThreadPool, Qt
from GUI.UpdateChecker.update_checker_runner import UpdCheckRun
from application import Settings
import datetime


class UpdCheckContr(QObject):
    threadpool: QThreadPool
    UpdCheckRun: UpdCheckRun or None
    minAutoUpdInterval_days = 7

    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.actionCheck_for_Updates.triggered.connect(self.checkUpdates_manual)
        self.UpdCheckRun = None
        self.manual_call = False
        self.checkUpdates_auto()

    def checkUpdates_auto(self):
        days_passed = self.daysSinceLastUpdCheck()
        if days_passed is None or days_passed >= self.minAutoUpdInterval_days:
            self.checkUpdates()

    def checkUpdates_manual(self):
        self.manual_call = True
        self.checkUpdates()

    def checkUpdates(self):
        if self.UpdCheckRun is not None and self.UpdCheckRun.in_process:
            return
        self.threadpool = QThreadPool()
        self.UpdCheckRun = UpdCheckRun()
        self.UpdCheckRun.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.UpdCheckRun.signals.error.connect(self.on_error, type=Qt.ConnectionType.UniqueConnection)
        self.threadpool.start(self.UpdCheckRun)
        self.mw_view.status.TempLabel.update(shown_text='Checking for updates...', time=-1)

    def on_error(self, msg: str):
        self.updCheckStoppedEnded()
        print(f'ERROR: {msg}')

    def on_finished(self):
        manual_call = self.manual_call
        self.updCheckStoppedEnded()
        if self.UpdCheckRun.upd_data is None:
            return
        if self.UpdCheckRun.upd_data == 'no_upd':
            self.saveLastSuccessfulCheck()
            if manual_call:
                self.mw_view.UpdCheckView.noUpdMsg()
            return
        if not isinstance(self.UpdCheckRun.upd_data, dict):
            return
        self.mw_view.UpdCheckView.showUpdWindow(self.UpdCheckRun.upd_data)
        self.saveLastSuccessfulCheck()

    def updCheckStoppedEnded(self):
        self.UpdCheckRun.signals.disconnect()
        self.UpdCheckRun.in_process = False
        self.manual_call = False
        self.mw_view.status.TempLabel.clear()

    @staticmethod
    def saveLastSuccessfulCheck():
        Settings.setValue('MainWindow/LastUpdCheck', datetime.datetime.now())

    @staticmethod
    def daysSinceLastUpdCheck():
        last_checked = Settings.value('MainWindow/LastUpdCheck', None)
        if last_checked is None:
            return None
        timedelta = datetime.datetime.now() - last_checked
        return timedelta.days
