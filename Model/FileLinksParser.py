from pathlib import Path, PureWindowsPath, PurePath
import mimetypes
from urllib import parse, request
import re
import xml.etree.ElementTree as ET
# from xspf_lib import Playlist
import platform


if platform.system() == 'Windows':
    mimetypes.add_type('application/pls+xml', '.pls')
    mimetypes.add_type('application/xspf+xml', '.xspf')
AudioMimes = ('audio/x-wav', 'audio/wav', 'audio/mpeg', 'audio/aiff', 'audio/x-aiff', 'audio/x-flac', 'audio/ogg',
              'application/ogg', )
m3u_mimes = ('audio/x-mpegurl', 'audio/mpegurl', 'application/x-mpegurl', 'application/vnd.apple.mpegurl', )
pls_mimes = ('audio/scpls', 'audio/x-scpls', 'application/pls+xml', )
xspf_mimes = ('application/xspf+xml', )
PLMimes = m3u_mimes + pls_mimes + xspf_mimes


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
            mimetypes.guess_type(path, strict=False)[0] in MimeTypes and not Path(path).name.startswith('.')]


def expandPlayLists(paths: list[str], callback=None):
    paths_expanded = []
    for path in paths:
        if mimetypes.guess_type(path, strict=False)[0] in PLMimes:
            files = files_from_PL(path, callback)
            paths_expanded.extend(files)
        else:
            paths_expanded.append(path)
    return paths_expanded


def files_from_PL(pl_path: str, callback=None):

    mime = mimetypes.guess_type(pl_path, strict=False)[0]
    err_mess = f'Error occurred while parsing "{pl_path}": '
    if mime in xspf_mimes:
        try:
            pl_links = parseLinksFromXSPF(pl_path)
        except Exception as e:
            _cb(callback, f'{err_mess}{e}')
            return []
    elif mime in [*m3u_mimes, *pls_mimes]:
        enc = 'utf-8' if Path(pl_path).suffix == '.m3u8' else None
        try:
            with open(pl_path, 'r', encoding=enc) as f:
                pl_lines = [line.rstrip() for line in f.readlines()]
        except Exception as e:
            _cb(callback, f'{err_mess}{e}')
            return []
        pl_links = pl_lines if mime not in [*pls_mimes] else list(map(parseLinkFrom_PLS, pl_lines))
    else:
        return []
    return linksToExistingFiles(pl_links, Path(pl_path).parent, callback=callback)


def parseLinkFrom_PLS(line: str):
    return re.sub('File\d+=', '', line, count=1)


def parseLinksFromXSPF(filepath: str):
    root = ET.parse(filepath).getroot()
    NS = {'xspf': "http://xspf.org/ns/0/"}
    return [parse.unquote(tr.find('xspf:location', NS).text, encoding='utf-8') for tr in root.find('xspf:trackList', NS).findall('xspf:track', NS)]
    # return [track.location[0] for track in Playlist.parse(filepath).data]


def linksToExistingFiles(links: list[str], current_dir, callback=None):
    files = []
    for link in links:
        link = _windows_file_url_mod(link)
        try:
            path = _urlparse_func()(link).path if isURL(link) else link
        except Exception as e:
            _cb(callback, f'Cannot parse URL "{link}"! {e}')
            continue
        abs_path = path if Path(path).is_absolute() \
            else str(PurePath.joinpath(current_dir, PureWindowsPath(path).as_posix()))
        if Path(abs_path).is_file():
            files.append(abs_path)
    return files


def _urlparse_func():
    return request.url2pathname if platform.system() == 'Windows' else parse.urlparse


def _windows_file_url_mod(link: str):
    if platform.system() != 'Windows' or parse.urlparse(link).scheme != 'file':
        return link
    return re.sub('file:[/]+', '', link, 1)


def isURL(arg: str):
    scheme = parse.urlparse(arg).scheme
    if scheme in ('file', 'http', 'https', 'ftp'):
        return True
    elif scheme == '':
        return False
    else:
        return None


def _cb(callback, arg):
    if callback is not None:
        callback(str(arg))
