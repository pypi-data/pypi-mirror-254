from dataclasses import dataclass, field
from typing import Optional

from shapely import GeometryCollection, LineString
from shapely.geometry.base import BaseGeometry
from shapelyM import MeasureLineString


@dataclass
class ImxGeometry:
    """
    A class representing an ImxGeometry.

    Args:
        shapely (shapely.BaseGeometry): shapely geometry of the value object.

    Attributes:
        azimuth (Optional[float]): the azimuth (rotation from north in direction east) of a value object, if not present None
        shapelyM (Optional[MeasureLineString]): shapely Measure linestring if shapely object is linestring else None.

    """

    shapely: BaseGeometry = GeometryCollection()
    azimuth: Optional[float] = None
    shapelyM: Optional[MeasureLineString] = field(init=False)

    def __post_init__(self) -> None:
        if isinstance(self.shapely, LineString):
            self.shapelyM = MeasureLineString(list(self.shapely.coords))
        else:
            self.shapelyM = None
