from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from imxInsights.diff.diffStatusEnum import DiffStatusEnum


@dataclass
class ChangeList:
    """
    A list of changes representing the difference between two objects.

    Args:
        status (DiffStatusEnum): A value from the `DiffStatus` enum indicating the status of the parent object.
        properties (list[Change]): A list of `Change` objects representing the changes made to the parent object's properties.

    """

    status: DiffStatusEnum
    properties: list[Change]

    def __post_init__(self):
        self._ensure_status_matches_props()

    def _ensure_status_matches_props(self):
        statuses = set((change.status for change in self.properties))
        if self.status == DiffStatusEnum.CREATED and statuses != {DiffStatusEnum.CREATED}:
            raise ValueError("Object is created but not all properties are")  # pragma: no cover
        if self.status == DiffStatusEnum.DELETED and statuses != {DiffStatusEnum.DELETED}:
            raise ValueError("Object is deleted but not all properties are")  # pragma: no cover
        if self.status not in [DiffStatusEnum.CREATED, DiffStatusEnum.DELETED] and any(status.is_changed() for status in statuses):
            self.status = DiffStatusEnum.UPDATED

    def to_dict(self, strip_attribute: bool = False, compact: Optional[bool] = True) -> dict[str, str]:
        """
        Returns a dictionary representing the `ChangeList` object.

        The keys of the dictionary are the property names, and the values are the changes.

        Args:
          strip_attribute: Whether to strip "@" from the beginning of the property names.
          compact: Boolean to return compact or old and new values.

        Returns:
          dict: A dictionary representing the `ChangeList` object.
        """
        # if compact:
        return {ChangeList._key_name(change.key, strip_attribute): change.display_compact for change in self.properties}
        # else:
        #     return {ChangeList._key_name(change.key, strip_attribute): {"old": change.a, "new": change.b} for change in self.props}

    @staticmethod
    def _key_name(key: str, strip_attribute: bool) -> str:
        if strip_attribute:
            return key.replace("@", "")
        return key


@dataclass
class Change:
    """
    Represents a change in a property of an object.

    Args:
        key (str): The property key.
        status (DiffStatusEnum): The status of the change.
        a (Optional[str]): The old value of the property.
        b (Optional[str]): The new value of the property.

    """

    key: str
    status: DiffStatusEnum
    a: Optional[str]
    b: Optional[str]

    def __post_init__(self):
        if self.status == DiffStatusEnum.NOT_APPLICABLE:
            raise ValueError(f"Cannot instantiate a Change with {self.status}")  # pragma: no cover

    def __repr__(self) -> str:
        return self.display_compact

    def __str__(self) -> str:
        return self.display_compact

    def has_location(self) -> bool:
        """
        Determines if the property key is a location by checking if it matches certain gml patterns.

        Returns:
            bool: True if the property key is a location, False otherwise.
        """
        return True if self.key in [".coordinates", ".Point.", ".LineString."] else False
        # return ".coordinates" in self.key or ".Point." in self.key or ".LineString." in self.key

    @property
    def display_compact(self) -> str:
        """
        Returns a formatted string representing the change.

        The format depends on the status of the change.

        - If the status is DiffStatusEnum.NO_CHANGE, it returns the new value.
        - If the status is DiffStatusEnum.CREATED, it returns the new value with a "++" prefix.
        - If the status is DiffStatusEnum.DELETED, it returns the old value with a "--" prefix.
        - If the status is DiffStatusEnum.UPDATED, it returns the old value followed by "->" and the new value.
        - If the status is DiffStatusEnum.UPGRADED, it returns the old value followed by "=>" and the new value.
        - If the status is DiffStatusEnum.NOT_APPLICABLE, it returns "N/A".

        Returns:
            str: A formatted string representing the change.
        """
        if self.key == "puic":
            return self.b if self.b is not None else f"{self.a}"

        match self.status.value:
            case DiffStatusEnum.NO_CHANGE.value:
                return f"{self.b}"
            case DiffStatusEnum.CREATED.value:
                return f"++ {self.b}"
            case DiffStatusEnum.DELETED.value:
                return f"-- {self.a}"
            case DiffStatusEnum.UPDATED.value:
                return f"{self.a} -> {self.b}"
            case DiffStatusEnum.UPGRADED.value:
                return f"{self.a} => {self.b}"
            case DiffStatusEnum.NOT_APPLICABLE.value:
                return "N/A"
        return "N/A"
