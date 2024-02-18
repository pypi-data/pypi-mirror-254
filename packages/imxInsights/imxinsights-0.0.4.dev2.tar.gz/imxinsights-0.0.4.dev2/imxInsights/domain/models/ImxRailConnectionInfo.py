from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from lxml import etree as ET
from shapely import GeometryCollection
from shapely.geometry.base import BaseGeometry
from shapelyM.measureLineString import MeasureProfile


@dataclass
class RailConnectionInfos:
    """
    Dataclass to list to list all RailConnectionInfo nodes of a value object.

    Args:
        rail_infos (List[RailConnectionInfoPoint | RailConnectionInfoLine | RailConnectionInfo]): list of all railConnectionInfo's.

    """

    rail_infos: List[RailConnectionInfoPoint | RailConnectionInfoLine | RailConnectionInfo] = field(default_factory=list)

    @staticmethod
    def from_element(element: ET.Element, object_type: str) -> Optional[RailConnectionInfos]:
        """Rail connection info factory."""
        rail_connection_infos_elements = element.findall(f".//{{*}}{object_type}")
        if len(rail_connection_infos_elements) == 0:
            return None

        _out = RailConnectionInfos()
        for rail_connection_info_element in rail_connection_infos_elements:
            ref = rail_connection_info_element.get("railConnectionRef")
            at_measure = rail_connection_info_element.get("atMeasure")
            from_measure = rail_connection_info_element.get("fromMeasure")
            to_measure = rail_connection_info_element.get("toMeasure")
            direction = rail_connection_info_element.get("direction")

            if ref and at_measure and direction:
                _out.rail_infos.append(RailConnectionInfoPoint(ref, float(at_measure), direction))
            elif ref and from_measure and to_measure:
                _out.rail_infos.append(RailConnectionInfoLine(ref, float(from_measure), float(to_measure), direction))
            else:
                _out.rail_infos.append(RailConnectionInfo(ref))

        return _out

    def __iter__(self):
        for rail_info in self.rail_infos:
            yield rail_info

    def get_geometry_collection(self):
        return GeometryCollection([item.geometry for item in self.rail_infos])

    # todo: make methode to check if invalid relations


@dataclass
class RailConnectionInfo:
    """
    RailConnectionInfo base object.

    Geometry and project will be set by repo.

    Args:
        ref (str): unique key (puic) to railConnection
        projection (Optional[BaseGeometry]): project if point else None.

    """

    ref: str
    present_in_dataset: bool = field(init=False, default=True)
    geometry: Optional[BaseGeometry] = field(init=False, default=None)
    _projection: Optional[MeasureProfile] = field(init=False, default="Not Implemented")


@dataclass
class RailConnectionInfoPoint(RailConnectionInfo):
    """
    RailConnectionInfo Point extension.

    Args:
        at_measure (float): at measure along railConnection.
        direction (): direction along railConnection.
    """

    at_measure: float
    direction: str
    at_measure_3d: Optional[float] = field(init=False, default=None)

    # todo: create projection property, set "point on track" and calculate 3d_measure
    # todo: create side_of_track property


@dataclass
class RailConnectionInfoLine(RailConnectionInfo):
    """
    RailConnectionInfo Line extension.

    A to measure can be lower than a from measure and vice verse.

    Args:
        from_measure (float): from measure along railConnection.
        to_measure (float): from measure along railConnection.
        direction (): direction along railConnection.
    """

    from_measure: float
    to_measure: float
    direction: str

    # todo: create geometry property, set line
