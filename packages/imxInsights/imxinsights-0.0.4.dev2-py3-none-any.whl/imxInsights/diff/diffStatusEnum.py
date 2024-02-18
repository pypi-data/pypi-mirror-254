from __future__ import annotations

from enum import Enum


class DiffStatusEnum(Enum):
    """Enum of possible change statuses."""

    NOT_APPLICABLE = "NOT_APPLICABLE"
    """The change does not apply."""

    NO_CHANGE = "NO_CHANGE"
    """The change is not applicable."""

    CREATED = "CREATED"
    """The change is created."""

    DELETED = "DELETED"
    """The change is deleted."""

    UPDATED = "UPDATED"
    """The change is updated."""

    UPGRADED = "UPGRADED"
    """The change is upgraded."""

    def is_changed(self) -> bool:
        """
        Returns True if the change is a created, deleted, updated or upgraded change, and False otherwise.

        Returns:
            (bool): True if the change is a created, deleted, updated or upgraded change, and False otherwise.

        """
        return self in {self.CREATED, self.DELETED, self.UPDATED, self.UPGRADED}
