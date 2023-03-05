import math


def expected_results(eq_mode: int, DualBand: bool):     # eq_mode 1 -- 1-octave; eq_mode 2 -- 1/3-octave EQ
    exp_res = (40, 40)
    if eq_mode == 1 and not DualBand:
        exp_res = (85, 95)
    elif eq_mode == 2 and not DualBand:
        exp_res = (75, 90)
    elif eq_mode == 1 and DualBand:
        exp_res = (70, 85)
    elif eq_mode == 2 and DualBand:
        exp_res = (65, 80)
    return exp_res


def passed_failed(user_score: int or float, exp_res: tuple, fail_line=5):
    if user_score < exp_res[0] - fail_line:
        return 'failed'
    elif exp_res[0] - fail_line <= user_score <= exp_res[1]:
        return 'passed'
    else:
        return 'passed+'


class ScoreCalculator:
    def __init__(self):
        self.CurrentRightAnswer = None
        self.CurrentUserAnswer = None
        self.ScoreList = []

    def input(self, RightAnswer: int or tuple, UserAnswer: int or tuple):
        if len(self.ScoreList) == 10:
            raise ValueError('The number of drills in a test cannot exceed 10.')
        self.CurrentRightAnswer = RightAnswer
        self.CurrentUserAnswer = UserAnswer
        self.ScoreList.append((self.CurrentRightAnswer, self.CurrentUserAnswer, self.count()))

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
    def next_ex_num(self):
        count = len(self.ScoreList)
        return f'{count + 1}/10' if count < 10 else ''

    @property
    def totalScore(self):
        return math.ceil(sum(x[2] for x in self.ScoreList))
