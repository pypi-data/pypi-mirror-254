from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
from lxml import etree as ET

from imxInsights.domain.area.imxProjectArea import ImxProjectArea
from imxInsights.utils.log import logger


class ProjectNaiadeRemarks:
    """
    Project remarks contains some Naiade configuration information.

    Info:
       - only Naiade Remarks are supported.

    """

    def __init__(self, elem: ET.Element):
        self._element = elem
        self._imx_remarks = self._get_remarks_dict()

    def _get_remarks_dict(self):
        try:
            imx_remarks = self._element.text.split(",")
            imx_remarks = dict([item.replace("'", "").split(":") for item in imx_remarks])
            imx_remarks = {x.strip().replace(" ", ""): v.strip() for x, v in imx_remarks.items()}
            return imx_remarks
        except Exception as e:  # pragma: no cover
            logger.warning(f"Metadata remarks not conform naiade format, will not be parsed. ({e})")
            return {}

    @property
    def application_version(self) -> str:
        """Returns the Naiade application version used when exporting, *read only property*."""
        if self._imx_remarks != {}:
            return str(self._imx_remarks["Applicationversion"])
        else:
            return "None"

    @property
    def environment(self) -> str:
        """Returns the Naiade environment used when exporting, *read only property*."""
        if self._imx_remarks != {}:
            return str(self._imx_remarks["Environment"])
        else:
            return "None"

    @property
    def project_type(self) -> str:
        """Returns the project type used when exporting, *read only property*."""
        if self._imx_remarks != {}:
            return str(self._imx_remarks["Projecttype"])
        else:
            return "None"

    @property
    def xsd(self) -> str:
        """Returns the xsd version used when exporting, *read only property*."""
        if self._imx_remarks != {}:
            return str(self._imx_remarks["XSD"])
        else:
            return "None"

    @property
    def validation_profile(self) -> str:
        """Returns the Naiade validation profile used when exporting, *read only property*."""
        if self._imx_remarks != {}:
            return str(self._imx_remarks["ValidationProfile"])
        else:
            return "None"


class SituationMetadata:
    """Situation metadata contains some information of the IMX data."""

    def __init__(self, elem: ET.Element):
        self._element: ET.Element = elem

    @property
    def reference_date(self) -> str:
        """
        Returns the external project reference as given in the project metadata, *read only property*.

        ***The reference date is the date that the data is valid, it could be historic or feature situation.***

        """
        return str(self._element.get("ReferenceDate"))

    @property
    def perspective_date(self) -> str:
        """
        Returns the perspective date as given in the situation metadata, *read only property*.

        *** The perspective date is the date the imx file is created and can be used to determinate if the data baseline is still up to date.***

        """
        return str(self._element.get("PerspectiveDate"))


class ProjectMetadata:
    """
    Project metadata contains some information of the IMX project.

    Attributes:
        user_area (ImxProjectArea): The imx user area.
        work_area (ImxProjectArea): The imx work area.
        context_area (ImxProjectArea): The imx context area.

    """

    def __init__(self, elem: ET.Element):
        self._element: ET.Element = elem
        self.user_area = self._areas_factory("UserArea")
        self.work_area = self._areas_factory("WorkArea")
        self.context_area = self._areas_factory("ContextArea")

    @property
    def project_areas(self) -> List[ImxProjectArea]:
        """Returns all imx project areas, *read only property*."""
        return [self.user_area, self.work_area, self.context_area]

    @property
    def external_project_reference(self) -> str:
        """Returns the external project reference as given in the project metadata, *read only property*."""
        return str(self._element.get("externalProjectReference"))

    @property
    def project_name(self) -> str:
        """Returns the project name as given in the project metadata, *read only property*."""
        return str(self._element.get("projectName"))

    @property
    def project_type(self) -> str:
        """Returns the project type as given in the project metadata, *read only property*."""
        return str(self._element.get("projectType"))

    @property
    def created_date(self) -> str:
        """
        Returns the created date as given in the project metadata, *read only property*.

        ***The created date is the date the file is mutated and saved and can be used to check if latest version.***

        """
        return str(self._element.get("createdDate"))

    @property
    def planned_delivery_date(self) -> str:
        """
        Returns the planned delivery date as given in the project metadata, *read only property*.

        ***The planned delivery date is the date the project will be live, in Dutch: indienststelling or IDS datum***

        """
        return str(self._element.get("plannedDeliveryDate"))

    @property
    def changeable_types(self) -> List[str]:
        """Returns a list of the changeable types given in the project metadata, *read only property*."""
        return str(self._element.get("ChangeableTypes")).split(",")

    def _areas_factory(self, area_name: str) -> ImxProjectArea:
        coordinates = self._element.find(f".//{{*}}{area_name}//{{*}}coordinates")
        if coordinates is None:
            raise ValueError(f"No project metadata in file {self._element.docinfo.URL}!")  # pragma: no cover

        return ImxProjectArea(name=area_name, gml_coordinates=coordinates.text)


