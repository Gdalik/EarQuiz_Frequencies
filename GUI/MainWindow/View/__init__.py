import sys
from GUI.Playlist import playlistwidget
from GUI import Icons_rc

sys.modules["playlistwidget"] = playlistwidget
sys.modules["Icons_rc"] = Icons_rc
