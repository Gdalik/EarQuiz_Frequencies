import json
import definitions
from pathlib import PurePath


class EQPatterns:
    def __init__(self):
        with open(PurePath(definitions.ROOT_DIR, 'Data', 'eq_patterns.json')) as f:
            d = json.load(f)
            self.List = d['Patterns']
        defaults = {'DualBandMode': False, 'DisableAdjacentFiltersMode': False, 'gain_depth': 12,
                    'BW_Q': '1/3 Oct (Q=4.32)'}
        for P in self.List:
            for key in defaults:
                P[key] = defaults[key] if key not in P else P[key]

    def get(self, mode_num: int):   # Enumeration starts from 1
        return self.List[mode_num - 1]
