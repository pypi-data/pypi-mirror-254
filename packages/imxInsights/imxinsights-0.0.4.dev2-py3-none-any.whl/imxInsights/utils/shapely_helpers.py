from __future__ import annotations

from typing import Union

import numpy as np
import pyproj
from shapely.geometry import LineString, Point, Polygon


def gml_point_to_shapely(gml_point_coordinates: str) -> Point:
    """
    Converts a GML point coordinate string to a Shapely Point object.

    Args:
        gml_point_coordinates (str): The GML point coordinate string in the format "(x,y)".

    Returns:
        (Shapely.Point): The Shapely Point object.

    """
    coordinates = [float(x) for x in gml_point_coordinates.replace("(", "").replace(")", "").replace("'", "").replace(" ", "").split(",")]
    return Point(coordinates)


def shapely_point_to_gml(shapely_point: Point):
    """
    Converts a Shapely Point object to a GML point coordinate string.

    Args:
        shapely_point (Point): The Shapely point".

    Returns:
        (str): gml:point string representation.

    """
    if shapely_point.has_z:
        return f"{round(shapely_point.x, 3)},{round(shapely_point.y, 3)},{round(shapely_point.z, 3)}"
    else:
        return f"{round(shapely_point.x, 3)},{round(shapely_point.y, 3)}"


def gml_linestring_to_shapely(gml_linestring_coordinates: str) -> LineString:
    """
    Converts a GML linestring coordinate string to a Shapely LineString object.

    Args:
        gml_linestring_coordinates (str): A string of GML linestring coordinates in "x,y" format separated by spaces.

    Returns:
        (Shapely.LineString): A Shapely LineString object.

    """
    return LineString([tuple(map(float, x.split(","))) for x in gml_linestring_coordinates.split(" ")])


def gml_polygon_to_shapely(gml_linestring_coordinates: str) -> Polygon:
    """
    Converts a GML polygon to a Shapely Polygon object.

    Args:
        gml_linestring_coordinates (str): A string containing the GML coordinates of the polygon.

    Returns:
        (Polygon): A Shapely Polygon object.

    """
    return Polygon([tuple(map(float, x.split(","))) for x in gml_linestring_coordinates.split(" ")])


class ShapelyTransform:
    """A utility class to transform between RD and WGS84 coordinate systems."""

    rd = pyproj.CRS("EPSG:28992")
    wgs = pyproj.CRS("EPSG:4326")
    transformer_to_wgs = pyproj.Transformer.from_crs(rd, wgs)
    transformer_to_rd = pyproj.Transformer.from_crs(wgs, rd)

    @classmethod
    def rd_to_wgs(cls, shapely: Union[Point, LineString, Polygon]) -> Union[Point, LineString, Polygon]:
        """
        Convert a Shapely geometry from Dutch RD (Rijksdriehoekstelsel) coordinates (EPSG:28992) to WGS84 coordinates (EPSG:4326).

        Args:
            shapely (Union[Point, LineString, Polygon]): A Shapely geometry in Dutch RD coordinates.

        Returns:
            (Union[Point, LineString, Polygon]): A Shapely geometry in WGS84 coordinates.

        """
        return cls._convert(shapely, cls.transformer_to_wgs)

    @staticmethod
    def _convert(shapely: Union[Point, LineString, Polygon], transformer: pyproj.Transformer) -> Union[Point, LineString, Polygon]:
        if isinstance(shapely, Point):
            return Point(*reversed(transformer.transform(shapely.x, shapely.y)))

        elif isinstance(shapely, LineString):
            return LineString(zip(*reversed(transformer.transform(*shapely.coords.xy))))

        elif isinstance(shapely, Polygon):
            return LineString(zip(*reversed(transformer.transform(*shapely.exterior.coords.xy))))
        else:
            return shapely


def reverse_line(shapely_polyline: LineString) -> LineString:
    """
    Reverses the order of coordinates in a Shapely LineString object.

    Args:
        shapely_polyline (LineString): The LineString object to reverse.

    Returns:
        (LineString): A new LineString object with the coordinates in reverse order.

    """
    return LineString(list(shapely_polyline.coords)[::-1])


def get_azimuth_from_points(point1: Point, point2: Point) -> float:
    """
    Calculates the azimuth angle between two points.

    Args:
        point1 (Point): The first Point object.
        point2 (Point): The second Point object.

    Returns:
        (float): The azimuth angle in degrees.

    """
    angle = np.arctan2(point2.x - point1.x, point2.y - point1.y)
    return float(np.degrees(angle)) if angle >= 0 else float(np.degrees(angle) + 360)


def check_point_in_area(point_str: str, area: Polygon):
    point_to_test = Point([float(item) for item in point_str.split(",")])
    return point_to_test.within(area)
