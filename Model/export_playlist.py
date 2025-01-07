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

import contextlib
from pathlib import Path
from GUI.Playlist.plsong import PlSong


def export_m3u_playlist(playlistdata: list[PlSong], out_fullpath: str, pathmode='absolute', ext='.m3u', encoding=None):
    encoding = 'utf-8' if ext == '.m3u8' else encoding
    out_fullpath = f'{out_fullpath}{ext}' if Path(out_fullpath).suffix != ext else out_fullpath
    out_dir = Path(out_fullpath).parent
    pl_paths = playlist_paths(playlistdata, out_dir=out_dir, pathmode=pathmode)
    pl_paths_str = '\n'.join(pl_paths)
    Path.mkdir(out_dir, parents=True, exist_ok=True)
    with open(out_fullpath, "w", encoding=encoding, errors='replace') as f:
        f.write(pl_paths_str)
    return out_fullpath if Path(out_fullpath).is_file() else False


def playlist_paths(playlistdata: list[PlSong], out_dir=None, pathmode='absolute'):
    if pathmode == 'absolute' or out_dir is None:
        pl_paths = [str(Path(P.path).absolute()) for P in playlistdata]
    else:
        pl_paths = []
        for P in playlistdata:
            _path = str(Path(P.path).absolute())
            with contextlib.suppress(ValueError):
                _path = str(Path(P.path).absolute().relative_to(out_dir))
            pl_paths.append(_path)
    return pl_paths
