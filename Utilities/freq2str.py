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

def freqString(answer: int or tuple):
    def hzTokHz(value: int):
        if value >= 1000:
            return f'{value / 1000}kHz' if value % 1000 != 0 else f'{int(value / 1000)}kHz'
        else:
            return f'{value}Hz'

    def bc(value: int):
        return '(+)' if value > 0 else '(-)'

    def valueToStr(value: int):
        return f'{hzTokHz(abs(value))}{bc(value)}'

    return valueToStr(answer) if isinstance(answer, int) else ', '.join([valueToStr(v) for v in answer])
