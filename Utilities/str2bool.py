def str2bool(value: str or bool) -> bool:
    if isinstance(value, bool):
        return value
    if not isinstance(value, str):
        raise ValueError('The value is neither string nor bool!')
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False
