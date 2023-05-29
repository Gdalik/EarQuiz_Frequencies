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

import contextlib
from pathlib import Path

from PyQt6.QtWidgets import QFileDialog

from GUI.Playlist.plsong import PlSong
from Model.export_playlist import export_m3u_playlist
from definitions import PLAYLIST_DIR, CURRENT_PLAYLIST_PATH


def exportPlaylistWithRelPaths(mw, playlistdata: list[PlSong]):
    return exportPlaylist(mw, playlistdata, pathmode='relative')


def exportPlaylist(mw, playlistdata: list[PlSong], pathmode='absolute'):
    Path(PLAYLIST_DIR).mkdir(parents=True, exist_ok=True)
    FileDialog = QFileDialog(mw)
    m3u_mask = 'M3U (*.m3u)'
    m3u8_mask = 'M3U8 (*.m3u8)'
    formats = f'{m3u_mask};;{m3u8_mask}'
    filename, _format = FileDialog.getSaveFileName(mw, 'Export Playlist As...',
                                                   PLAYLIST_DIR, filter=formats, initialFilter=m3u8_mask)
    result = False
    if filename and _format in (m3u_mask, m3u8_mask):
        ext = '.m3u8' if _format == m3u8_mask else '.m3u'
        enc = 'utf-8' if _format == m3u8_mask else None
        try:
            result = export_m3u_playlist(playlistdata, filename, pathmode=pathmode, ext=ext, encoding=enc)
        except Exception as e:
            mw.error_msg(f'Error exporting playlist! {str(e)}')
    return result


def saveCurrentPlaylist(playlistdata: list[PlSong]):
    Path(Path(CURRENT_PLAYLIST_PATH).parent).mkdir(parents=True, exist_ok=True)
    with contextlib.suppress(Exception):
        export_m3u_playlist(playlistdata, CURRENT_PLAYLIST_PATH, pathmode='absolute', ext='.m3u8', encoding='utf-8')
