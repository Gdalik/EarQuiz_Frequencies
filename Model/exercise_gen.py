import copy
import random
import itertools


class ExerciseGenerator:
    def __init__(self, freq_options: list, boost_cut: str, dualBandMode: bool, order: str, boost_cut_priority=1,
                 disableAdjacent=1):
        # order: 'asc', 'desc', 'rand-no-repeat', 'rand'
        # boost_cut_priority 1 (Each Band Boosted, then Cut) / 2 (All Bands Boosted, then All Bands Cut)
        self.freq_options = freq_options
        self.boost_cut = boost_cut
        self.dualBandMode = dualBandMode
        self.order = order
        self.boost_cut_priority = boost_cut_priority
        self.disableAdjacent = disableAdjacent
        self._source_sequence = []
        self.full_sequence = []
        self._lastRandomChoice = None
        self.cycle = None

    def seqGen(self, start_freq=None):
        self.cycle = None
        if not self.dualBandMode:
            return self._singleBandSeqGen(start_freq)

    def seqOut(self, start_freq=None):
        if not self.full_sequence or start_freq is not None:
            self.seqGen(start_freq)
        if not self.cycle:
            self.cycle = itertools.cycle(self.full_sequence)
        return next(self.cycle)

    def randOut(self):
        if not self.full_sequence:
            self.seqGen()
        return self._getRand(self.full_sequence)

    def _singleBandSeqGen(self, start_freq=None):
        if self.order == 'asc':
            self._genAscSeq()
        elif self.order == 'desc':
            self._genDescSeq()
        elif self.order == 'rand-no-repeat':
            self._genRandNoRepeatSeq()
        start_freq = self._source_sequence[0] if start_freq is None else start_freq
        source_seq = self._source_seq_reorder(abs(start_freq))
        if self.boost_cut == '-':
            source_seq = [x * -1 for x in source_seq]
        elif self.boost_cut == '+-':
            startfrom = '+' if start_freq > 0 else '-'
            source_seq = self._make_single_boostcut_seq(source_seq, startfrom=startfrom)
        self.full_sequence = source_seq
        return self.full_sequence

    def _make_single_boostcut_seq(self, source_seq: list, startfrom='+'):
        k = -1 if startfrom == '-' else 1
        if self.boost_cut_priority == 1:
            source_seq = list(itertools.chain.from_iterable([[x, x] for x in source_seq]))
            source_seq = [el * next(itertools.cycle([k, k * -1])) for el in source_seq]
        elif self.boost_cut_priority == 2:
            source_seq = [x * k for x in source_seq] + [x * k * -1 for x in source_seq]
        return source_seq

    def _genAscSeq(self):
        self._source_sequence = copy.copy(self.freq_options)
        self._source_sequence.sort()
        return self._source_sequence

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
