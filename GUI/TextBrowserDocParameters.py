from PyQt6.QtGui import QTextBlockFormat


def setParameters(TextBrowser, document, font_size=16, line_height=120):
    font = document.defaultFont()
    font.setPointSize(font_size)
    document.setDefaultFont(font)
    blockFmt = QTextBlockFormat()
    blockFmt.setLineHeight(line_height, 1)
    TextBrowser.selectAll()
    theCursor = TextBrowser.textCursor()
    theCursor.mergeBlockFormat(blockFmt)
    theCursor.clearSelection()
    theCursor.setPosition(0)
    TextBrowser.setTextCursor(theCursor)
