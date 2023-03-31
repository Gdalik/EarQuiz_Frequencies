import contextlib
import platform
import subprocess
import os
from PyQt6.QtWidgets import QMessageBox


def SuccessDialog(mw, filespath: str, mode_name='Learning'):
    msg = QMessageBox(mw)
    msg.setText(f'{mode_name} files successfully created in "{filespath}"!')
    msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Close)
    manager = 'Explorer' if platform.system() == 'Windows' else 'Finder'
    msg.button(QMessageBox.StandardButton.Open).setText(f'Show in {manager}')
    btn = msg.exec()
    if btn == QMessageBox.StandardButton.Open:
        if platform.system() == 'Darwin':
            with contextlib.suppress(Exception):
                subprocess.run(["open", filespath])
        elif platform.system() == 'Windows':
            os.startfile(filespath)
