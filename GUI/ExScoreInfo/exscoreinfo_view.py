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

from Utilities.freq2str import freqString
from GUI.MainWindow.View.dark_theme import green_color
from GUI.Misc.colorStr import colorStr


class ExScoreInfoView:
    ExNum_t = 'Example:'
    UserAnsw_t = 'Your answer:'
    CorAnsw_t = 'Right answer:'
    AnswScore_t = 'Answer score:'
    TotalScore_t = 'Total score:'
    TestStatus_t = 'Test status:'

    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.ExNum = mw_view.ExampleNLab
        self.UserAnsw = mw_view.UserAnswerLab
        self.CorAnsw = mw_view.CorAnswerLab
        self.AnswScore = mw_view.AnswerScoreLab
        self.TotalScore = mw_view.TotalScoreLab
        self.TestStatus = mw_view.TestStatusLab
        self.init_texts()

    def init_texts(self, onlyLastExcInfo=False):
        self.ExNum.setText(self.ExNum_t)
        self.UserAnsw.setText(self.UserAnsw_t)
        self.CorAnsw.setText(self.CorAnsw_t)
        self.AnswScore.setText(self.AnswScore_t)
        if onlyLastExcInfo:
            return
        self.TotalScore.setText(self.TotalScore_t)
        self.TestStatus.setText(self.TestStatus_t)

    def showExNum(self, value):
        self.ExNum.setText(f'{self.ExNum_t} <b>{value}</b>/10') if value else ''

    def showUserAnsw(self, value):
        self.UserAnsw.setText(f'{self.UserAnsw_t} {freqString(value)}')

    def showCorAnsw(self, value):
        self.CorAnsw.setText(f'{self.CorAnsw_t} {freqString(value)}')

    def showAnswScore(self, value: int or float or None):
        shown_value = f'<b>{value}</b>/10' if value is not None else ''
        self.AnswScore.setText(f'{self.AnswScore_t} {shown_value}')

    def showTotalScore(self, value: int or float, underlined=False):
        text = f'{self.TotalScore_t} <b>{value}</b>/100'
        text = f'<u>{text}</u>' if underlined else text
        self.TotalScore.setText(text)

    def showStatus(self, status: str):
        if 'passed' in status or 'progress' in status:
            status = colorStr(status, green_color())
        elif 'failed' in status or 'canceled' in status:
            status = colorStr(status, 'red')
        self.TestStatus.setText(f'{self.TestStatus_t} {status}')
