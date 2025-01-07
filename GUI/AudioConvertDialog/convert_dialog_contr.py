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

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QRadioButton
from GUI.AudioConvertDialog.convert_dialog_view import Ui_AudioConvertDialog


class ConvertFilesDialogContr(QDialog, Ui_AudioConvertDialog):
    def __init__(self):
        super().__init__()
        Flags = Qt.WindowType(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
                              Qt.WindowType.WindowCloseButtonHint)
        self.setWindowFlags(Flags)
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText('Convert')
        self.WAVBut.setChecked(True)
        self.SameAsOriginalBut.setChecked(True)

    @property
    def audio_format(self):
        return [RB.text() for RB in self.FormatGroup.findChildren(QRadioButton) if RB.isChecked()][0]

    @property
    def target_samplerate_mode(self):
        if self.SameAsOriginalBut.isChecked():
            return 'original'
        if self.SR441But.isChecked():
            return '44.1k'
        if self.SR48But.isChecked():
            return '48k'
        if self.DivisibleBut.isChecked():
            return 'auto_div'
