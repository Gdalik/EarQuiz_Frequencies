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
import platform
import sys
import copy
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSettings, QLibraryInfo
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtGui import QFont
from definitions import SETTINGS_PATH

app_name = 'EarQuiz Frequencies'
launch_files_onstart = sys.argv[1:] if len(sys.argv) > 1 else None
IsWin11 = platform.system() == 'Windows' and sys.getwindowsversion().build >= 22000


class EQFreqApp(QtWidgets.QApplication):
    openFileRequest = QtCore.pyqtSignal(QtCore.QUrl, name='openFileRequest')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setApplicationDisplayName(app_name)
        self.setApplicationName(app_name)
        if platform.system() != 'Linux':
            self.setOrganizationDomain("earquiz.org")
        if IsWin11:
            self.setStyle('Fusion')
        self.setOrganizationName("EarQuiz")
        self.set_app_font()
        self.files_to_be_opened = copy.copy(launch_files_onstart)

    def event(self, event):
        if event.type() == QtCore.QEvent.Type.FileOpen:
            self.openFileRequest.emit(event.url())
            return True
        return super().event(event)

    def set_app_font(self):
        if platform.system() == 'Darwin':
            self.setFont(QFont('Arial', 13))
        else:
            self.setFont(QFont('Arial', 11))

    def handle_open_file_request(self, url):
        if self.files_to_be_opened is None:
            self.files_to_be_opened = []
        self.files_to_be_opened.append(url.toLocalFile())


app = EQFreqApp(list(sys.argv))
MediaDevices = QMediaDevices()
Settings = QSettings(SETTINGS_PATH, QSettings.Format.IniFormat)
QtVersion = QLibraryInfo.version().toString()
