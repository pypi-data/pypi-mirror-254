from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

from imxInsights.domain.models.imxEnums import ImxSituationsEnum
from imxInsights.domain.models.imxSituations import ImxProject, ImxSituation
from imxInsights.report.file_info import write_situation_info
from imxInsights.utils.helpers import hash_sha256
from imxInsights.utils.log import logger
from imxInsights.utils.xml_helpers import XmlFile


class Imx:
    """
    Imx main object is used as an entry point for imx files.

    Args:
        imx_file_path (str): File path of the IMX file.

    Attributes:
        situation (Optional[ImxSituation]): The situation of an IMX file if present.
        project (Optional[ImxProject]): The ImxProject of an IMX file if present.
    """

    def __init__(self, imx_file_path: str):
        logger.info(f"Loading file {imx_file_path}")

        self.file_path = Path(imx_file_path)
        self.file_hash = hash_sha256(self.file_path)
        self._xml_file = XmlFile(self.file_path)
        self._imx_version: str = self._xml_file.root.find("[@imxVersion]").attrib["imxVersion"]
        logger.info(f"IMX version: {self.imx_version}")

        self.situation: Optional[ImxSituation] = None
        self.project: Optional[ImxProject] = None
        if self._xml_file.root.find(".//{*}Project") is not None:
            self.project = ImxProject(self._xml_file)
        else:
            self.situation = ImxSituation(self._xml_file)
            # raise NotImplementedError

        logger.info("IMX parsed, DONE!")

    @property
    def imx_version(self) -> str:
        """Returns the IMX version of the file, *read only property*."""
        return self._imx_version

    def get_situation_repository(self, situation_type: ImxSituationsEnum) -> Optional[ImxSituation]:
        """
        Get a specific situation repository  from an IMX project or situation file.

        Args:
            situation_type (ImxSituationsEnum): The IMX situation to get the repo.

        Returns:
            (SituationRepo): The given situation if exists in file.

        """
        if situation_type == ImxSituationsEnum.InitialSituation:
            if self.project is not None:
                return self.project.initial_situation
        elif situation_type == ImxSituationsEnum.NewSituation:
            if self.project is not None:
                return self.project.new_situation
        else:
            if self.situation is not None:
                return self.situation
        return None

    @staticmethod
    def _reshape_df_worksheet(df, worksheet, filter=True):
        (max_row, max_col) = df.shape
        worksheet.set_column(0, max_col - 1, 12)
        if filter:
            worksheet.autofilter(0, 0, max_row, max_col)
        worksheet.autofit()
        worksheet.freeze_panes(1, 0)

    def generate_population_excel(self, file_path: str, situation: ImxSituationsEnum):
        repo = self.get_situation_repository(situation)

        writer = pd.ExcelWriter(file_path, engine="xlsxwriter")
        workbook = writer.book

        worksheet_info = workbook.add_worksheet("info")
        worksheet_info.set_column(0, 0, 25)
        worksheet_info.set_column(1, 1, 150)

        worksheet_info.write(1, 0, "process datestamp")
        worksheet_info.write(1, 1, datetime.now().astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f"))

        write_situation_info(worksheet_info, repo, 2, "a")

        overview_records = []
        overview_keys_to_keep = [
            "puic",
            "path",
            "area",
            "name",
            "parent",
            "Metadata.@originType",
            "Metadata.@source",
            "Metadata.@registrationTime",
            "Metadata.@lifeCycleStatus",
            "Metadata.@isInService",
            "Location.GeographicLocation.@dataAcquisitionMethod",
            "Location.GeographicLocation.@accuracy",
        ]

        df_dict = repo.get_pandas_df_dict()

        pivot_index = [
            "path",
            "Metadata.@lifeCycleStatus",
            "Location.GeographicLocation.@accuracy",
            "Location.GeographicLocation.@dataAcquisitionMethod",
        ]

        for key, df in df_dict.items():
            records_ = df.to_dict(orient="records")

            for record_ in records_:
                records_to_add = {key: value for key, value in record_.items() if key in overview_keys_to_keep} | {"counter": 1}
                if records_to_add["parent"] == "":
                    records_to_add["_parent"] = records_to_add["puic"]
                else:
                    records_to_add["_parent"] = records_to_add["parent"]

                for item in pivot_index:
                    if item not in records_to_add.keys():
                        records_to_add[item] = ""

                overview_records.append(records_to_add)

        df = pd.DataFrame.from_records(overview_records)

        # create pivot
        table = pd.pivot_table(
            df,
            values="counter",
            index=pivot_index,
            columns=["area"],
            aggfunc="count",
            fill_value=" ",
        )
        table.to_excel(writer, sheet_name="population_pivot", index=True)
        worksheet = writer.sheets["population_pivot"]
        self._reshape_df_worksheet(table, worksheet, filter=False)

        temp_df = df["path"].str.split(".", expand=True)
        df["main_type"] = temp_df[0]
        del df["counter"]

        df_grouped = df.groupby(["main_type", "_parent", "path"], group_keys=True).apply(lambda group: group)
        df_grouped = df_grouped.assign(row_number=range(len(df)))
        df = df_grouped.set_index("row_number")

        first_column = df.pop("main_type")
        df.insert(2, "main_type", first_column)
        del df["_parent"]

        df.to_excel(writer, sheet_name="all_objects", startrow=0, startcol=0, index=1)
        worksheet = writer.sheets["all_objects"]
        self._reshape_df_worksheet(df, worksheet)

        for key, df in sorted(df_dict.items()):
            records_ = df.to_dict(orient="records")
            for record_ in records_:
                records_to_add = {key: value for key, value in record_.items() if key in overview_keys_to_keep}
                overview_records.append(records_to_add)

            sheet_name = f"{key[:14]}...{key[-14:]}" if len(key) > 30 else key
            df.to_excel(writer, sheet_name=sheet_name)

            worksheet = writer.sheets[sheet_name]
            self._reshape_df_worksheet(df, worksheet)

        worksheet_info.activate()

        writer.close()
