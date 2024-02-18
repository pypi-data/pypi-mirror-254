from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree as ET

NS_IMSPOOR = "http://www.prorail.nl/IMSpoor"
NS_GML = "http://www.opengis.net/gml"


@dataclass(frozen=True)
class XmlFile:
    """
    Represents an XML file, providing methods for parsing and checking its existence.

    This class allows you to work with XML files by providing a convenient interface for
    parsing and checking the existence of an XML file. It can be used to load and parse
    an XML file, and to determine whether the file exists.

    Args:
        path (Path): The path to the XML file.
        root (ET.ElementTree, optional): An optional pre-parsed XML root element. Default is None.

    Attributes:
        path (Path): The path to the XML file.
        root (ET.ElementTree): The parsed XML root element. It is set to None initially and
            will be parsed when necessary using the `ET.parse` method.

    Raises:
        ValueError: If the provided `path` does not exist or is not a file.

    Note:
        When parsing XML files, this class uses an XMLParser with comments removed to ensure
        that comments are not parsed as nodes. However, please note that comments will be lost
        when saving the XML file.

    Examples:
        >>> xml_path = Path("example.xml")
        >>> xml_file = XmlFile(xml_path)
        >>> xml_file.exists
        True
        >>> xml_file.root  # The XML root element is automatically parsed when accessed.
        <Element 'root' at 0x7f5de6f18d10>

    """

    path: Path
    root: ET.ElementTree = field(kw_only=True, hash=False, repr=False, default=None)
    # tag: str | None = None

    def __post_init__(self) -> None:
        if self.root is not None:
            return

        if not self.exists:
            raise ValueError(f"Invalid path {self.path}")

        # mutcho use of comments for local purposes ET will parse them as nodes so make sure comments are not parsed...
        # when saving xml comments are lost!
        parser = ET.XMLParser(remove_comments=True)
        super().__setattr__("root", ET.parse(self.path, parser))

    @property
    def exists(self) -> bool:
        return self.path.exists() and self.path.is_file()


def trim_tag(tag: ET._Element | str) -> str:
    if isinstance(tag, ET._Element):
        tag = str(tag.tag)
    return tag.split("}")[1] if "}" in tag else tag


def find_base_entity(elem: ET._Element) -> ET._Element:
    while elem is not None and "puic" not in elem.keys():
        elem = elem.getparent()
    if elem is None:
        raise ValueError
    return elem


def find_parent_entity(elem: ET._Element) -> ET._Element | None:
    assert "puic" in elem.keys(), "Element has no puic!"
    try:
        parent = find_base_entity(elem.getparent())
    except ValueError:
        return None

    return parent if trim_tag(parent.tag) != "Project" else None


def find_coordinates(elem: ET._Element) -> list[ET._Element]:
    target = f"{{{NS_GML}}}coordinates"
    if elem.tag == target:
        return [elem]

    matches: list[ET._Element] = elem.findall(f".//{target}")

    # filter out coordinates of child entities
    # assert "puic" in elem.keys(), "Cannot find coordinates of non-entity"
    return [coord for coord in matches if find_base_entity(coord) == elem]


def find_puic(elem: ET._Element) -> str:
    return str(find_base_entity(elem).get("puic"))


def lxml_element_to_dict(node: ET.Element, attributes: object = True, children: object = True) -> dict[str, dict | str | list]:
    """
    Convert lxml.etree node into a dict. adapted from https://gist.github.com/jacobian/795571.

    Args:
        node (ET.Element): the lxml.etree node to convert into a dict
        attributes (Optional[bool]): include the attributes of the node in the resulting dict, defaults to True

    Returns:
        ( dict[str, dict | str | list]): A dictionary representation of the lxml.etree node

    """
    result = dict[str, dict | str | list]()
    if attributes:
        for key, value in node.attrib.items():
            result[f"@{key}"] = value

    if not children:
        return result

    for element in node.iterchildren():
        key = trim_tag(element)

        # Process element as tree element if the inner XML contains non-whitespace content
        if element.text and element.text.strip():
            value = element.text
        else:
            value = lxml_element_to_dict(element)

        if key in result:
            match = result[key]
            if isinstance(match, list):
                match.append(value)
            else:
                result[key] = [match, value]
        else:
            result[key] = value

    return result
