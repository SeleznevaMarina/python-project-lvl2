import json, copy
from pathlib import Path


def generate_diff(file1, file2):

    #if file1 !=

    file_1 = json.load(open(Path().absolute() / 'gendiff' / file1))
    file_2 = json.load(open(Path().absolute() / 'gendiff' / file2))
    compare_dict = {}
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
