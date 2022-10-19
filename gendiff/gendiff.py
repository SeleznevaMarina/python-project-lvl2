import json
import yaml
from pathlib import Path
from gendiff.formatters import formatter


def get_data(path):

    with open(Path().absolute() / 'gendiff' / path, "r") as f:
        return parse_data(f, path.suffix[1:])


def parse_data(raw_data, format_file):

    if format_file == 'yaml' or format_file == 'yml':
        return yaml.load(raw_data, Loader=yaml.FullLoader)
    elif format_file == 'json':
        return json.load(raw_data)
    else:
        raise IOError('Invalid file format!')


def generate_diff(file1, file2, format_name='stylish'):

    data_1 = get_data(file1)
    data_2 = get_data(file2)
    diff_dict = build_dicts_diff(data_1, data_2)
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
