from pathlib import Path
import mimetypes
from urllib import parse
import re
from xspf_lib import Playlist


AudioMimes = ['audio/x-wav', 'audio/mpeg', 'audio/x-aiff', 'audio/x-flac', 'audio/ogg']
PLMimes = ['audio/x-mpegurl', 'application/pls+xml', 'application/xspf+xml']


def pathsResolve(Paths: list):
    paths = []
    for path in Paths:
        _Path = Path(path)
        if _Path.is_file():
            paths.append(path)
        elif _Path.is_dir():
            paths.extend(filesFromDir(_Path))
            paths.sort()
    return filePathsFilter(expandPlayLists(filePathsFilter(paths)))


def filesFromDir(dirpath: Path):
    dir_content = dirpath.glob('**/*')
    return [str(el) for el in dir_content if el.is_file()]


def filePathsFilter(paths: list):
    MimeTypes = AudioMimes + PLMimes
    return [path for path in paths if mimetypes.guess_type(path)[0] in MimeTypes and not Path(path).name.startswith('.')]


def expandPlayLists(paths: list):
    paths_expanded = []
    for path in paths:
        if mimetypes.guess_type(path)[0] in PLMimes:
            files = files_from_PL(path)
            paths_expanded.extend(files)
        else:
            paths_expanded.append(path)
    return paths_expanded


def files_from_PL(pl_path: str):
    mime = mimetypes.guess_type(pl_path)[0]
    if mime == 'application/xspf+xml':
        pl_urls = parseUrlsFromXSPF(pl_path)
    elif mime in ('audio/x-mpegurl', 'application/pls+xml'):
        with open(pl_path, 'r') as f:
            pl_lines = [line.rstrip() for line in f.readlines()]
        pl_urls = list(map(parseUrlFrom_PLS, pl_lines)) if mime == 'application/pls+xml' else pl_lines
    else:
        return []
    return urlsToExistingFiles(pl_urls, Path(pl_path).parent)


def parseUrlFrom_PLS(line: str):
    return re.sub('File\d+=', '', line, count=1)


def parseUrlsFromXSPF(filepath: str):
    return [track.location[0] for track in Playlist.parse(filepath).data]


def urlsToExistingFiles(urls: list, current_dir):
    files = []
    for url in urls:
        path = parse.urlparse(url).path
        abs_path = path if Path(path).is_absolute() else str(Path(current_dir, path))
        if Path(abs_path).is_file():
            files.append(abs_path)
    return files
