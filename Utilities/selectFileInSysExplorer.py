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
import os
import platform
import subprocess


def selectFile(filepath: str):
    if not os.path.isfile(filepath):
        return
    if platform.system() == 'Darwin':
        cmd = ["open", "-R", filepath]
    elif platform.system() == 'Windows':
        filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        filepath = rf'{filepath}'
        cmd = [filebrowser_path, '/select,', filepath]
    else:
        cmd = ''
    with contextlib.suppress():
        subprocess.run(cmd)
