from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class ImxReffedObjects:
    """A dataclass representing a collection of ImxRelation objects, object is iterable."""

    objects: List[ImxRelation] = field(default_factory=list)
    has_invalid_relations: bool = False

    def __iter__(self):
        for related_object in self.objects:
            yield related_object

    def __repr__(self):
        return f"<{self.__class__.__name__} {len(self.objects)} has_invalid_relations={self.has_invalid_relations}>"


@dataclass
class ImxRelation:
    """A data class representing a relationship between two objects."""

    type: str
    key: str
    reffed_object: Any
    present_in_dataset: bool = True

    def __post_init__(self):
        if self.reffed_object is None:
            self.present_in_dataset = False
