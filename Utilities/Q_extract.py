import re


def Qextr(arg: int or float or str):
    if isinstance(arg, (int, float)):
        return arg
    if not isinstance(arg, str):
        return
    arg = arg.replace(' ', '')
    res = re.search('(?<=Q\=)\d+.?,?\d+', arg)
    return float(res.group()) if res else None
