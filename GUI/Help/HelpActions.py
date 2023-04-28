import platform

from PyQt6.QtCore import QObject
from PyQt6.QtGui import QTextDocument
from GUI.Help.QuickHelpWin import QuickHelpWin
from GUI.Misc.TextBrowserDocParameters import setParameters
from definitions import ROOT_DIR, Settings
from pathlib import Path
from Utilities.str2bool import str2bool
from Model.get_version import version


class HelpActions(QObject):
    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.actionGetting_Started.triggered.connect(self.onGettingStarted_called)
        self.mw_contr.signals.audioSourcesRestored.connect(self.onAppStartup)
        self.GS_Win = QuickHelpWin(self.mw_view, title=f'Getting Started with EarQuiz Frequencies v{version()}',
                           showagain_settings_path='MessageBoxes/ShowGettingStartedOnStartup')

    def onGettingStarted_called(self):
        if self.GS_Win.isVisible():
            return
        content_path = Path(ROOT_DIR, 'GUI', 'Help', 'Data', 'get_started.md').absolute()
        with open(content_path, 'r') as f:
            content = f.read()
        document = QTextDocument()
        document.setMarkdown(content)
        self.GS_Win.TextBr.setDocument(document)
        if platform.system() == 'Darwin':
            font_size = 16
            line_height = 120
        else:
            font_size = 13
            line_height = 110
        setParameters(self.GS_Win.TextBr, document, font_size=font_size, line_height=line_height)
        self.GS_Win.show()

    def onAppStartup(self):
        if str2bool(Settings.value('MessageBoxes/ShowGettingStartedOnStartup', True)):
            self.onGettingStarted_called()
