from PyQt6.QtWidgets import QStatusBar, QLabel, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt


class StatusBar(QStatusBar):
    def __init__(self, mw_view):
        super().__init__()
        self.mw_view = mw_view
        self.mw_view.setStatusBar(self)
        self.NormLabel = NormalizationLabel(self)
        self.statusLayout = QHBoxLayout()
        self.statusLayout.addWidget(self.NormLabel)
        self.statusLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.statusLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget()
        self.container.setMinimumHeight(20)
        self.container.setLayout(self.statusLayout)
        self.addPermanentWidget(self.container)
        self.setFixedHeight(28)

    def showNormalization(self, value: int or float):
        self.NormLabel.update(value)
        self.NormLabel.show()

    def clearNormalization(self):
        self.NormLabel.hide()


class NormalizationLabel(QLabel):
    def __init__(self, parent, value=0):
        super().__init__()
        self.value = value
        self.parent = parent
        self.update()

    def update(self, value=None):
        self.value = value or self.value
        self.setText(f'Peak Normalization: {self.value}dB')
