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


import os
import platform
from application import NativeAudioBackend


def setAudioBackend():
    native_backend_var = {'Windows': 'windows', 'Darwin': 'darwin', 'Linux': 'gstreamer'}
    value = 'ffmpeg' if not NativeAudioBackend else native_backend_var[platform.system()]
    os.environ['QT_MEDIA_BACKEND'] = value


def currentAudioBackend():
    return systemNativeBackend() if NativeAudioBackend else 'FFmpeg'


def systemNativeBackend():
    native_backend = {'Windows': 'WMF', 'Darwin': 'AVFoundation', 'Linux': 'GStreamer'}
    return native_backend[platform.system()]


def formatNotSupported(af: str):
    format_backend_list = (('.aiff', 'WMF'), ('.ogg', 'WMF'), ('.ogg', 'AVFoundation'))
    return (af, currentAudioBackend()) in format_backend_list
