from __future__ import annotations

from dataclasses import dataclass, field

from shapely.geometry.base import BaseGeometry

from imxInsights.domain.area.imxProjectArea import ImxProjectArea


@dataclass(frozen=True)
class Area:
    geometry: ImxProjectArea = field(repr=False, hash=False)  # referer to Area BaseGeometry does not typehint.
    name: str | None = field(kw_only=True, default=None)

    def __post_init__(self):
        if self.name is None and hasattr(self.geometry, "name"):
            super().__setattr__("name", self.geometry.name)

    def intersects(self, other: BaseGeometry) -> bool:
        return self.geometry.intersects(other)
