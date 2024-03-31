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
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSettings
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtGui import QFont
from Model.del_temp_audio import delTempAudio
from Utilities.str2bool import str2bool
from definitions import SETTINGS_PATH

app_name = 'EarQuiz Frequencies'


class EQFreqApp(QtWidgets.QApplication):
    openFileRequest = QtCore.pyqtSignal(QtCore.QUrl, name='openFileRequest')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setApplicationDisplayName(app_name)
        self.setApplicationName(app_name)
        if platform.system() != 'Linux':
            self.setOrganizationDomain("earquiz.org")
        self.setOrganizationName("EarQuiz")
        self.set_app_font()
        self.aboutToQuit.connect(delTempAudio)

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


app = EQFreqApp(list(sys.argv))
launch_files_onstart = sys.argv[1:] if len(sys.argv) > 1 else None
MediaDevices = QMediaDevices()
Settings = QSettings(SETTINGS_PATH, QSettings.Format.IniFormat)
NativeAudioBackend = str2bool(Settings.value('Actions/actionNative', False))
