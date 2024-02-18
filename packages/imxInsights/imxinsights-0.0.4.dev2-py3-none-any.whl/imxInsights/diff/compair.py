from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Optional

from shapely import LineString, Point
from shapely.geometry.base import BaseGeometry

from imxInsights.diff.areaStatusEnum import AreaStatusEnum
from imxInsights.diff.change import Change, ChangeList
from imxInsights.diff.diffStatusEnum import DiffStatusEnum
from imxInsights.domain.area.imxProjectArea import ImxProjectArea
from imxInsights.repo.imxRepo import ImxObject, ObjectTree
from imxInsights.utils.log import logger
from imxInsights.utils.shapely_helpers import (
    gml_linestring_to_shapely,
    gml_point_to_shapely,
)


class ImxPropertyCompare:
    @classmethod
    def compare(cls, a: dict[str, str] | None, b: dict[str, str] | None) -> ChangeList:
        """
        Compares two flat dictionaries, detects changes & IMX specific changes (location).

        Args:
            a (Union[dict[str, str], None]): First dictionary to be compared.
            b (Union[dict[str, str], None]): Second dictionary to be compared.

        Returns:
            (ChangeList): A ChangeList object representing the changes between the two dictionaries.

        """
        keys = set(a.keys() if a is not None else []).union(b.keys() if b is not None else [])
        assert len(keys) > 0, "should find at lease 1 key in to compare"
        props = [cls._compare_property(key, a, b) for key in sorted(keys)]

        base_status = DiffStatusEnum.CREATED if a is None else DiffStatusEnum.DELETED if b is None else DiffStatusEnum.NO_CHANGE

        return ChangeList(status=base_status, properties=props)

    @classmethod
    def _compare_property(cls, key: str, a: dict[str, str] | None, b: dict[str, str] | None) -> Change:
        """
        Compares a single key in two dictionaries and returns a Change object representing the changes.

        Args:
            key (str): The key to be compared.
            a (Union[dict[str, str], None]): A dictionary to be compared.
            b (Union[dict[str, str], None]): A dictionary to be compared.

        Returns:
            (Change): A Change object representing the changes between the two values of the key.

        """
        val_a = a[key] if a is not None and key in a else None
        val_b = b[key] if b is not None and key in b else None

        def make_change(status: DiffStatusEnum) -> Change:
            return Change(key=key, status=status, a=val_a, b=val_b)

        if val_a is None:
            return make_change(DiffStatusEnum.CREATED)

        if b is None or key not in b or val_b is None:
            return make_change(DiffStatusEnum.DELETED)

        if val_a == val_b:
            return make_change(DiffStatusEnum.NO_CHANGE)

        if ".coordinates" in key:
            return make_change(cls._compare_gml_coordinates(key, val_a, val_b))

        return make_change(DiffStatusEnum.UPDATED)

    @classmethod
    def _compare_gml_coordinates(cls, key: str, coords_a: str, coords_b: str) -> DiffStatusEnum:
        """
        Compares two sets of coordinates and returns the status of the comparison.

        Args:
            key (str): The key of the coordinates to be compared.
            coords_a (str): The first set of coordinates.
            coords_b (str): The second set of coordinates.

        Returns:
            (DiffStatusEnum): A DiffStatus object representing the status of the comparison.

        """
        assert coords_a is not None and coords_b is not None
        if "Point.coordinates" in key:
            geom_a = gml_point_to_shapely(coords_a)
            geom_b = gml_point_to_shapely(coords_b)
        elif "LineString.coordinates" in key:
            geom_a = gml_linestring_to_shapely(coords_a)
            geom_b = gml_linestring_to_shapely(coords_b)
        else:
            logger.warning(f"Cannot determine if {key} is data upgrade, assuming changed if not exactly equal")
            return DiffStatusEnum.NO_CHANGE if coords_a == coords_b else DiffStatusEnum.UPDATED

        return cls._compare_geometry(geom_a, geom_b)

    @classmethod
    def _compare_geometry(cls, a: BaseGeometry, b: BaseGeometry, tolerance: Optional[float] = 4e-4) -> DiffStatusEnum:
        """
        Compares two geometries.

        Args:
            a (BaseGeometry): The first geometry object to compare.
            b (BaseGeometry): The second geometry object to compare.
            tolerance (Optional[float]): the tolerance level for determining if two geometries are equal, defaults to 4e-4.

        Returns:
            (DiffStatusEnum): The status of the comparison, whether the geometries are updated, not changed, or upgraded.

        """

        def get_values_to_compair(_a: BaseGeometry, _b: BaseGeometry) -> List[List[float], List[float], bool]:
            a_z, b_z = None, None
            z_status = 0
            match (_a.has_z, _b.has_z):
                case (False, False):
                    pass
                    # z_status = 0
                case (True, True):
                    # z_status = 0
                    if isinstance(_a, LineString) and isinstance(_b, LineString):
                        a_z = [item[2] for item in list(_a.coords)]
                        b_z = [item[2] for item in list(_b.coords)]
                    elif isinstance(_a, Point) and isinstance(_b, Point):
                        a_z = _a.z
                        b_z = _b.z
                    else:
                        raise ValueError("Should be same object types")

                case (True, False):
                    z_status = -1
                    if isinstance(_a, LineString):
                        a_z = [item[2] for item in list(_a.coords)]
                    elif isinstance(_a, Point):
                        a_z = _a.z
                    else:
                        raise ValueError("Should be same object types")

                case (False, True):
                    z_status = 1
                    if isinstance(_b, LineString):
                        b_z = [item[2] for item in list(_b.coords)]
                    elif isinstance(_b, Point):
                        b_z = _b.z
                        # b_z = _a.z
                    else:
                        raise ValueError("Should be same object types")

            return [a_z, b_z, z_status]

        def z_in_line_changed(_a_z: List[float], _b_z: List[float]) -> bool:
            for idx, item in enumerate(_a_z):
                if item != _b_z[idx]:
                    return True
            return False

        def z_value_changed(_a: BaseGeometry, _a_z: List[float], _b: BaseGeometry, _b_z: List[float]) -> bool:
            if isinstance(_a, LineString) or isinstance(_b, LineString):
                if len(_a_z) != len(_b_z):
                    return True
                else:
                    if z_in_line_changed(_a_z, _b_z):
                        return True
            if isinstance(_a, Point) or isinstance(_b, Point):
                if _a_z - _b_z != 0:
                    return True
            return False

        # TODO: make loads of local getting complex!

        a_z, b_z, z_status = get_values_to_compair(a, b)

        if a_z is not None and b_z is not None:
            if z_value_changed(a, a_z, b, b_z):
                return DiffStatusEnum.UPDATED

        if a.equals_exact(b, tolerance=tolerance):
            if z_status >= 0:
                return DiffStatusEnum.NO_CHANGE if z_status == 0 else DiffStatusEnum.UPGRADED

        return DiffStatusEnum.UPDATED


