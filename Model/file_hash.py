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

import hashlib
from functools import partial


def filehash(filepath: str, buffer_size=1024 * 1024 * 50):
    hash_obj = hashlib.md5
    content = b''
    with open(filepath, 'rb') as f:
        for chunk in iter(partial(f.read, buffer_size), b''):
            content = b''.join([content, chunk])
    return hash_obj(content).hexdigest()
