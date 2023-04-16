from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextBrowser, QCheckBox, QLineEdit, \
    QToolButton, QStyle
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor, QTextDocument, QKeySequence, QAction
from definitions import Settings
from Utilities.str2bool import str2bool


class QuickHelpWin(QWidget):
    def __init__(self, *args, title='', showagain_settings_path=None, **kwargs):
        super(QuickHelpWin, self).__init__(*args, **kwargs)
        self.title = title
        self.showagain_settings_path = showagain_settings_path
        self.setup_view()
        self.TextBr.setFocus()

    def setup_view(self):
        self.setWindowFlags(Qt.WindowType.Window |
                            Qt.WindowType.WindowStaysOnTopHint |
                            Qt.WindowType.WindowCloseButtonHint |
                            Qt.WindowType.CustomizeWindowHint |
                            Qt.WindowType.WindowMaximizeButtonHint)
        self.setWindowTitle(self.title)
        self.resize(600, 400)

        self.SearchLine = QLineEdit()
        self.SearchLine.setPlaceholderText('Search...')
        self.SearchLine.textChanged.connect(self.onSearchTextChanged)
        self.SearchLine.setClearButtonEnabled(True)
        actionActivateSearch = QAction(self)
        actionActivateSearch.setShortcut(QKeySequence.StandardKey.Find)
        actionActivateSearch.triggered.connect(self.SearchLine.setFocus)
        self.addAction(actionActivateSearch)
        self.SearchLine.returnPressed.connect(self.findNext)
        actionEscPressed = QAction(self.SearchLine)
        actionEscPressed.setShortcut(QKeySequence(Qt.Key.Key_Escape))
        actionEscPressed.triggered.connect(self.searchLineEscapePressed)
        self.SearchLine.addAction(actionEscPressed)

        searchButSS = 'QToolButton{\nborder: None;\n}\nQToolButton:hover{\nbackground: rgba(192, 192, 192, 128);' \
                         '\nborder-radius: 4px;\n}' \
                         '\nQToolButton:pressed{\nborder: 1px inset gray;\nbackground: rgba(118, 214, 255, 85)\n}'
        self.SearchForward = QToolButton()
        self.SearchForward.setStyleSheet(searchButSS)
        next_arrow = QStyle.StandardPixmap.SP_ArrowDown
        next_icon = self.style().standardIcon(next_arrow)
        self.SearchForward.setIcon(next_icon)
        self.SearchForward.clicked.connect(self.findNext)

        self.SearchBack = QToolButton()
        prev_arrow = QStyle.StandardPixmap.SP_ArrowUp
        prev_icon = self.style().standardIcon(prev_arrow)
        self.SearchBack.setIcon(prev_icon)
        self.SearchBack.setStyleSheet(searchButSS)
        self.SearchBack.clicked.connect(self.findPrev)
        self.setBackForwButEnabed(False)

        self.SearchLay = QHBoxLayout()
        self.SearchLay.setSpacing(0)
        self.SearchLay.addWidget(self.SearchLine)
        self.SearchLay.addWidget(self.SearchBack)
        self.SearchLay.addWidget(self.SearchForward)

        self.TextBr = QTextBrowser()
        self.TextBr.setOpenExternalLinks(True)
        self.TextBr.setOpenLinks(True)
        self.TextBr.setStyleSheet("selection-color: white; selection-background-color: rgb(0, 150, 255);")

        self.OkButton = QPushButton('Ok')
        self.OkButton.setMaximumWidth(50)
        self.OkButton.clicked.connect(self.onOk_clicked)

        self.NotShowAgainBut = QCheckBox("Don't show this window on startup")
        self.NotShowAgainBut.setCheckable(True)

        self.restoreNotShowAgainBut()

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SearchLay)
        self.layout.addWidget(self.TextBr)
        self.layout.addWidget(self.NotShowAgainBut)
        self.layout.addWidget(self.OkButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.layout)

    def onOk_clicked(self):
        if self.showagain_settings_path is not None:
            Settings.setValue(self.showagain_settings_path, not self.NotShowAgainBut.isChecked())
        self.close()

    def closeEvent(self, ev):
        self.restoreNotShowAgainBut()
        super(QuickHelpWin, self).closeEvent(ev)

    def restoreNotShowAgainBut(self):
        if self.showagain_settings_path is not None:
            showagain = Settings.value(self.showagain_settings_path)
            if showagain is not None:
                self.NotShowAgainBut.setChecked(not str2bool(showagain))

    def findText(self, fromStart=True, mode='forward'):
        if text := self.SearchLine.text():
            if fromStart:
                self._cursorToStart()
            if mode == 'forward':
                self.TextBr.find(text)
            elif mode == 'backward':
                self.TextBr.find(text, QTextDocument.FindFlag.FindBackward)
        else:
            self.deselectAll()

    def setBackForwButEnabed(self, arg: bool):
        self.SearchBack.setEnabled(arg)
        self.SearchForward.setEnabled(arg)

    def onSearchTextChanged(self, value):
        self.findText()
        self.setBackForwButEnabed(len(value) > 0)

    def _cursorToStart(self):
        cursor = QTextCursor()
        cursor.setPosition(0)
        self.TextBr.setTextCursor(cursor)

    def deselectAll(self):
        cursor = self.TextBr.textCursor()
        cursor.clearSelection()
        self.TextBr.setTextCursor(cursor)

    def findNext(self):
        self.findText(fromStart=False)

    def findPrev(self):
        self.findText(fromStart=False, mode='backward')

    def searchLineEscapePressed(self):
        self.SearchLine.clear()
        self.TextBr.setFocus()
