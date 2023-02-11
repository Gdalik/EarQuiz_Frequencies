from PyQt6.QtCore import QObject
from PyQt6.QtMultimedia import QMediaDevices
from PyQt6.QtGui import QActionGroup
from definitions import MediaDevices


class AudioDevicesView(QObject):
    def __init__(self, parent):
        super().__init__()
        self.mw = parent
        self.audio_devices = MediaDevices
        self.default_name = 'Default System Device'
        self.mw.AudioDevicesGroup = QActionGroup(self)
        self.setAudioDeviceActions()
        self.audio_devices.audioOutputsChanged.connect(self.updateAudioDeviceActions)
        self.selectOutput(self.default_name)

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

    def selectedOutput(self):
        outputs = self.audio_devices.audioOutputs()
        current = self.mw.AudioDevicesGroup.checkedAction()
        if current.text() == self.default_name:
            return self.audio_devices.defaultAudioOutput()
        for device in outputs:
            if device.description() == current.text():
                return device
