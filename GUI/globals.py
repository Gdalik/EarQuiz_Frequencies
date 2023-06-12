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

from definitions import Settings

default_pn_slice_length = None
default_audio_slice_length = None

SliderAmplitude = 2

def defaultSliceLenUpd():
    global default_pn_slice_length
    global default_audio_slice_length
    Settings.beginGroup('GlobalVars')
    default_pn_slice_length = int(Settings.value('PinknoiseSliceLength', 10))
    default_audio_slice_length = int(Settings.value('ExtAudioSliceLength', 12))
    Settings.endGroup()


defaultSliceLenUpd()
