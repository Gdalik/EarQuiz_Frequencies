from PyQt6.QtCore import QObject
from PyQt6.QtGui import QTextDocument, QTextBlockFormat, QTextCursor
from GUI.Help.QuickHelpWin import QuickHelpWin
from definitions import ROOT_DIR, Settings
from pathlib import Path
from Utilities.str2bool import str2bool


class HelpActions(QObject):
    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.actionGetting_Started.triggered.connect(self.onGettingStarted_called)
        self.mw_contr.signals.audioSourcesRestored.connect(self.onAppStartup)
        self.GS_Win = QuickHelpWin(self.mw_view, title='Getting Started with EarQuiz Frequencies',
                           showagain_settings_path='MessageBoxes/ShowGettingStartedOnStartup')

    def onGettingStarted_called(self):
        if self.GS_Win.isVisible():
            return
        content_path = Path(ROOT_DIR, 'GUI', 'Help', 'Data', 'get_started.md').absolute()
        with open(content_path, 'r') as f:
            content = f.read()
        document = QTextDocument()
        document.setMarkdown(content)
        font = document.defaultFont()
        font.setPointSize(16)
        document.setDefaultFont(font)
        self.GS_Win.TextBr.setDocument(document)
        blockFmt = QTextBlockFormat()
        blockFmt.setLineHeight(120, 1)
        self.GS_Win.TextBr.selectAll()
        theCursor = self.GS_Win.TextBr.textCursor()
        theCursor.mergeBlockFormat(blockFmt)
        theCursor.clearSelection()
        theCursor.setPosition(0)
        self.GS_Win.TextBr.setTextCursor(theCursor)
        self.GS_Win.show()

    def onAppStartup(self):
        if str2bool(Settings.value('MessageBoxes/ShowGettingStartedOnStartup', True)):
            self.onGettingStarted_called()
