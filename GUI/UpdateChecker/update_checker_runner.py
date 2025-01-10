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

from PyQt6.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot
import json
import certifi
from urllib import request
from Model.get_version import version_int


class UpdRunSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)


class UpdCheckRun(QRunnable):
    VersionData_URL = 'https://www.dropbox.com/s/gha3fm6duhh87so/version.json?dl=1'
    signals = UpdRunSignals()
    cert = certifi.where()

    def __init__(self):
        super().__init__()
        self.upd_data = None
        self.in_process = False

    @pyqtSlot()
    def run(self):
        self.in_process = True
        try:
            upd_data = request.urlopen(self.VersionData_URL, cafile=self.cert).read()
            latest_version = version_int(external_data=upd_data)
        except Exception as e:
            self.signals.error.emit(str(e))
            return

        curr_version = version_int()
        if latest_version <= curr_version:
            self._no_upd()
            return
        self.upd_data = json.loads(upd_data)
        if not self.upd_data['update_active']:
            self._no_upd(value='no_active_upd')
            return
        elif self.checkVersionInfo():
            self.signals.finished.emit()
        else:
            self.signals.error.emit('Could not load the new version info!')

    def checkVersionInfo(self):
        info_url = self.upd_data['info_file']
        if not info_url:
            return True
        try:
            info_data = request.urlopen(info_url, cafile=self.cert).read()
            self.upd_data['info_data'] = info_data.decode('utf-8')
        except Exception as e:
            self.signals.error.emit(str(e))
            return False
        return True

    def _no_upd(self, value='no_upd'):
        self.upd_data = value
        self.signals.finished.emit()
