from PyQt6.QtWidgets import QDialog, QDialogButtonBox
from PyQt6.QtCore import Qt
from GUI.MakeLearnTestFiles.make_learn_test_dialog_view import Ui_MakeLearnTest_Dialog
from Model.globals import supported_bitrates_mp3, supported_bitrates_ogg


class MakeLearnTestDialogContr(QDialog, Ui_MakeLearnTest_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText('Make')
        self.WaveButt.setChecked(True)
        self.setBitrateComboEnabled(False)
        self.WaveButt.toggled.connect(self.onLosslessFormatToggled)
        self.AiffButt.toggled.connect(self.onLosslessFormatToggled)
        self.FlacBut.toggled.connect(self.onLosslessFormatToggled)
        self.Mp3But.toggled.connect(self.onLossyFormatToggled)
        self.OggBut.toggled.connect(self.onLossyFormatToggled)


    def setBitrateComboEnabled(self, arg: bool):
        self.BitrateLab.setEnabled(arg)
        self.BitrateCombo.setEnabled(arg)
        self.BitrateCombo.clear()

    def onLosslessFormatToggled(self, value):
        if not value:
            return
        self.setBitrateComboEnabled(False)

    def onLossyFormatToggled(self, value):
        if not value:
            return
        bitrates = supported_bitrates_ogg if self.OggBut.isChecked() else supported_bitrates_mp3
        self.setBitrateComboEnabled(True)
        for br in bitrates:
            self.BitrateCombo.addItem(f'{br}kbps')
        self.BitrateCombo.setCurrentText('320kbps')