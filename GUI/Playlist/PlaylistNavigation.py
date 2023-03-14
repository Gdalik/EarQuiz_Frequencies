from GUI.Playlist.plsong import PlSong
import random


class PlNavi:
    def __init__(self, playlistdata: list, currentSong=None, shuffle=False):
        self.playlistdata = playlistdata
        self._currentSong = currentSong
        self._currentSongId = None
        self._shuffle = shuffle
        self.playedSongs = []

    @property
    def playlist_paths(self):
        return {P.path for P in self.playlistdata}

    @property
    def playedSong_paths(self):
        return {P.path for P in self.playedSongs}

    def dataSync(self, newPlData):
        self.playlistdata = newPlData
        self.playedSongs = [S for S in self.playedSongs if S in self.playlistdata]

    def next(self):
        if not self.playlistdata or self._currentSong is None:
            return None
        if self._shuffle:
            return self._nextShuffle()
        if self._currentSong not in self.playlistdata:
            curSong_id = self.currentSongId() or 0
            return self.playlistdata[min(len(self.playlistdata) - 1, curSong_id)]
        return self.playlistdata[self.playlistdata.index(self._currentSong) + 1] \
            if self.playlistdata[-1] != self._currentSong else None

    def _nextShuffle(self):
        if not self.playlistdata:
            return None
        if len(self.playedSongs) > 0 and self._currentSong.path != self.playedSongs[-1].path:
            for ind, S in enumerate(self.playedSongs):
                if S.path == self._currentSong.path:
                    return self.playedSongs[ind + 1]
        return self._getShuffled()

    def prev(self):
        if not self.playlistdata or self._currentSong is None:
            return None
        if self._shuffle:
            return self._prevShuffle()
        if self._currentSong not in self.playlistdata:
            curSong_id = self.currentSongId() or 0
            prevSong_id = min(max(curSong_id - 1, 0), len(self.playlistdata) - 1)
            return self.playlistdata[prevSong_id]
        return self.playlistdata[self.playlistdata.index(self._currentSong) - 1] \
            if self.playlistdata[0] != self._currentSong else self._currentSong

    def _prevShuffle(self):
        if len(self.playedSongs) == 0:
            return None
        for ind, S in enumerate(self.playedSongs):
            if S.path == self._currentSong.path:
                return self.playedSongs[max(ind - 1, 0)]

    def setCurrentSong(self, Song: PlSong or None):
        self._currentSong = Song
        self.updCurrentSongId()
        if Song is None:
            return
        if Song.path not in self.playedSong_paths and Song.path in self.playlist_paths:
            self.playedSongs.append(Song)

    def currentSong(self):
        return self._currentSong

    def currentSongId(self):
        return self._currentSongId

    def updCurrentSongId(self):
        self._currentSongId = self.playlistdata.index(self._currentSong) if self._currentSong in self.playlistdata \
            else None
        return self._currentSongId

    def _getShuffled(self):
        playlist_paths = self.playlist_paths
        playedSong_paths = self.playedSong_paths
        if playlist_paths == playedSong_paths:
            return None
        unplayed = playlist_paths - playedSong_paths
        choice = random.choice(tuple(unplayed))
        return next((S for S in self.playlistdata if choice == S.path), None)

    def setShuffle(self, arg):
        self._shuffle = arg

    def shuffle(self):
        return self._shuffle
