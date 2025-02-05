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

from PySide6.QtCore import QObject
from PySide6.QtGui import QActionGroup


class LearnFreqOrderHandler(QObject):
    LearnFreqOrderActionGroup: QActionGroup
    BoostCutOrderActionGroup: QActionGroup

    def __init__(self, parent):
        super().__init__()
        self.mw_contr = parent
        self.mw_view = parent.mw_view
        self.setLearnFreqOrderAG()
        self.setBoostCutOrderAG()

    def setLearnFreqOrderAG(self):
        self.LearnFreqOrderActionGroup = QActionGroup(self)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionAscendingEQ)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionDescendingEQ)
        self.LearnFreqOrderActionGroup.addAction(self.mw_view.actionShuffleEQ)
        self.LearnFreqOrderActionGroup.triggered.connect(self.onLearnFreqOrderActionChanged)

    def setBoostCutOrderAG(self):
        self.BoostCutOrderActionGroup = QActionGroup(self)
        self.BoostCutOrderActionGroup.addAction(self.mw_view.actionEach_Band_Boosted_then_Cut)
        self.BoostCutOrderActionGroup.addAction(self.mw_view.actionAll_Bands_Boosted_then_All_Bands_Cut)
        self.BoostCutOrderActionGroup.triggered.connect(self.onBoostCutOrderActionChanged)

    def onLearnFreqOrderActionChanged(self):
        if self.mw_contr.ADGen is None:
            return
        self.mw_contr.ADGen.order = self.mw_contr.freqOrder()

    def onBoostCutOrderActionChanged(self):
        if self.mw_contr.ADGen is None:
            return
        self.mw_contr.ADGen.boost_cut_priority = self.mw_contr.boostCutPriority
