from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
from lxml import etree as ET
from shapely import GeometryCollection, LineString, Point
from shapely.geometry.base import BaseGeometry
from shapely.ops import linemerge

from imxInsights.domain.models.imxEnums import AreaNameEnum
from imxInsights.domain.models.imxGeometry import ImxGeometry

# from imxInsights.domain.models.ImxRailConnectionInfo import (
#     RailConnectionInfoLine,
#     RailConnectionInfoPoint,
# )
from imxInsights.domain.models.imxRelation import ImxRelation
from imxInsights.repo.tree.imxTreeObject import ImxObject
from imxInsights.repo.tree.objectTree import ObjectTree
from imxInsights.utils.helpers import hash_sha256
from imxInsights.utils.log import logger
from imxInsights.utils.shapely_geojson import GeoJsonFeature, GeoJsonFeatureCollection
from imxInsights.utils.shapely_helpers import (
    ShapelyTransform,
    gml_linestring_to_shapely,
    gml_point_to_shapely,
    gml_polygon_to_shapely,
    reverse_line,
)
from imxInsights.utils.xml_helpers import (
    NS_GML,
    NS_IMSPOOR,
    XmlFile,
    find_coordinates,
    trim_tag,
)

# from shapelyM import MeasureLineString


class SituationRepo:
    """
    A repository of all imx value objects.

    ***Class is responsible for parsing a IMX situation xml element into value objects.***

    !!! danger "Value objects"
        ***ImxInsights is not scoped to edit an IMX file therefor we cant add or change value objects in the repository.***

    !!! info "Value objects"
        ***Every object with a puic attribute is a value object.*** Some objects do not have a puic attribute but are objects of intrest we can
        specify a custom puic on specific imx types.

        *The custom puic configuration can be found in the custom_puic_config.yaml.*

    !!! info "Value object geometry"
        Value object can have geometry specified in a gml node. If no gml node is present we can try to construct geometry:

        - RailConnection geometry is constructed by From- and ToNode attributes in the MicroLink.
        - TrackFragments will be constructed by from- and toMeasures, this results in LineString geometry.
        - Demarcation marker will be projected and results in (Point) geometry.

    ??? tip "Object path vs object type"
        Some IMX object are sub objects of many IMX objects types, by using path instead of imx types we can get only those of interest.

        As an example: we want to get all switch mechanisms of single switches, if we use the imx type Lock we get all Locks. Instead, use the
        Path SingleSwitch.SwitchMechanism to get only the locks that are sub objects of SingleSwitch.

    Attributes:
        element (ET.Element): Exml element of the situation.
        tree (ObjectTree): the tree containing all value objects.

    """

    def __init__(self, element: ET.Element, xml_file: XmlFile):
        assert element.tag.endswith("Situation"), "Element should be a imx situation"
        self._xml_file = xml_file
        self.imx_version = self._xml_file.root.find("[@imxVersion]").attrib["imxVersion"]
        self.file_path: Path = self._xml_file.path
        self.file_hash: str = hash_sha256(self._xml_file.path)
        self._element: ET.Element = element
        self.situation_type: str = trim_tag(self.element.tag)
        self._tree: ObjectTree = ObjectTree(self._element)
        self._link_reffed_objects()
        self._parse_geometry()
        self._construct_rail_connections_geometry()
        self._construct_track_fragment_geometry()
        self._construct_demarcation_markers()
        self._link_rail_connection_info()
        self._register_children()

    @property
    def reference_date(self) -> str:
        """
        Returns the external project reference as given in the project metadata, *read only property*.

        !!! Info
            The reference date is the date that the data is valid, it could be historic or feature situation.

        """
        return str(self._element.get("referenceDate"))

    @property
    def perspective_date(self) -> str:
        """
        Returns the perspective date as given in the situation metadata, *read only property*.

        !!! info
            The perspective date is the date the imx file is created and can be used to determinate if the data baseline is still up to date.

        """
        return str(self._element.get("perspectiveDate"))

    @property
    def element(self) -> ET.Element:
        return self._element

    @property
    def tree(self) -> ObjectTree:
        return self._tree

    def _parse_geometry(self):
        # todo: add parse azimuth as property
        for entity in self._tree.objects():
            location_node = entity.element.findall(f"{{{NS_IMSPOOR}}}Location")
            if len(location_node) == 0:
                entity.geometry = ImxGeometry(GeometryCollection())
            else:
                geographic_location = location_node[0].find(f"{{{NS_IMSPOOR}}}GeographicLocation")
                assert len(location_node) == 1, "main object should not have multiple locations"
                coordinates_element = location_node[0].findall(f".//{{{NS_GML}}}coordinates")
                coordinates = find_coordinates(coordinates_element[0])
                geometry = self._parse_coordinates(coordinates[0])
                azimuth = geographic_location.get("azimuth")
                if azimuth is not None:
                    azimuth = float(azimuth)
                entity.geometry = ImxGeometry(geometry, azimuth=azimuth)

    @staticmethod
    def _parse_coordinates(coordinates: ET.Element) -> BaseGeometry:
        assert coordinates.tag.endswith("coordinates"), "Please provide <gml:coordinates/> element"
        parent_tag = trim_tag(coordinates.getparent().tag)
        match parent_tag:
            case "Point":
                return gml_point_to_shapely(coordinates.text)
            case "LineString":
                return gml_linestring_to_shapely(coordinates.text)
            case "LinearRing":
                return gml_polygon_to_shapely(coordinates.text)
            case _:
                raise ValueError("Cannot parse coordinates for element")

    def _construct_rail_connections_geometry(self) -> None:
        rail_connections = self.get_by_types(["RailConnection"])
        for rail_connection in rail_connections:
            if rail_connection.puic == "07e61000-dc0c-4ff7-97b1-2201b37d6e8e":
                print()

            if "trackRef" in rail_connection.element.attrib:
                track_ref = rail_connection.element.attrib["trackRef"]
            else:
                track_ref = None

            if "passageRefs" in rail_connection.element.attrib:
                passage_refs = rail_connection.element.attrib["passageRefs"].split(" ")
            else:
                passage_refs = []

            if len(passage_refs) == 0:
                passage_refs = rail_connection.element.findall(".//{*}PassageRefs")
                if len(passage_refs) == 0:
                    passage_refs = []
                else:
                    if passage_refs[0].text is None:
                        passage_refs = []
                    elif " " in passage_refs[0].text:
                        passage_refs = passage_refs[0].text.split(" ")
                    else:
                        passage_refs = [passage_refs[0].text]

            geometries = []
            if len(passage_refs) != 0:
                for passage_ref in passage_refs:
                    passage_obj = self.tree.find(passage_ref)
                    if passage_obj is None:
                        raise ValueError(f"RailConnection {rail_connection.puic}: passageRef {passage_ref} not present in dataset")
                    geometries.append(passage_obj.shapely)

            if track_ref is not None:
                track_obj = self.tree.find(track_ref)
                if track_obj is None:
                    raise ValueError(f"RailConnection {rail_connection.puic}: trackRef {track_ref} not present in dataset")
                geometries.append(track_obj.shapely)

            line_geometry = linemerge(geometries)
            # todo: make it accept bad constructed geometry....?
            #  - seems z is not issue on merging line string.... z is only along the ride...
            assert isinstance(
                line_geometry, LineString
            ), f"RailConnection {rail_connection.puic} constructed geometry should be a single polyline geometry"

            logger.info(f'RailConnection {rail_connection.puic} geometry constructed from track: {track_ref} and passages:{", ".join(passage_refs)}')

            if rail_connection.topo_object is not None:
                from_node_point = self.tree.find(rail_connection.topo_object.element.findall(".//{*}FromMicroNode")[0].attrib["nodeRef"])
                if from_node_point is not None:
                    from_node_point = from_node_point.shapely

                to_node_point = self.tree.find(rail_connection.topo_object.element.findall(".//{*}ToMicroNode")[0].attrib["nodeRef"])
                if to_node_point is not None:
                    to_node_point = to_node_point.shapely

            first_coord_distance_from_from_node = Point(line_geometry.coords[0]).distance(from_node_point)
            first_coord_distance_from_to_node = Point(line_geometry.coords[0]).distance(to_node_point)

            if first_coord_distance_from_to_node < first_coord_distance_from_from_node:
                logger.debug(f'RailConnection {rail_connection.puic} "FromNode" seems to be on end of the polyline: reversed geometry')
                line_geometry = reverse_line(line_geometry)

            rail_connection.geometry = ImxGeometry(line_geometry)

    def _construct_track_fragment_geometry(self):
        for item in self.get_all():
            if item.track_fragments is not None:
                for rail_info in item.track_fragments.rail_infos:
                    if hasattr(rail_info, "from_measure") and hasattr(rail_info, "to_measure"):
                        rail_con = self.tree.find(rail_info.ref)

                        if not rail_con:
                            logger.error(f"{item.tag} {item.puic} doest not have valid railRef {rail_info.ref} cant create geometry")

                        elif rail_info.from_measure == rail_info.to_measure:
                            logger.warning(
                                f"{item.tag} {item.puic} doest not have valid TrackFragments (same from and to) railRef {rail_info.ref} cant create geometry"  # noqa: E501
                            )

                        else:
                            if rail_info.from_measure < rail_info.to_measure:
                                projection = rail_con.geometry.shapelyM.cut_profile(rail_info.from_measure, rail_info.to_measure)
                            else:
                                projection = rail_con.geometry.shapelyM.cut_profile(rail_info.to_measure, rail_info.from_measure)

                            if not projection.result:
                                logger.error(f"{item.tag} {item.puic} doest not have valid line cut result, cant create geometry")
                            else:
                                rail_info.geometry = projection.result.shapely
                    else:
                        logger.warning(f"{item.tag} {item.puic} doest not have valid TrackFragments railRef {rail_info.ref} cant create geometry")

    def _construct_demarcation_markers(self):
        for item in self.get_all():
            if item.demarcation_markers is not None:
                for rail_info in item.demarcation_markers.rail_infos:
                    if hasattr(rail_info, "at_measure"):
                        rail_con = self.tree.find(rail_info.ref)
                        projection = rail_con.geometry.shapely.interpolate(rail_info.at_measure)
                        rail_info.geometry = projection
                    else:
                        logger.warning(f"{item.tag} {item.puic} doest not have valid DemarcationMarker cant create geometry")

    def _link_reffed_objects(self) -> None:
        def _check_and_warn(_imx_object, _attrib, _puic, _found_object):
            if _found_object is None:
                logger.warning(f"{_imx_object.tag} {_imx_object.puic}: {_attrib} {_puic} not present in dataset.")

        def has_puic_ancestor(_element, _root, _parent_map):
            if "puic" in _element.attrib and _element is not _root:
                return True
            parent = _parent_map.get(_element)
            while parent is not None and parent is not _root:
                if "puic" in parent.attrib:
                    return True
                parent = _parent_map.get(parent)
            return False

        def _append_relation(_puic, _imx_object, _attrib):
            found_object = self.tree.find(_puic)
            _check_and_warn(_imx_object, _attrib, _puic, found_object)
            _imx_object.reffed_objects.objects.append(ImxRelation(_attrib, _puic, found_object))

        for imx_object in self._tree.objects():
            parent_map = {c: p for p in imx_object.element.iter() for c in p}
            elements = [elem for elem in imx_object.element.iter() if not has_puic_ancestor(elem, imx_object.element, parent_map)]

            for element in elements:
                for attrib in element.attrib:
                    if attrib[-3:] == "Ref":
                        puic = element.attrib[attrib]
                        _append_relation(puic, imx_object, attrib)

                    if attrib[-4:] == "Refs":
                        for puic in element.attrib[attrib].split(" "):
                            _append_relation(puic, imx_object, attrib)

                for node in element:
                    if node.tag.endswith("Ref"):
                        attrib = ET.QName(node.tag).localname
                        puic = node.text
                        _append_relation(puic, imx_object, attrib)

                    if node.tag.endswith("Refs"):
                        if node.text is not None:
                            for puic in node.text.split(" "):
                                attrib = ET.QName(node.tag).localname
                                _append_relation(puic, imx_object, attrib)

            count_of_invalid_relations = 0

            for imx_ref_relation in imx_object.reffed_objects.objects:
                if imx_ref_relation.reffed_object is None:
                    count_of_invalid_relations += 1

            if count_of_invalid_relations != 0:
                imx_object.reffed_objects.has_invalid_relations = True

    def _link_rail_connection_info(self):
        for imx_object in self._tree.objects():
            if imx_object.rail_connection_infos:
                for item in imx_object.rail_connection_infos:
                    found_object = self.tree.find(item.ref)
                    if found_object:
                        item.present_in_dataset = True

                        # if isinstance(item, RailConnectionInfoPoint):
                        #     item._projection = MeasureLineString(found_object.shapely.coords).\
                        #         project(imx_object.shapely, imx_object.geometry.azimuth)
                        #
                        # elif isinstance(item, RailConnectionInfoLine):
                        #     rail_con = MeasureLineString(found_object.shapely.coords)
                        #     if item.from_measure < item.to_measure:
                        #         item._projection = rail_con.cut_profile(item.from_measure, item.to_measure)
                        #     else:
                        #         item._projection = rail_con.cut_profile(item.to_measure, item.from_measure)

                    else:
                        item.present_in_dataset = False
                        logger.warning(f"RailConnection with puic {item.ref} not present in dataset.")
            # print()

    def _register_children(self):
        for imx_object in self._tree.objects():
            children = imx_object.element.findall(".//*[@puic]")
            if children is not None:
                imx_object.children = [self._tree.find(child.get("puic")) for child in children]

    def get_all(self, areas: Optional[List[AreaNameEnum]] = None) -> List[ImxObject]:
        """
        Get all value objects in repository.

        Returns:
            (List[ImxObject]): List of all value objects.
        """
        all_objects = list(self._tree.objects())
        if areas is None:
            return all_objects
        else:
            return [item for item in all_objects if item.area is None or item.area.name in areas]

    def get_by_puic(self, puic: str) -> Optional[ImxObject]:
        """
        Get value objects by PUIC.

        Returns:
            (ImxObject): Value object.
        """
        return self._tree.find(puic)

    def get_all_types(self) -> List[str]:
        """
        Get all value object types present in repository.

        Returns:
            (List[str]): List of value objects types.
        """
        return list(set([item.tag for item in self.get_all()]))

    def get_by_types(self, object_types: List[str]) -> List[ImxObject]:
        """
        Get all value object of a specific type.

        Returns:
            (List[ImxObject]): List of all value objects.
        """
        return [item[0] for item in self.tree._tree_dict.values() if item[0].tag in object_types]

    def get_all_paths(self):
        """
        Get all value object paths present in repository.

        Returns:
            (List[str]): List of value objects paths.
        """
        return list(set([item.path for item in self.get_all()]))

    def get_by_paths(self, object_paths: List[str]) -> List[ImxObject]:
        """
        Get all value object of a specific path.

        Returns:
            (List[ImxObject]): List of all value objects.
        """
        return [item[0] for item in self.tree._tree_dict.values() if item[0].path in object_paths]

    def get_pandas_df(self, object_type_or_path: Optional[str] = None, puic_as_index=True) -> pd.DataFrame:
        """
        Get Pandas dataframe of one value object type or limited view of all objects.

        When using a object type or path all properties will be flatted, when getting a dataframe of all object most attributes will be stripped
            except some metadata. In both cases it will include parent puic, path and classified area.

        Args:
            object_type_or_path: path or imx type to get df off
            puic_as_index: if true puic value will lbe the index

        Returns:
            (pd.DataFrame): pandas dataframe of the object properties
        """
        if object_type_or_path is None:
            props_in_overview = [
                "Location.GeographicLocation.@accuracy",
                "Location.GeographicLocation.@dataAcquisitionMethod",
                "Metadata.@isInService",
                "Metadata.@lifeCycleStatus",
                "Metadata.@source",
            ]
            records = []
            for item in self.get_all():
                props = {key: value for key, value in item.properties.items() if key in props_in_overview}
                records.append(
                    {
                        "puic": item.puic,
                        "area": item.area.name if item.area is not None else "No Area classified",
                        "path": item.path,
                        "parent": item.parent.puic if item.parent is not None else "",
                        "name": item.name,
                    }
                    | props
                )

        else:
            if "." in object_type_or_path:
                value_objects = self.get_by_paths([object_type_or_path])
            else:
                value_objects = self.get_by_types([object_type_or_path])

            records = []
            for item in value_objects:
                records.append(
                    {
                        "puic": item.puic,
                        "area": item.area.name if item.area is not None else "No Area classified",
                        "path": item.path,
                        "parent": item.parent.puic if item.parent is not None else "",
                        "name": item.name,
                    }
                    | item.properties
                )

        df = pd.DataFrame.from_records(records)
        if len(records) != 0 and puic_as_index:
            df["index"] = df["puic"]
            df.set_index("index", inplace=True)
            df = df.fillna("")
        return df

    def get_pandas_df_dict(self, key_based_on_type: bool = False) -> Dict[str, pd.DataFrame]:
        """
        Get a dictionary of Pandas dataframe of all type bases on keys or path.

        Args:
            key_based_on_type: if true key based on type, else on path

        Returns: dictionary of pandas dataframe

        """
        out_dict = {}
        if key_based_on_type:
            for imx_type in self.get_all_types():
                out_dict[imx_type] = self.get_pandas_df(imx_type)

        for imx_path in self.get_all_paths():
            out_dict[imx_path] = self.get_pandas_df(imx_path)

        return out_dict

    def get_geojson(self, object_type_or_path: str, in_rd: bool = False) -> GeoJsonFeatureCollection:
        """
        Get a geojson feature collection of certain type or path.

        Args:
            object_type_or_path: object type or path
            in_rd: if True returns coordinates in RD else WGS84

        Return:
             GeojsonFeatureCollection

        """
        if "." in object_type_or_path:
            records = self.get_by_paths([object_type_or_path])
        else:
            records = self.get_by_types([object_type_or_path])

        if in_rd:
            features = [GeoJsonFeature(properties=record.properties, geometry_list=[record.shapely]) for record in records]
        else:
            features = [
                GeoJsonFeature(properties=record.properties, geometry_list=[ShapelyTransform.rd_to_wgs(record.shapely)]) for record in records
            ]

        feature_collection = GeoJsonFeatureCollection(features)
        return feature_collection

    def get_geojson_dict(self, key_based_on_type: bool = False, in_rd: bool = False) -> Dict[str, GeoJsonFeatureCollection]:
        """
        Get a dictionary of geojson feature collection of all types or paths.

        Args:
            key_based_on_type:
            in_rd: if True returns coordinates in RD else WGS84

        Returns:
             Dict of geojson feature collections.
        """
        out_dict = {}
        if key_based_on_type:
            for imx_type in self.get_all_types():
                out_dict[imx_type] = self.get_geojson(imx_type, in_rd)

        for imx_path in self.get_all_paths():
            out_dict[imx_path] = self.get_geojson(imx_path, in_rd)

        return out_dict
