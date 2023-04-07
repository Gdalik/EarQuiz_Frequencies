from pathlib import Path, PureWindowsPath, PurePath
import mimetypes
from urllib import parse
import re
from xspf_lib import Playlist
import platform


if platform.system() == 'Windows':
    mimetypes.add_type('application/pls+xml', '.pls')
    mimetypes.add_type('application/xspf+xml', '.xspf')
AudioMimes = ['audio/x-wav', 'audio/wav', 'audio/mpeg', 'audio/aiff', 'audio/x-aiff', 'audio/x-flac', 'audio/ogg',
              'application/ogg']
PLMimes = ['audio/x-mpegurl', 'audio/mpegurl', 'audio/scpls', 'application/pls+xml', 'application/xspf+xml']


def pathsResolve(Paths: list[str], return_dict: dict):
    def make_error_list(msg):
        errors.append(str(msg))
    paths = []
    errors = []
    for path in Paths:
        _Path = Path(path)
        if _Path.is_file():
            paths.append(path)
        elif _Path.is_dir():
            paths.extend(filesFromDir(_Path))
            paths.sort()
    paths = filePathsFilter(expandPlayLists(filePathsFilter(paths), callback=make_error_list))
    return_dict['Paths'] = paths
    return_dict['Errors'] = errors
    return return_dict


def filesFromDir(dirpath: Path):
    dir_content = dirpath.glob('**/*')
    return [str(el) for el in dir_content if el.is_file()]


def filePathsFilter(paths: list[str]):
    MimeTypes = AudioMimes + PLMimes
    return [path for path in paths if
            mimetypes.guess_type(path)[0] in MimeTypes and not Path(path).name.startswith('.')]


def expandPlayLists(paths: list[str], callback=None):
    paths_expanded = []
    for path in paths:
        if mimetypes.guess_type(path)[0] in PLMimes:
            files = files_from_PL(path, callback)
            paths_expanded.extend(files)
        else:
            paths_expanded.append(path)
    return paths_expanded


def files_from_PL(pl_path: str, callback=None):
    def cb(arg):
        if callback is not None:
            callback(str(arg))

    mime = mimetypes.guess_type(pl_path)[0]
    err_mess = f'Error occurred while parsing "{pl_path}": '
    if mime == 'application/xspf+xml':
        try:
            pl_links = parseLinksFromXSPF(pl_path)
        except Exception as e:
            cb(f'{err_mess}{e}')
            return []
    elif mime in ('audio/x-mpegurl', 'application/pls+xml', 'audio/mpegurl', 'audio/scpls'):
        enc = 'utf-8' if Path(pl_path).suffix == '.m3u8' else None
        try:
            with open(pl_path, 'r', encoding=enc) as f:
                pl_lines = [line.rstrip() for line in f.readlines()]
        except Exception as e:
            cb(f'{err_mess}{e}')
            return []
        pl_links = pl_lines if mime not in ('application/pls+xml', ) else list(map(parseLinkFrom_PLS, pl_lines))
    else:
        return []
    return linksToExistingFiles(pl_links, Path(pl_path).parent)


def parseLinkFrom_PLS(line: str):
    return re.sub('File\d+=', '', line, count=1)


def parseLinksFromXSPF(filepath: str):
    return [track.location[0] for track in Playlist.parse(filepath).data]


def linksToExistingFiles(links: list, current_dir):
    files = []
    for link in links:
        path = parse.urlparse(link).path if isURL(link) else link
        abs_path = path if Path(path).is_absolute() \
            else str(PurePath.joinpath(current_dir, PureWindowsPath(path).as_posix()))
        if Path(abs_path).is_file():
            files.append(abs_path)
    return files


def isURL(arg: str):
    scheme = parse.urlparse(arg).scheme
    if scheme in ('file', 'http', 'https', 'ftp'):
        return True
    elif scheme == '':
        return False
    else:
        return None

