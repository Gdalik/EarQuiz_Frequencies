from PySide6 import QtWidgets, QtCore


def error_message(window, msg: str, modal='WinModal'):
    if window is not None:
        emsg = QtWidgets.QErrorMessage(window)
    else:
        emsg = QtWidgets.QErrorMessage()
    if modal == 'AppModal':
        emsg.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
    elif modal == 'WinModal':
        emsg.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
    else:
        emsg.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        emsg.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
    emsg.showMessage(msg)
