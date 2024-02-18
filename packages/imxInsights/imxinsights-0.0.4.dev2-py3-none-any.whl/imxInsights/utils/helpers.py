import hashlib
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from ruamel.yaml import YAML

# commented out: code that is not used but could be handy.


def yaml_load(file_path):
    """
    Load a YAML file and return its contents as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a dictionary.
    """
    yaml = YAML()
    yaml.default_flow_style = True
    with open(file_path, "r") as stream:
        return yaml.load(stream)


def yaml_save(data, out_file_path):
    """
    Save a dictionary as a YAML file.

    Args:
        data (dict): The dictionary to be saved as YAML.
        out_file_path (str): The path to save the YAML file.
    """
    yaml = YAML()
    yaml.default_flow_style = True
    with open(out_file_path, "w") as outfile:
        yaml.dump(data, outfile)


def get_file_path(current_path: str, path: str) -> str:
    my_dir = os.path.dirname(current_path)
    config_file_path = os.path.join(my_dir, path)
    return config_file_path


# def is_float(element: Any) -> bool:
#     """
#     Check if a given value can be converted to a float.
#
#     :param element: The value to check.
#     :type element: any
#     :return: True if the value can be converted to a float, False otherwise.
#     :rtype: bool
#     """
#     if element is None:
#         return False
#     try:
#         float(element)
#         return True
#     except ValueError:
#         return False


def hash_dict_ignor_nested(dictionary: Dict):
    """
    Compute the SHA-1 hash of the dictionary's non-nested values.

    This function takes a dictionary as input and computes the SHA-1 hash of its
    content, excluding nested dictionaries. It extracts non-dictionary values
    from the input dictionary and creates a new dictionary containing only those
    values. Then, it sorts the keys of the new dictionary and computes the SHA-1
    hash of the resulting JSON-encoded string.

    Args:
        dictionary (Dict): The dictionary whose content should be hashed.

    Returns:
        str: A hexadecimal string representing the SHA-1 hash of the non-nested
             values in the dictionary.

    Examples:
        >>> input_dict = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
        >>> hash_value = hash_dict_ignor_nested(input_dict)
        >>> hash_value
        'a1e3d40cd5262ccef85a17b7698b9d5e8a61a5f6'

    Note:
        This function excludes nested dictionaries when computing the hash,
        focusing only on non-dictionary values. If the input dictionary contains
        nested dictionaries, their content will not be included in the hash.
    """
    new_dict = {}
    for key, value in dictionary.items():
        if not isinstance(value, dict):
            new_dict[key] = value

    hash_object = hashlib.sha1(json.dumps(new_dict, sort_keys=True).encode())
    return hash_object.hexdigest()


def flatten_dict(data_dict: Dict[str, Dict | str | List], skip_key: Optional[str] = "@puic", prefix="", sep=".") -> dict[str, str]:
    def _custom_sorting(key_, remaining_: List[Dict]):
        mapping = {
            "RailConnectionInfo": "@railConnectionRef",
            "Announcement": "@installationRef",
        }
        if key_ in mapping.keys():
            return sorted(remaining_, key=lambda x: x[mapping[key_]])
        else:
            return sorted(remaining_, key=hash_dict_ignor_nested)

    result: Dict[str, str] = {}

    # Skip root node if this is a recursive call and key is found
    if prefix and skip_key in data_dict:
        return result

    for key, value in data_dict.items():
        if not isinstance(value, list) and not isinstance(value, dict):
            result[f"{prefix}{key}"] = value
            continue

        new_prefix = f"{prefix}{key}{sep}"

        if isinstance(value, list) and len(value) > 0 and not isinstance(value[0], dict):
            # ERMTS properties -> add index and add to current.
            for i, child in enumerate(value):
                result[f"{new_prefix}{i}"] = child
            continue

        # Multiple children -> list of dicts. Convert single dict to list with dict.
        if isinstance(value, dict):
            value = [value]

        assert len(value) > 0 and isinstance(value[0], dict)

        # Filter children with skip_key.
        remaining = list[dict]() if skip_key is not None else value
        if skip_key is not None:
            for child in value:
                if skip_key in child:
                    continue
                remaining.append(child)

        # Add index for each child if >1 and recurse, order can be changed in xml, so sort before indexing..
        if len(remaining) > 1:
            # sorting is done on a specified key.
            # if no key is present make hash of attributes, if no attributes hash first node attributes...
            remaining = _custom_sorting(key, remaining)

        for i, child in enumerate(remaining):
            child_prefix = f"{new_prefix}{i}{sep}" if len(remaining) > 1 else new_prefix
            flattened = flatten_dict(child, skip_key=skip_key, prefix=child_prefix, sep=sep)
            result = result | flattened

    return result


def hash_sha256(path: Path):
    """
    Calculate the SHA-256 hash sum of a file located at the specified path.

    This function takes a `Path` object representing the path to a file and
    calculates the SHA-256 hash sum of the file's contents. It returns the
    hash sum as a hexadecimal string.

    Args:
        path (Path): The path to the file for which the SHA-256 hash sum
            should be calculated.

    Returns:
        str: A hexadecimal string representing the SHA-256 hash sum of the file.

    Examples:
        >>> file_path = Path("example.txt")
        >>> hash_value = hash_sha256(file_path)
        >>> hash_value
        'a12b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3'

    Note:
        This function reads the entire contents of the file into memory
        to calculate the hash sum. For large files, this may consume a
        significant amount of memory. Make sure to handle large files
        appropriately when using this function.

    """
    return f"{hashlib.sha256(path.read_bytes()).hexdigest()}"
