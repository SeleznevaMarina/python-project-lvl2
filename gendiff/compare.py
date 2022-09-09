import json
import yaml
from pathlib import Path
from gendiff import stylish


def get_opening_file(path):

    if path.suffix == '.yaml' or path.suffix == '.yml':
        with open(Path().absolute() / 'gendiff' / path) as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
    elif path.suffix == '.json':
        file = json.load(open(Path().absolute() / 'gendiff' / path))

    return file


def generate_diff(file1, file2):

    file_1 = get_opening_file(file1)
    file_2 = get_opening_file(file2)
    compare_dict = get_comparing(file_1, file_2)
    return stylish.stringify(compare_dict, '-')


def get_comparing(file_1, file_2):
    compare_dict = {}
    keys = list(file_1.keys())
    keys.extend(list(file_2.keys()))
    keys = sorted(set(keys))

    for key in keys:
        condition_1 = key in file_1 and type(file_1[key]) is dict
        condition_2 = key in file_2 and type(file_2[key]) is dict

        if condition_1 and condition_2:
            compare_dict[f"   {key}"] = get_comparing(file_1[key], file_2[key])
        else:

            if key in file_1 and key in file_2 and file_1[key] == file_2[key]:
                compare_dict[f"   {key}"] = file_1[key]
            elif key in file_1:
                compare_dict[f" - {key}"] = file_1[key]

                if key in file_2:
                    compare_dict[f" + {key}"] = file_2[key]

            elif key in file_2:
                compare_dict[f" + {key}"] = file_2[key]

    return compare_dict

