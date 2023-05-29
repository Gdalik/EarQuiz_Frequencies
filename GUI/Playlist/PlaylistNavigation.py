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

import copy
import random
from GUI.Playlist.plsong import PlSong


class PlNavi:
    def __init__(self, playlistdata: list[PlSong], currentSong=None, shuffle=False, repeat_playlist=True):
        self.playlistdata = playlistdata
        self.playedSongs = []
        self.prev_playlistdata = []
        self.prev_playedSongs = []
        self._currentSong = currentSong
        self._shuffle = shuffle
        self._repeat_playlist = repeat_playlist

    @property
    def maxId(self):
        return len(self.playlistdata) - 1

    @property
    def currentSong_path(self):
        return self.currentSong().path if self.currentSong() is not None else None

    def dataSync(self, newPlData):
        self.playlistdata = newPlData
        self.playedSongs = [S for S in self.playedSongs if S in self.playlistdata]

    def findCurrentSong(self, availableOnly=True, avoidActualCurrentSong=False):
        if len(self.playlistdata) == 0:
            return None
        #   When current song is in playlist
        if not avoidActualCurrentSong and self.currentSongInside() is not None:
            return self.firstAvailable() if availableOnly and not self.currentSongInside().available \
                else self.currentSongInside()
        #   When current song is missing in playlist, and any song in playlist is acceptable
        elif not availableOnly:
            return self._getShuffled() if self.shuffle() else self.playlistdata[0]
        #   When current song is missing in playlist, and only available one is acceptable
        elif self.firstAvailable() is not None:
            return self.firstAvailable()
        return None

    def next(self):
        if len(self.playlistdata) == 0 or self.currentSong() is None:
            return None
        if self.shuffle():
            return self._nextShuffle()
        if self.currentSong() == self.playlistdata[-1]:
            return self.findCurrentSong(availableOnly=False, avoidActualCurrentSong=True) if self.repeat_playlist() \
                else None
        if not self.currentSongInside():
            return self._findNextToDeletedCurrentSong()
        next_song_id = self.playlistdata.index(self._currentSong) + 1
        return self.playlistdata[next_song_id]

    def _nextShuffle(self):
        if len(self.playlistdata) == 0:
            return None
        if len(self.playedSongs) > 0 and self.currentSong() != self.playedSongs[-1]:
            for ind, S in enumerate(self.playedSongs):
                if S == self.currentSong():
                    return self.playedSongs[ind + 1]
        return self._getShuffled()

    def _findNextToDeletedCurrentSong(self):
        if len(self.playlistdata) == 0 or len(self.prev_playlistdata) == 0 or self.currentSong() is None \
                or self.currentSong() not in self.prev_playlistdata:
            return None
        start_ind = self.prev_playlistdata.index(self.currentSong())
        return next(
            (
                self.prev_playlistdata[i]
                for i in range(start_ind, len(self.prev_playlistdata))
                if self.prev_playlistdata[i] in self.playlistdata
            ),
            self.findCurrentSong(availableOnly=False)
            if self.repeat_playlist()
            else None,
        )

    def prev(self):
        if len(self.playlistdata) == 0 or self.currentSong() is None:
            return None
        if self._shuffle:
            return self._prevShuffle()
        if not self.currentSongInside():
            prevSong = self._findPrevToDeletedCurrentSong(self.playlistdata, self.prev_playlistdata)
            return prevSong if prevSong is not None else self.findCurrentSong(availableOnly=False)
        prev_song_id = max(self.playlistdata.index(self._currentSong) - 1, 0)
        return self.playlistdata[prev_song_id]

    def _prevShuffle(self):
        if len(self.playedSongs) == 0 or self.currentSong() is None:
            return None
        if self.currentSong() not in self.playedSongs:
            prev_song = self._findPrevToDeletedCurrentSong(self.playedSongs, self.prev_playedSongs)
            return prev_song if prev_song is not None else self.playedSongs[0]
        prev_song_id = max(self.playedSongs.index(self._currentSong) - 1, 0)
        return self.playedSongs[prev_song_id]

    def _findPrevToDeletedCurrentSong(self, curr_list: list, prev_list: list):
        if (
                not curr_list
                or not prev_list
                or self.currentSong() is None
                or self.currentSong() not in prev_list
        ):
            return None
        stop_ind = prev_list.index(self.currentSong())
        return next(
            (
                prev_list[i]
                for i in reversed(range(stop_ind))
                if prev_list[i] in curr_list
            ),
            None,
        )

    def setCurrentSong(self, Song: PlSong or None):
        self._currentSong = Song
        if Song is None:
            return
        if Song not in self.playedSongs and Song in self.playlistdata:
            self.playedSongs.append(Song)
        self.prev_playlistdata = copy.copy(self.playlistdata)
        self.prev_playedSongs = copy.copy(self.playedSongs)

    def firstAvailable(self):
        if len(self.playlistdata) == 0:
            return None
        if self.shuffle():
            shuffled = self._getShuffled()
            if shuffled is not None and shuffled.available:
                return shuffled
        for S in self.playlistdata:
            if S.available:
                return S

    @property
    def playlist_paths(self):
        return {P.path for P in self.playlistdata}

    def _getShuffled(self):
        if len(self.playlistdata) == 0:
            return
        playlist_paths = self.playlist_paths
        playedSong_paths = {P.path for P in self.playedSongs}
        if playlist_paths == playedSong_paths:
            return self.playedSongs[0] if self.repeat_playlist() else None
        not_played = playlist_paths - playedSong_paths
        choice = random.choice(tuple(not_played))
        return next((S for S in self.playlistdata if choice == S.path), None)

    def currentSongInside(self):
        return None if self.currentSong() is not None and self.currentSong() not in self.playlistdata \
            else self._currentSong

    def currentSong(self):
        return self._currentSong

    def setShuffle(self, arg: bool):
        self._shuffle = arg

    def shuffle(self):
        return self._shuffle

    def setRepeatPlaylist(self, arg: bool):
        self._repeat_playlist = arg

    def repeat_playlist(self):
        return self._repeat_playlist
