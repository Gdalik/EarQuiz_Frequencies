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

import re
from pathlib import Path
from pedalboard.io import AudioFile
from Utilities.exceptions import InterruptedException


def get_target_samplerate(source_sr: int or float, sr_mode: str):
    if sr_mode == 'original':
        ts = source_sr
    elif sr_mode == '48k':
        ts = 48000
    elif sr_mode == 'auto_div' and source_sr % 48000 == 0:
        ts = 48000
    else:
        ts = 44100
    return float(ts)


def avoid_same_name(audiofile_path: str):
    result = Path(audiofile_path)
    while result.exists():
        name_noext = str(result.with_suffix(''))
        digit_end = re.search(r'(?<=__)\d+$', name_noext)
        if digit_end is not None:
            digit_end = digit_end.group()
            name_noext = f"{name_noext[:-len(f'{digit_end}')]}{int(digit_end) + 1}"
        else:
            name_noext = f"{name_noext}__1"
        result = Path(name_noext + result.suffix)
    return str(result)


def convert_audio(audiofile_path: str, source_samplerate: int or float, audio_format='WAVE',
                  target_samplerate_mode='original', callback=None):
    # audio_format: WAVE / AIFF
    # sampling_rate_mode: original / 44.1k / 48k / auto_div
    def callback_out():
        if callback is not None:
            callback(out_stat)

    if not Path(audiofile_path).is_file():
        return None
    target_samplerate = get_target_samplerate(source_samplerate, target_samplerate_mode)
    out_ext = '.aiff' if audio_format == 'AIFF' else '.wav'
    output_path = Path(audiofile_path).with_suffix(out_ext)
    if str(output_path) == audiofile_path and source_samplerate == target_samplerate:
        return None
    if source_samplerate == target_samplerate:
        input_af = AudioFile(audiofile_path, 'r')
    else:
        input_af = AudioFile(audiofile_path, 'r').resampled_to(target_samplerate)
        output_path = Path(f"{output_path.with_suffix('')} - Resampled{out_ext}")
    output_path = Path(avoid_same_name(str(output_path)))
    result = None
    out_stat = {'State': f'Converting "{Path(audiofile_path).name}" to "{output_path.name}"', 'Percent': 0}
    callback_out()
    with input_af as in_f:
        with AudioFile(str(output_path), 'w', target_samplerate, in_f.num_channels) as out_f:
            while in_f.tell() < in_f.frames:
                ch = in_f.read(int(target_samplerate))
                out_f.write(ch)
                out_stat['Percent'] = int(out_f.frames / in_f.frames * 100)
                try:
                    callback_out()
                except InterruptedException:
                    out_f.close()
                    output_path.unlink()
                    return None
            if in_f.frames == out_f.frames:
                result = str(output_path)
        return result
