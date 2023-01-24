import json
import definitions
from pathlib import PurePath


class EQPatterns:
    def __init__(self):
        with open(PurePath(definitions.ROOT_DIR, 'Model', 'Data', 'eq_patterns.json')) as f:
            d = json.load(f)
            self.List = d['Patterns']
        for P in self.List:
            defaults = self.get_defaults(P['EQtype'])
            for key in defaults:
                P[key] = defaults[key] if key not in P else P[key]

    def get(self, mode_num: int):  # Enumeration starts from 1
        return self.List[mode_num - 1]

    @staticmethod
    def get_defaults(EQtype: str):
        return {'DualBandMode': False, 'DisableAdjacentFiltersMode': False, 'Gain_depth': 12,
                'BW_Q': '1 Oct (Q=1.41)'} if EQtype == 'EQ1' \
            else {'DualBandMode': False, 'DisableAdjacentFiltersMode': False, 'Gain_depth': 15,
                  'BW_Q': '1/3 Oct (Q=4.32)'}
