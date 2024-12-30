#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
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
from GUI import globals as gb


class PinkNoiseMode:
    def __init__(self, parent):  # parent: MainWindowContr
        self.parent = parent
        self.name = 'Pinknoise'
        self.view = parent.mw_view
        self.parent.SRC.savePrevSourceAudioRange()
        with contextlib.suppress(AttributeError):
            self.parent.AL.setNoAudio()
        self.default_slice_length = gb.default_pn_slice_length
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(gb.default_pn_slice_length)
        self.parent.setMakeAudioActionsEnabled(True)
        self.parent.AL.load_pinknoise()


class AudioFileMode:
    def __init__(self, parent):  # parent: MainWindowContr
        self.parent = parent
        self.name = 'Audiofile'
        self.view = parent.mw_view
        with contextlib.suppress(AttributeError):
            self.parent.AL.setNoAudio()
        self.default_slice_length = gb.default_audio_slice_length
        self.parent.TransportContr.TransportView.SliceLenSpin.setValue(gb.default_audio_slice_length)
        self.view.TransportPanel.show()
