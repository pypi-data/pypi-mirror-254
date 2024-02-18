import pytest
from shapely import LineString, MultiPoint, Point
from shapely.geometry.base import BaseGeometry

from imxInsights import GeoJsonFeature, GeoJsonFeatureCollection


def test_geojson_features_and_feature_collection():
    feature = GeoJsonFeature(geometry_list=[Point(0, 0)])
    feature2 = GeoJsonFeature(geometry_list=[Point(1, 1)])

    assert feature == feature, "feature __eq__ equal failed"
    assert feature != feature2, "feature __eq__ not equal failed"

    assert (
        str(feature) == "<Feature 'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (0.0, 0.0)}>"
    ), "__repr__ representation failed"  # noqa: E501
    feature_collection = GeoJsonFeatureCollection([feature, feature2])
    assert (
        str(feature_collection)
        == "<FeatureCollection 'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:EPSG::4326'}}, 'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (0.0, 0.0)}}, {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (1.0, 1.0)}}]>"  # noqa: E501
    )
    assert feature_collection == feature_collection, "feature collection __eq__ equal failed"
    assert feature_collection != GeoJsonFeatureCollection([feature])
    assert len(GeoJsonFeatureCollection([Point()]).features) == 1, "should handle shapely as well"

    assert len(feature_collection.as_dict()["features"]) == 2, "as dict should contain features"
    assert feature_collection.as_dict() == {
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::4326"}},
        "type": "FeatureCollection",
        "features": [
            {"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": (0.0, 0.0)}},
            {"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": (1.0, 1.0)}},
        ],
    }, "should return dict"  # noqa: E501

    with pytest.raises(ValueError):
        GeoJsonFeature(geometry_list=[None])  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeature(geometry_list=[""])  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeature(geometry_list=[Point()], properties="str")  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeature(geometry_list=[Point()], properties=1.00)  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeature(geometry_list=[Point()], properties=[])  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeatureCollection([feature, ""])  # type: ignore
    with pytest.raises(ValueError):
        GeoJsonFeatureCollection([[Point(), Point()]])  # type: ignore

    point = Point(0, 0)
    point_feature = GeoJsonFeature(geometry_list=[point])
    assert point_feature.properties == {}, "should not have properties"
    assert len(point_feature.geometry_list) == 1, "should contain one geometry object"
    assert point_feature.geometry_list[0] == point, "should be the same geometry"

    point_z_feature = GeoJsonFeature(geometry_list=[Point(2, 2, 10)])
    assert point_z_feature.geometry_list[0].has_z is True, "should have z value"
    assert point_z_feature.as_dict()["geometry"]["coordinates"][2] == 10, "dict should have z value"

    empty_point = GeoJsonFeature(geometry_list=[LineString()])
    assert empty_point.as_dict()["geometry"] is None, "should return a empty geometry"
    empty_list = GeoJsonFeature(geometry_list=[])
    assert empty_list.as_dict()["geometry"] is None, "should return a empty geometry"

    multi_feature = GeoJsonFeature(geometry_list=[MultiPoint([Point(3, 3), Point(6, 6), Point(12, 12), Point(15, 15)])])
    assert multi_feature.as_dict()["geometry"]["type"] == "MultiPoint", "should return mutipoint type"
    assert len(multi_feature.as_dict()["geometry"]["coordinates"]) == 4

    multi_multi_feature = GeoJsonFeature(geometry_list=[Point(3, 3), LineString([[0, 3], [1, 5]])])
    assert multi_multi_feature.as_dict()["geometry"]["type"] == "GeometryCollection", "should return mutipoint type"

    feature_list = [point_feature, point_z_feature, empty_point, multi_feature, multi_multi_feature]
    feature_collection = GeoJsonFeatureCollection(feature_list)
    for item in feature_collection:
        assert item in feature_list, "feature should be in input features"

    for item in feature_collection.geometries_iterator():
        assert isinstance(item, BaseGeometry), "should return a shapely geometry"
