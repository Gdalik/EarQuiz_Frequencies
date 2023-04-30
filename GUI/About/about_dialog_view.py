import platform
from pathlib import Path
from definitions import ROOT_DIR
from GUI.About.AboutDialog import Ui_AboutDialog
from GUI.Misc.TextBrowserDocParameters import setParameters
from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6.QtGui import QTextDocument
from Model.get_version import version


class AboutDialogView(QDialog, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win_os_settings()
        self.setCredits()
        self.VersionLab.setText(f'Version {version()}')
        self.tabWidget.setCurrentIndex(0)

    def win_os_settings(self):
        if platform.system() != 'Windows':
            return
        labels = self.findChildren(QLabel)
        L: QLabel
        for L in labels:
            font = L.font()
            size = font.pointSize() - 2
            font.setPointSize(size)
            L.setFont(font)

    def setCredits(self):
        content_path = Path(ROOT_DIR, 'GUI', 'About', 'credits.md').absolute()
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
        document = QTextDocument()
        document.setMarkdown(content)
        self.creditsText.setDocument(document)
        if platform.system() == 'Darwin':
            font_size = 14
            line_height = 120
        else:
            font_size = 12
            line_height = 110
        setParameters(self.creditsText, document, font_size=font_size, line_height=line_height)
