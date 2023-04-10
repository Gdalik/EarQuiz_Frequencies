import hashlib
from functools import partial


def filehash(filepath: str, buffer_size=1024 * 1024 * 50):
    hash_obj = hashlib.md5
    content = b''
    with open(filepath, 'rb') as f:
        for chunk in iter(partial(f.read, buffer_size), b''):
            content = b''.join([content, chunk])
    return hash_obj(content).hexdigest()
