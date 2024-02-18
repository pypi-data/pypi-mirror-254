from __future__ import annotations

from typing import List, Optional, Tuple

from lxml import etree as ET
from shapely.geometry.base import BaseGeometry

from imxInsights.domain.area.area import Area
from imxInsights.domain.area.areaClassifiedTypeEnum import AreaClassifiedTypeEnum
from imxInsights.domain.area.imxProjectArea import ImxProjectArea
from imxInsights.repo.imxRepo import ImxObject
from imxInsights.utils.log import logger
from imxInsights.utils.shapely_helpers import (
    gml_linestring_to_shapely,
    gml_point_to_shapely,
    gml_polygon_to_shapely,
)
from imxInsights.utils.xml_helpers import find_coordinates, find_puic, trim_tag


class AreaClassifier:
    """
    ImxProjectArea classifier to determinate the widest area that a object is in.

    Args:
        areas (List[Area]): list of all area that can be used to classify

    """

    def __init__(self, areas: List[ImxProjectArea]):
        self._areas: List[Area] = [Area(area) for area in areas]
        if len(self._areas) == 0:
            raise ValueError("No user/work/context or other area passed to classifier!")  # pragma: no cover

    def determine_area(self, geometry: BaseGeometry, element: Optional[ET.Element] = None) -> Area:
        for area in self._areas:
            if area.intersects(geometry):
                return area

        outside = find_puic(element) if element is not None else "<unknown>"
        logger.warning(f"Object {outside} lies outside context area, added to context area")

        return area

    def categorize_element(self, imx_object: ImxObject) -> Tuple[Optional[Area], Optional[AreaClassifiedTypeEnum]]:
        """
        Determines which of the areas intersect with this element.

        If multiple coordinates are found inside this entity which do not belong to any other entity (e.g. mathematical point on switch),
        all areas are computed and the widest is chosen.

        Classify strategie:
         - use gml geometry or constructed railConnection geometry
         - use track fragments and demarcation markers
         - use reffed objects

        Args:
            imx_object (ImxObject): imx value object to categorize

        Returns:
            Tuple[(Optional[Area],  (Optional[str]]): widest area

        Todo:
         - move logic to set geometry to imx object, including AreaClassifiedTypeEnum as a generic enum

        """
        areas = list[Area]()
        classify_type: Optional[AreaClassifiedTypeEnum] = None
        coordinates = find_coordinates(imx_object.element)
        if imx_object.element.tag == "{http://www.prorail.nl/IMSpoor}RailConnection":
            classify_type = AreaClassifiedTypeEnum.CONSTRUCTED_GEOMETRY
            areas.append(self.determine_area(geometry=imx_object.shapely))

        elif len(coordinates) > 0:
            classify_type = AreaClassifiedTypeEnum.OBJECT_GEOMETRY
            for coords in coordinates:
                geometry = self._parse_coordinates(coords)
                areas.append(self.determine_area(geometry=geometry, element=coords))

        else:
            if imx_object.track_fragments is not None:
                classify_type = AreaClassifiedTypeEnum.TRACK_FRAGMENTS_AND_DEMARCATION_MARKERS
                for track_fragment in imx_object.track_fragments.rail_infos:
                    areas.append(self.determine_area(geometry=track_fragment.geometry))

            if imx_object.demarcation_markers is not None:
                classify_type = AreaClassifiedTypeEnum.TRACK_FRAGMENTS_AND_DEMARCATION_MARKERS
                for demarcation_marker in imx_object.demarcation_markers.rail_infos:
                    areas.append(self.determine_area(geometry=demarcation_marker.geometry))

        if len(areas) == 0:
            if imx_object.reffed_objects.has_invalid_relations:
                classify_type = AreaClassifiedTypeEnum.FAILED
                logger.warning(f"{imx_object.tag} {imx_object.puic} ")
                return None, classify_type

            if len(imx_object.reffed_objects.objects) > 0:
                classify_type = AreaClassifiedTypeEnum.RELATED_OBJECTS
                for ref_relation in imx_object.reffed_objects.objects:
                    if ref_relation.present_in_dataset and not ref_relation.reffed_object.shapely.is_empty:
                        areas.append(self.determine_area(geometry=ref_relation.reffed_object.shapely))

        if len(areas) == 0:
            logger.warning(f"{imx_object.tag} {imx_object.puic} can't classify area.")
            return None, classify_type

        elif len(areas) == 1 or len(set(areas)) == 1:
            return areas[0], classify_type

        widest_area = self._areas[max(map(self._areas.index, areas))]
        return widest_area, classify_type

    @staticmethod
    def _parse_coordinates(coordinates: ET.Element) -> BaseGeometry:
        assert coordinates.tag.endswith("coordinates"), "xml element does not have <gml:coordinates/>"
        parent_tag = trim_tag(coordinates.getparent().tag)
        match parent_tag:
            case "Point":
                return gml_point_to_shapely(coordinates.text)
            case "LineString":
                return gml_linestring_to_shapely(coordinates.text)
            case "LinearRing":
                return gml_polygon_to_shapely(coordinates.text)
            case _:  # pragma: no cover
                raise ValueError("Cannot parse coordinates for element")
