from PySide6.QtWidgets import QListWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class PlayListWidget(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self._placeholder_text = "Add new tracks by pressing '+'\n or directly drag the items here"

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.count() == 0:
            painter = QPainter(self.viewport())
            painter.save()
            painter.setPen('gray')
            font_metrics = self.fontMetrics()
            elided_text = font_metrics.elidedText(self._placeholder_text, Qt.TextElideMode.ElideNone, self.viewport().width())
            painter.drawText(self.viewport().rect(), Qt.AlignmentFlag.AlignCenter, elided_text)
            painter.restore()
