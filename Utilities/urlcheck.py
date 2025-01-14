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

from pathlib import Path


def validUrls(urls: list):
    available_ext = ('.wav', '.aiff', '.flac', '.ogg', '.mp3', '.m3u', '.m3u8', '.pls', '.xspf')
    available_ext = tuple(list(available_ext) + [EXT.upper() for EXT in available_ext])
    return [url for url in urls if url.toLocalFile() and Path(url.toLocalFile()).exists()
            and (Path(url.toLocalFile()).is_dir() or Path(url.toLocalFile()).suffix in available_ext)]
