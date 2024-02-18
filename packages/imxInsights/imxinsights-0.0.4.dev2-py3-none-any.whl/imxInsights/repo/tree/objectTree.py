from __future__ import annotations

from collections import defaultdict
from itertools import chain
from typing import Dict, Iterable, List

from lxml import etree as ET

from imxInsights.repo.tree.imxTopoTreeObject import ImxTopoObject
from imxInsights.repo.tree.imxTreeObject import ImxObject
from imxInsights.utils.log import logger
from imxInsights.utils.xml_helpers import NS_IMSPOOR


class ObjectTree:
    """
    Object tree of puic objects and topo objects.

    Args:
        root_element (ET.Element): root element (situation or project situation) to parse.

    """

    def __init__(self, root_element: ET.Element):
        self._root_element = root_element
        self._tree_dict: defaultdict[str, List[ImxObject]] = self._create_tree_dict(ImxObject.lookup_tree_from_root_element(root_element))
        self._update_keys()
        self._topo_dict: defaultdict[str, List[ImxTopoObject]] = self._create_topo_dict(ImxTopoObject.from_root_element(root_element))
        self._link_topo()
        self._check_junction_has_topo()

    def _update_keys(self) -> None:
        self._keys = frozenset[str]((key for key in self._tree_dict.keys()))

    @property
    def keys(self) -> frozenset[str]:
        """Get all keys of value objects in tree."""
        return self._keys

    @property
    def topo_dict(self) -> Dict[str, List[ImxTopoObject]]:
        """Get topo dict corresponding whit value objects in tree."""
        return self._topo_dict

    def objects(self) -> Iterable[ImxObject]:
        """
        Get all value objects in tree.

        Returns:
            (Iterable[ImxObject]): all value objects in tree.

        """
        return chain(*self._tree_dict.values())

    def duplicates(self) -> list[str]:
        """
        Get a list of keys that has duplicated value objects.

        Returns:
            (List[str]): list of keys.
        """
        return [k for (k, v) in self._tree_dict.items() if len(v) > 1]

    def find(self, key: str | ImxObject) -> ImxObject | None:
        """
        Find a value object given the key or the value object itself.

        Args:
            key (str | ImxObject): key or object to find in tree.

        """
        if isinstance(key, ImxObject):
            key = key.puic

        if key not in self._keys:
            return None

        match = self._tree_dict[key]
        assert len(match) == 1, f"KeyError, multiple results for {key}"
        return match[0]

    def _link_topo(self) -> None:
        for topo_object in self._topo_dict.values():
            puic_object = self.find(topo_object[0].key)
            if puic_object is not None:
                puic_object.register_topo_object(topo_object[0])
            else:
                logger.error(f"Topo object {topo_object[0].key} should have a puic object")

    def _check_junction_has_topo(self) -> None:
        for puic_object in self._tree_dict.values():
            parent = puic_object[0].element.getparent()
            if parent.tag == f"{{{NS_IMSPOOR}}}Junctions":
                try:
                    self._topo_dict[puic_object[0].puic]
                except ValueError:
                    logger.error(f"Junction object {puic_object[0].puic} should have a topo object")

    @staticmethod
    def _create_tree_dict(objects: Iterable[ImxObject]) -> defaultdict[str, list[ImxObject]]:
        result = defaultdict[str, list[ImxObject]](list)
        for o in objects:
            result[o.puic].append(o)
        duplicated = [o for o in objects if len(result[o.puic]) != 1]
        assert len(duplicated) == 0, f"KeyError, multiple results for {[item.puic for item in duplicated]}"
        return result

    @staticmethod
    def _create_topo_dict(topo_objects: Iterable[ImxTopoObject]) -> defaultdict[str, list[ImxTopoObject]]:
        result = defaultdict[str, list[ImxTopoObject]](list)
        for o in topo_objects:
            result[o.key].append(o)

        duplicated = [o for o in topo_objects if len(result[o.key]) != 1]
        assert len(duplicated) == 0, f"KeyError, multiple results for {[item.key for item in duplicated]}"
        return result
