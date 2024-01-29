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

import json
from pathlib import PurePath

import definitions


class EQPatterns:
    def __init__(self):
        with open(PurePath(definitions.ROOT_DIR, 'Model', 'Data', 'eq_patterns.json')) as f:
            d = json.load(f)
            self.List = d['Patterns']
        P: dict
        for P in self.List:
            defaults = self.get_defaults(P['EQtype'])
            for key in defaults:
                P.setdefault(key, defaults[key])

    def get(self, mode_num: int):  # Enumeration starts from 1
        return self.List[mode_num - 1]

    @staticmethod
    def get_defaults(EQtype: str):
        return {'DualBandMode': False, 'DisableAdjacentFiltersMode': False, 'Gain_depth': 12,
                'BW_Q': '1 Oct (Q=1.41)'} if EQtype == 'EQ1' \
            else {'DualBandMode': False, 'DisableAdjacentFiltersMode': False, 'Gain_depth': 15,
                  'BW_Q': '1/3 Oct (Q=4.32)'}
