import pathlib
from definitions import ROOT_DIR
from Model.AudioEngine.load_audio import AudioChunk
from pedalboard.io import AudioFile
from Model.exercise_gen import ExerciseGenerator
from Model.AudioEngine.process import eq_proc


pinknoise_path = str(pathlib.PurePath(ROOT_DIR, 'Model', 'Data', 'pink_noise.wav'))
EQ1_freq = [31, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
EQ2_freq = [32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500,
            3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000]


class AudioDrillGen:
    def __init__(self, freq_options: list, boost_cut='+-', DualBandMode=False, audio_source=pinknoise_path,
                 starttime=0, endtime=None, drill_length=15,
                 gain_depth=12, Q=4.32, order='asc', boost_cut_priority=1, disableAdjacent=1, inf_cycle=True, proc_t_perc=40, callback=None):
        # order: 'asc', 'desc', 'shuffle', 'random'
        # boost_cut: '+', '-', '+-'
        # boost_cut_priority 1 (Each Band Boosted, then Cut) / 2 (All Bands Boosted, then All Bands Cut) -- ignored in random mode
        # disableAdjacent -- actual for DualBandMode
        # self.order, self.boost_cut_priority, self.Q, self.gain_depth are dynamically adjustable

        self.freq_options = freq_options
        self.boost_cut = boost_cut
        self.audio_source = AudioFile(audio_source)
        self._gain_depth = abs(gain_depth)
        headroom = -3 if DualBandMode else 0
        self.audiochunk = AudioChunk(self.audio_source,
                                     starttime=starttime,
                                     endtime=endtime or self.audio_source.frames / self.audio_source.samplerate,
                                     slice_length=drill_length, norm_level=self.gain_depth/-2 + headroom, callback=callback)
        self._Q = Q
        self._order = order
        self._boost_cut_priority = boost_cut_priority
        self.proc_t_perc = proc_t_perc
        self._exercise_gen = ExerciseGenerator(freq_options, boost_cut, DualBandMode, order,
                                               boost_cut_priority=boost_cut_priority, disableAdjacent=disableAdjacent, inf_cycle=inf_cycle)
        self._last_freq = None

    @property
    def gain_depth(self):
        return self._gain_depth

    @gain_depth.setter
    def gain_depth(self, value: int):
        old_value = self._gain_depth
        self._gain_depth = abs(value)
        if old_value != self._gain_depth:
            self.audiochunk.normalize(self._gain_depth*-1 - 1)

    @property
    def Q(self):
        return self._Q

    @Q.setter
    def Q(self, value: int or float):
        self._Q = value

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, arg: str):
        self._order = arg
        self._exercise_gen.order = arg
        self._on_EQ_order_change()

    @property
    def boost_cut_priority(self):
        return self._boost_cut_priority

    @boost_cut_priority.setter
    def boost_cut_priority(self, value: int):
        self._boost_cut_priority = value
        self._exercise_gen.boost_cut_priority = value
        self._on_EQ_order_change()

    def output(self, force_freq=None, audio_path=None):
        freq = self._freq_out(force_freq)
        audio = self._audio_out()
        if audio_path:
            with AudioFile(audio_path, 'w', self.audio_source.samplerate, self.audio_source.num_channels) as o:
                o.write(audio)
        return freq, audio

    def _freq_out(self, force_freq=None):
        self._last_freq = self._exercise_gen.seqOut(force_freq)
        return self._last_freq

    def _audio_out(self):
        if isinstance(self._last_freq, tuple):
            freq1, freq2 = self._last_freq
        else:
            freq1, freq2 = self._last_freq, None
        return eq_proc(self.audiochunk.slice_iter(), self.audiochunk.samplerate, freq1, freq2=freq2,
                       gain_depth=self.gain_depth, Q=self.Q, proc_t_perc=self.proc_t_perc)

    def _on_EQ_order_change(self):
        self._exercise_gen.inf_cycle = True
        self._exercise_gen.seqGen(self._last_freq)
        if self._last_freq is not None:
            self._exercise_gen.seqOut()
