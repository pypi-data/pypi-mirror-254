from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from lxml import etree as ET

from imxInsights.utils.log import logger


class PuicKeyTypeEnum(str, Enum):
    """
    An enumeration of the different types of keys.

    Attributes:
        NORMAL_KEY: Puic attribute is used as key.
        DUMMY_KEY: Puic is a dummy value, generated new UUID4 to use as key.
        GENERATED_KEY: If no puic is given, just generated one.
        CONSTRUCTED_KEY: Does not have a puic but is relevant, we use attributes to construct a unique key.
    """

    NORMAL_KEY = "normal"
    DUMMY_KEY = "dummy_puic"
    GENERATED_KEY = "generated_key"
    CONSTRUCTED_KEY = "constructed_key"


@dataclass
class PuicConstructedByAttribute:
    """
    PuicConstructedByAttribute class that is used if a IMX object does not have a puic, it uses a set of attributes to construct an uniek key.

    Args:
        object_type (str): File path of the IMX file.
        ref_key (str): File path of the IMX file.
        attributes_to_make_unique (List[str]): File path of the IMX file.

    """

    object_type: str
    ref_key: str
    attributes_to_make_unique: List[str]

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} "
            f"ref:{self.ref_key} "
            f"attributes_to_make_unique:{' '.join(self.attributes_to_make_unique)} "
            f"object_type:{self.object_type}>"
        )


@dataclass(frozen=True)
class ImxPuic:
    """
    Unique Identifier Code, using puic if attribute is present else generate or construct a unique key.

    Args:
        valid_uuid4 (bool): returns True if the PUIC value is a valid uuid4 else False.
        puic_type (PuicConstructedByAttribute): returns the type of PUIC key.
        constructed_by_attribute (Optional[PuicConstructedByAttribute]): object that constructed PUIC by attributes.

    Raises:
        ValueError: If PUIC value is None when puic is constructed from attributes.
        AssertionError: If `constructed_puic` is None and `element` is None or `puic` attribute is not present.
        AssertionError: If `constructed_puic` is not None and `element` is None or any of the attributes in
            `constructed_puic.attributes_to_make_unique` are not present.

    """

    _puic: Optional[str | uuid.UUID] = field(default=None)
    valid_uuid4: bool = field(default=False)
    puic_type: PuicKeyTypeEnum = field(default=PuicKeyTypeEnum.NORMAL_KEY)
    constructed_by_attribute: Optional[PuicConstructedByAttribute] = field(default=None)

    def __post_init__(self):
        if self.constructed_by_attribute is not None:
            if self._puic is None:
                raise ValueError("puic value should be given when puic is constructed from attributes")
            super().__setattr__("puic_type", PuicKeyTypeEnum.CONSTRUCTED_KEY)

        if self._puic in ["00000000-0000-4000-aaad-000000000000"]:
            super().__setattr__("_puic", str(uuid.uuid4()))
            super().__setattr__("puic_type", PuicKeyTypeEnum.DUMMY_KEY)
            logger.warning(f"Dummy puic, created new puic {self._puic}")

        elif self._puic is None and self.puic_type != PuicKeyTypeEnum.CONSTRUCTED_KEY:
            super().__setattr__("_puic", str(uuid.uuid4()))
            super().__setattr__("puic_type", PuicKeyTypeEnum.GENERATED_KEY)
            logger.info(f"No Puic: create constructed key: {self._puic}")

        if isinstance(self._puic, str) and self.puic_type != PuicKeyTypeEnum.CONSTRUCTED_KEY:
            super().__setattr__("_puic", uuid.UUID(self.puic))
            super().__setattr__("valid_uuid4", True)

    def __str__(self) -> str:
        return str(self._puic)

    def __repr__(self) -> str:
        if self.puic_type == PuicKeyTypeEnum.CONSTRUCTED_KEY:
            constructed = "constructed_puic_by_attribute:" + self.constructed_by_attribute.__repr__()
        else:
            constructed = ""
        return f"<{self.__class__.__name__} {self._puic} " f"puic_type:{self.puic_type.value} " f"{constructed}>"

    @property
    def puic(self) -> str:
        """Returns the string representation of the PUIC."""
        return str(self._puic)

    @staticmethod
    def from_element(element: ET.Element, constructed_puic: Optional[PuicConstructedByAttribute] = None) -> ImxPuic:
        """Creates an instance of ImxPuic from an XML element.

        Args:
            element (bool):
            constructed_puic (Optional[PuicConstructedByAttribute]):

        Raises:
            AssertionError: If `constructed_puic` is None and `element` is None or `puic` attribute is not present.
            AssertionError: If `constructed_puic` is not None and `element` is None or any of the attributes in
                `constructed_puic.attributes_to_make_unique` are not present.

        Returns:
            (ImxPuic):

        """
        if constructed_puic is None:
            assert element is not None and "puic" in element.keys()
            return ImxPuic(element.get("puic"))

        for key in constructed_puic.attributes_to_make_unique:
            assert element is not None and key in element.keys()

        if len(constructed_puic.attributes_to_make_unique) == 0:
            custom_puic = f"{element.get(constructed_puic.ref_key)}_" + f"{constructed_puic.object_type}"
        else:
            custom_puic = f"{element.get(constructed_puic.ref_key)}_" + "".join(
                [element.get(key) for key in constructed_puic.attributes_to_make_unique]
            )

        return ImxPuic(custom_puic, constructed_by_attribute=constructed_puic)
