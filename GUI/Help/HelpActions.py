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

import platform
import webbrowser
from PyQt6.QtCore import QObject, QTimer
from PyQt6.QtGui import QTextDocument
from GUI.Help.QuickHelpWin import QuickHelpWin
from GUI.Misc.TextBrowserDocParameters import setParameters
from definitions import ROOT_DIR
from application import Settings
from pathlib import Path
from Utilities.str2bool import str2bool
from Model.get_version import version


class HelpActions(QObject):
    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.actionGetting_Started.triggered.connect(self.onGettingStarted_called)
        self.mw_view.actionOnline_Help.triggered.connect(self.onOnlineHelp_called)
        self.mw_view.actionVideo_Tutorial.triggered.connect(self.onVideoTutorial_called)
        self.mw_view.actionVideo_Tutorial_Rus.triggered.connect(self.onVideoTutorialRus_called)
        self.mw_view.actionReport_an_Issue.triggered.connect(self.onReportIssue_called)
        self.mw_view.actionGo_To_Source_Code.triggered.connect(self.onGoToSourceCode_called)
        self.mw_view.actionAsk_and_Discuss.triggered.connect(self.onAskAndDiscuss_called)
        self.mw_view.signals.MWFirstShown.connect(self.onAppStartup)
        self.GS_Win = QuickHelpWin(self.mw_view, title=f'Getting Started with EarQuiz Frequencies v{version()}',
                           showagain_settings_path='MessageBoxes/ShowGettingStartedOnStartup')

    def onGettingStarted_called(self, StartUp=False):
        if self.GS_Win.isVisible():
            return
        content_path = Path(ROOT_DIR, 'GUI', 'Help', 'Data', 'get_started.md').absolute()
        with open(content_path, 'r', encoding='utf-8') as f:
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
        self.GS_Win.show() if not StartUp else QTimer.singleShot(1000, self.GS_Win.show)

    def onAppStartup(self):
        if str2bool(Settings.value('MessageBoxes/ShowGettingStartedOnStartup', True)):
            self.onGettingStarted_called(StartUp=True)

    def onOnlineHelp_called(self):
        webbrowser.open('https://earquiz.org/manuals/earquiz-frequencies-help/')

    def onVideoTutorial_called(self):
        webbrowser.open('https://youtu.be/XOJai5Fdofw')

    def onVideoTutorialRus_called(self):
        webbrowser.open('https://youtu.be/pz-V5KNaBWU')

    def onReportIssue_called(self):
        webbrowser.open('https://github.com/Gdalik/EarQuiz_Frequencies/issues')

    def onAskAndDiscuss_called(self):
        webbrowser.open('https://github.com/Gdalik/EarQuiz_Frequencies/discussions')

    def onGoToSourceCode_called(self):
        webbrowser.open('https://github.com/Gdalik/EarQuiz_Frequencies')

