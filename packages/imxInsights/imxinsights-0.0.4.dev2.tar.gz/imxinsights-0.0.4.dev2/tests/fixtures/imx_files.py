import pytest

from imxInsights import Imx


@pytest.fixture(scope="module")
def imx_v500_project_instance(imx_v500_project_test_file_path) -> Imx:
    return Imx(imx_v500_project_test_file_path)


@pytest.fixture(scope="module")
def imx_v124_project_instance(imx_v124_project_test_file_path) -> Imx:
    return Imx(imx_v124_project_test_file_path)
