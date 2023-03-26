from Model.AudioEngine.load_audio import AudioChunk
from pedalboard.io import AudioFile
from Model.exercise_gen import ExampleGenerator
from Model.AudioEngine.process import eq_proc
from Utilities.exceptions import InterruptedException
from tempfile import NamedTemporaryFile
from definitions import TEMP_AUDIO_DIR
from pathlib import Path

EQ1_freq = [31, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
EQ2_freq = [32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500,
            3150, 4000, 5000, 6300, 8000, 10000, 12500, 16000]


def create_temp_wavefile():
    Path(TEMP_AUDIO_DIR).mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode="w+b", suffix='.wav', delete=False, dir=TEMP_AUDIO_DIR) as f:
        return f.name


class AudioDrillGen:
    def __init__(self, freq_options: list[int], boost_cut='+-', DualBandMode=False, audio_source_path='pinknoise',
                 starttime=0, endtime=None, drill_length=15,
                 gain_depth=12, Q=4.32, order='asc', boost_cut_priority=1, disableAdjacent=1, inf_cycle=True,
                 proc_t_perc=40, callback=None):
        # order: 'asc', 'desc', 'shuffle', 'random'
        # boost_cut: '+', '-', '+-'
        # boost_cut_priority 1 (Each Band Boosted, then Cut) / 2 (All Bands Boosted, then All Bands Cut) -- ignored in random mode
        # disableAdjacent -- actual for DualBandMode
        # self.order, self.boost_cut_priority, self.Q, self.proc_t_perc are dynamically adjustable
        # with another EQ_Pattern on the same audio source use self.resetExGen

        if audio_source_path == 'pinknoise':
            self.af_duration = 30
            self.af_samplerate = 44100
            self.af_num_channels = 1
        else:
            with AudioFile(audio_source_path) as af:
                self.af_duration = af.duration
                self.af_samplerate = af.samplerate
                self.af_num_channels = af.num_channels
        self._gain_depth = abs(gain_depth)
        self._DualBandMode = DualBandMode
        self.audiochunk = AudioChunk(audio_source_path,
                                     starttime=starttime,
                                     endtime=endtime or self.af_duration,
                                     slice_length=drill_length, norm_level=self.gain_headroom, callback=callback)
        if self.audiochunk.user_stopped:
            raise InterruptedException
        self._Q = Q
        self._order = order
        self._boost_cut_priority = boost_cut_priority
        self.proc_t_perc = proc_t_perc
        self.exercise_gen = ExampleGenerator(freq_options, boost_cut, DualBandMode, order,
                                             boost_cut_priority=boost_cut_priority, disableAdjacent=disableAdjacent,
                                             inf_cycle=inf_cycle)
        self._last_freq = None

    def gain_depth(self):
        return self._gain_depth

    def setGain_depth(self, value: int, normalize_audio=True, callback=None):
        if value == self._gain_depth and \
                self.audiochunk.last_norm_level == self.gain_headroom_calc(value, self._DualBandMode):
            return
        self._gain_depth = abs(value)
        self.audiochunk.norm_level = self.gain_headroom
        if normalize_audio:
            self.audiochunk.normalize(callback=callback)

    @property
    def Q(self):
        return self._Q

    @Q.setter
    def Q(self, value: int or float):
        self._Q = value

    @property
    def order(self):
        return self._order

    @property
    def gain_headroom(self):
        return self.gain_headroom_calc(self.gain_depth(), self._DualBandMode)

    @staticmethod
    def gain_headroom_calc(gain_depth: int, DualBandMode: bool):
        headroom = -3 if DualBandMode else 0
        if gain_depth < abs(headroom):
            headroom = gain_depth * -1
        k = -1
        return gain_depth / k + headroom

    @order.setter
    def order(self, arg: str):
        self._order = arg
        self.exercise_gen.order = arg
        self._on_EQ_order_change()

    @property
    def boost_cut_priority(self):
        return self._boost_cut_priority

    @boost_cut_priority.setter
    def boost_cut_priority(self, value: int):
        self._boost_cut_priority = value
        self.exercise_gen.boost_cut_priority = value
        self._on_EQ_order_change()

    def output(self, force_freq=None, fromStart=False, audio_path=None):
        freq = self._freq_out(force_freq=force_freq)
        audio = self._audio_out(fromStart=fromStart)
        if audio_path:
            with AudioFile(audio_path, 'w', self.af_samplerate, self.af_num_channels) as o:
                o.write(audio)
        return freq, audio

    def refresh_audio(self, filepath=None):
        if self._last_freq is None:
            return
        audio = self._audio_out(renderCurrent=True, fromStart=False)
        if filepath is None:
            return audio
        with AudioFile(filepath, 'w', self.af_samplerate, self.af_num_channels) as o:
            o.write(audio)
        return filepath

    def _freq_out(self, force_freq=None):
        self._last_freq = self.exercise_gen.seqOut(force_freq)
        return self._last_freq

    def _audio_out(self, renderCurrent=False, fromStart=False):
        if isinstance(self._last_freq, tuple):
            freq1, freq2 = self._last_freq
        else:
            freq1, freq2 = self._last_freq, None
        source = self.audiochunk.slice_iter(refresh=fromStart) \
            if not renderCurrent or self.audiochunk.current_slice is None else self.audiochunk.current_slice
        return eq_proc(source, self.audiochunk.samplerate, freq1, freq2=freq2,
                       gain_depth=self.gain_depth(), Q=self.Q, proc_t_perc=self.proc_t_perc)

    def _on_EQ_order_change(self):
        self.exercise_gen.inf_cycle = True
        self.exercise_gen.seqGen(self._last_freq)
        if self._last_freq is not None:
            self.exercise_gen.seqOut()

    def resetExGen(self, freq_options, boost_cut='+-', DualBandMode=False, order='asc',
                                               boost_cut_priority=1, disableAdjacent=1, inf_cycle=True):
        self.exercise_gen = ExampleGenerator(freq_options=freq_options, boost_cut=boost_cut,
                                             DualBandMode=DualBandMode, order=order,
                                             boost_cut_priority=boost_cut_priority, disableAdjacent=disableAdjacent,
                                             inf_cycle=inf_cycle)
        self._DualBandMode = DualBandMode
