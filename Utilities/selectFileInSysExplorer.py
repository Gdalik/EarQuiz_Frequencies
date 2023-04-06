import contextlib
import platform
import subprocess
import os


def selectFile(filepath: str):
    if not os.path.isfile(filepath):
        return
    if platform.system() == 'Darwin':
        cmd = ["open", "-R", filepath]
    elif platform.system() == 'Windows':
        filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        filepath = rf'{filepath}'
        cmd = [filebrowser_path, '/select,', filepath]
    else:
        cmd = ''
    with contextlib.suppress():
        subprocess.run(cmd)
