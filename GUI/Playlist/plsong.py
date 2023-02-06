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
        self._path = str(PurePath(urlparse(self.inputPath).path))
        return self._path

    @cached_property
    def name(self):
        self._name = str(PurePath(self.path).name)
        return self._name

    @cached_property
    def dirPath(self):
        path = str(PurePath(self.path).parent)
        self._dirPath = path if path != '.' else ''
        return self._dirPath

    @cached_property
    def exists(self):
        return Path(self.path).is_file()

    @cached_property
    def duration(self):
        try:
            with AudioFile(self.path) as f:
                dur_sec = f.frames / f.samplerate
            self._duration = dur_sec
        except Exception:
            self._duration = False
        finally:
            return self._duration

    @cached_property
    def duration_str(self):
        self._duration_str = ':'.join(mmss(self.duration, string=True)) if self.duration else 'n/d'
        return self._duration_str

    @property
    def canLoad(self):
        return self._canLoad if hasattr(self, '_canLoad') else True

    @canLoad.setter
    def canLoad(self, arg: bool):
        self._canLoad = arg

    @property
    def available(self):
        return bool(self.exists and self.duration >= 30 and self.canLoad)
