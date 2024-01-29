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

class EQSetView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.GainRangeSpin = self.mw_view.GainRangeSpin
        self.BWBox = self.mw_view.BWBox
        self.ResetBut = self.mw_view.ResetEQBut
        self.LockEQSettingsBut = self.mw_view.LockEQSettingsBut
        self.mw_view.LockEQSettingsBut.setDefaultAction(self.mw_view.actionLockEQSettings)
        self.mw_view.GainRangeSpin.valueChanged.connect(self.mw_view.status.FreqGainLabel.update)

    def refreshBWQList(self, items: list[str]):
        self.BWBox.clear()
        for item in items:
            self.BWBox.addItem(item)

    def update(self, gain_depth: int, BW: str):
        self.update_gain_depth(gain_depth)
        self.update_BW(BW)

    def update_gain_depth(self, gain_depth: int):
        self.GainRangeSpin.blockSignals(True)
        self.GainRangeSpin.setValue(gain_depth)
        self.GainRangeSpin.blockSignals(False)
        self.mw_view.status.FreqGainLabel.update(gain_depth)

    def update_BW(self, BW: str):
        self.BWBox.blockSignals(True)
        self.BWBox.setCurrentText(BW)
        self.BWBox.blockSignals(False)

    def setEnabled(self, arg: bool):
        self.BWBox.setEnabled(arg)
        self.GainRangeSpin.setEnabled(arg)
        self.ResetBut.setEnabled(arg)
        self.LockEQSettingsBut.setEnabled(arg)
