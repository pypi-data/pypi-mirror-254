from __future__ import annotations

from dataclasses import InitVar, dataclass, field

from shapely import Polygon
from shapely.geometry.base import BaseGeometry

from imxInsights.utils.shapely_helpers import gml_polygon_to_shapely


@dataclass(frozen=True)
class ImxProjectArea:
    """
    IMX project areas does have a name and coordinates, those coordinates will be parsed to a polygon.

    The touches and intersects methods use the polygon attribute of the object to check whether it touches or intersects with the Polygon
      object of the other ImxProjectArea object. The Polygon object can also be directly passed as an argument.

    !!! info "Every area has his own mutation regiem, below some context about ImxProjectAres."

        - A Imx project has a geographic scope this is the UserArea, objects within this area dont have a mutation limitation.
        - Object within the UserArea could have a interact whit a object outsidethe UserArea, those object define the WorkArea and do
          have some mutation limitations.
        - Object within the WorkArea could have relations whit object outside the WorkArea, those objects define the ContextArea and cant be changed.

    Args:
        name (str): The name of the area.
        gml_coordinates (str): The GML coordinates of the area.
        polygon (Polygon): The Shapely Polygon object representing the area.
        coordinates (InitVar[tuple[tuple[int | float, ...], ...]]): The coordinates of the area as a tuple of tuples.

    Todo:
        Use enum for project area name
    """

    name: str
    gml_coordinates: InitVar[str]
    polygon: Polygon = field(repr=False, hash=False, default=None)
    coordinates: InitVar[tuple[tuple[int | float, ...], ...]] = None

    def __post_init__(self, gml_coordinates: str, coordinates: tuple[tuple[int | float, ...], ...]):
        if self.polygon is not None:
            return  # pragma: no cover

        poly = gml_polygon_to_shapely(gml_coordinates) if gml_coordinates is not None else Polygon(coordinates) if coordinates is not None else None
        super().__setattr__("polygon", poly)

    def touches(self, area: ImxProjectArea | BaseGeometry) -> bool:
        """
        Checks if the area touches another area.

        Args:
            area (ImxProjectArea | shapley.BaseGeometry): The other area to check, could be a shapely.Polygon.

        Returns:
            (bool): True if the area touches the other area, False otherwise.
        """
        other = area.polygon if isinstance(area, ImxProjectArea) else area
        return bool(self.polygon.touches(other))

    def intersects(self, area: ImxProjectArea | BaseGeometry) -> bool:
        """
        Checks if the area intersects with another area.

        Args:
            area (ImxProjectArea | shapley.BaseGeometry): The other area to check, could be a shapely.Polygon.

        Returns:
            (bool): True if the area intersects with the other area, False otherwise.

        """
        other = area.polygon if isinstance(area, ImxProjectArea) else area
        return bool(self.polygon.intersects(other))
