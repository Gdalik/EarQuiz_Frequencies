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

from GUI.ExScoreInfo.exscoreinfo_view import ExScoreInfoView
from Model.scorecalc import ScoreCalculator as SC
from Model.scorecalc import expected_results as ER
from Model.scorecalc import passed_failed as PF


class ExScoreInfoContr:
    CurTest: SC

    def __init__(self, mw_contr):
        self.mw_contr = mw_contr
        self.view = ExScoreInfoView(mw_contr.mw_view)
        self.refresh()

    @property
    def test_status(self):
        if 0 <= len(self.CurTest.ScoreList) < 10:
            if self.mw_contr.CurrentMode.name == 'Test':
                return 'in progress'
            elif len(self.CurTest.ScoreList) > 0:
                return 'canceled'
        return self._detectPassedFailed() if len(self.CurTest.ScoreList) == 10 else ''

    def _detectPassedFailed(self):
        if len(self.CurTest.ScoreList) < 10:
            return ''
        eq_pattern = self.mw_contr.EQContr.EQpattern
        eq_type = 1 if eq_pattern['EQtype'] == 'EQ1' else 2
        er = ER(eq_type, eq_pattern['DualBandMode'])
        return PF(self.CurTest.totalScore, er)

    def refresh(self, onlyLastExcInfo=False):
        self.CurTest = SC()
        self.view.init_texts(onlyLastExcInfo=onlyLastExcInfo)

    def nextEx(self):
        self.view.showExNum(self.CurTest.next_ex_num)
        self.view.showUserAnsw('')
        self.view.showCorAnsw('')
        self.view.showAnswScore(None)

    def onAnswerAccepted(self, RightAnswer: int or tuple, UserAnswer: int or tuple):
        self.CurTest.input(RightAnswer, UserAnswer)
        self.showScore()
        self.view.showCorAnsw(RightAnswer)
        self.view.showUserAnsw(UserAnswer)

    def showScore(self):
        if self.CurTest.ScoreList:
            self.view.showAnswScore(self.CurTest.ScoreList[-1][2])
            self.view.showTotalScore(self.CurTest.totalScore, underlined=len(self.CurTest.ScoreList) == 10)

    def showTestStatus(self, reset_mark=True):
        if not reset_mark and self.markInStr(self.view.TestStatus.text()):
            return
        self.view.showStatus(self.test_status)

    @staticmethod
    def markInStr(value: str):
        return 'passed' in value or 'failed' in value
