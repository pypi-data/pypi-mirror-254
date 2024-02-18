from __future__ import annotations

from enum import Enum


class ImxSituationsEnum(str, Enum):
    """
    Valid situations in a imx project file.

    Attributes:
        InitialSituation (str): The initial situation in a imx project file.
        NewSituation (str): The new situation in a imx project file.
        Situation (str): A situation in a imx situation file.
    """

    InitialSituation = "InitialSituation"
    NewSituation = "NewSituation"
    Situation = "Situation"


class AreaNameEnum(Enum):
    """
    Valid imx areas in a imx project file.

    Attributes:
        CONTEXT: ContextArea.....
        USER: UserArea.....
        WORK: WorkArea.....
    """

    CONTEXT = "ContextArea"
    USER = "UserArea"
    WORK = "WorkArea"
