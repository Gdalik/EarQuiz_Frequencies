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

import math
import random


def proc_unproc_len(total_chunk_len: int or float, proc_perc=40):
    proc_perc = max(proc_perc, 33)
    proc_len = total_chunk_len * proc_perc / 100
    return proc_len, (total_chunk_len - proc_len) / 2


def rand_buffer():
    return 32 * math.pow(2, random.randint(4, 8))


def find_divider(x: int, Min=2):
    div = Min
    while x % div != 0:
        div += 1
    return div


def optimal_range_length(total_length: int or float, slice_length: int or float, num_slices=10):
    return min(total_length // slice_length, num_slices) * slice_length


def abs_tuple(value: tuple):
    return tuple(abs(f) for f in value)
