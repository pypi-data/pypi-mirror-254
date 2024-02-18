from pathlib import Path
from typing import Any

import pandas as pd
import pytest
from shapely import GeometryCollection, LineString, Point

from imxInsights import AreaStatusEnum, GeoJsonFeatureCollection, ImxSituationsEnum
from imxInsights.diff.imxDiff import ImxDiff


def test_diff_area_status_enums():
    for item in [AreaStatusEnum[item] for item in ["DELETED", "CREATED"]]:
        assert item.is_created_or_deleted() is True

    for item in [AreaStatusEnum[item] for item in ["NO_CHANGE", "MOVED", "INDETERMINATE"]]:
        assert item.is_created_or_deleted() is not True


@pytest.mark.slow
def test_imx_parse_project_v124(imx_v124_project_instance):
    imx = imx_v124_project_instance
    assert imx.imx_version == "1.2.4", "imx version should be 1.2.4"


@pytest.mark.slow
def test_imx_parse_project_v500(imx_v500_project_instance):
    imx = imx_v500_project_instance
    assert imx.imx_version == "5.0.0", "imx version should be 5.0.0"


def _population_excel(imx):
    imx.generate_population_excel("tester.xlsx", ImxSituationsEnum.InitialSituation)
    file_path = Path("tester.xlsx")
    assert file_path.exists(), "file should exist"
    file_path.unlink()


@pytest.mark.slow
def test_population_excel_imx_v124(imx_v124_project_instance):
    _population_excel(imx_v124_project_instance)


@pytest.mark.slow
def test_population_excel_imx_v500(imx_v500_project_instance):
    _population_excel(imx_v500_project_instance)


def _geojson_export(imx):
    signals_geojson = imx.project.initial_situation.get_geojson(object_type_or_path="Signal")
    assert isinstance(signals_geojson, GeoJsonFeatureCollection), "should return feature collection"

    geojson_dict = imx.project.initial_situation.get_geojson_dict()
    assert isinstance(geojson_dict, dict), "should return dict"
    for key, value in geojson_dict.items():
        assert isinstance(value, GeoJsonFeatureCollection), f"{key}, should contain a dataframe"


@pytest.mark.slow
def test_geojson_export_imx_v124(imx_v124_project_instance):
    _geojson_export(imx_v124_project_instance)


@pytest.mark.slow
def test_geojson_export_imx_v500(imx_v500_project_instance):
    _geojson_export(imx_v500_project_instance)


def _diff_by_object_type(diff):
    signals_geojson_diff = diff.as_geojson(object_type_or_path="Signal")
    assert isinstance(signals_geojson_diff, GeoJsonFeatureCollection), "should return feature collection"


def _diff_geojson_dict(diff):
    geojson_dict_diff = diff.generate_geojson_dict()
    assert isinstance(geojson_dict_diff, dict), "should return dict"


def _diff_pandas_dict(diff):
    dict_of_df_of_all_types = diff.pandas_dataframe_dict()
    assert isinstance(dict_of_df_of_all_types, dict), "should return dict"


def _check_geometry_columns(df_signals: pd.DataFrame, geometry_type: Any):
    assert "geometry_a" in list(df_signals.columns), "Should have a a_geometry column"
    for item in df_signals["geometry_a"]:
        assert item == "" or isinstance(item, geometry_type)
    assert "geometry_b" in list(df_signals.columns), "Should have a b_geometry column"
    for item in df_signals["geometry_b"]:
        assert item == "" or isinstance(item, geometry_type)


def _diff_pandas_gml_geometry(diff):
    df = diff.pandas_dataframe("Signal", geometry=True)
    assert isinstance(df, pd.DataFrame), "should pd.DataFrame"
    _check_geometry_columns(df, Point)

    df = diff.pandas_dataframe("Track", geometry=True)
    assert isinstance(df, pd.DataFrame), "should pd.DataFrame"
    _check_geometry_columns(df, LineString)


def _diff_pandas_linked_geometry(diff):
    df_micro_nodes = diff.pandas_dataframe("MicroNode", geometry=False)
    assert isinstance(df_micro_nodes, pd.DataFrame), "should pd.DataFrame"
    _check_geometry_columns(df_micro_nodes, GeometryCollection)


def _diff_pandas_constructed_geometry(diff):
    df_rail_con = diff.pandas_dataframe("RailConnection", geometry=True)
    assert isinstance(df_rail_con, pd.DataFrame), "should pd.DataFrame"
    _check_geometry_columns(df_rail_con, LineString)


@pytest.mark.slow
def test_diff_imx_v124(imx_v124_project_instance):
    diff = ImxDiff(imx_v124_project_instance.project.initial_situation, imx_v124_project_instance.project.new_situation)
    _diff_by_object_type(diff)
    _diff_geojson_dict(diff)
    _diff_pandas_dict(diff)
    _diff_pandas_gml_geometry(diff)
    _diff_pandas_linked_geometry(diff)
    _diff_pandas_constructed_geometry(diff)


@pytest.mark.slow
def test_diff_imx_v500(imx_v500_project_instance):
    diff = ImxDiff(imx_v500_project_instance.project.initial_situation, imx_v500_project_instance.project.new_situation)
    _diff_by_object_type(diff)
    _diff_geojson_dict(diff)
    _diff_pandas_dict(diff)
    _diff_pandas_gml_geometry(diff)
    _diff_pandas_linked_geometry(diff)
    _diff_pandas_constructed_geometry(diff)
