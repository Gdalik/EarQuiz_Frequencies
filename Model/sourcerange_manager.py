import os
from definitions import SourceRangeLib_DIR
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from pathlib import Path
import json


class SourceRangeManager:
    def __init__(self):
        pass

    def save(self, filehash: str, filename: str, SourceRange: PreviewAudioCrop):
        out_path = Path(SourceRangeLib_DIR, self._filename(filehash)).absolute()
        os.makedirs(SourceRangeLib_DIR, exist_ok=True)
        content = {'Audiofile': filename, 'Range': (SourceRange.starttime, SourceRange.endtime),
                   'SliceLength': SourceRange.slice_length}
        with open(out_path, 'w') as f:
            f.write(json.dumps(content, indent=1))

    def get(self, filehash: str):
        filename = self._filename(filehash)
        filepath = Path(SourceRangeLib_DIR, filename)
        if not filepath.is_file():
            return None
        filepath = filepath.absolute()
        with open(filepath) as f:
            content = json.loads(f.read())
            return *content['Range'], content['SliceLength']

    @staticmethod
    def _filename(filehash: str):
        return f'{filehash}.afab'
