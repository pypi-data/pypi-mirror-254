from __future__ import annotations

import json
from typing import IO, Dict, List, cast

from shapely.geometry import LineString, Point, Polygon, mapping
from shapely.geometry.base import BaseGeometry

# todo make own pipy module and make dependency


class GeoJsonFeature:
    """
    A geojson feature build from one or more shapely geometries and a set of properties as a dictionary.

    It's possible to use multi geometry types, but most applications wont support geojson multigeometry types, same as nested property dictionaries.

    Args:
        geometry_list: list of shapley geometry
        properties: dictionary of properties of the feature

    """

    def __init__(self, geometry_list: List[BaseGeometry], properties: Dict | None = None) -> None:
        self.geometry_list: List[BaseGeometry] = geometry_list
        self.properties: Dict | None = properties

    @property
    def geometry_list(self):
        return self.__geometry_list

    @geometry_list.setter
    def geometry_list(self, geometry_list: List[BaseGeometry]):
        for item in geometry_list:
            if not isinstance(item, BaseGeometry):
                raise ValueError("geometry entry must be a shapely geometry.")
        self.__geometry_list = geometry_list

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if properties is None:
            self._properties = {}
        elif isinstance(properties, dict):
            self._properties = properties
        else:
            raise ValueError("properties must be a dict.")

    def _get_geo_interface(self):
        geometries = []

        if len(self.geometry_list) == 0:
            geometries = None

        elif len(self.geometry_list) > 1:
            for item in self.geometry_list:
                geometries.append(item.__geo_interface__)
        else:
            if self.geometry_list[0].is_empty:
                geometries = None
            else:
                geometries = self.geometry_list[0].__geo_interface__

        return geometries

    @property
    def __geo_interface__(self):
        geometry = self._get_geo_interface()
        geo_json_type = "Feature"

        if len(self.__geometry_list) == 0:
            geometry = {"geometry": None}
        elif len(self.__geometry_list) == 1:
            geometry = {"geometry": geometry}
        elif len(self.__geometry_list) > 1:
            geometry = {"geometry": {"type": "GeometryCollection", "geometries": geometry}}

        return {
            "type": geo_json_type,
            "properties": self.properties,
        } | geometry

    def __eq__(self, other):
        return self.__geo_interface__ == other.__geo_interface__

    def __repr__(self):
        return f"<Feature {str(self.__geo_interface__)[1:-1]}>"

    def as_dict(self):
        return self.__geo_interface__


class GeoJsonFeatureCollection:
    """
    GeoJson FeatureCollection stores geojson Features.

    Args:
        geojson_features (list[GeoJsonFeature]):

    """

    def __init__(self, geojson_features: List[GeoJsonFeature | BaseGeometry]):
        # todo: make crs init parameter
        # todo: validate if features are in crs range
        self.features: List[GeoJsonFeature] = geojson_features
        self.crs: Dict = {
            "crs": {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:EPSG::4326"
                    # RD: http://www.opengis.net/def/crs/EPSG/0/28992 # RD/NAP: EPSG:7415 # CRS84: 4326
                },
            }
        }

    @property
    def features(self) -> list[GeoJsonFeature]:
        """Get all features."""
        return self._features

    @features.setter
    def features(self, objects: List[GeoJsonFeature | BaseGeometry]):
        all_are_features = all(isinstance(feature, GeoJsonFeature) for feature in objects)
        if all_are_features:
            self._features: List[GeoJsonFeature] = objects
        else:
            for item in objects:
                if not isinstance(item, BaseGeometry):
                    raise ValueError("features can be either a Feature or shapely geometry.")
            self._features = [GeoJsonFeature(cast(List[BaseGeometry], [geometry])) for geometry in objects]

    def __iter__(self):
        return iter(self.features)

    def geometries_iterator(self):
        for feature in self.features:
            if len(feature.geometry_list) > 1:
                for geometry in feature.geometry_list:
                    yield geometry
            else:
                yield feature.geometry_list[0]

    @property
    def __geo_interface__(self):
        return {
            "crs": self.crs["crs"],
            "type": "FeatureCollection",
            "features": [feature.__geo_interface__ for feature in self.features],
        }

    def __eq__(self, other):
        return self.__geo_interface__ == other.__geo_interface__

    def __repr__(self):
        return f"<FeatureCollection {str(self.__geo_interface__)[1:-1]}>"

    def as_dict(self):
        return self.__geo_interface__

    def as_string(self) -> str:
        """Returns geojson string."""
        return dumps(self)


class ShapleyGeojsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Point, LineString, Polygon)):
            return obj.wkt
        return json.JSONEncoder.default(self, obj)


def dump(feature_collection: GeoJsonFeatureCollection, file_path: IO[str], *args, **kwargs) -> None:
    """
    Dump FeatureCollection to file.

    Args:
        feature_collection: FeatureCollection
        file_path: output file path
    """
    json.dump(mapping(feature_collection), file_path, cls=ShapleyGeojsonEncoder, *args, **kwargs)


def dumps(feature_collection: GeoJsonFeatureCollection, *args, **kwargs) -> str:
    """
    Dump FeatureCollection to string.

    Args:
        feature_collection (GeoJsonFeatureCollection): FeatureCollection

    Returns:
        (str)): geojson string representation of the FeatureCollection.
    """
    return json.dumps(mapping(feature_collection), cls=ShapleyGeojsonEncoder, *args, **kwargs)
