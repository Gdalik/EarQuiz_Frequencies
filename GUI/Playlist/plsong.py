from urllib.parse import urlparse
from dataclasses import dataclass
from pedalboard.io import AudioFile
from Utilities.common_calcs import mmss
from pathlib import PurePath, Path


@dataclass
class PlSong:
    inputPath: str

    @property
    def path(self):
        if hasattr(self, '_path'):
            return self._path
        self._path = str(PurePath(urlparse(self.inputPath).path))
        return self._path

    @property
    def name(self):
        if hasattr(self, '_name'):
            return self._name
        self._name = str(PurePath(self.path).name)
        return self._name

    @property
    def dirPath(self):
        if hasattr(self, '_dirPath'):
            return self._dirPath
        path = str(PurePath(self.path).parent)
        self._dirPath = path if path != '.' else ''
        return self._dirPath

    @property
    def exists(self):
        return Path(self.path).is_file()

    @property
    def duration(self):
        if not self.exists:
            return False
        if hasattr(self, '_duration'):
            return self._duration
        try:
            with AudioFile(self.path) as f:
                dur_sec = f.frames / f.samplerate
            self._duration = dur_sec
        except Exception:
            self._duration = False
        finally:
            return self._duration

    @property
    def duration_str(self):
        if hasattr(self, '_duration_str'):
            return self._duration_str
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
