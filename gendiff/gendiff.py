from gendiff.formatters import formatter
from gendiff import parser


def generate_diff(file1, file2, format_name='stylish'):

    data_1 = parser.get_data(file1)
    data_2 = parser.get_data(file2)
    diff_dict = build_dicts_diff(data_1, data_2)
    return formatter.format(diff_dict, format_name)


def build_dicts_diff(data_1, data_2):
    diff_dict = {}
    keys_1 = list(data_1.keys())
    keys_2 = list(data_2.keys())
    keys = sorted(set(keys_1) | set(keys_2))
    added_keys = list(set(keys_2) - set(keys_1))
    removed_keys = list(set(keys_1) - set(keys_2))
    common_keys = list(set(keys_1) & set(keys_2))

    for key in keys:

        if key in added_keys:
            diff_dict[key] = {'type': 'added', 'new': data_2[key]}
        elif key in removed_keys:
            diff_dict[key] = {'type': 'removed', 'old': data_1[key]}
        elif type(data_1[key]) is dict and type(data_2[key]) is dict:
            diff_dict[key] = {'type': 'nested', 'no_diff': build_dicts_diff(data_1[key], data_2[key])}
        elif key in common_keys and data_1[key] == data_2[key]:
            diff_dict[key] = {'type': 'nested', 'no_diff': data_1[key]}
        elif key in common_keys and data_1[key] != data_2[key]:
            diff_dict[key] = {'type': 'updated', 'old': data_1[key], 'new': data_2[key]}

    return diff_dict
