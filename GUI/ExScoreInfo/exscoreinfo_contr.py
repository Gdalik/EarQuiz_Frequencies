from Model.scorecalc import ScoreCalculator as SC
from Model.scorecalc import expected_results as ER
from Model.scorecalc import passed_failed as PF
from GUI.ExScoreInfo.exscoreinfo_view import ExScoreInfoView


class ExScoreInfoContr:
    def __init__(self, mw_contr):
        self.mw_contr = mw_contr
        self.view = ExScoreInfoView(mw_contr.mw_view)
        self.CurTest = SC()
        self.refresh()

    def refresh(self):
        self.view.init_texts()

    def nextEx(self):
        self.view.showExNum(self.CurTest.next_ex_num)
        self.view.showUserAnsw('')
        self.view.showCorAnsw('')
        self.view.showAnswScore(None)

    def showScore(self):
        if self.CurTest.ScoreList:
            self.view.showAnswScore(self.CurTest.ScoreList[-1][2])
            self.view.showTotalScore(self.CurTest.totalScore)

    def showTestStatus(self):
        pass