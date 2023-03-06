class ExScoreInfoView:
    ExNum_t = 'Exercise:'
    UserAnsw_t = 'Your answer:'
    CorAnsw_t = 'Correct answer:'
    AnswScore_t = 'Answer score:'
    TotalScore_t = 'Total score:'
    TestStatus_t = 'Test status:'

    def __init__(self, mw_view):
        self.mw_view = mw_view
        self.ExNum = mw_view.ExerciseNLab
        self.UserAnsw = mw_view.UserAnswerLab
        self.CorAnsw = mw_view.CorAnswerLab
        self.AnswScore = mw_view.AnswerScoreLab
        self.TotalScore = mw_view.TotalScoreLab
        self.TestStatus = mw_view.TestStatusLab
        self.init_texts()

    def init_texts(self):
        self.ExNum.setText(self.ExNum_t)
        self.UserAnsw.setText(self.UserAnsw_t)
        self.CorAnsw.setText(self.CorAnsw_t)
        self.AnswScore.setText(self.AnswScore_t)
        self.TotalScore.setText(self.TotalScore_t)
        self.TestStatus.setText(self.TestStatus_t)

    def showExNum(self, value):
        self.ExNum.setText(f'{self.ExNum_t} {value}')

    def showUserAnsw(self, value):
        self.UserAnsw.setText(f'{self.UserAnsw_t} {value}')

    def showCorAnsw(self, value):
        self.CorAnsw.setText(f'{self.CorAnsw_t} {value}')

    def showAnswScore(self, value: int or float or None):
        shown_value = f'{value}/10' if value is not None else ''
        self.AnswScore.setText(f'{self.AnswScore_t} {shown_value}')

    def showTotalScore(self, value: int or float):
        self.TotalScore.setText(f'{self.TotalScore_t} {value}/100')