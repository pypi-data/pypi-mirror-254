from __future__ import annotations

import warnings

# from pathlib import Path
from typing import Iterable, List, Optional

from lxml import etree as ET
from shapely import GeometryCollection
from shapely.geometry.base import BaseGeometry

from imxInsights.domain.area.areaClassifiedTypeEnum import AreaClassifiedTypeEnum
from imxInsights.domain.area.imxProjectArea import ImxProjectArea
from imxInsights.domain.models.imxGeometry import ImxGeometry
from imxInsights.domain.models.imxMetadata import ImxObjectMetadata
from imxInsights.domain.models.imxPuic import ImxPuic, PuicConstructedByAttribute
from imxInsights.domain.models.ImxRailConnectionInfo import RailConnectionInfos
from imxInsights.domain.models.imxRelation import ImxReffedObjects
from imxInsights.repo.tree.imxTopoTreeObject import ImxTopoObject
from imxInsights.utils.helpers import flatten_dict, get_file_path, yaml_load
from imxInsights.utils.xml_helpers import (
    find_parent_entity,
    lxml_element_to_dict,
    trim_tag,
)


class ImxObject:
    """
    Imx value object.

    Every imx object of interest is parsed as a value object.

    Args:
        element (ET.Element):
        parent (Optional[ET.Element]):
        constructed_puic (Optional[PuicConstructedByAttribute]):

    Attributes:
        metadata (ImxObjectMetadata): contains value object metadata.
        geometry (ImxGeometry): contains geometry of value object

        rail_connection_infos (Optional[RailConnectionInfos]): contains all railConnectionInfo objects in value object.
        track_fragments (Optional[RailConnectionInfos]): contains all railConnectionInfo objects of the track fragments in value object.
        demarcation_markers (Optional[RailConnectionInfos]): contains all railConnectionInfo objects of the demarcation markers in value object.

        reffed_objects (ImxReffedObjects): reffed objects wrapper.
        children (List[ImxObject]): child value objects.
        topo_object (ImxTopoObject): corresponding topo object.
        area (Optional[ImxProjectArea]): classified area set by AreaClassifier.
        area_classify_type (AreaClassifiedTypeEnum): methode used to classify area.

    """

    def __init__(
        self,
        element: ET.Element,
        parent: Optional[ET.Element] = None,
        constructed_puic: Optional[PuicConstructedByAttribute] = None,
    ):
        self._element: ET.Element = element

        self.parent: Optional[ImxObject] = parent
        if constructed_puic is not None:
            self._puic: ImxPuic = ImxPuic.from_element(self._element, constructed_puic)
        else:
            self._puic = ImxPuic.from_element(self._element)

        self.properties: dict[str, str] = flatten_dict(lxml_element_to_dict(self._element))
        self.metadata = ImxObjectMetadata(self.element)
        self.geometry: Optional[ImxGeometry] = None
        self.rail_connection_infos: Optional[RailConnectionInfos] = RailConnectionInfos.from_element(self.element, "RailConnectionInfo")

        self.track_fragments: Optional[RailConnectionInfos] = RailConnectionInfos.from_element(self.element, "TrackFragment")
        self.demarcation_markers: Optional[RailConnectionInfos] = RailConnectionInfos.from_element(self.element, "DemarcationMarker")

        self.children = List[ImxObject]
        self.reffed_objects: ImxReffedObjects = ImxReffedObjects()
        self.topo_object: Optional[ImxTopoObject] = None

        self.area: Optional[ImxProjectArea] = None
        self.area_classify_type: Optional[AreaClassifiedTypeEnum] = None

    def __repr__(self) -> str:
        return f"<ImxObject {self.path} puic={self.puic} name='{self.name}'/>"

    @property
    def element(self) -> ET.Element:
        return self._element

    @property
    def tag(self) -> str:
        """Returns the ImxObject type of the value objectm (same as xml tag), *read only property*."""
        return trim_tag(self._element.tag)

    @property
    def path(self) -> str:
        """Returns the Object path of the value object, *read only property*."""
        tags = [parent.tag for parent in self._parents_generator()]
        tags.reverse()
        tags.append(self.tag)
        return ".".join(tags)

    @property
    def puic(self) -> str:
        """Returns the Puic or constructed puic of the value object, *read only property*."""
        return str(self._puic)

    @property
    def name(self) -> str:
        """Returns the name of the value obejct if present else empty string, *read only property*."""
        return str(self._element.get("name")) if "name" in self._element.keys() else ""

    @property
    def shapely(self) -> BaseGeometry:
        """Returns the Shapely object that represent the main geometry of the value object, *read only property*."""
        if self.geometry is not None:
            return self.geometry.shapely
        return GeometryCollection()

    def _parents_generator(self) -> Iterable[ImxObject]:
        parent = self.parent
        while True:
            if parent is None:
                break
            yield parent
            parent = parent.parent

    def register_topo_object(self, topo_object: ImxTopoObject):
        """
        Guard and register topology objects on imx object.

        Warning:
            ImxInsights repo is responsible for registering topo objects, this methode should not be used manually.

        Args:
            topo_object (ImxTopoObject):

        Raises:
            ValueError: If puic and topo key not same.

        """
        if topo_object.key == self.puic:
            self.topo_object = topo_object
        else:
            raise ValueError("topo object should have same key as value object")

    def can_compare(self, other: ImxObject | None) -> bool:
        """
        Checks if object can be compared whit other object, it should if it has the same puic and same object type.

        Args:
            other (ImxObject):

        Returns:
            (bool): True if can compair else False.
        """
        if other is None:
            return True

        if other.puic != self.puic:
            return False

        if other.path != self.path:
            warnings.warn(f"Cant to compare {self.path} with {other.path}, tags do not match")
            return False

        return True

    @staticmethod
    def lookup_tree_from_root_element(start: ET.Element) -> list[ImxObject]:
        """
        Factory method to initialize ImxObject lookup tree from xml root element.

        Methode generates a tree of objects given a start element by finding all objects with a puic attribute, or those specified by custom key.

        Args:
            start (ET.Element):

        """
        imx_key = "@puic"
        lookup = dict[ET.Element, ImxObject]()
        entities: list[ET.Element] = start.findall(f".//*[{imx_key}]")

        version: str = start.getroottree().getroot().attrib["imxVersion"]

        # config_file_path = f"{Path(__file__).parent.parent.parent}\\custom_puic_config.yaml"
        config_file_path = get_file_path(__file__, "../../custom_puic_config.yaml")

        custom_puic_config = yaml_load(config_file_path)
        if version == "1.2.4":
            custom_puic_config = custom_puic_config["v124"]
        elif version == "5.0.0":
            custom_puic_config = custom_puic_config["v500"]

        for entity in entities:
            parent = find_parent_entity(entity)
            if parent is not None:
                assert parent in lookup, "Expected parent in lookup"
                parent = lookup[parent]
            assert entity not in lookup
            lookup[entity] = ImxObject(parent=parent, element=entity)

        custom_attribute_puics: List[PuicConstructedByAttribute] = [
            PuicConstructedByAttribute(object_type, values[0], values[1]) for object_type, values in custom_puic_config.items()
        ]

        for custom_puic in custom_attribute_puics:
            objects_with_special_key: list[ET.Element] = start.findall(".//{*}" + custom_puic.object_type)
            for entity in objects_with_special_key:
                assert entity not in lookup
                lookup[entity] = ImxObject(parent=None, element=entity, constructed_puic=custom_puic)

        return list(lookup.values())
