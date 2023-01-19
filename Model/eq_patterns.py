mode1 = {'Name': '1. Lowest five (31-500 Hz) 1-octave bands boosted (+)', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 500),
         'EQ_boost_cut': '+'}
mode2 = {'Name': '2. Middle five (250-4000 Hz) 1-octave bands boosted (+)', 'EQtype': 'EQ1', 'ActiveFreqRange': (250, 4000),
         'EQ_boost_cut': '+'}
mode3 = {'Name': '3. Highest five (1-16 kHz) 1-octave bands boosted (+)', 'EQtype': 'EQ1', 'ActiveFreqRange': (1000, 16000),
         'EQ_boost_cut': '+'}
mode4 = {'Name': '4. Lowest five (31-500 Hz) 1-octave bands cut (-)', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 500),
         'EQ_boost_cut': '-'}
mode5 = {'Name': '5. Middle five (250-4000 Hz) 1-octave bands cut (-)', 'EQtype': 'EQ1', 'ActiveFreqRange': (250, 4000),
         'EQ_boost_cut': '-'}
mode6 = {'Name': '6. Highest five (1-16 kHz) 1-octave bands cut (-)', 'EQtype': 'EQ1', 'ActiveFreqRange': (1000, 16000),
         'EQ_boost_cut': '-'}
mode7 = {'Name': '7. All ten 1-octave bands boosted (+)', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 16000), 'EQ_boost_cut': '+'}
mode8 = {'Name': '8. All ten 1-octave bands cut (-)', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 16000), 'EQ_boost_cut': '-'}
mode9 = {'Name': '9. All ten 1-octave bands boosted (+) or cut (-)', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 16000),
         'EQ_boost_cut': '+-'}
mode10 = {'Name': '10. Low (32-315 Hz) 1/3-octave bands boosted (+) or cut (-)', 'EQtype': 'EQ2',
          'ActiveFreqRange': (32, 315), 'EQ_boost_cut': '+-'}
mode11 = {'Name': '11. Mid (315-1250 Hz) 1/3-octave bands boosted (+) or cut (-)', 'EQtype': 'EQ2',
          'ActiveFreqRange': (315, 1250), 'EQ_boost_cut': '+-'}
mode12 = {'Name': '12. High (1.6 kHz - 16 kHz) 1/3-octave bands boosted (+) or cut (-)', 'EQtype': 'EQ2', 'ActiveFreqRange': (1600, 16000),
          'EQ_boost_cut': '+-'}
mode13 = {'Name': '13. All 1/3-octave bands boosted (+) or cut (-)', 'EQtype': 'EQ2', 'ActiveFreqRange': (32, 16000), 'EQ_boost_cut': '+-'}
mode14 = {'Name': '14. Two 1-octave bands treated (boosted/cut) simultaneously', 'EQtype': 'EQ1', 'ActiveFreqRange': (31, 16000),
          'EQ_boost_cut': '+-', 'dualBandMode': True, 'disableAdjacentFiltersMode': 1}

eqPatterns = [mode1, mode2, mode3, mode4, mode5, mode6, mode7, mode8, mode9, mode10, mode11, mode12, mode13, mode14]

