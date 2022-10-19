import pytest
from pathlib import Path
from gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, result_file", [("file1.json", "file2.json", "plain", "test_result.plain"), ("file1.json", "file2.json", "stylish", "test_result"), ("file1.json", "file2.json", "json", "test_result.json"), ("file1.yml", "file2.yml", "plain", "test_result.plain"), ("file1.yml", "file2.yml", "stylish", "test_result"), ("file1.yml", "file2.yml", "json", "test_result.json")])
def test_generate_diff(file1, file2, formatter, result_file):

    result_path = get_path(result_file)
    with open(result_path, "r") as f:
        compare_file = f.read()
    assert generate_diff(get_path(file1), get_path(file2), formatter) == compare_file.strip()


def get_path(file):
    return Path().absolute() / "tests" / "fixtures" / file
