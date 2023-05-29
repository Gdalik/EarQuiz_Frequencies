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

class PatternBoxView:
    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.Widget = mw_view.PatternBox
        self.NextButton = mw_view.NextPatternBut

    def loadItems(self, mode_names: list[str]):
        for ind, N in enumerate(mode_names):
            self.Widget.addItem(f'{ind + 1}. {N}')

    def setEnabled(self, arg: bool):
        self.Widget.setEnabled(arg)
        self.NextButton.setEnabled(arg)
