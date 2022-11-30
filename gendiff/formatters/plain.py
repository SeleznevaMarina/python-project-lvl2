def stringify(value):

    return walk(value, "")


def walk(value, path):
    diff = ''

    for key in value:

        if value[key]['type'] == 'nested' and type(value[key]['no_diff']) is dict:
            new_path = path + f"{key}."
            diff += f'{walk(value[key]["no_diff"], new_path)}'

        if value[key]['type'] == 'updated':
            new_path = path + f"{key}"
            diff += f"Property '{new_path}' was updated. From {convert_to_string(value[key]['old'])} to {convert_to_string(value[key]['new'])}\n"

        if value[key]['type'] == 'removed':
            new_path = path + f"{key}"
            diff += f"Property '{new_path}' was removed\n"

        if value[key]['type'] == 'added':
            new_path = path + f"{key}"
            diff += f"Property '{new_path}' was added with value: {convert_to_string(value[key]['new'])}\n"

    return diff


def convert_to_string(value):

    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, bool):

        if value is True:
            return 'true'
        else:
            return 'false'

    if value is None:
        return 'null'

    return f"'{value}'"
