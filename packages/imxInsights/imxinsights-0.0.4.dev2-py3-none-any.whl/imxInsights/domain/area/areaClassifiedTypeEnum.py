from enum import Enum


class AreaClassifiedTypeEnum(str, Enum):
    """
    Possible classification types.

    Attributes:
        OBJECT_GEOMETRY (str): ....
        CONSTRUCTED_GEOMETRY (str): ....
        TRACK_FRAGMENTS_AND_DEMARCATION_MARKERS (str): ....
        RELATED_OBJECTS (str): ....
        FAILED (str): ....
    """

    OBJECT_GEOMETRY = "objects gml:geometry is used"
    CONSTRUCTED_GEOMETRY = "using constructed geometry."
    TRACK_FRAGMENTS_AND_DEMARCATION_MARKERS = "track fragments and demarcation markers"
    RELATED_OBJECTS = "related objects geometry"
    FAILED = "common strategy failed because of reasons"
