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

from dataclasses import dataclass
from functools import cached_property
from pathlib import PurePath, Path
from pedalboard.io import AudioFile
from Model.globals import MinAudioDuration
from Utilities.common_calcs import mmss
from definitions import PN


@dataclass(eq=False)
class PlSong:
    inputPath: str

    @cached_property
    def isPinkNoise(self):
        return self.inputPath == PN

    @cached_property
    def path(self):
        if self.isPinkNoise:
            return self.inputPath
        return str(Path(self.inputPath).absolute()) if self.inputPath else ''

    @cached_property
    def name(self):
        return str(PurePath(self.path).name)

    @cached_property
    def dirPath(self):
        path = str(PurePath(self.path).parent)
        return path if path != '.' else ''

    @property
    def exists(self):
        return True if self.isPinkNoise else Path(self.path).is_file()

    @cached_property
    def file_properties(self):
        return_dict = self._default_dict
        if not self.exists or self.isPinkNoise:
            return return_dict
        try:
            with AudioFile(self.path) as f:
                return_dict['duration'] = f.duration
                num_channels = f.num_channels
                if num_channels == 1:
                    num_channels = 'Mono'
                elif num_channels == 2:
                    num_channels = 'Stereo'
                else:
                    num_channels = f'{num_channels} Channels'
                return_dict['num_channels'] = num_channels
                return_dict['samplerate'] = int(f.samplerate)
        except Exception:
            pass
        finally:
            return return_dict

    @property
    def duration(self):
        return self.file_properties['duration']

    @property
    def num_channels(self):
        return self.file_properties['num_channels']

    @property
    def samplerate(self):
        return self.file_properties['samplerate']

    @property
    def duration_str(self):
        return ':'.join(mmss(self.duration, string=True)) if self.duration else 'n/d'

    @property
    def canLoad(self):
        return self._canLoad if hasattr(self, '_canLoad') else True

    @canLoad.setter
    def canLoad(self, arg: bool):
        self._canLoad = arg

    @property
    def available(self):
        return bool(self.exists and self.duration >= MinAudioDuration and self.canLoad and self.samplerate >= 44100)

    @property
    def _default_dict(self):
        if self.isPinkNoise:
            return {'duration': 30, 'num_channels': 'Mono', 'samplerate': 44100}
        else:
            return {'duration': False, 'num_channels': None, 'samplerate': None}
