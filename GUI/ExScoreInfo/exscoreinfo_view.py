class ExScoreInfoView:
    ExNum_t = 'Exercise:'
    UserAnsw_t = 'Your answer:'
    CorAnsw_t = 'Correct answer:'
    AnswScore_t = 'Answer score:'
    TotalScore_t = 'Total score:'
    TestStatus_t = 'Test status:'

    def __init__(self, parent):
        self.parent = parent
        self.ExNum = self.parent.ExerciseNLab
        self.UserAnsw = self.parent.UserAnswerLab
        self.CorAnsw = self.parent.CorAnswerLab
        self.AnswScore = self.parent.AnswerScoreLab
        self.TotalScore = self.parent.TotalScoreLab
        self.TestStatus = self.parent.TestStatusLab
        self.init_texts()

    def init_texts(self):
        self.ExNum.setText(self.ExNum_t)
        self.UserAnsw.setText(self.UserAnsw_t)
        self.CorAnsw.setText(self.CorAnsw_t)
        self.AnswScore.setText(self.AnswScore_t)
        self.TotalScore.setText(self.TotalScore_t)
        self.TestStatus.setText(self.TestStatus_t)