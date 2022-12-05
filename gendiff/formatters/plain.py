def stringify(value):

    return walk(value, "")


def walk(value, path):
    diff = []

    for key in value:

        if value[key]['type'] == 'nested' and type(value[key]['no_diff']) is dict:
            new_path = path + f"{key}."
            diff.append(f'{walk(value[key]["no_diff"], new_path)}')

        if value[key]['type'] == 'updated':
            new_path = path + f"{key}"
            diff.append(f"Property '{new_path}' was updated. From {convert_to_string(value[key]['old'])} to {convert_to_string(value[key]['new'])}")

        if value[key]['type'] == 'removed':
            new_path = path + f"{key}"
            diff.append(f"Property '{new_path}' was removed")

        if value[key]['type'] == 'added':
            new_path = path + f"{key}"
            diff.append(f"Property '{new_path}' was added with value: {convert_to_string(value[key]['new'])}")

    return '\n'.join(diff)


def convert_to_string(value):

    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    if isinstance(value, int):
        return value

    return f"'{value}'"
