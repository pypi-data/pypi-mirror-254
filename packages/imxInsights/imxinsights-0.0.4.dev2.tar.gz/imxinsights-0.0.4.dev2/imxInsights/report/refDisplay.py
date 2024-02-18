import re
from dataclasses import dataclass
from typing import Any, List, Optional, Set, Tuple, TypeVar

from imxInsights.repo.imxRepo import SituationRepo
from imxInsights.report.imxObjectDisplay import ImxObjectDisplay, ImxPuicDisplay

T = TypeVar("T")


@dataclass
class GuidComparisonResult:
    added_guids: List[str]
    removed_guids: List[str]
    unchanged_guids: List[str]


class ImxRefDisplay:
    def __init__(self, imx_situation_init: SituationRepo, imx_situation_new: SituationRepo) -> None:
        self._puic_display = ImxObjectDisplay(imx_situation_init, imx_situation_new)

    def get_display(self, value: T) -> T:
        if not isinstance(value, str):
            return value

        status, guids = self.get_uuid_from_diff_str(value)

        if not guids:
            return value

        guid_comparison_result = self._process_guids(value, guids)

        removed = self._nice_display_comprehension(guid_comparison_result.removed_guids)
        unchanged = self._nice_display_comprehension(guid_comparison_result.unchanged_guids)
        added = self._nice_display_comprehension(guid_comparison_result.added_guids)

        return self._format_ref_output(removed, added, unchanged)

    def _nice_display_comprehension(self, guids: List[str]) -> list[ImxPuicDisplay]:
        return [self._puic_display.get_nice_display(guid) for guid in guids]

    def _process_guids(self, value: Any, guids: List[str]) -> GuidComparisonResult:
        # todo: use status from re magic instead of if else below in code

        if " -> " in value:
            left, right = value.split(" -> ")
            __, left_guids = self.get_uuid_from_diff_str(left)
            __, right_guids = self.get_uuid_from_diff_str(right)
            return GuidComparisonResult(*self._compare_guid_lists(left_guids, right_guids))
        else:
            if value.startswith("++"):
                return GuidComparisonResult(added_guids=guids, removed_guids=[], unchanged_guids=[])
            elif value.startswith("--"):
                return GuidComparisonResult(added_guids=[], removed_guids=guids, unchanged_guids=[])
            else:
                return GuidComparisonResult(added_guids=[], removed_guids=[], unchanged_guids=guids)

    @staticmethod
    def _format_ref_output(removed: List[ImxPuicDisplay], added: List[ImxPuicDisplay], unchanged: List[ImxPuicDisplay]):
        output = []

        if len(removed) == 1 and len(added) == 1:
            return f"{removed[0]} -> {added[0]}"

        if removed:
            output.append(f"-- {', '.join(map(str, removed))}")
        if added:
            output.append(f"++ {', '.join(map(str, added))}")
        if unchanged:
            output.append(", ".join(map(str, unchanged)))

        return "\n".join(output)

    @staticmethod
    def _compare_guid_lists(old_guids: List[str], new_guids: List[str]) -> Tuple[Set, Set, Set]:
        # todo: move to helper
        old_set = set(old_guids)
        new_set = set(new_guids)

        common = old_set.intersection(new_set)
        unique_to_old = old_set - new_set
        unique_to_new = new_set - old_set

        return unique_to_new, unique_to_old, common

    @staticmethod
    def get_uuid_from_diff_str(value: str) -> Tuple[Optional[str], List[str]]:
        # todo: make custom for dif, get guid and multi guid move to helper
        guid_pattern = r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}"
        pattern = rf"^(?:(?P<status>\+\+|--)\s*)?({guid_pattern}(?:\s*{guid_pattern})*)"
        match = re.match(pattern, value)
        return (match.group("status"), match.group(2).split()) if match else (None, [])

    def get_parent_display(self, value: T) -> T:
        if not isinstance(value, str):
            return value
        return self._puic_display.get_parent_display(value)
