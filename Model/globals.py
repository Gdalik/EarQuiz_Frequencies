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

from Model.AudioEngine.pinknoise_gen import generate_pinknoise

supported_bitrates_mp3 = (32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320)
supported_bitrates_ogg = (64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 500)
pinknoise = generate_pinknoise()
MinAudioDuration = 10  # in sec
PinknoiseLength = 30  # in sec
