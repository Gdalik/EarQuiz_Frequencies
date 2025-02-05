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

from PySide6.QtCore import QObject
from PySide6.QtGui import QActionGroup
from PySide6.QtMultimedia import QMediaDevices
from application import MediaDevices, Settings


class AudioDevicesView(QObject):
    def __init__(self, parent):
        super().__init__()
        self.mw = parent
        self.audio_devices = MediaDevices
        self.default_name = 'System Sound Output Device'
        self.mw.AudioDevicesGroup = QActionGroup(self)
        self.setAudioDeviceActions()
        self.audio_devices.audioOutputsChanged.connect(self.updateAudioDeviceActions)
        self.selectOutput(Settings.value('Actions/SelectedAudioOut', self.default_name))

    def setAudioDeviceActions(self):
        audio_outs = [out.description() for out in QMediaDevices.audioOutputs()]
        audio_outs.insert(0, self.default_name)
        for AO in audio_outs:
            action = self.mw.menuAudio_Device.addAction(AO)
            self.mw.AudioDevicesGroup.addAction(action)
            action.setCheckable(True)

    def updateAudioDeviceActions(self):
        items = self.mw.menuAudio_Device.actions()
        checked_act = self.mw.AudioDevicesGroup.checkedAction().text() if self.mw.AudioDevicesGroup.checkedAction() else None
        for item in items:
            self.mw.AudioDevicesGroup.removeAction(item)
            self.mw.menuAudio_Device.removeAction(item)
        self.setAudioDeviceActions()
        if checked_act:
            self.selectOutput(checked_act)

    def selectOutput(self, name: str):
        items = self.mw.menuAudio_Device.actions()
        for act in items:
            if act.text() == name and not act.isChecked():
                act.toggle()
                return
        self.selectOutput(self.default_name)

    def selectedOutput(self):
        outputs = self.audio_devices.audioOutputs()
        current = self.mw.AudioDevicesGroup.checkedAction()
        if current.text() == self.default_name:
            return self.audio_devices.defaultAudioOutput()
        for device in outputs:
            if device.description() == current.text():
                return device