@dataclass
class ImxObjectMetadata:
    """Stores metadata for an IMX object."""

    _element: ET.Element = field(repr=False)
    _metadata_node = False
    _location_node = False

    def __post_init__(self) -> None:
        metadata = self._element.findall("{*}Metadata")
        if len(metadata) != 0:
            self._metadata = metadata[0]
            self._metadata_node = True

        geo_location = self._element.findall("{*}Location/{*}GeographicLocation")
        if len(geo_location) != 0:
            self._location_node = True
            self._geo_location = geo_location[0]

    @staticmethod
    def _get_attribute_or_none(element: ET.Element, attribute: str) -> Optional[str]:
        if attribute in element.attrib:
            return str(element.attrib[attribute])
        else:
            return None

    @staticmethod
    def _return_string(value: str | None) -> str:
        if value:
            return str(value)
        else:
            return ""

    @property
    def origin_type(self) -> str:
        """Returns the origin type of the value object, *read only property*."""
        value = self._get_attribute_or_none(self._metadata, "originType")
        return self._return_string(value)

    @property
    def source(self) -> str:
        """Returns the source of the value object, *read only property*."""
        value = self._get_attribute_or_none(self._metadata, "source")
        return self._return_string(value)

    @property
    def life_cycle_status(self) -> str:
        """Returns the life cycle status of the value object, *read only property*."""
        value = self._get_attribute_or_none(self._metadata, "lifeCycleStatus")
        return self._return_string(value)

    @property
    def is_in_service(self) -> str:
        """Returns the is in service status of the value object, *read only property*."""
        value = self._get_attribute_or_none(self._metadata, "isInService")
        return self._return_string(value)

    @property
    def location_accuracy(self) -> float:
        """Returns the location accuracy of the value object, *read only property*."""
        accuracy = self._get_attribute_or_none(self._geo_location, "accuracy")
        if accuracy:
            return float(accuracy)
        else:
            return np.NaN

    @property
    def location_data_acquisition_method(self) -> str:
        """Returns the location data acquisition method of the value object, *read only property*."""
        value = self._get_attribute_or_none(self._geo_location, "dataAcquisitionMethod")
        return self._return_string(value)

    def has_location(self) -> bool:
        """
        Returns True if value object has location metadata.

        Returns:
            (bool):True if the object is a design object, False otherwise.

        """
        return True if self._location_node else False

    def has_metadata(self) -> bool:
        """Returns True if value object has object metadata.

        Returns:
            (bool):True if the object is a design object, False otherwise.

        """
        return True if self._metadata_node else False

    def is_design(self):
        """Returns whether the object is a design object.

        Returns:
            (bool):True if the object is a design object, False otherwise.

        """
        return True if self.is_in_service and self.location_data_acquisition_method in ["Design"] else False
