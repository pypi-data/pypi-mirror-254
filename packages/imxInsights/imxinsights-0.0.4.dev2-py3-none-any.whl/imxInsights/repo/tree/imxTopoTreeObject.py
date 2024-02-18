from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from lxml import etree as ET


@dataclass
class ImxTopoObject:
    """
    Imx topo value object.

    Args:
        element (ET.Element):
        key (str):

    """

    _element: ET.Element = field(repr=False, hash=False)
    key: str = field(init=False)

    def __post_init__(self) -> None:
        ref = next((v for k, v in self._element.attrib.items() if k.endswith("Ref")), None)
        assert isinstance(ref, str), "ref key should be a string"
        assert len(ref) != 0, "ref key should not be empty"
        self.key = ref

    @property
    def element(self) -> ET.Element:
        return self._element

    @staticmethod
    def from_root_element(start: ET.Element) -> List[ImxTopoObject]:
        micro_nodes: list[ET.Element] = start.findall(".//{*}MicroNode")
        micro_links: list[ET.Element] = start.findall(".//{*}MicroLink")

        lookup = dict[ET.Element, ImxTopoObject]()
        entities: list[ET.Element] = micro_nodes + micro_links
        for entity in entities:
            lookup[entity] = ImxTopoObject(_element=entity)

        return list(lookup.values())
