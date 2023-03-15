from dataclasses import dataclass
from pedalboard.io import AudioFile
from Utilities.common_calcs import mmss
from pathlib import PurePath, Path
from functools import cached_property


@dataclass(eq=False)
class PlSong:
    inputPath: str

    @cached_property
    def path(self):
        # return str(Path(urlparse(self.inputPath).path).absolute())
        if self.inputPath == 'pinknoise':
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
        return True if self.name == 'pinknoise' else Path(self.path).is_file()

    @cached_property
    def file_properties(self):
        return_dict = self._default_dict
        if not self.exists:
            return return_dict
        try:
            with AudioFile(self.path) as f:
                return_dict['duration'] = f.frames / f.samplerate
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
        return bool(self.exists and self.duration >= 30 and self.canLoad)

    @property
    def _default_dict(self):
        if self.name == 'pinknoise':
            return {'duration': 30, 'num_channels': 1, 'samplerate': 44100}
        else:
            return {'duration': False, 'num_channels': None, 'samplerate': None}

