import math
import random


def proc_unproc_len(total_chunk_len: int or float, proc_perc=40):
    proc_perc = max(proc_perc, 33)
    proc_len = total_chunk_len * proc_perc / 100
    return proc_len, (total_chunk_len - proc_len) / 2


def rand_buffer():
    return 32*math.pow(2, random.randint(4, 8))


def find_divider(x: int, min=10):
    div = min
    while x % div != 0:
        div += 1
    return div
