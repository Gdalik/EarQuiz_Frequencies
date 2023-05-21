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