@dataclass(frozen=True)
class ImxObjectCompare:
    """
    Represents the comparison of two ImxObjects.

    Args:
        a (ImxObject): The first ImxObject to compare.
        b (ImxObject): The second ImxObject to compare.
        changes (ChangeList): The list of changes between the two objects.

    """

    a: ImxObject | None
    b: ImxObject | None
    changes: ChangeList = field(init=False)

    def __post_init__(self):
        assert self.a is not None or self.b is not None, "Must have at least one object"
        if self.a is not None:
            assert self.a.can_compare(self.b)

        a_props = self.a.properties if self.a is not None else None
        b_props = self.b.properties if self.b is not None else None
        changes = ImxPropertyCompare.compare(a_props, b_props)
        super().__setattr__("changes", changes)

    def __repr__(self) -> str:
        return (
            f"<ImxObjectCompare {self.path} name='{self.name}' puic={self.puic} " f"area_status={self.area_status} diff_status={self.diff_status}/>"
        )

    def __str__(self) -> str:
        parts = [self.path, self.name, str(self.area_status), self.puic]
        return "; ".join((part for part in parts if part is not None))

    @property
    def puic(self) -> str:
        """Returns the puic of the ObjectComparison."""
        return self._any().puic

    @property
    def tag(self) -> str:
        """Returns the tag of the ObjectComparison."""
        return self._any().tag

    @property
    def path(self) -> str:
        """Returns the path of the ObjectComparison."""
        return self._any().path

    @property
    def diff_status(self) -> DiffStatusEnum:
        """Returns the diff status of the ObjectComparison."""
        return self.changes.status

    @property
    def name(self) -> str | None:
        """Returns the Combined name, '<NewName> (<OldName>)' or just the '<Name>' if same."""
        if self.only_one:
            name = self._any().name
            return name if name is not None else None

        assert self.a is not None and self.b is not None
        a = self.a.name
        b = self.b.name
        return f"*{b} {f'({a})' if len(a) > 0 else ''}".rstrip() if a != b else a

    @property
    def area_a(self) -> ImxProjectArea | None:
        """Returns the area of `a`."""
        return self.a.area if self.a is not None else None

    @property
    def area_b(self) -> ImxProjectArea | None:
        """Returns the area of `b`."""
        return self.b.area if self.b is not None else None

    @property
    def area_status(self) -> AreaStatusEnum:
        """Determines the status of the comparison of two ImxObjects based on their areas."""
        if self.area_a is None and self.a is not None or self.area_b is None and self.b is not None:
            return AreaStatusEnum.INDETERMINATE

        elif self.area_a is None and self.area_b is not None:
            return AreaStatusEnum.CREATED

        elif self.area_a is not None and self.area_b is None:
            return AreaStatusEnum.DELETED

        elif self.area_a.name == self.area_b.name:
            return AreaStatusEnum.NO_CHANGE

        elif self.area_a.name != self.area_b.name:
            return AreaStatusEnum.MOVED

        raise ValueError(f"Unknown area combination: A={self.area_a}, B={self.area_b}")

    @property
    def only_one(self) -> bool:
        """Returns a boolean value indicating whether only one object is present."""
        return (self.a is None) ^ (self.b is None)

    def _any(self) -> ImxObject:
        if self.a is not None:
            return self.a

        assert self.b is not None, "Should have a or b"
        return self.b

    @staticmethod
    def object_tree_factory(a: ObjectTree, b: ObjectTree) -> Iterable[ImxObjectCompare]:
        """
        Compares two object trees and returns an iterable of ObjectComparison instances representing the comparison between the two trees.

        Args:
            a (ObjectTree): The second object tree to compare.
            b (ObjectTree): The second object tree to compare.

        Returns:
            (Iterable[ImxObjectCompare]): An iterable of ObjectComparison instances representing the comparison between the two trees.

        """
        all_keys = a.keys.union(b.keys)
        for key in all_keys:
            match_a = a.find(key)
            match_b = b.find(key)
            yield ImxObjectCompare(match_a, match_b)

    @staticmethod
    def imx_object_list_factory(a: List[ImxObject], b: List[ImxObject]) -> Iterable[ImxObjectCompare]:
        """
        Generates `ObjectComparison` instances by comparing two lists of `ImxObject` instances.

        If an `ImxObject` instance is present in both lists, it is compared, otherwise it is compared to `None`.

        Args:
            a (List[ImxObject]): The first list of `ImxObject` instances to compare.
            b (List[ImxObject]): The second list of `ImxObject` instances to compare.

        Returns:
            (Iterable[ImxObjectCompare]): An iterable of `ObjectComparison` instances.

        """
        dict_a = {f"{item.puic}": item for item in a}
        dict_b = {f"{item.puic}": item for item in b}
        for puic, value in dict_a.items():
            if puic in dict_b.keys():
                yield ImxObjectCompare(value, dict_b[puic])
            else:
                yield ImxObjectCompare(value, None)

        for puic, value in dict_b.items():
            if puic not in dict_a.keys():
                yield ImxObjectCompare(value, None)
