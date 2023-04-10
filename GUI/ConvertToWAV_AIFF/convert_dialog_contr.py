from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QDialogButtonBox

from GUI.ConvertToWAV_AIFF.convert_dialog_view import Ui_ConvertToWAV_AIFF_Dialog


class ConvertFilesDialogContr(QDialog, Ui_ConvertToWAV_AIFF_Dialog):
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
        return 'AIFF' if self.AIFFBut.isChecked() else 'WAVE'

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
