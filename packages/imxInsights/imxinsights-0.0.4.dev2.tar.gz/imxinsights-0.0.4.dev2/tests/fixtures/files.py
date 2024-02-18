import pytest

from tests.helpers import sample_path


@pytest.fixture(scope="module")
def imx_v500_project_test_file_path() -> str:
    return sample_path("IMX_E-R50008_EKB_Perceel_2_V1.3_5_0_0_test_Niki.xml")
    # encrypted_file_path = sample_path("imx_500-encrypted.xml")
    # tester = get_decrypted_temp_file_path(encrypted_file_path)
    # return tester


@pytest.fixture(scope="module")
def imx_v124_project_test_file_path() -> str:
    return sample_path("20221018_V18_A_Hengelo_Zutphen_Wintersw_71_SK0240_Arcadis.xml")
    # encrypted_file_path = sample_path("imx_124-encrypted.xml")
    # tester = get_decrypted_temp_file_path(encrypted_file_path)
    # return tester
