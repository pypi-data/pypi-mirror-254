from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from imxInsights.repo.imxRepo import SituationRepo
from imxInsights.repo.tree.imxTreeObject import ImxObject


class InSituationEnum(Enum):
    INIT_AND_NEW = "In init and new situation"
    ONLY_INIT = "Only in init situation"
    ONLY_NEW = "Only in new situation"
    NOT_PRESENT = "Not in init and not in new situation"


@dataclass
class ImxPuicDisplay:
    path: str
    puic: str
    status: InSituationEnum
    name: str

    def display(self) -> str:
        return f"{self.path} {self.name} ({self.puic}:{self.status.name})"

    def __repr__(self) -> str:
        return self.display()

    def __str__(self) -> str:
        return self.display()


class ImxObjectDisplay:
    def __init__(self, imx_situation_init: SituationRepo, imx_situation_new: SituationRepo) -> None:
        self.init_situation = imx_situation_init
        self.new_situation = imx_situation_new

    def get_nice_display(self, puic: str) -> ImxPuicDisplay:
        init_obj, new_obj = self.init_situation.get_by_puic(puic), self.new_situation.get_by_puic(puic)
        return ImxPuicDisplay(
            path=(new_obj or init_obj).path, puic=puic, status=self._get_status(init_obj, new_obj), name=self._get_name(init_obj, new_obj)
        )

    @staticmethod
    def _get_status(init_obj: Optional[ImxObject], new_obj: Optional[ImxObject]) -> InSituationEnum:
        if init_obj and new_obj:
            return InSituationEnum.INIT_AND_NEW
        if not init_obj and new_obj:
            return InSituationEnum.ONLY_NEW
        if init_obj and not new_obj:
            return InSituationEnum.ONLY_INIT
        return InSituationEnum.NOT_PRESENT

    @staticmethod
    def _get_name(init_obj: Optional[ImxObject], new_obj: Optional[ImxObject]) -> str:
        if not init_obj:
            return f'"{new_obj.name}"'
        if not new_obj:
            return f'"{init_obj.name}"'
        if init_obj.name == new_obj.name:
            return f'"{new_obj.name}"'
        return f'"{init_obj.name} -> {new_obj.name}"' if init_obj.name else f'"{None} -> {new_obj.name}"'

    @staticmethod
    def _get_all_parents(imx_object: ImxObject) -> List[ImxObject]:
        if not imx_object:
            return []
        parents = []
        while imx_object.parent:
            parents.append(imx_object.parent)
            imx_object = imx_object.parent
        return parents

    def _create_parent_path(self, obj: ImxObject) -> List[str]:
        parents = self._get_all_parents(obj) + [obj]
        return [f"<{item.tag} {item.name if item.name else 'NoName'} ({item.puic}) />" for item in parents]

    def _get_formatted_path(self, obj: ImxObject) -> str:
        if not obj:
            return ""
        return ".".join(self._create_parent_path(obj)[::-1])

    def get_parent_display(self, puic_value: str) -> str:
        if not puic_value:
            return puic_value

        init_object = self.init_situation.get_by_puic(puic_value)
        init_path = self._get_formatted_path(init_object)

        new_object = self.new_situation.get_by_puic(puic_value)
        new_path = self._get_formatted_path(new_object)

        if not new_object and init_path:
            return init_path
        elif not init_object and new_object:
            return new_path
        elif init_path == new_path or init_path == []:
            return new_path

        return f"{init_path} -> {new_path}"
