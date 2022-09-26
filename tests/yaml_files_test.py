import pytest
from pathlib import Path
from package_gendiff import *
from gendiff import generate_diff


@pytest.fixture
def coll_1():
    path1 = Path().absolute() / "tests" / "fixtures" / "test_file1.yml"
    path2 = Path().absolute() / "tests" / "fixtures" / "test_file2.yaml"
    return (path1, path2, 'plain')


@pytest.fixture
def coll_2():
    path1 = Path().absolute() / "tests" / "fixtures" / "test_file1.yml"
    path2 = Path().absolute() / "tests" / "fixtures" / "test_file2.yaml"
    return (path1, path2)


@pytest.fixture
def coll_3():
    path1 = Path().absolute() / "package_gendiff" / "file1.yaml"
    path2 = Path().absolute() / "package_gendiff" / "file2.yml"
    return (path1, path2, 'json')


def test_plain_formarter(coll_1):
    file_1, file_2, formarter = coll_1
    path = Path().absolute() / "tests" / "fixtures" / "test_result.plain"
    compare_file = open(path, "r").read()
    assert generate_diff(file_1, file_2, formarter) == compare_file


def test_generate_diff(coll_2):
    file_1, file_2 = coll_2
    path = Path().absolute() / "tests" / "fixtures" / "test_result"
    compare_file = open(path, "r").read()
    assert generate_diff(file_1, file_2, 'stylish') == compare_file


def test_json_formarter(coll_3):
    file_1, file_2, formarter = coll_3
    path = Path().absolute() / "tests" / "fixtures" / "test_result.json"
    compare_file = open(path, "r").read()
    assert generate_diff(file_1, file_2, formarter) == compare_file
