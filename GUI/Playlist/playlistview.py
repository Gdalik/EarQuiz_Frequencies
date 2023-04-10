from PyQt6.QtCore import Qt, pyqtSignal, QObject, QMimeData, QUrl, QItemSelection, QItemSelectionModel, QModelIndex
from PyQt6.QtGui import QPainter, QDrag, QColor
from PyQt6.QtWidgets import QTableView, QAbstractItemView, QHeaderView

from Utilities.urlcheck import validUrls


class PL_Signals(QObject):
    urlsDropped = pyqtSignal(list, int)
    dragDropFromPLFinished = pyqtSignal(Qt.DropAction)
    keyPressed = pyqtSignal(int)


class PlaylistView(QTableView):
    signals = PL_Signals()

    def __init__(self, parent):
        super().__init__()
        self._placeholder_text = "Add new tracks by pressing '+'\n or directly drag the items here"
        self.setDragDrop()
        self.setSelect()
        self.setHeader()
        self.setShowGrid(False)
        self.selectedItems = []
        self.MouseButtonPressed = None
        self.alt_pressed = None

    @property
    def Model(self):
        return self.model().sourceModel() if self.model() else None

    def setDragDrop(self):
        self.viewport().setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QTableView.DragDropMode.DragDrop)
        self.setDragDropOverwriteMode(False)

    def setSelect(self):
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def setHeader(self):
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.Model or self.Model.rowCount(QModelIndex) == 0:
            painter = QPainter(self.viewport())
            painter.save()
            painter.setPen(QColor('gray'))
            font_metrics = self.fontMetrics()
            elided_text = font_metrics.elidedText(self._placeholder_text, Qt.TextElideMode.ElideNone,
                                                  self.viewport().width())
            painter.drawText(self.viewport().rect(), Qt.AlignmentFlag.AlignCenter, elided_text)
            painter.restore()

    def dragEnterEvent(self, event):
        super(PlaylistView, self).dragEnterEvent(event)
        if self.checkDroppedMimeData(event.mimeData()):
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()

    def dragMoveEvent(self, event):
        super(PlaylistView, self).dragMoveEvent(event)
        if self.checkDroppedMimeData(event.mimeData()):
            cur_index = self.indexAt(self.viewport().mapFromGlobal(self.cursor().pos()))
            self.setCurrentIndex(cur_index)
            event.accept()

    def dropEvent(self, event):
        super(PlaylistView, self).dropEvent(event)
        if self.checkDroppedMimeData(event.mimeData()):
            event.accept()
            valid_urls = validUrls(event.mimeData().urls())
            if valid_urls:
                self.signals.urlsDropped.emit(valid_urls, self.model().mapToSource(self.currentIndex()).row())

    def checkDroppedMimeData(self, data):
        return data.hasUrls() and data.objectName() != 'FromPlaylist'

    def mousePressEvent(self, e) -> None:
        super(PlaylistView, self).mousePressEvent(e)
        self.MouseButtonPressed = e.button()

    def mouseMoveEvent(self, event):
        super(PlaylistView, self).mouseMoveEvent(event)
        if not self.selectionModel().selectedRows():
            return
        if self.MouseButtonPressed != Qt.MouseButton.LeftButton:
            return
        drag = QDrag(self)
        mimeData = QMimeData()
        mimeData.setObjectName('FromPlaylist')
        paths = [QUrl.fromLocalFile(item.path) for item in self.selectedItems]
        mimeData.setUrls(paths)
        drag.setMimeData(mimeData)
        action = drag.exec(Qt.DropAction.CopyAction) if self.alt_pressed \
            else drag.exec(Qt.DropAction.CopyAction | Qt.DropAction.MoveAction)
        self.signals.dragDropFromPLFinished.emit(action)

    def keyPressEvent(self, e):
        super(PlaylistView, self).keyPressEvent(e)
        self.signals.keyPressed.emit(e.key())

    def selectRows(self, first: int, last: int, scrolling=True):
        selection = QItemSelection()
        selection.select(self.Model.index(first, 0),
                         self.Model.index(last, 0))
        self.selectionModel().select(self.model().mapSelectionFromSource(selection),
                                     QItemSelectionModel.SelectionFlag.SelectCurrent |
                                     QItemSelectionModel.SelectionFlag.ClearAndSelect |
                                     QItemSelectionModel.SelectionFlag.Rows)
        if scrolling:
            self.scrollTo(self.model().mapFromSource(self.Model.index(first, 0)),
                          hint=QAbstractItemView.ScrollHint.EnsureVisible)

    def plStatsLabText(self, tracks_num: int):
        tr = 'track' if tracks_num == 1 else 'tracks'
        return f'Total: {tracks_num} {tr}'
