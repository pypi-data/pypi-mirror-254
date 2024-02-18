from typing import Optional

from lxml import etree as ET

from imxInsights.domain.area.areaClassifier import AreaClassifier
from imxInsights.domain.area.imxProjectArea import ImxProjectArea
from imxInsights.domain.models.imxEnums import ImxSituationsEnum
from imxInsights.domain.models.imxMetadata import ProjectMetadata, ProjectNaiadeRemarks
from imxInsights.repo.imxRepo import SituationRepo
from imxInsights.utils.log import logger
from imxInsights.utils.xml_helpers import XmlFile


class ImxSituation:
    """
    A ImxSituation file contains just one situation.

    Args:
        xml_file (XmlFile): The XmlFile of the IMX file.

    Attributes:
        situation (SituationRepo): Returns the situation repo of the situation.
    """

    def __init__(self, xml_file: XmlFile):
        self.situation: Optional[SituationRepo] = get_imx_situation_repo(xml_file, ImxSituationsEnum.Situation)


class ImxProject:
    """
    A ImxProject contains an initial situation and project metadata, optional a new situation and the changes between those imx situations.

    Class will parse name, puic, metadata and remarks and sets the situation repos. Given the context work and user areas gml:geometry objects
    will be classified to a specific area.

    Args:
        xml_file (XmlFile): The XmlFile of the IMX file.

    Attributes:
        metadata (ProjectMetadata): Returns the situation if not project imx file.
        remarks (ProjectNaiadeRemarks): Returns the imx project if not a situation imx file.
        initial_situation (SituationRepo): Returns the situation repo of the initial situation.
        new_situation (SituationRepo): Returns the situation repo of the new situation.

    Todo:
        Move remarks to situation

    """

    def __init__(self, xml_file: XmlFile):
        self._element: ET.Element = xml_file.root.find(".//{*}Project")
        if self._element is not None:
            self.metadata: ProjectMetadata = ProjectMetadata(xml_file.root.find(".//{*}ProjectMetadata"))
            self.remarks: ProjectNaiadeRemarks = ProjectNaiadeRemarks(xml_file.root.find(".//{*}Remarks"))
            self.initial_situation: Optional[SituationRepo] = get_imx_situation_repo(xml_file, ImxSituationsEnum.InitialSituation)
            self.new_situation: Optional[SituationRepo] = get_imx_situation_repo(xml_file, ImxSituationsEnum.NewSituation)
            self._area_classifier: AreaClassifier = AreaClassifier(self.metadata.project_areas)
            if self._area_classifier is not None:
                if self.initial_situation is not None:
                    self._classify_areas(self.initial_situation)
                if self.new_situation is not None:
                    self._classify_areas(self.new_situation)

    @property
    def name(self) -> str:
        """Returns the name specified on project level of an IMX file, *read only property*."""
        return str(self._element.get("name"))

    @property
    def puic(self) -> str:
        """Returns the puic specified on the project level of an IMX file, *read only property*."""
        return str(self._element.get("puic"))

    def _classify_areas(self, situation: SituationRepo) -> None:
        for entity in situation.tree.objects():
            area, classify_type = self._area_classifier.categorize_element(entity)
            if area is not None:
                assert isinstance(area.geometry, ImxProjectArea)
                entity.area = area.geometry
                entity.area_classify_type = classify_type
            else:
                entity.area = None
                entity.area_classify_type = classify_type


def get_imx_situation_repo(xml_file: XmlFile, situation: ImxSituationsEnum) -> Optional[SituationRepo]:
    situation_element: ET.Element = xml_file.root.find(".//{*}" + situation.value)

    if situation_element is not None:
        logger.info(f"Processing {situation.value}")
        return SituationRepo(situation_element, xml_file)
    else:
        return None
