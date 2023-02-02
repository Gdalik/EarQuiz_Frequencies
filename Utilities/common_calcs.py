import math
from fractions import Fraction


def findAdjacentEl(L: list, element, num=1):  # num: the maximum number of adjacent elements from each side of given element
    element_ind = L.index(element)
    min_ind = max(0, element_ind - num)
    max_ind = min(len(L) - 1, element_ind + num)
    return [L[i] for i in range(min_ind, max_ind + 1) if L[i] != element]


def Qcalc(BW_Noct: float or int or str):
    N = float(Fraction(BW_Noct)) if isinstance(BW_Noct, str) else BW_Noct
    return round(math.sqrt(2**N) / (2**N - 1), 2)


def mmss(s, string=False):
    m, s = divmod(s, 60)
    return ['%02d' % m, '%02d' % s] if string else [m, s]
