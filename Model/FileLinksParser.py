#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023, Gdaliy Garmiza.
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

import mimetypes
import platform
import re
import xml.etree.ElementTree as ET
from pathlib import Path, PureWindowsPath, PurePath
from urllib import parse, request

mimetypes.add_type('audio/x-scpls', '.pls')
mimetypes.add_type('application/xspf+xml', '.xspf')
mimetypes.add_type('audio/x-mpegurl', '.m3u')
mimetypes.add_type('audio/x-mpegurl', '.m3u8')
mimetypes.add_type('audio/ogg', '.ogg')
AudioMimes = ('audio/wav', 'audio/x-wav', 'audio/mpeg', 'audio/x-mpeg', 'audio/aiff', 'audio/x-aiff', 'audio/flac',
              'audio/x-flac', 'audio/ogg', 'audio/x-ogg',)
m3u_mimes = ('audio/x-mpegurl', 'audio/mpegurl', 'application/x-mpegurl', 'application/vnd.apple.mpegurl',)
pls_mimes = ('audio/scpls', 'audio/x-scpls', 'application/pls+xml',)
xspf_mimes = ('application/xspf+xml',)
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
    enc = 'utf-8' if Path(pl_path).suffix in ('.m3u8', '.xspf',) else None
    try:
        if mime in xspf_mimes:
            pl_links = parseLinksFromXSPF(pl_path)
        elif mime in m3u_mimes:
            pl_links = parseLinksFrom_M3U(pl_path, encoding=enc)
        elif mime in pls_mimes:
            pl_links = parseLinksFrom_PLS(pl_path)
        else:
            return []
    except Exception as e:
        _cb(callback, f'{err_mess}{e}')
        return []
    pl_links = [parse.unquote(link, encoding=enc) for link in pl_links] if enc is not None else pl_links
    return linksToExistingFiles(pl_links, Path(pl_path).parent, callback=callback)


def parseLinksFrom_M3U(pl_path: str, encoding=None):
    with open(pl_path, 'r', encoding=encoding, errors='replace') as f:
        pl_links = [line.rstrip() for line in f.readlines()]
    return pl_links


def parseLinksFrom_PLS(pl_path: str):
    with open(pl_path, 'r', errors='replace') as f:
        pl_lines = [re.sub('File\d+=', '', line.rstrip()) for line in f.readlines()]
    return pl_lines


def parseLinksFromXSPF(filepath: str):
    root = ET.parse(filepath).getroot()
    NS = {'xspf': "http://xspf.org/ns/0/"}
    return [tr.find('xspf:location', NS).text for tr in root.find('xspf:trackList', NS).findall('xspf:track', NS)]


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
