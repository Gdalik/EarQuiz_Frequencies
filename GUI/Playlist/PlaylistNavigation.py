from GUI.Playlist.plsong import PlSong
import random


class PlNavi:
    def __init__(self, playlistdata: list[PlSong], currentSong=None, shuffle=False, repeat_playlist=True):
        self.playlistdata = playlistdata
        self._currentSong = currentSong
        self._currentSongId = None
        self._shuffle = shuffle
        self._repeat_playlist = repeat_playlist
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

    def firstAvailable(self):
        if not self.playlistdata:
            return None
        if self.shuffle():
            shuffled = self._getShuffled()
            if shuffled.available:
                return shuffled
        for S in self.playlistdata:
            if S.available:
                return S

    def next(self):
        if not self.playlistdata or self._currentSong is None:
            return None
        if self._repeat_playlist and self.currentSong() == self.lastSongInQueue:
            return self.thisSong(availableOnly=False, avoidCurrent=True)
        if self._shuffle:
            return self._nextShuffle()
        if self._currentSong not in self.playlistdata:
            curSong_id = self.currentSongId() or 0
            return self.playlistdata[min(len(self.playlistdata) - 1, curSong_id)]
        return self.playlistdata[self.playlistdata.index(self._currentSong) + 1] \
            if self.playlistdata[-1] != self._currentSong else None

    @property
    def lastSongInQueue(self):
        if not self.shuffle() and self.playlistdata:
            return self.playlistdata[-1]
        return self.playedSongs[-1] if self.shuffle() and self.playedSongs else None

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

    # returns current / available / random / first song depending on conditions:
    def thisSong(self, availableOnly=True, avoidCurrent=False):
        if not self.playlistdata:
            return None
        if not avoidCurrent and self.currentSongInside() is not None:
            return None if availableOnly and not self.currentSongInside().available else self.currentSongInside()
        elif not availableOnly:
            return self._getShuffled() if self.shuffle() else self.playlistdata[0]
        elif self.firstAvailable() is not None:
            return self.firstAvailable()
        return None

    def currentSong(self):
        return self._currentSong

    def currentSongInside(self):
        return self._currentSong if self._currentSong in self.playlistdata else None

    def currentSongId(self):
        return self._currentSongId

    def updCurrentSongId(self):
        self._currentSongId = self.playlistdata.index(self._currentSong) if self._currentSong in self.playlistdata \
            else None
        return self._currentSongId

    def _getShuffled(self):
        if not self.playlistdata:
            return
        playlist_paths = self.playlist_paths
        playedSong_paths = self.playedSong_paths
        if playlist_paths == playedSong_paths:
            return self.playedSongs[0] if self.repeat_playlist() else None
        unplayed = playlist_paths - playedSong_paths
        choice = random.choice(tuple(unplayed))
        return next((S for S in self.playlistdata if choice == S.path), None)

    def setShuffle(self, arg: bool):
        self._shuffle = arg

    def shuffle(self):
        return self._shuffle

    def setRepeatPlaylist(self, arg: bool):
        self._repeat_playlist = arg

    def repeat_playlist(self):
        return self._repeat_playlist
