import contextlib
import platform
import subprocess
import os
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt


def SuccessDialog(mw, filespath: str, mode_name='Learning'):
    msg = QMessageBox(mw)
    msg.setWindowModality(Qt.WindowModality.ApplicationModal)
    msg.setText(f'{mode_name} files successfully created in "{filespath}"!')
    msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Ok)
    manager = 'Explorer' if platform.system() == 'Windows' else 'Finder'
    msg.button(QMessageBox.StandardButton.Open).setText(f'Show in {manager}')
    btn = msg.exec()
    if btn == QMessageBox.StandardButton.Open:
        if platform.system() == 'Darwin':
            with contextlib.suppress(Exception):
                subprocess.run(["open", filespath])
        elif platform.system() == 'Windows':
            os.startfile(filespath)
            '''filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            video_win_path = rf'{filespath}'
            cmd = [filebrowser_path, '/select,', video_win_path]'''
