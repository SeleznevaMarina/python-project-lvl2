import pytest
from pathlib import Path
from gendiff.compare import generate_diff


@pytest.fixture
def coll_1():
    return (test_file1.json, test_file2.json)


@pytest.fixture
def coll_2():
    path1 = Path().absolute() / "tests" / "fixtures" / "test_file1.json"
    path2 = Path().absolute() / "tests" / "fixtures" / "test_file2.json"
    return (path1, path2)


def test_generate_diff(coll_1):
    file_1, file_2 = coll_1
    path = Path().absolute() / "tests" / "fixtures" / "test_result"
    compare_file = open(path, "r").read()
    assert generate_diff(file_1, file_2) == compare_file


def test_generate_diff(coll_2):
    file_1, file_2 = coll_2
    path = Path().absolute() / "tests" / "fixtures" / "test_result"
    compare_file = open(path, "r").read()
    assert generate_diff(file_1, file_2) == compare_file
