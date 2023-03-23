import copy
import random
import itertools
from Utilities.common_calcs import findAdjacentEl as findAdj


class ExampleGenerator:
    def __init__(self, freq_options: list[int], boost_cut: str, DualBandMode: bool, order: str, boost_cut_priority=1,
                 disableAdjacent=1, inf_cycle=True):
        # order: 'asc', 'desc', 'shuffle', 'random'
        # boost_cut_priority 1 (Each Band Boosted, then Cut) / 2 (All Bands Boosted, then All Bands Cut)
        self.freq_options = freq_options
        self.boost_cut = boost_cut
        self.DualBandMode = DualBandMode
        self.order = order
        self.boost_cut_priority = boost_cut_priority
        self.disableAdjacent = disableAdjacent
        self._source_sequence = []
        self.full_sequence = []
        self._lastRandomChoice = None
        self.cycle = None
        self.inf_cycle = inf_cycle if order != 'random' else True
        self._isLastItemInSeq = None

    @property
    def isLastItemInSeq(self):
        return self._isLastItemInSeq

    def seqGen(self, start_freq=None):
        self.cycle = None
        return self._dualBandSeqGen(start_freq) if self.DualBandMode else self._singleBandSeqGen(start_freq)

    def seqOut(self, start_freq=None):
        first_run = False
        if self.order == 'random':
            return self.randOut()
        if not self.full_sequence or start_freq is not None:
            self.seqGen(start_freq)
        if not self.cycle:
            self.cycle = itertools.cycle(self.full_sequence)
            first_run = True
        output = next(self.cycle)
        self._isLastItemInSeq = (output == self.full_sequence[-1])
        if not self.inf_cycle and output == self.full_sequence[0] and not first_run:
            raise StopIteration
        return output

    def randOut(self):
        if not self.full_sequence:
            self.seqGen()
        return self._getRand(self.full_sequence)

    def _singleBandSeqGen(self, start_freq=None):
        self._genSourceSequence()
        start_freq = self._source_sequence[0] if start_freq is None else start_freq
        source_seq = self._source_seq_reorder(abs(start_freq))
        if self.boost_cut == '-':
            source_seq = [x * -1 for x in source_seq]
        elif self.boost_cut == '+-':
            startfrom = '+' if start_freq > 0 else '-'
            source_seq = self._make_single_boostcut_seq(source_seq, startfrom=startfrom)
        self.full_sequence = source_seq
        return self.full_sequence

    def _dualBandSeqGen(self, start_freq=None):
        def abs_source(t: tuple, n: int):
            L = [abs(x) for x in t]
            return t[L.index(abs(n))]

        def crop_tuple(x):
            if not isinstance(x, tuple):
                return x
            return abs_source(x, max(abs(x[0]), abs(x[1]))) if self.order == 'desc' \
                else abs_source(x, min(abs(x[0]), abs(x[1])))
        self._genSourceSequence()
        _start_freq = self._source_sequence[0] if start_freq is None else start_freq
        source_seq = self._source_seq_reorder(abs(crop_tuple(_start_freq)))
        source_seq = list(itertools.combinations(source_seq, 2))
        if self.order == 'shuffle':
            rand = random.Random()
            rand.shuffle(source_seq)
        if self.disableAdjacent:
            source_seq = list(filter(self._filterAdjacent, source_seq))
        if self.boost_cut == '-':
            source_seq = list(map(lambda x: (x[0]*-1, x[1]*-1), source_seq))
        elif self.boost_cut == '+-':
            startfrom = '+' if crop_tuple(_start_freq) > 0 else '-'
            source_seq = self._make_dual_boostcut_seq(source_seq, startfrom=startfrom)
        self.full_sequence = source_seq

        if isinstance(_start_freq, int) and start_freq is not None and self.order == 'shuffle':
            for f in self.full_sequence:
                if _start_freq in f:
                    self.full_sequence.remove(f)
                    self.full_sequence.insert(0, f)
                    break
        elif isinstance(_start_freq, tuple):
            try:
                self.full_sequence.remove(_start_freq)
            except ValueError:
                self.full_sequence.remove((_start_freq[1], _start_freq[0]))
            self.full_sequence.insert(0, _start_freq)
        return source_seq

    def _make_single_boostcut_seq(self, source_seq: list[int], startfrom='+'):
        k = -1 if startfrom == '-' else 1
        if self.boost_cut_priority == 1:
            bc_cycle = itertools.cycle([k, k * -1])
            source_seq = list(itertools.chain.from_iterable([[x, x] for x in source_seq]))
            source_seq = [el * next(bc_cycle) for el in source_seq]
        elif self.boost_cut_priority == 2:
            source_seq = [x * k for x in source_seq] + [x * k * -1 for x in source_seq]
        return source_seq

    def _make_dual_boostcut_seq(self, source_seq: list[int], startfrom='+'):
        def applyPattern(el: tuple, pattern: tuple):
            return el[0] * pattern[0], el[1] * pattern[1]
        k = -1 if startfrom == '-' else 1
        bc_patterns = list(itertools.product([1 * k, -1 * k], repeat=2))
        if self.boost_cut_priority == 1:
            bc_patterns_cycle = itertools.cycle(bc_patterns)
            source_seq = list(itertools.chain.from_iterable([itertools.repeat(x, 4) for x in source_seq]))
            source_seq = [applyPattern(el, next(bc_patterns_cycle)) for el in source_seq]
        elif self.boost_cut_priority == 2:
            res_seq = []
            for i in range(4):
                res_seq += [applyPattern(el, bc_patterns[i]) for el in source_seq]
            source_seq = res_seq
        return source_seq

    def _genAscSeq(self):
        self._source_sequence = copy.copy(self.freq_options)
        self._source_sequence.sort()
        return self._source_sequence

    def _genSourceSequence(self):
        if self.order == 'desc':
            self._genDescSeq()
        elif self.order == 'shuffle':
            self._genRandNoRepeatSeq()
        else:
            self._genAscSeq()

    def _genDescSeq(self):
        self._source_sequence = copy.copy(self.freq_options)
        self._source_sequence.reverse()
        return self._source_sequence

    def _genRandNoRepeatSeq(self):
        self._source_sequence = random.sample(self.freq_options, k=len(self.freq_options))
        return self._source_sequence

    def _getRand(self, options=None):
        options = self.freq_options if options is None else options
        rand = random.Random()
        res = rand.choice(options)
        while res == self._lastRandomChoice:
            res = rand.choice(options)
        self._lastRandomChoice = res
        return res

    def _source_seq_reorder(self, start_freq: int):
        start_ind = self._source_sequence.index(abs(start_freq))
        return self._source_sequence[start_ind:] + self._source_sequence[:start_ind]

    def _filterAdjacent(self, frequencies: tuple):
        freq_list = sorted(self.freq_options)
        return frequencies[1] not in findAdj(freq_list, frequencies[0], num=self.disableAdjacent)
