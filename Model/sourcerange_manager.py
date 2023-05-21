#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

import json
import os
from pathlib import Path
from Model.AudioEngine.preview_audio import PreviewAudioCrop
from definitions import SourceRangeLib_DIR


class SourceRangeManager:
    def __init__(self):
        pass

    def save(self, filehash: str, filename: str, SourceRange: PreviewAudioCrop):
        out_path = Path(SourceRangeLib_DIR, self._filename(filehash)).absolute()
        os.makedirs(SourceRangeLib_DIR, exist_ok=True)
        content = {'Audiofile': filename, 'Range': (SourceRange.starttime, SourceRange.endtime),
                   'SliceLength': SourceRange.slice_length}
        with open(out_path, 'w', encoding='utf-8', errors='replace') as f:
            f.write(json.dumps(content, indent=1))

    def get(self, filehash: str):
        filename = self._filename(filehash)
        filepath = Path(SourceRangeLib_DIR, filename)
        if not filepath.is_file():
            return None
        filepath = filepath.absolute()
        with open(filepath, encoding='utf-8', errors='replace') as f:
            content = json.loads(f.read())
            try:
                return *content['Range'], content['SliceLength']
            except KeyError:
                return None

    @staticmethod
    def _filename(filehash: str):
        return f'{filehash}.afab'
