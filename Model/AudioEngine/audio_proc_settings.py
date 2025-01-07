#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

from application import Settings
from Utilities.str2bool import str2bool


default_EQOnTimePerc = 40
default_EQTransitionDur = 35 / 1000
default_ExFadeInOutDur = 5 / 1000


def getEQOnTimePerc():
    return int(Settings.value('AudioProcessing/EQOnTimePerc', default_EQOnTimePerc))   # in percentage


def getEQTransitionDur():
    return float(Settings.value('AudioProcessing/EQTransitionDur', default_EQTransitionDur))     # in seconds


def getExFadeInOutDur():
    return float(Settings.value('AudioProcessing/ExFadeInOutDur', default_ExFadeInOutDur))     # in seconds


def getEQAlwaysOnInTest():
    return str2bool(Settings.value('AudioProcessing/EQAlwaysOnInTest', False))


def setEQOnTimePerc(v: int):
    Settings.setValue('AudioProcessing/EQOnTimePerc', v)


def setEQTransitionDur(v: int):     # v: value in ms
    Settings.setValue('AudioProcessing/EQTransitionDur', v / 1000)


def setExFadeInOutDur(v: int):     # v: value in ms
    Settings.setValue('AudioProcessing/ExFadeInOutDur', v / 1000)   # in seconds


def setEQAlwaysOnInTest(v: bool):
    Settings.setValue('AudioProcessing/EQAlwaysOnInTest', v)
