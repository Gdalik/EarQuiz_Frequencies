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

