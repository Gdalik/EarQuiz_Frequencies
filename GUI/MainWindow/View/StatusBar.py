from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QStatusBar, QLabel, QHBoxLayout, QWidget, QFrame


class StatusBar(QStatusBar):
    def __init__(self, mw_view):
        super().__init__()
        self.mw_view = mw_view
        self.mw_view.setStatusBar(self)
        self.setFixedHeight(28)
        self._setLayout()
        self._setContainer()
        self._setTempLabel()
        self._setEQStateLabel()
        self._setFreqGainLabel()
        self._setNormalizationLabel()

    def _setLayout(self):
        self.statusLayout = QHBoxLayout()
        self.statusLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.statusLayout.setContentsMargins(0, 0, 0, 0)

    def _setContainer(self):
        self.container = QWidget()
        self.container.setMinimumHeight(20)
        self.container.setLayout(self.statusLayout)
        self.addPermanentWidget(self.container)

    def _setNormalizationLabel(self):
        self.NormLabel = NormalizationLabel(self)
        self.statusLayout.addWidget(self.NormLabel)

    def _setEQStateLabel(self):
        self.EQStateLabel = EQStateLabel(self)
        self.statusLayout.addWidget(self.EQStateLabel)

    def _setFreqGainLabel(self):
        self.FreqGainLabel = FreqGainLabel(self)
        self.statusLayout.addWidget(self.FreqGainLabel)

    def _setTempLabel(self):
        self.TempLabel = TempLabel(self)
        self.statusLayout.addWidget(self.TempLabel)

    def showNormalization(self, value: int or float):
        self.NormLabel.update(value)
        self.NormLabel.show()

    def clearNormalization(self):
        self.NormLabel.hide()


class NormalizationLabel(QLabel):
    def __init__(self, parent, value=0):
        super().__init__()
        self.hide()
        self.value = value
        self.parent = parent
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.update()

    def update(self, value=None):
        self.value = value or self.value
        self.setText(f'Peak Normalization: {self.value}dB')


class EQStateLabel(QLabel):
    def __init__(self, parent, isOn=False):
        super().__init__()
        self.hide()
        self.parent = parent
        self.isOn = isOn
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFixedWidth(50)
        self.update()

    def update(self, isOn=False):
        self.isOn = isOn
        self._updView()

    def _updView(self):
        _text = 'EQ On' if self.isOn else 'EQ Off'
        ss = 'color: green; font-weight: bold' if self.isOn else 'color: gray; font-weight: bold'
        self.setText(_text)
        self.setStyleSheet(ss)


class FreqGainLabel(QLabel):
    def __init__(self, parent, value=0):
        super().__init__()
        self.value = value
        self.parent = parent
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.update()

    def update(self, value=0):
        self.value = value or self.value
        self.setText(f'Freq. Gain: ±{self.value}dB')


class TempLabel(QLabel):
    def __init__(self, parent, shown_text='', time=5000):
        super().__init__()
        self.parent = parent
        self.setStyleSheet('color: blue;')
        self.shown_text = shown_text
        self.time = time
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def update(self, shown_text='', time=5000):
        self.shown_text = shown_text or self.shown_text
        self.time = time or self.time
        self.setText(self.shown_text)
        QTimer.singleShot(self.time, self.clear)
