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

import contextlib
import platform
import webbrowser
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QTextBrowser
from PyQt6.QtGui import QTextDocument
from PyQt6.QtCore import Qt
from Model.get_version import version
from GUI.Misc.TextBrowserDocParameters import setParameters


class UpdCheckDialog(QWidget):
    def __init__(self, *args, **kwargs):
        super(UpdCheckDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle('Check for Updates...')
        self.setup_view()

    def setup_view(self):
        self.setWindowFlags(Qt.WindowType.Window |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.WindowCloseButtonHint |
                            Qt.WindowType.CustomizeWindowHint |
                            Qt.WindowType.WindowMaximizeButtonHint)

        self.MainLab = QLabel('New version of EarQuiz Frequencies is available!')

        self.TextBr = QTextBrowser()
        self.TextBr.setOpenExternalLinks(True)
        self.TextBr.setStyleSheet("selection-color: white; selection-background-color: rgb(0, 150, 255);")

        self.DownloadBut = QPushButton('Download')
        self.DownloadBut.setMaximumWidth(85)
        self.CloseBut = QPushButton('Close')
        self.CloseBut.setMaximumWidth(60)
        self.CloseBut.clicked.connect(self.close, type=Qt.ConnectionType.SingleShotConnection)

        self.ButtonBox = QHBoxLayout()
        self.ButtonBox.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ButtonBox.addWidget(self.DownloadBut)
        self.ButtonBox.addWidget(self.CloseBut)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.MainLab)
        self.layout.addWidget(self.TextBr)
        self.layout.addLayout(self.ButtonBox)
        self.setLayout(self.layout)
        self.resize(500, 300)


class UpdCheckView:
    Dialog: None or UpdCheckDialog

    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.Dialog = None
        self.download_link = None

    def noUpdMsg(self):
        msg = QMessageBox(self.mw_view)
        msg.setText(f'You are running the latest version of EarQuiz Frequencies: {version()}!')
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def showUpdWindow(self, data: dict):
        if self.Dialog is not None and self.Dialog.isVisible():
            return
        self.download_link = data['download_mac'] if platform.system() == 'Darwin' else data['download_win']
        self.Dialog = UpdCheckDialog(self.mw_view)
        self.setMainLabelText(data)
        self.setVersionInfo(data)
        self.setDownloadButton()
        self.Dialog.show()

    def setMainLabelText(self, data: dict):
        v_data = data['version']
        version_data_str = "%d.%d.%d" % (v_data['major'], v_data['minor'], v_data['patch'])
        self.Dialog.MainLab.setText(f'EarQuiz Frequencies v{version_data_str} is available for download!')

    def setVersionInfo(self, data: dict):
        info_data = data.get('info_data')
        if not info_data:
            self.Dialog.TextBr.setVisible(False)
            self.Dialog.resize(250, 100)
            return
        document = QTextDocument()
        document.setMarkdown(info_data)
        self.Dialog.TextBr.setDocument(document)
        if platform.system() == 'Darwin':
            font_size = 14
            line_height = 120
        else:
            font_size = 12
            line_height = 110
        setParameters(self.Dialog.TextBr, document, font_size=font_size, line_height=line_height)

    def setDownloadButton(self):
        with contextlib.suppress(TypeError):
            self.Dialog.DownloadBut.clicked.disconnect()
        self.Dialog.DownloadBut.clicked.connect(self.onDownloadClicked)

    def onDownloadClicked(self):
        webbrowser.open(self.download_link)
