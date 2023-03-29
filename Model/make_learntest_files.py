from Model.audiodrill_gen import AudioDrillGen
from pathlib import Path
from Utilities.freq2str import freqString
from pedalboard.io import AudioFile
from Utilities.exceptions import InterruptedException


def makeLearnFiles(audiosource: str, output_dir: str, freq_options: list[int], filename_prefix='', format='.wav',
                   bitrate=None, boost_cut='+-', DualBandMode=False, starttime=0, endtime=None, drill_length=15,
                   gain_depth=12, Q=4.32, disableAdjacent=1, proc_t_perc=40, cropped=None, callback=None):
    def callback_out(out_stat: dict):
        if callback is not None:
            callback(out_stat)
    Path.mkdir(Path(output_dir), parents=True, exist_ok=True)
    ADGen = AudioDrillGen(freq_options, audio_source_path=audiosource, boost_cut=boost_cut, DualBandMode=DualBandMode,
                          starttime=starttime, endtime=endtime, drill_length=drill_length, gain_depth=gain_depth, Q=Q,
                          disableAdjacent=disableAdjacent, proc_t_perc=proc_t_perc, order='asc', inf_cycle=False, cropped=cropped,
                          callback=callback)
    count = 0
    filename = ''
    while True:
        try:
            freq, audio = ADGen.output()
            prefix = f'{filename_prefix}__' if filename_prefix else ''
            filename = f'{prefix}{freqString(freq)}{format}'
            filepath = str(Path(output_dir, filename))
            callback_out({'State': f'Exporting "{filename}"', 'Percent': int(count / len(ADGen.exercise_gen.full_sequence) * 100)})
        except StopIteration:
            break
        except InterruptedException:
            return
        with AudioFile(filepath, 'w', samplerate=ADGen.af_samplerate, num_channels=ADGen.af_num_channels,
                       quality=bitrate) as f:
            f.write(audio)
        count += 1
    callback_out({'State': f'Exporting "{filename}"', 'Percent': 100})


def makeTestFiles(audiosource: str, output_dir: str, freq_options: list[int], filename_prefix='', format='.wav',
                   bitrate=None, boost_cut='+-', DualBandMode=False, starttime=0, endtime=None, drill_length=15,
                   gain_depth=12, Q=4.32, disableAdjacent=1, proc_t_perc=40, cropped=None, callback=None):
    def callback_out(out_stat: dict):
        if callback is not None:
            callback(out_stat)
    def makeAnswersFile():
        answ_filename = f'{prefix}Answers.txt'
        answ_path = str(Path(output_dir, answ_filename))
        source = 'Pink noise' if audiosource == 'pinknoise' else Path(audiosource).name
        answers.insert(0, f'Audio source: {source}\n\n')
        with open(answ_path, 'w') as tf:
            tf.writelines(answers)
    Path.mkdir(Path(output_dir), parents=True, exist_ok=True)
    ADGen = AudioDrillGen(freq_options, audio_source_path=audiosource, boost_cut=boost_cut, DualBandMode=DualBandMode,
                          starttime=starttime, endtime=endtime, drill_length=drill_length, gain_depth=gain_depth, Q=Q,
                          disableAdjacent=disableAdjacent, proc_t_perc=proc_t_perc, order='random', cropped=cropped,
                          callback=callback)
    filename = ''
    answers = []
    for i in range(10):
        try:
            freq, audio = ADGen.output()
            prefix = f'{filename_prefix}__' if filename_prefix else ''
            filename = f'{prefix}Example{i + 1}{format}'
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

