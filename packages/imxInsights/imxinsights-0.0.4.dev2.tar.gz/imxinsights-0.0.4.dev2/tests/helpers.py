from __future__ import annotations

import tempfile
from pathlib import Path
from pkgutil import ModuleInfo, walk_packages
from types import ModuleType
from typing import Iterable

from tests.data_shield import DataShield


def workspace_path(*parts: str) -> Path:
    directory = Path(__file__).parent
    while directory is not None and not any([f for f in directory.iterdir() if f.name.lower() == "pyproject.toml"]):
        directory = directory.parent

    return directory.joinpath(*parts).absolute()


def sample_path(*parts: str) -> str:
    return str(workspace_path("sample_data", *parts))


def packages_in_module(m: ModuleType) -> Iterable[ModuleInfo]:
    return walk_packages(m.__path__, prefix=m.__name__ + ".")  # type: ignore


def package_paths_in_module(m: ModuleType) -> Iterable[str]:
    return [package.name for package in packages_in_module(m)]


def get_decrypted_temp_file_path(encrypted_file_path: str) -> str:
    temp_file = tempfile.NamedTemporaryFile(mode="wb", delete=False)
    data = DataShield.decrypt(encrypted_file_path)
    temp_file.write(data)
    temp_file.close()
    with open(temp_file.name, "rb") as f:
        assert f.read() == data, "temp file should contain data that is writen to it"
    return temp_file.name
