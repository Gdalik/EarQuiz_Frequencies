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


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon
from Model.del_temp_audio import delTempAudio
import definitions as defs


class EQFreqApp(QtWidgets.QApplication):
    openFileRequest = QtCore.pyqtSignal(QtCore.QUrl, name='openFileRequest')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
        self.setApplicationDisplayName(defs.app_name)
        self.setApplicationName(defs.app_name)
        self.setOrganizationDomain("earquiz.org")
        self.aboutToQuit.connect(delTempAudio)

    def event(self, event):
        if event.type() == QtCore.QEvent.Type.FileOpen:
            self.openFileRequest.emit(event.url())
            return True
        return super().event(event)
