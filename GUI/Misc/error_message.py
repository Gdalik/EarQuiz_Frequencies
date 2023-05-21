#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox


def error_message(window, msg: str, modal='WinModal'):
    emsg = QtWidgets.QErrorMessage(window)
    if modal == 'AppModal':
        emsg.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
    elif modal == 'WinModal':
        emsg.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
    else:
        emsg.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        emsg.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
    emsg.showMessage(msg)


def reformat_message(window, msg='The file seems to be unreadable. Try to reformat it?'):
    win = QMessageBox(window)
    win.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    win.setDefaultButton(QMessageBox.StandardButton.Yes)
    win.setIcon(QMessageBox.Icon.Question)
    win.setText(msg)
    return win.exec()
