from gendiff.formarters.stylish import boolean_transformation


def stringify(value):

    def walk(value, path):
        diff = ''

        for key in value:

            if value[key]['type'] == 'no_different' and type(value[key]['no_diff']) is dict:
                new_path = path + f"{key}."
                diff += f'{walk(value[key]["no_diff"], new_path)}'

            if value[key]['type'] == 'updated':
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was updated. From {is_dict(value[key]['old'])} to {is_dict(value[key]['new'])}\n"

            if value[key]['type'] == 'removed':
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was removed\n"

            if value[key]['type'] == 'added':
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was added with value: {is_dict(value[key]['new'])}\n"

        return diff

    return walk(value, "'")


def is_dict(value):

    if type(value) is dict:
        return '[complex value]'

    if type(value) is bool or value is None:
        return f"{boolean_transformation(value)}"

    if type(value) is int:
        return value

    return f"'{value}'"
