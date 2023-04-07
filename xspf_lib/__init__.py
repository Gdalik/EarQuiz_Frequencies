"""Module helps to work with xspf playlists.
    Modified by Gdaliy Garmiza for EarQuiz Frequencies (c) project

MIT License

Copyright (c) 2020 Dzmitry Izaitka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


import xml.etree.ElementTree as ET
from typing import Iterable, Optional, Union, Dict
from datetime import datetime, timezone
from collections import UserList
import urllib.parse as urlparse
from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractstaticmethod

__all__ = ["Playlist", "Track", "Extension", "Link", "Meta", "URI",
           "Attribution"]

URI = str
NS = {'xspf': "http://xspf.org/ns/0/"}

ET.register_namespace('', NS['xspf'])


def quote(value: str) -> str:
    return value


def quoteInvalidChars(value: str) -> str:   #   introduced by Gdaliy Garmiza
    _value = ''
    for char in value:
        _char = char if char in _Parser.uric else urlparse.quote(char)
        _value += _char
    return _value


class XMLAble(ABC):

    @abstractmethod
    def to_xml_element(self) -> ET.Element:
        pass

    @abstractstaticmethod
    def parse_from_xml_element(element):
        pass


class Extension(XMLAble):
    """Class for XML extensions of XSPF playlists and tracks."""

    __slots__ = ['application', 'extra_attrib', 'content']

    def __init__(self, application: URI,
                 extra_attrib: Dict[str, str] = {},
                 content: Iterable[ET.Element] = []) -> None:
        """Create Extension for xspf_lib.Track and xspf_lib.Playlist.

        Extension must have attribute `application` URI wich point to
        extension standart. Extension can have an `elements` of type
        `xml.etree.ElementTree.Element`. Addtional xml attributes are welcome.

            Parameters
            :param: application: URI of specification of extension
            :param extra_attrib: list additionsl xml attributes
                for xml extension
            :param content: list of `xml.etree.ElementTree.Elements`,
                content of extension

        """
        self.application = application
        self.extra_attrib = extra_attrib
        self.content = content

    def to_xml_element(self) -> ET.Element:
        """Extention to `xml.etree.ElementTree.Element` conversion."""
        el = ET.Element('extension',
                        attrib={'application': self.application,
                                **self.extra_attrib},)
        el.extend(self.content)
        return el

    @staticmethod
    def parse_from_xml_element(element: ET.Element) -> 'Extension':
        """`xml.etree.ElementTree.Element` to Extension coversion."""
        application = _Parser.urify(element.get("application"))
        if application is None:
            raise TypeError(
                "Extension parsing missing attribute `application`")
        attribs = dict(
            [item for item in element.items() if item[0] != "application"])
        return Extension(application=application,
                         extra_attrib=attribs,
                         content=list(element))


@dataclass
class Link(XMLAble):
    """Object representation of `link` element.

    The link element allows XSPF to be extended without the use of
    XML namespaces.

    Content 2 arguments:
        `rel` - URI of resourse type. (required)
        `content` - URI of resourse.
    """

    rel: URI
    content: URI = ''

    @staticmethod
    def parse_from_xml_element(element):
        rel = _Parser.urify(element.get('rel'))
        if rel is None:
            raise TypeError("`rel` attribute of link is missing\n"
                            f"{ET.tostring(element)}")
        return Link(rel=rel, content=_Parser.urify(element.text))

    def to_xml_element(self) -> ET.Element:
        el = ET.Element('link', {'rel': str(self.rel)})
        el.text = str(self.content)
        return el


@dataclass()
class Meta(XMLAble):
    """Object representation of `meta` element.

    The meta element allows metadata fields to be added to XSPF.

    Content 2 arguments:
        `rel` -- URI of resourse type. (required)
        `content` -- value of metadata element. Usualy plain text.
    """

    rel: URI
    content: str = ''

    @staticmethod
    def parse_from_xml_element(element):
        # Check for markup.
        if len(list(element)) > 0:
            raise ValueError("Got nested elements in expected text. "
                             "Probably, this is unexpected HTML insertion.\n"
                             f"{ET.tostring(element)}")
        rel = _Parser.urify(element.get('rel'))
        if rel is None:
            raise TypeError("`rel` attribute of meta is missing\n"
                            f"{ET.tostring(element)}")
        return Meta(rel=rel, content=element.text)

    def to_xml_element(self) -> ET.Element:
        el = ET.Element('meta', {'rel': str(self.rel)})
        el.text = str(self.content)
        return el


class Attribution(XMLAble):
    """Object representation of `attribution` element.

    Can contain `location` attribute or `identifier` atribute or both.
    """

    __slots__ = ['location', 'identifier']

    def __init__(self, location: Optional[URI] = None,
                 identifier: Optional[URI] = None):
        """Create new attribution.

        Generate representation of `Attribution` element of
        `xpsf_lib.Playlist`.

        Parameters.
        :param location: -- data for `location` attribution.
        :param identifier: -- data for `identifier` attribution.

        It's obvious to add something to `location` to create location
        attribution. Or, you can add only `identifier` to create identifier
        attribute. You also can add both `attribution` and `location` field to
        create 2 attribution elements. Not putting both attributes is little
        odd.
        """
        self.location = location
        self.identifier = identifier

    def __repr__(self) -> repr:
        """Representation of `Attribute` object and that fields."""
        resp = "<Attribution {"
        if self.location is not None:
            resp += f"location={self.location}"
            if self.identifier is not None:
                resp += ', '
        if self.identifier is not None:
            resp += f"identifier={self.identifier}"
        resp += "}>"
        return resp

    def xml_elements(self):
        """Create generator of xml representation."""
        if self.location is not None:
            el = ET.Element('location')
            el.text = str(quote(self.location))
            yield el
        if self.identifier is not None:
            el = ET.Element('identifier')
            el.text = str(self.identifier)
            yield el

    def to_xml_element(self) -> ET.Element:
        return ET.Element('attribution').extend(self.xml_elements)

    @staticmethod
    def parse_from_xml_element(element) -> 'Attribution':
        if element.tag == ''.join(['{', NS['xspf'], '}location']):
            return Attribution(
                location=urlparse.unquote(_Parser.urify(element.text.strip())))
        elif element.tag == ''.join(['{', NS['xspf'], '}identifier']):
            return Attribution(identifier=_Parser.urify(element.text))
        else:
            # No `location` and `identifier` attribution is not allowed
            raise TypeError("Forbidden element in attribution.\n"
                            "Only `location` and `identifier` is "
                            "allowed.\n"
                            f"Got {ET.tostring(element)}.")


class Track(XMLAble):
    """Track info class."""

    def __init__(self,
                 location: Union[Iterable[URI], URI, None] = None,
                 identifier: Union[Iterable[URI], URI, None] = None,
                 title: Optional[str] = None,
                 creator: Optional[str] = None,
                 annotation: Optional[str] = None,
                 info: Optional[URI] = None,
                 image: Optional[URI] = None,
                 album: Optional[str] = None,
                 trackNum: Optional[int] = None,
                 duration: Optional[int] = None,
                 link: Iterable[Link] = [],
                 meta: Iterable[Meta] = [],
                 extension: Iterable[Extension] = []) -> None:
        """Track info class.

        Generate instances of tracks, ready to be put in Playlist class.

        Parameters
        :param location: URI or list of URI of resourse to be rendered
        :param identifier: canonical ID or list of ID for this resourse
        :param title: name o fthe track
        :param creator: name of creator of resourse
        :param annotation: comment on the track
        :param info: IRI of a place where info of this resourse can be
        founded
        :param image: URI of an image to display for the duration of the
        track
        :param album: name of the collection from which this resourse comes
        :param trackNum: integer giving the ordinal position of the media
        on the album
        :param duration: the time to render a resourse in milliseconds
        :param link: The link elements allows playlist extended without the
        use of XML namespace. List of entities of `xspf_lib.Link`.
        :param meta: Metadata fields of playlist.
        List of entities of `xspf_lib.Meta`.
        :param extension: Extension of non-XSPF XML elements. Must be a list
        tuples like `[Extension, ...]`

        """
        _Builder().build_track(self, locals())

    __slots__ = ('location', 'identifier', 'title', 'creator', 'annotation',
                 'info', 'image', 'album', 'link', 'meta', 'extension')

    def __repr__(self) -> str:
        """Return representation `repr(self)`."""
        repr = "<Track"
        if self.title is not None:
            repr += f'"{self.title}"'
        else:
            repr += " NONAME"
        if self.location is not None:
            repr += f' at "{self.location[0]}">'
        else:
            repr += '>'
        return repr

    @property
    def trackNum(self) -> int:
        return self.__trackNum

    @trackNum.setter
    def trackNum(self, value: int) -> None:
        if value is not None:
            if value < 0:   # modified by Gdaliy Garmiza in order to include trackNum == 0
                raise ValueError("trackNum must be positive number.\n"
                                 "| Expected: {1, 2, ..}\n"
                                 f"| Got: {value}")
            self.__trackNum = value
        else:
            self.__trackNum = None

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, value: int) -> None:
        if value is not None:
            if value < 0:
                raise ValueError("duration must be a non negative integer\n"
                                 "| Expected: {0, 1, 2, ..}\n"
                                 f"| Got: {value}")
            self.__duration = value
        else:
            self.__duration = None

    def to_xml_element(self) -> ET.Element:
        """Create `xml.ElementTree.Element` of the track."""
        return _XML_Builder(self).build_track()

    def xml_string(self) -> str:
        """Return XML representation of track."""
        return ET.tostring(self.to_xml_element(), encoding="UTF-8").decode()

    @staticmethod
    def parse_from_xml_element(element) -> 'Track':
        return _TrackParser(element).parse()


class Playlist(UserList, XMLAble):
    """Playlist info class."""

    def __init__(self,
                 title: Optional[str] = None,
                 creator: Optional[str] = None,
                 annotation: Optional[str] = None,
                 info: Optional[URI] = None,
                 location: Optional[URI] = None,
                 identifier: Optional[URI] = None,
                 image: Optional[URI] = None,
                 license: Optional[URI] = None,
                 attribution: Iterable[Union['Playlist', Attribution]] = [],
                 link: Iterable[Link] = [],
                 meta: Iterable[Meta] = [],
                 extension: Iterable[Extension] = [],
                 trackList: Iterable[Track] = []) -> None:
        """
        Playlist info class.

        Parameters:
        :param title: Title of the playlist.
        :param creator: Name of the entity that authored playlist.
        :param annotation: Comment of the playlist.
        :param info: URI of a web page to find out more about playlist.
        :param location: Source URI for the playlist
        :param identifier: Canonical URI for the playlist.
        :param image: URI of image to display in the absence of track image.
        :param license: URI of resource that describes the licence of playlist.
        :param attribution: List of attributed playlists or `Attribution`
        entities.
        :param link: The link elements allows playlist extended without the
        use of XML namespace. List of entities of `xspf.Link`.
        :param meta: Metadata fields of playlist.
        List of entities of `xspf.Meta`.
        :param extension: Extension of non-XSPF XML elements. Must be a list
            of xspf_lib.Extension objects.`
        :param trackList: Ordered list of track elements.

        """
        self.title = title
        self.creator = creator
        self.annotation = annotation
        self.info = info
        self.location = location
        self.identifier = identifier
        self.image = image
        self.date = datetime.now(timezone.utc).astimezone()
        self.license = license
        self.attribution = attribution
        self.link = list(link)
        self.meta = list(meta)
        self.extension = list(extension)
        self.trackList = list(trackList)

    @property
    def data(self):
        """`self.data` member required by `collections.UserList` class."""
        return self.trackList

    def __repr__(self):
        """Return representation `repr.self`."""
        repr = "<Playlist"
        if self.title is not None:
            repr += f' "{self.title}"'
        repr += f': {len(self.trackList)} tracks>'
        return repr

    def to_xml_element(self) -> ET.Element:
        """Return `xml.ElementTree.Element` of the playlist."""
        return _XML_Builder(self).build_playlist()

    @property
    def xml_eltree(self) -> ET.ElementTree:
        """Return `xml.etree.ElementTree.ElementTree` object of playlist."""
        return ET.ElementTree(element=self.to_xml_element())

    def xml_string(self) -> str:
        """Return XML representation of playlist."""
        return ET.tostring(self.to_xml_element(), encoding="UTF-8").decode()

    def write(self, file_or_filename, encoding="utf-8") -> None:
        """Write playlist into file."""
        self.xml_eltree.write(file_or_filename,
                              encoding="UTF-8",
                              method="xml",
                              short_empty_elements=True,
                              xml_declaration=True)

    @classmethod
    def parse(cls, filename) -> 'Playlist':
        """Parse XSPF file into `xspf_lib.Playlist` entity."""
        return cls.parse_from_xml_element(ET.parse(filename).getroot())

    @staticmethod
    def parse_from_xml_element(root) -> 'Playlist':
        return _PlaylistParser(root).parse()

    def _to_attribution(self) -> Attribution:
        return Attribution(location=self.location, identifier=self.identifier)


class _Builder():
    def build_track(self, entity, parameters: Dict):
        self.entity = entity
        self.parameters = parameters

        self.add_location()
        self.add_identifier()
        self.add_title()
        self.add_creator()
        self.add_annotation()
        self.add_info()
        self.add_image()
        self.add_album()
        self.add_trackNum()
        self.add_duration()
        self.add_link()
        self.add_meta()
        self.add_extension()

        return self.entity

    def add_location(self):
        if isinstance(self.parameters['location'], URI):
            self.entity.location = [self.parameters['location']]
        else:
            self.entity.location = self.parameters['location']

    def add_identifier(self):
        if isinstance(self.parameters['identifier'], URI):
            self.entity.identifier = [self.parameters['identifier']]
        else:
            self.entity.identifier = self.parameters['identifier']

    def add_title(self):
        self.add_simple_parameter('title')

    def add_creator(self):
        self.add_simple_parameter('creator')

    def add_annotation(self):
        self.add_simple_parameter('annotation')

    def add_info(self):
        self.add_simple_parameter('info')

    def add_image(self):
        self.add_simple_parameter('image')

    def add_album(self):
        self.add_simple_parameter('album')

    def add_trackNum(self):
        self.add_simple_parameter('trackNum')

    def add_duration(self):
        self.add_simple_parameter('duration')

    def add_link(self):
        self.entity.link = list(self.parameters['link'])

    def add_meta(self):
        self.entity.meta = list(self.parameters['meta'])

    def add_extension(self):
        self.entity.extension = list(self.parameters['extension'])

    def add_simple_parameter(self, parameter_name: str):
        self.entity.__setattr__(parameter_name,
                                self.parameters[parameter_name])


class _XML_Builder:
    def __init__(self, entity):
        self.entity = entity

    def build_track(self):
        self.xml_element = ET.Element('track')

        self.add_locations()
        self.add_identifiers()
        self.add_title()
        self.add_creator()
        self.add_annotation()
        self.add_info()
        self.add_image()
        self.add_album()
        self.add_trackNum()
        self.add_duration()
        self.add_links()
        self.add_metas()
        self.add_extensions()

        return self.xml_element

    def build_playlist(self):
        self.xml_element = ET.Element('playlist', {'version': "1",
                                      'xmlns': NS['xspf']})
        self.add_title()
        self.add_creator()
        self.add_annotation()
        self.add_info()
        self.add_location()
        self.add_identifier()
        self.add_image()
        self.add_date()
        self.add_license()
        self.add_attribution()
        self.add_links()
        self.add_metas()
        self.add_extensions()
        self.add_trackList()

        return self.xml_element

    def add_locations(self):
        if self.entity.location is not None:
            for loc in self.entity.location:
                ET.SubElement(self.xml_element, 'location').text = \
                    str(quote(loc))

    def add_identifiers(self):
        if self.entity.identifier is not None:
            for id in self.entity.identifier:
                ET.SubElement(self.xml_element, 'identifier').text = str(id)

    def add_license(self):
        self.add_simple_subelement('license')

    def add_attribution(self):
        if len(self.entity.attribution) > 0:
            attribution = ET.SubElement(self.xml_element, 'attribution')
            for attr in self.entity.attribution[0:9]:
                if attr.location is not None:
                    ET.SubElement(attribution, 'location').text = attr.location
                if attr.identifier is not None:
                    ET.SubElement(attribution, 'identifier').text = \
                        attr.identifier

    def add_trackList(self):
        ET.SubElement(self.xml_element, 'trackList').extend(
            track.to_xml_element() for track in self.entity.trackList
        )

    def add_title(self):
        self.add_simple_subelement('title')

    def add_creator(self):
        self.add_simple_subelement('creator')

    def add_annotation(self):
        self.add_simple_subelement('annotation')

    def add_info(self):
        self.add_simple_subelement('info')

    def add_image(self):
        self.add_simple_subelement('image')

    def add_album(self):
        self.add_simple_subelement('album')

    def add_trackNum(self):
        self.add_simple_subelement('trackNum')

    def add_duration(self):
        self.add_simple_subelement('duration')

    def add_links(self):
        self.add_iterable_parameter('link')

    def add_metas(self):
        self.add_iterable_parameter('meta')

    def add_extensions(self):
        self.add_iterable_parameter('extension')

    def add_location(self):
        self.add_simple_subelement('location')

    def add_identifier(self):
        self.add_simple_subelement('identifier')

    def add_date(self):
        ET.SubElement(self.xml_element, 'date').text = \
            self.entity.date.isoformat()

    def add_simple_subelement(self, parameter_name: str):
        parameter = getattr(self.entity, parameter_name, None)
        if parameter is not None:
            ET.SubElement(self.xml_element, parameter_name).text = \
                str(parameter)

    def add_iterable_parameter(self, parameter_name: str):
        parameter_iter: iter[XMLAble] = getattr(self.entity, parameter_name)
        self.xml_element.extend(parameter.to_xml_element()
                                for parameter in parameter_iter)


class _Parser():
    def __init__(self, xml_element):
        self.xml_element = xml_element

    # URI checker By RFC 3986
    lowalpha = 'abcdefghijklmnopqrstuvwxyz'
    upalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = lowalpha + upalpha
    digit = '0123456789'
    unreserved = alpha + digit + '-._~'
    gen_delims = ':/?#[]@'
    sub_delims = '!$&\'()*+,;='
    reserved = gen_delims + sub_delims
    quoted = '%'
    uric = reserved + unreserved + quoted

    @staticmethod
    def urify(value):
        value = quoteInvalidChars(value)
        if all(char in _Parser.uric for char in value):
            return value
        else:
            raise ValueError("Only valid URI is acceptable.\n"
                             f"Got `{value}`")

    @staticmethod
    def check_element_nonleaf_content(element) -> None:
        if element.text is not None and \
                not element.text.isspace():
            raise TypeError(f"Element <{element.tag}> nonleaf "
                            "content is not allowed.\n"
                            f"| Got `{element.text}`.")

    def insert_title(self) -> None:
        title = self.get_xml_leaf_parameter_value('title')
        self.insert_parameter_if_not_null('title', title)

    def insert_creator(self) -> None:
        creator = self.get_xml_leaf_parameter_value('creator')
        self.insert_parameter_if_not_null('creator', creator)

    def insert_annotation(self) -> None:
        annotation = self.get_xml_leaf_parameter_value('annotation')
        self.insert_parameter_if_not_null('annotation', annotation)

    def insert_info(self):
        info = self.get_xml_leaf_parameter_uri_value('info')
        self.insert_parameter_if_not_null('info', info)

    def insert_image(self) -> None:
        image = self.get_xml_leaf_parameter_uri_value('image')
        self.insert_parameter_if_not_null('image', image)

    def insert_links(self) -> None:
        self.parsing_entity.link.extend(
            Link.parse_from_xml_element(link) for link in
            self.xml_element.findall("xspf:link", NS))

    def insert_metas(self) -> None:
        self.parsing_entity.meta.extend(
            Meta.parse_from_xml_element(meta) for meta in
            self.xml_element.findall("xspf:meta", NS))

    def insert_extensions(self) -> None:
        self.parsing_entity.extension.extend(
            Extension.parse_from_xml_element(extension) for extension in
            self.xml_element.findall('xspf:extension', NS))

    def insert_parameter_if_not_null(self, parameter_name: str,
                                     parameter_value: Union[str, int]) -> None:
        if parameter_value is not None:
            self.parsing_entity.__setattr__(parameter_name, parameter_value)

    def get_xml_leaf_parameter_value(self, parameter_name: str) -> str:
        return self._get_xml_leaf_parameter_value_with_urify(
            parameter_name,
            need_urify=False)

    def get_xml_leaf_parameter_int_value(self, parameter_name: str) -> str:
        string = self.get_xml_leaf_parameter_value(parameter_name)
        if string is not None:
            return int(string)

    def get_xml_leaf_parameter_uri_value(self, parameter_name: str) -> str:
        return self._get_xml_leaf_parameter_value_with_urify(
            parameter_name,
            need_urify=True)

    def _get_xml_leaf_parameter_value_with_urify(self,
                                                 parameter_name: str,
                                                 need_urify: bool = False) \
            -> str:
        self.check_single_element_in_root(parameter_name)
        parameter = self.xml_element.find("xspf:" + parameter_name, NS)
        if parameter is not None:
            self.__class__.check_inserted_markup(parameter)
            self.__class__.check_forbidden_element_attributes(parameter)
            ret_text = parameter.text
            if need_urify:
                ret_text = self.__class__.urify(ret_text)
            return ret_text

    def check_single_element_in_root(self, element_name: str) -> None:
        if len(self.xml_element.findall("xspf:" + element_name, NS)) > 1:
            raise TypeError(f"Got too many `{element_name}` elements in "
                            "playlist.\n"
                            f"{ET.tostring(self.xml_element)}")

    @staticmethod
    def check_inserted_markup(element) -> None:
        if len(list(element)) > 0:
            raise ValueError("Got nested elements in expected text. "
                             "Probably, this is unexpected HTML "
                             "insertion.\n"
                             f"{ET.tostring(element)}")

    @staticmethod
    def check_forbidden_element_attributes(element) -> None:
        if len(element.attrib) > 0 and \
                element.keys() != \
                ["{http://www.w3.org/XML/1998/namespace}base"]:
            raise TypeError("Element contains forbidden attribute "
                            f"{element.attrib}.\n"
                            f"{ET.tostring(element)}")


class _TrackParser(_Parser):
    def __init__(self, xml_element: ET.Element):
        super().__init__(xml_element)
        self.parsing_entity = Track()

    def parse(self) -> Track:
        self.check_all_track_element()
        self.insert_all_parameters()
        return self.parsing_entity

    def check_all_track_element(self) -> None:
        self.check_root_name_and_namespace()
        self.check_track_nonleaf_content()

    def check_root_name_and_namespace(self) -> None:
        if self.xml_element.tag != ''.join(['{', NS["xspf"], '}track']):
            raise TypeError("Track element not contain 'track' tag ",
                            "or namespace setted wrong",
                            object=self.xml_element)

    def check_track_nonleaf_content(self) -> None:
        self.__class__.check_element_nonleaf_content(self.xml_element)

    def insert_all_parameters(self):
        self.insert_locations()
        self.insert_identifiers()
        self.insert_title()
        self.insert_creator()
        self.insert_annotation()
        self.insert_info()
        self.insert_image()
        self.insert_album()
        self.insert_trackNum()
        self.insert_duration()
        self.insert_links()
        self.insert_metas()
        self.insert_extensions()

    def insert_locations(self) -> None:
        locations = self.xml_element.findall("xspf:location", NS)
        if len(locations) > 0:
            self.parsing_entity.location = [
                urlparse.unquote(self.__class__.urify(location.text.strip()))
                for location in locations]

    def insert_identifiers(self) -> None:
        identifiers = self.xml_element.findall("xspf:identifier", NS)
        if len(identifiers) > 0:
            self.parsing_entity.identifier = [
                urlparse.unquote(self.__class__.urify(identifier.text.strip()))
                for identifier in identifiers]

    def insert_album(self) -> None:
        album = self.get_xml_leaf_parameter_value('album')
        self.insert_parameter_if_not_null('album', album)

    def insert_trackNum(self) -> None:
        trackNum = self.get_xml_leaf_parameter_int_value('trackNum')
        self.insert_parameter_if_not_null('trackNum', trackNum)

    def insert_duration(self) -> None:
        duration = self.get_xml_leaf_parameter_int_value('duration')
        self.insert_parameter_if_not_null('duration', duration)


class _PlaylistParser(_Parser):

    def __init__(self, xml_element: ET.Element):
        super().__init__(xml_element)
        self.parsing_entity = Playlist()

    def parse(self) -> Playlist:
        self.check_all_in_root_element()
        self.insert_all_parameters()
        return self.parsing_entity

    def check_all_in_root_element(self) -> None:
        self.check_namespace_is_exist()
        self.check_for_right_namespace_string()
        self.check_root_tag_name()
        self.check_version_attribute_is_exist()
        self.check_forbidden_root_attributes()
        self.check_value_of_version()
        self.check_root_nonleaf_content()

    def check_namespace_is_exist(self) -> None:
        if not self.xml_element.tag[0] == '{':
            raise TypeError("Playlist namespace attribute is missing.\n"
                            f"{ET.tostring(self.xml_element)}")

    def check_for_right_namespace_string(self) -> None:
        if not self.xml_element.tag.startswith(
                ''.join(['{', NS["xspf"], '}'])):
            wrong_namespace = self.xml_element.tag.split('}')[0].lstrip('{')
            raise ValueError("Namespace is wrong string.\n"
                             f"| Expected `{NS['xspf']}`.\n"
                             f"| Got `{wrong_namespace}`.")

    def check_root_tag_name(self) -> None:
        if self.xml_element.tag != ''.join(['{', NS['xspf'], '}playlist']):
            raise ValueError("Root tag name is not correct.\n"
                             "| Expected: `playlist`.\n"
                             f"| Got: `{self.xml_element.tag.split('}')[1]}`")

    def check_version_attribute_is_exist(self) -> None:
        # Version attribute check.
        if 'version' not in self.xml_element.keys():
            raise TypeError("version attribute of playlist is missing.")

    def check_forbidden_root_attributes(self) -> None:
        root_attribs = self.xml_element.keys()
        if not (root_attribs == ['version'] or root_attribs == [
                'version', '{http://www.w3.org/XML/1998/namespace}base']):
            forbidden_attributes = list(root_attribs)
            try:
                forbidden_attributes.remove('version')
            except ValueError:
                pass
            try:
                forbidden_attributes.remove(
                    '{http://www.w3.org/XML/1998/namespace}base')
            except ValueError:
                pass
            raise TypeError("<playlist> element contains forbidden elements.\n"
                            f"{forbidden_attributes}")

    def check_value_of_version(self) -> None:
        version = int(self.xml_element.get("version"))
        # 0 version not implemented
        if version == 0:
            raise ValueError("XSPF version 0 not maintained, "
                             "switch to version 1.")
        # Another version than 1 not accepted.
        elif version != 1:
            raise ValueError(
                "The 'version' attribute must be 1.\n"
                f"Your playlist version setted to {version}.\n"
                "See http://xspf.org/xspf-v1.html#rfc.section.4.1.1.1.2")

    def check_root_nonleaf_content(self) -> None:
        self.__class__.check_element_nonleaf_content(self.xml_element)

    def insert_all_parameters(self) -> None:
        self.insert_title()
        self.insert_creator()
        self.insert_annotation()
        self.insert_info()
        self.insert_location()
        self.insert_identifier()
        self.insert_image()
        self.insert_license()
        self.insert_date()
        self.insert_attributions()
        self.insert_links()
        self.insert_metas()
        self.insert_extensions()
        self.insert_trackList()

    def insert_location(self) -> None:
        location = self.get_xml_leaf_parameter_uri_value('location')
        self.insert_parameter_if_not_null('location', location)

    def insert_identifier(self) -> None:
        identifier = self.get_xml_leaf_parameter_uri_value('identifier')
        self.insert_parameter_if_not_null('identifier', identifier)

    def insert_license(self) -> None:
        license = self.get_xml_leaf_parameter_uri_value('license')
        self.insert_parameter_if_not_null('license', license)

    def insert_date(self) -> None:
        date_string = self.get_xml_leaf_parameter_value('date')
        if date_string is not None:
            date_string = date_string.strip()
            date_object = datetime.fromisoformat(date_string)
            self.insert_parameter_if_not_null('date', date_object)

    def insert_attributions(self) -> None:
        self.check_single_element_in_root('attribution')
        attribution = self.xml_element.find("xspf:attribution", NS)
        if attribution is not None:
            self.__class__.check_element_nonleaf_content(attribution)
            self.parsing_entity.attribution.extend(
                Attribution().parse_from_xml_element(attr)
                for attr in attribution)

    def insert_trackList(self) -> None:
        self.check_trackList_is_only_one()
        trackList = self.xml_element.find("xspf:trackList", NS)
        self.__class__.check_element_nonleaf_content(trackList)
        self.parsing_entity.trackList.extend(
            Track.parse_from_xml_element(track) for track in trackList)

    def check_trackList_is_only_one(self) -> None:
        self.check_single_element_in_root('trackList')
        trackList = self.xml_element.find("xspf:trackList", NS)
        if trackList is None:
            raise TypeError("trackList element not founded.")
