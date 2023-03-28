from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog
from PyQt6.QtCore import Qt
from GUI.MakeLearnTestFiles.make_learn_test_dialog_view import Ui_MakeLearnTest_Dialog
from Model.globals import supported_bitrates_mp3, supported_bitrates_ogg
from definitions import EXERCISE_DIR
from pathlib import Path
import re


class MakeLearnTestDialogContr(QDialog, Ui_MakeLearnTest_Dialog):
    def __init__(self, mw_contr):
        super().__init__()
        self.setupUi(self)
        Flags = Qt.WindowType(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
                              Qt.WindowType.WindowCloseButtonHint)
        self.setWindowFlags(Flags)
        self.setWindowTitle(f'{self.windowTitle()} (Source: {mw_contr.SourceAudio.name})')
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText('Make')
        self.WaveButt.setChecked(True)
        self.setBitrateComboEnabled(False)
        self.WaveButt.toggled.connect(self.onLosslessFormatToggled)
        self.AiffButt.toggled.connect(self.onLosslessFormatToggled)
        self.FlacBut.toggled.connect(self.onLosslessFormatToggled)
        self.Mp3But.toggled.connect(self.onLossyFormatToggled)
        self.OggBut.toggled.connect(self.onLossyFormatToggled)
        self.UseAsFolderNameBut.setChecked(True)
        self.UseAsPrefixNameBut.setChecked(True)
        self.parent_path = EXERCISE_DIR
        Path.mkdir(Path(self.parent_path), parents=True, exist_ok=True)
        self.ExerciseFolderLine.setText(self.parent_path)
        self.ExerciseNameLine.textChanged.connect(self.onExerciseNameChanged)
        self.UseAsFolderNameBut.toggled.connect(self.onExerciseNameChanged)
        self.ChangeFolderBut.clicked.connect(self.onChangeFolderBut_clicked)
        self.ExerciseNameLine.setText(self.generateExcName())


    def setBitrateComboEnabled(self, arg: bool):
        self.BitrateLab.setEnabled(arg)
        self.BitrateCombo.setEnabled(arg)
        self.BitrateCombo.clear()

    def onChangeFolderBut_clicked(self):
        Dialog = QFileDialog.getExistingDirectory(self, "Select folder:", self.parent_path,
                                                        QFileDialog.Option.ShowDirsOnly)
        if not Dialog:
            return
        self.parent_path = Dialog
        self.ExerciseFolderLine.setText(self.excPath)
        if self.UseAsFolderNameBut.isChecked():
            self.ExerciseNameLine.setText(self.avoid_same_dirpath(self.excPath)[1])

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

    def generateExcName(self):
        return self.avoid_same_dirpath(str(Path(self.ExerciseFolderLine.text(), 'Exercise1')))[1]

    def onExerciseNameChanged(self):
        self.ExerciseFolderLine.setText(self.excPath)

    @staticmethod
    def avoid_same_dirpath(dirpath: str):
        result = Path(dirpath)
        while result.exists():
            digit_end = re.search(r'\d+$', dirpath)
            if digit_end is not None:
                digit_end = int(digit_end.group())
                result = Path(f'{str(result)[:-len(str(digit_end))]}{digit_end + 1}')
            else:
                result = Path(f'{result}1')
        return str(result), result.name

    @property
    def excPath(self):
        return str(Path(self.parent_path, self.ExerciseNameLine.text())) if self.UseAsFolderNameBut.isChecked() \
            else self.parent_path
