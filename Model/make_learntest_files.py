from pathlib import Path

from pedalboard.io import AudioFile

from Model.audiodrill_gen import AudioDrillGen
from Utilities.exceptions import InterruptedException
from Utilities.freq2str import freqString
from Model.get_version import version


def makeLearnFiles(audiosource: str, output_dir: str, freq_options: list[int], filename_prefix='', extension='.wav',
                   bitrate=None, boost_cut='+-', DualBandMode=False, starttime=0, endtime=None, drill_length=15,
                   order='asc', gain_depth=12, Q=4.32, disableAdjacent=1, proc_t_perc=40,
                   cropped=None, cropped_normalized=None, enumerate_examples=False, callback=None):
    def callback_out(out_stat: dict):
        if callback is not None:
            callback(out_stat)

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
            callback_out({'State': f'Exporting "{filename}"',
                          'Percent': int(count / len(ADGen.exercise_gen.full_sequence) * 100)})
        except StopIteration:
            break
        except InterruptedException:
            return
        with AudioFile(filepath, 'w', samplerate=ADGen.af_samplerate, num_channels=ADGen.af_num_channels,
                       quality=bitrate) as f:
            f.write(audio)
        count += 1
    callback_out({'State': f'Exporting "{filename}"', 'Percent': 100})


def makeTestFiles(audiosource: str, output_dir: str, freq_options: list[int], audiodata='', filename_prefix='',
                  extension='.wav', bitrate=None, boost_cut='+-', DualBandMode=False, starttime=0, endtime=None,
                  drill_length=15, gain_depth=12, Q=4.32, disableAdjacent=1, proc_t_perc=40,
                  cropped=None, cropped_normalized=None, callback=None):
    def callback_out(out_stat: dict):
        if callback is not None:
            callback(out_stat)

    def makeAnswersFile():
        answ_filename = f'{prefix}Answers.txt'
        answ_path = str(Path(output_dir, answ_filename))
        info = []
        info.append(f'Audio source: {audiodata}\n')
        gain_bc = boost_cut if boost_cut != '+-' else '±'
        info.append(f'Frequency gain: {gain_bc}{gain_depth}dB; Q: {Q}\n')
        info.append(f'Peak normalization: {ADGen.gain_headroom}dB\n\n')
        nonlocal answers
        tag = [f'\nGenerated with EarQuiz Frequencies v{version()} (c) 2023, Gdaliy Garmiza.\nWebsite: www.earquiz.org']
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
    answers = []
    for i in range(10):
        try:
            freq, audio = ADGen.output()
            prefix = f'{filename_prefix}__' if filename_prefix else ''
            filename = f'{prefix}Example{i + 1}{extension}'
            filepath = str(Path(output_dir, filename))
            callback_out({'State': f'Exporting "{filename}"',
                          'Percent': int(i * 10)})
        except InterruptedException:
            makeAnswersFile()
            return
        with AudioFile(filepath, 'w', samplerate=ADGen.af_samplerate, num_channels=ADGen.af_num_channels,
                       quality=bitrate) as f:
            f.write(audio)
        answers.append(f'{i + 1}. {freqString(freq)}\n')
    callback_out({'State': f'Exporting "{filename}"', 'Percent': 100})
    makeAnswersFile()
