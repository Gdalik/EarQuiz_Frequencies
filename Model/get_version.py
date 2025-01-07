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

import json
from pathlib import Path
from definitions import ROOT_DIR


def _get_version_data(external_data=None):  # external_data in JSON format
    if external_data is None:
        with open(Path(ROOT_DIR, 'Model', 'Version', 'version.json'), 'r', encoding='utf-8') as f:
            external_data = f.read()
    v_data = json.loads(external_data)['version']
    return v_data['major'], v_data['minor'], v_data['patch']


def version(external_data=None):
    v_data = _get_version_data(external_data=external_data)
    return "%d.%d.%d" % (v_data[0], v_data[1], v_data[2])


def version_int(external_data=None):
    v_data = _get_version_data(external_data=external_data)
    return int("%02d%02d%02d" % (v_data[0], v_data[1], v_data[2]))
