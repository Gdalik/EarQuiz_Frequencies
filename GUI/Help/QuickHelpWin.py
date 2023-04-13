from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTextBrowser, QCheckBox
from PyQt6.QtCore import Qt
from definitions import Settings
from Utilities.str2bool import str2bool


class QuickHelpWin(QWidget):
    def __init__(self, *args, title='', showagain_settings_path=None, **kwargs):
        super(QuickHelpWin, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowMaximizeButtonHint)
        self.setWindowTitle(title)
        self.resize(600, 400)

        self.TextBr = QTextBrowser()
        self.TextBr.setOpenExternalLinks(True)
        self.TextBr.setOpenLinks(True)

        self.OkButton = QPushButton('Ok')
        self.OkButton.setMaximumWidth(50)
        self.OkButton.clicked.connect(self.onOk_clicked)

        self.NotShowAgainBut = QCheckBox("Don't show this window on startup")
        self.NotShowAgainBut.setCheckable(True)

        self.showagain_settings_path = showagain_settings_path
        if showagain_settings_path is not None:
            showagain = Settings.value(showagain_settings_path)
            if showagain is not None:
                self.NotShowAgainBut.setChecked(not str2bool(showagain))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.TextBr)
        self.layout.addWidget(self.NotShowAgainBut)
        self.layout.addWidget(self.OkButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def onOk_clicked(self):
        if self.showagain_settings_path is not None:
            Settings.setValue(self.showagain_settings_path, not self.NotShowAgainBut.isChecked())
        self.close()
