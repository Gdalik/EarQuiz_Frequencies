from GUI.About.AboutDialog import Ui_AboutDialog
from PyQt6.QtWidgets import QDialog
from Model.get_version import version


class AboutDialogView(QDialog, Ui_AboutDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.VersionLab.setText(f'Version {version()}')
        self.tabWidget.setCurrentIndex(0)
