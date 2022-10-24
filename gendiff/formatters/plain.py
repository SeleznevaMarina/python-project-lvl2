from gendiff.formatters.stylish import convert_to_string


def stringify(value):

    return walk(value, "'")


def walk(value, path):
    diff = ''

    for key in value:

        if value[key]['type'] == 'nested' and type(value[key]['no_diff']) is dict:
            new_path = path + f"{key}."
            diff += f'{walk(value[key]["no_diff"], new_path)}'

        if value[key]['type'] == 'updated':
            new_path = path + f"{key}"
            diff += f"Property {new_path}' was updated. From {type_checking(value[key]['old'])} to {type_checking(value[key]['new'])}\n"

        if value[key]['type'] == 'removed':
            new_path = path + f"{key}"
            diff += f"Property {new_path}' was removed\n"

        if value[key]['type'] == 'added':
            new_path = path + f"{key}"
            diff += f"Property {new_path}' was added with value: {type_checking(value[key]['new'])}\n"

    return diff


def type_checking(value):

    if type(value) is dict:
        return '[complex value]'

    if type(value) is bool or value is None:
        return f"{convert_to_string(value)}"

    if type(value) is int:
        return value

    return f"'{value}'"
