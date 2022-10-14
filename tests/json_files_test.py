import pytest
from pathlib import Path
from gendiff import generate_diff


PATH1 = Path().absolute() / "tests" / "fixtures" / "file1.json"
PATH2 = Path().absolute() / "tests" / "fixtures" / "file2.json"

@pytest.mark.parametrize("formarter, result_file", [("plain", "test_result.plain"), ("stylish", "test_result"), ("json", "test_result.json")])
def test_generate_diff(formarter, result_file):

    result_path = Path().absolute() / "tests" / "fixtures" / result_file
    compare_file = open(result_path, "r").read()
    assert generate_diff(PATH1, PATH2, formarter) == compare_file.strip()
