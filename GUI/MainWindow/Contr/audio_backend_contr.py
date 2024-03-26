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

import os
import sys
from PyQt6.QtCore import QObject, QTimer
from PyQt6.QtGui import QActionGroup
from PyQt6.QtWidgets import QMessageBox
from GUI.Misc.restart_message import restart_message
from application import NativeAudioBackend


class AudioBackendContr(QObject):
    AudioBackendActionGroup: QActionGroup

    def __init__(self, parent):  # parent: MainWindowContr
        super().__init__()
        self.parent = parent
        self.mw_view = self.parent.mw_view
        self.actionFFmpeg = self.mw_view.actionFFmpeg
        self.actionNative = self.mw_view.actionNative
        self.setAudioBackendAG()

    def setAudioBackendAG(self):
        self.AudioBackendActionGroup = QActionGroup(self)
        self.AudioBackendActionGroup.setExclusive(True)
        self.AudioBackendActionGroup.addAction(self.actionFFmpeg)
        self.AudioBackendActionGroup.addAction(self.actionNative)
        self.AudioBackendActionGroup.triggered.connect(self.onAudioEngineActionToggled)

    def onAudioEngineActionToggled(self, act):
        if act == self.storedOption:
            return
        if restart_message(self.mw_view) == QMessageBox.StandardButton.Yes:
            self.parent.onAppClose()
            QTimer.singleShot(0, lambda: os.execl(sys.executable, sys.executable, sys.argv[0]))
        else:
            self.AudioBackendActionGroup.blockSignals(True)
            if NativeAudioBackend:
                self.actionNative.setChecked(True)
            else:
                self.actionFFmpeg.setChecked(True)
            self.AudioBackendActionGroup.blockSignals(False)

    @property
    def storedOption(self):
        return self.actionNative if NativeAudioBackend else self.actionFFmpeg
