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

import contextlib
import os
import platform
import subprocess
from GUI.Misc.filemanager_name import fn
from PyQt6.QtWidgets import QMessageBox


def SuccessDialog(mw, filespath: str, mode_name='Learning'):
    msg = QMessageBox(mw)
    msg.setText(f'{mode_name} files successfully created in "{filespath}"!')
    msg.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Close)
    msg.button(QMessageBox.StandardButton.Open).setText(f'Show in {fn()}')
    btn = msg.exec()
    if btn == QMessageBox.StandardButton.Open:
        if platform.system() == 'Darwin':
            with contextlib.suppress(Exception):
                subprocess.run(["open", filespath])
        elif platform.system() == 'Windows':
            os.startfile(filespath)
        elif platform.system() == 'Linux':
            subprocess.run(['dbus-send', '--session', '--print-reply', '--dest=org.freedesktop.FileManager1',
                            '--type=method_call', '/org/freedesktop/FileManager1',
                            'org.freedesktop.FileManager1.ShowItems',
                            f'array:string:"file://{filespath}"', 'string:""'])
