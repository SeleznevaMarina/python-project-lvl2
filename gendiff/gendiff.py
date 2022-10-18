import json
import yaml
from pathlib import Path
from gendiff.formatters import formatter


def get_opening_file(path):

    if type(path) is str:
        path = Path(path)

    raw_data = open(Path().absolute() / 'gendiff' / path)

    return parse_file(raw_data, path.suffix)


def parse_file(raw_data, extension):

    if extension == '.yaml' or extension == '.yml':
        return yaml.load(raw_data, Loader=yaml.FullLoader)
    elif extension == '.json':
        return json.load(raw_data)


def generate_diff(file1, file2, format_name='stylish'):

    file_1 = get_opening_file(file1)
    file_2 = get_opening_file(file2)
    diff_dict = build_dicts_diff(file_1, file_2)
    return formatter.format(diff_dict, format_name)


def build_dicts_diff(data_1, data_2):
    diff_dict = {}
    keys = list(data_1.keys())
    keys.extend(list(data_2.keys()))
    keys = sorted(set(keys))

    for key in keys:

        if key in data_1 and type(data_1[key]) is dict and key in data_2 and type(data_2[key]) is dict:
            diff_dict[key] = {'type': 'nested', 'no_diff': build_dicts_diff(data_1[key], data_2[key])}
        elif key in data_1 and key in data_2 and data_1[key] == data_2[key]:
            diff_dict[key] = {'type': 'nested', 'no_diff': data_1[key]}
        elif key in data_1:
            diff_dict[key] = {'type': 'removed', 'old': data_1[key]}

            if key in data_2:
                diff_dict[key]['new'] = data_2[key]
                diff_dict[key]['type'] = 'updated'

        elif key in data_2:
            diff_dict[key] = {'type': 'added', 'new': data_2[key]}

    return diff_dict
