import math


class ScoreCalculator:
    def __init__(self):
        self._ex_count = 0
        self.CurrentRightAnswer = None
        self.CurrentUserAnswer = None

    def input(self, RightAnswer: int or tuple, UserAnswer: int or tuple):
        if self._ex_count == 10:
            raise ValueError('The number of drills in a test cannot exceed 10.')
        self.CurrentRightAnswer = RightAnswer
        self.CurrentUserAnswer = UserAnswer

    def count(self):
        if isinstance(self.CurrentRightAnswer, int):
            return self._singleBand_count()
        if isinstance(self.CurrentRightAnswer, tuple):
            return self._dualBand_count()

    def _singleBand_count(self, max_score=10):
        A = self.CurrentRightAnswer
        U = self.CurrentUserAnswer
        error = math.log(max(abs(A), abs(U)) / min(abs(A), abs(U))) / math.log(2)
        rem_error = error - int(error)
        rem_error_w = min([0, 0.33, 0.66, 1], key=lambda x: abs(x - rem_error))
        error = int(error) + rem_error_w
        boost_cut_error = 2 if abs(A) / A != abs(U) / U else 0
        return max_score - error - boost_cut_error

    def _dualBand_count(self):
        score_list = []
        A = self.CurrentRightAnswer
        U = self.CurrentUserAnswer
        combinations = (((A[0], U[0]), (A[1], U[1])), ((A[0], U[1]), (A[1], U[0])))
        for comb in combinations:
            sc1 = ScoreCalculator()
            sc1.input(*comb[0])
            sc1_count = sc1._singleBand_count(max_score=5)
            sc2 = ScoreCalculator()
            sc2.input(*comb[1])
            sc2_count = sc2._singleBand_count(max_score=5)
            score_list.append(max(0, sc1_count) + max(0, sc2_count))
        return max(score_list)

    @property
    def ex_num(self):
        return f'{self._ex_count}/10'
