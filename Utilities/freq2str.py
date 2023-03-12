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
