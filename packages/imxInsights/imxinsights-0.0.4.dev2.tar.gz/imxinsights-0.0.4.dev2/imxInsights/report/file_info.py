import re


def write_situation_info(worksheet, situation, start_row: int, suffix=""):
    if suffix != "":
        suffix = f" {suffix}"

    worksheet.write(start_row + 0, 0, f"file{suffix}")
    worksheet.write(start_row + 0, 1, situation.file_path.name)

    worksheet.write(start_row + 1, 0, f"imx version{suffix}")
    worksheet.write(start_row + 1, 1, situation.imx_version)

    worksheet.write(start_row + 2, 0, f"sha256{suffix}")
    worksheet.write(start_row + 2, 1, situation.file_hash)

    worksheet.write(start_row + 3, 0, f"situation{suffix}")
    worksheet.write(start_row + 3, 1, situation.situation_type)


def sorted_path_methode(value):
    parts = value.split(".")
    sorted_parts = []

    for part in parts:
        num_part = re.search(r"\d+", part)
        if num_part:
            sorted_parts.append((int(num_part.group()), part))
        else:
            sorted_parts.append((-1, part))  # Use a negative value to prioritize non-numeric parts

    return sorted_parts


def sort_pandas_dataframe_columns(df, column_order_pre_fix_list, column_order_suffix_list=None):
    if column_order_suffix_list is None:
        column_order_suffix_list = []

    columns_in_pre_fix_list = [col for col in column_order_pre_fix_list if col in df.columns]
    columns_in_sur_fix_list = [col for col in column_order_suffix_list if col in df.columns]

    columns_not_in_lists = [col for col in df.columns if col not in column_order_pre_fix_list and col not in columns_in_sur_fix_list]
    columns_not_in_lists = sorted(columns_not_in_lists, key=sorted_path_methode)
    ordered_columns = columns_in_pre_fix_list + columns_not_in_lists + columns_in_sur_fix_list

    return df[ordered_columns]
