#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QActionGroup
from GUI.Modes.LearnMode import LearnMode
from GUI.Modes.PreviewMode import PreviewMode
from GUI.Modes.TestMode import TestMode
from GUI.Modes.UniMode import UniMode
from GUI.Modes.audiosource_modes import PinkNoiseMode, AudioFileMode
from Utilities.exceptions import InterruptedException


class AppModesHandler(QObject):
    modesActionGroup: QActionGroup

    def __init__(self, parent):
        super().__init__()
        self.mw_view = parent.mw_view
        self.mw_contr = parent
        self.setModesActions()
        self.setModesButtons()
        self.setSourceButtons()

    def setModesButtons(self):
        self.mw_view.PreviewBut.setDefaultAction(self.mw_view.actionPreview_Mode)
        self.mw_view.LearnBut.setDefaultAction(self.mw_view.actionLearn_Mode)
        self.mw_view.TestBut.setDefaultAction(self.mw_view.actionTest_Mode)

    def setSourceButtons(self):
        self.mw_view.PinkNoiseRBut.toggled.connect(self.setAudioSourceMode)
        self.mw_view.AudiofileRBut.toggled.connect(self.setAudioSourceMode)

    def setAudioSourceMode(self, value):
        if not value:
            return
        if self.mw_view.PinkNoiseRBut.isChecked():
            self.mw_contr.CurrentSourceMode = PinkNoiseMode(self.mw_contr)
        elif self.mw_view.AudiofileRBut.isChecked():
            self.mw_contr.CurrentSourceMode = AudioFileMode(self.mw_contr)
        if self.mw_view.actionPreview_Mode.isChecked():
            self._setPreviewMode()
        else:
            self.mw_view.actionPreview_Mode.setChecked(True)

    def setModesActions(self):
        self.modesActionGroup = QActionGroup(self)
        self.modesActionGroup.setExclusive(True)
        self.modesActionGroup.addAction(self.mw_view.actionPreview_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionLearn_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionTest_Mode)
        self.modesActionGroup.addAction(self.mw_view.actionUni_Mode)
        self.mw_view.actionPreview_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionLearn_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionTest_Mode.toggled.connect(self.setCurrentMode)
        self.mw_view.actionUni_Mode.toggled.connect(self.setCurrentMode)
        self.modesActionGroup.triggered.connect(self.onmodesActionGroupTriggered)

    def onmodesActionGroupTriggered(self):
        if self.mw_view.ModeButtonGroup.checkedButton().text() == self.mw_contr.CurrentMode.name:
            return
        player = self.mw_contr.TransportContr.PlayerContr
        player.onStopTriggered(checkPlaybackState=True)

    def _setPreviewMode(self):
        self.mw_contr.CurrentMode = PreviewMode(self.mw_contr)

    def _setLearnMode(self):
        self.mw_contr.CurrentMode = LearnMode(self.mw_contr)

    def _setTestMode(self):
        self.mw_contr.CurrentMode = TestMode(self.mw_contr)

    def _setUniMode(self):
        self.mw_contr.CurrentMode = UniMode(self.mw_contr, contrEnabled=self.mw_contr.LastMode.name != 'Test')

    def setCurrentMode(self, value):
        if not value:
            return
        try:
            if self.modesActionGroup.checkedAction() == self.mw_view.actionPreview_Mode:
                self._setPreviewMode()
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionLearn_Mode:
                self._setLearnMode()
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionTest_Mode:
                self._setTestMode()
            elif self.modesActionGroup.checkedAction() == self.mw_view.actionUni_Mode:
                self._setUniMode()
        except InterruptedException:
            self.mw_view.actionPreview_Mode.setChecked(True)
        QTimer.singleShot(0, self.pushBackToPreview)
        self.mw_contr.LastMode = self.mw_contr.CurrentMode

    def pushBackToPreview(self, ignoreADGen=False):
        if not ignoreADGen and self.mw_contr.ADGen is not None:
            return
        if self.mw_contr.CurrentMode.name not in ('Preview', 'Uni'):
            self.mw_view.actionPreview_Mode.setChecked(True)
