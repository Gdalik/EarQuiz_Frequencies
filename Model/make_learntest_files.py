#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from pathlib import Path
from pedalboard.io import AudioFile
from Model.audiodrill_gen import AudioDrillGen
from Utilities.exceptions import InterruptedException
from Utilities.freq2str import freqString
from Utilities.common_calcs import eq_off_perc
from Utilities.common_calcs import perc2sec
from Model.get_version import version
import Model.AudioEngine.audio_proc_settings as APS


tag = [f'\nGenerated with EarQuiz Frequencies v{version()} (c) 2023-2025, Gdaliy Garmiza.\nWebsite: https://earquiz.org']


def files_info(audiodata: str, EQPattern: str, boost_cut: str, gain_headroom: int or float,
               gain_depth: int or float, Q: float, proc_t_perc: int or float, slice_length: int or float):
    gain_bc = boost_cut if boost_cut != '+-' else '±'
    EQOffPerc = eq_off_perc(proc_t_perc)
    EQOnLength = perc2sec(slice_length, proc_t_perc)
    EQOffLength = perc2sec(slice_length, EQOffPerc)
    return [
        f'Audio source: {audiodata}\n', f'Pattern: {EQPattern}\n',
            f'Frequency gain: {gain_bc}{gain_depth}dB; Q: {Q}\n',
            f'Peak normalization: {gain_headroom}dB\n',
            f'EQ Off/EQ On/EQ Off: {EQOffPerc}%/{proc_t_perc}%/{EQOffPerc}% '
            f'({EQOffLength}s/{EQOnLength}s/{EQOffLength}s)\n',
    ]


def makeLearnFiles(audiosource: str, output_dir: str, freq_options: list[int], audiodata='', EQPattern='',
                   filename_prefix='', extension='.wav', bitrate=None, boost_cut='+-', DualBandMode=False,
                   starttime=0, endtime=None,
                   drill_length=15, order='asc', gain_depth=12, Q=4.32, disableAdjacent=1,
                   proc_t_perc=APS.getEQOnTimePerc(),
                   cropped=None, cropped_normalized=None, enumerate_examples=False, callback=None):
    def makeInfoFile():
        tf_name = 'Info.txt'
        info_filename = f'{prefix}__{tf_name}' if prefix else tf_name
        info_path = str(Path(output_dir, info_filename))
        info = files_info(audiodata, EQPattern, boost_cut, ADGen.gain_headroom, gain_depth, Q, proc_t_perc,
                          ADGen.audiochunk.slice_length)
        with open(info_path, 'w', encoding='utf-8', errors='replace') as tf:
            tf.writelines(info + tag)

    Path.mkdir(Path(output_dir), parents=True, exist_ok=True)
    ADGen = AudioDrillGen(freq_options, audio_source_path=audiosource, boost_cut=boost_cut, DualBandMode=DualBandMode,
                          starttime=starttime, endtime=endtime, drill_length=drill_length, gain_depth=gain_depth, Q=Q,
                          disableAdjacent=disableAdjacent, proc_t_perc=proc_t_perc, order=order, inf_cycle=False,
                          cropped=cropped, cropped_normalized=cropped_normalized,
                          callback=callback)
    count = 0
    filename = ''
    while True:
        try:
            freq, audio = ADGen.output()
            prefix = f'{filename_prefix}' if filename_prefix else ''
            ex_num = f'{count + 1}' if enumerate_examples else ''
            full_prefix = f"{'.'.join([el for el in [prefix, ex_num] if el])}__" if prefix or ex_num else ''
            filename = f'{full_prefix}{freqString(freq)}{extension}'
            filepath = str(Path(output_dir, filename))
            callback_out(callback, {'State': f'Exporting "{filename}"',
                          'Percent': int(count / len(ADGen.exercise_gen.full_sequence) * 100)})
        except StopIteration:
            break
        except InterruptedException:
            return
        with AudioFile(filepath, 'w', samplerate=ADGen.af_samplerate, num_channels=ADGen.af_num_channels,
                       quality=bitrate) as f:
            f.write(audio)
        count += 1
    callback_out(callback, {'State': f'Exporting "{filename}"', 'Percent': 100})
    makeInfoFile()


def makeTestFiles(audiosource: str, output_dir: str, freq_options: list[int], audiodata='', EQPattern='',
                  filename_prefix='', extension='.wav', bitrate=None, boost_cut='+-', DualBandMode=False,
                  starttime=0, endtime=None,
                  drill_length=15, gain_depth=12, Q=4.32, disableAdjacent=1, proc_t_perc=APS.getEQOnTimePerc(),
                  cropped=None, cropped_normalized=None, callback=None):

    def makeAnswersFile():
        answ_filename = f'{prefix}Answers.txt'
        answ_path = str(Path(output_dir, answ_filename))
        info = files_info(audiodata, EQPattern, boost_cut, ADGen.gain_headroom, gain_depth, Q, proc_t_perc,
                          ADGen.audiochunk.slice_length)
        nonlocal answers
        answers = info + answers + tag
        with open(answ_path, 'w', encoding='utf-8', errors='replace') as tf:
            tf.writelines(answers)

    Path.mkdir(Path(output_dir), parents=True, exist_ok=True)
    ADGen = AudioDrillGen(freq_options, audio_source_path=audiosource, boost_cut=boost_cut, DualBandMode=DualBandMode,
                          starttime=starttime, endtime=endtime, drill_length=drill_length, gain_depth=gain_depth, Q=Q,
                          disableAdjacent=disableAdjacent, proc_t_perc=proc_t_perc, order='random',
                          cropped=cropped, cropped_normalized=cropped_normalized,
                          callback=callback)
    filename = ''
    answers = ['\n']
    for i in range(10):
        try:
            freq, audio = ADGen.output()
            prefix = f'{filename_prefix}__' if filename_prefix else ''
            filename = f'{prefix}Example{i + 1}{extension}'
            filepath = str(Path(output_dir, filename))
            callback_out(callback, {'State': f'Exporting "{filename}"',
                          'Percent': int(i * 10)})
        except InterruptedException:
            makeAnswersFile()
            return
        with AudioFile(filepath, 'w', samplerate=ADGen.af_samplerate, num_channels=ADGen.af_num_channels,
                       quality=bitrate) as f:
            f.write(audio)
        answers.append(f'{i + 1}. {freqString(freq)}\n')
    callback_out(callback, {'State': f'Exporting "{filename}"', 'Percent': 100})
    makeAnswersFile()


def callback_out(callback, out_stat: dict):
    if callback is not None:
        callback(out_stat)
