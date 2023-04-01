from PyQt6.QtWidgets import QFileDialog
from Model.export_playlist import export_m3u_playlist
from definitions import PLAYLIST_DIR
from GUI.Playlist.plsong import PlSong
from pathlib import Path


def exportPlaylistWithRelPaths(mw, playlistdata: list[PlSong]):
    return exportPlaylist(mw, playlistdata, pathmode='relative')


def exportPlaylist(mw, playlistdata: list[PlSong], pathmode='absolute'):
    Path(PLAYLIST_DIR).mkdir(parents=True, exist_ok=True)
    FileDialog = QFileDialog(mw)
    m3u_mask = 'M3U (*.m3u)'
    formats = f'{m3u_mask}'
    filename, _format = FileDialog.getSaveFileName(mw, 'Export Playlist As...',
                                                   PLAYLIST_DIR, filter=formats)
    result = False
    if filename and _format == m3u_mask:
        result = export_m3u_playlist(playlistdata, filename, pathmode=pathmode)
    return result
