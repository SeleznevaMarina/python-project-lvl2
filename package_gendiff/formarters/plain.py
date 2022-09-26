from package_gendiff.formarters.stylish import boolean_transformation


def stringify(value):

    def walk(value, path):
        diff = ''

        for key in value:

            cond_1 = 'old' in value[key]
            cond_2 = 'new' in value[key]
            cond_3 = 'no_diff' in value[key] and type(value[key]['no_diff']) is dict

            if cond_3:
                new_path = path + f"{key}."
                diff += f'{walk(value[key]["no_diff"], new_path)}'

            if cond_1 and cond_2:
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was updated. From {is_dict(value[key]['old'])} to {is_dict(value[key]['new'])}\n"

            if cond_1 and not cond_2:
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was removed\n"

            if not cond_1 and cond_2:
                new_path = path + f"{key}"
                diff += f"Property {new_path}' was added with value: {is_dict(value[key]['new'])}\n"

        return diff

    return walk(value, "'")


def is_dict(value):

    if type(value) is dict:
        return '[complex value]'

    if type(value) is bool or value is None:
        return f"{boolean_transformation(value)}"

    return f"'{value}'"
