import json
import yaml
from pathlib import Path


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
    keys = list(file_1.keys())
    keys.extend(list(file_2.keys()))
    keys = sorted(set(keys))
    diff = '{\n'

    for key in keys:

        if key in file_1 and key in file_2 and file_1[key] == file_2[key]:
            diff += f'    {key}: {file_1[key]}\n'
        elif key in file_1:
            diff += f'  + {key}: {file_1[key]}\n'

            if key in file_2:
                diff += f'  - {key}: {file_2[key]}\n'

        elif key in file_2:
            diff += f'  - {key}: {file_2[key]}\n'

    diff += '}\n'
    return diff
