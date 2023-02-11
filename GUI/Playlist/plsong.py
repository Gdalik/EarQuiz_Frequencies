from urllib.parse import urlparse
from dataclasses import dataclass
from pedalboard.io import AudioFile
from Utilities.common_calcs import mmss
from pathlib import PurePath, Path
from functools import cached_property


@dataclass
class PlSong:
    inputPath: str

    @cached_property
    def path(self):
        return str(PurePath(urlparse(self.inputPath).path))

    @cached_property
    def name(self):
        return str(PurePath(self.path).name)

    @cached_property
    def dirPath(self):
        path = str(PurePath(self.path).parent)
        return path if path != '.' else ''

    @property
    def exists(self):
        return Path(self.path).is_file()

    @cached_property
    def file_properties(self):
        duration = False
        num_channels = None
        samplerate = None
        try:
            with AudioFile(self.path) as f:
                duration = f.frames / f.samplerate
                num_channels = f.num_channels
                if num_channels == 1:
                    num_channels = 'Mono'
                elif num_channels == 2:
                    num_channels = 'Stereo'
                else:
                    num_channels = f'{num_channels} Channels'
                samplerate = f.samplerate
        except Exception:
            pass
        finally:
            return {'duration': duration, 'num_channels': num_channels, 'samplerate': int(samplerate)}

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
