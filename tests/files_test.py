import pytest
from pathlib import Path
from gendiff import generate_diff


json_parameters = [("json", "plain", "test_result.plain"), ("json", "stylish", "test_result"), ("json", "json", "test_result.json")]
yml_parameters = [("yml", "plain", "test_result.plain"), ("yml", "stylish", "test_result"), ("yml", "json", "test_result.json")]


@pytest.mark.parametrize("file_type, formatter, result_file", json_parameters + yml_parameters)
def test_generate_diff(file_type, formatter, result_file):

    path1 = Path().absolute() / "tests" / "fixtures" / f"file1.{file_type}"
    path2 = Path().absolute() / "tests" / "fixtures" / f"file2.{file_type}"
    result_path = Path().absolute() / "tests" / "fixtures" / result_file
    compare_file = open(result_path, "r").read()
    assert generate_diff(path1, path2, formatter) == compare_file.strip()
