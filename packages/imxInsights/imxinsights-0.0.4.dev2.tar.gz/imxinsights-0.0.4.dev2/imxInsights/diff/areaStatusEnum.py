from __future__ import annotations

from enum import Enum


class AreaStatusEnum(Enum):
    """Enum to classify an IMX object based on it's geometry comparison."""

    NO_CHANGE = "NO_CHANGE"
    """Indicates that the object has not changed."""

    CREATED = "CREATED"
    """Indicates that the object has been created."""

    DELETED = "DELETED"
    """Indicates that the object is deleted."""

    MOVED = "MOVED"
    """Indicates that the object is moved from one to a other area."""

    INDETERMINATE = "INDETERMINATE"
    """Indicates that the object cant be classified."""

    def is_created_or_deleted(self):
        """
        Return True if the AreaStatus is CREATED or DELETED, False otherwise.

        Returns:
            (bool): True if the AreaStatus is CREATED or DELETED, False otherwise.
        """
        return self == AreaStatusEnum.CREATED or self == AreaStatusEnum.DELETED
