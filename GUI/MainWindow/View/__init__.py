import sys
from GUI.Playlist import playlistview
from GUI import Icons_rc

sys.modules["playlistview"] = playlistview
sys.modules["Icons_rc"] = Icons_rc
