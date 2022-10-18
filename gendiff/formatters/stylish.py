def stringify(value, replacer=' ', spaces_count=1):

    if type(value) is not dict:
        return str(value)

    def walk(value, depth):
        diff = '{'

        if type(value) is not dict:
            return boolean_transformation(value)

        for key in value:
            indent = replacer * spaces_count * depth
            value[key] = boolean_transformation(value[key])

            if type(value[key]) is not dict:
                diff += f'\n{indent}{key}: {value[key]}'
                continue

            if 'type' not in value[key]:
                diff += f'\n{indent}{key}: {walk(value[key], depth + 1)}'

            elif value[key]['type'] == 'removed':
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}- {key}: {walk(value[key]["old"], depth + 1)}'

            elif value[key]['type'] == 'added':
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}+ {key}: {walk(value[key]["new"], depth + 1)}'

            elif value[key]['type'] == 'updated':
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}- {key}: {walk(value[key]["old"], depth + 1)}'
                diff += f'\n{indent}+ {key}: {walk(value[key]["new"], depth + 1)}'

            elif value[key]['type'] == 'nested':
                diff += f'\n{indent}{key}: {walk(value[key]["no_diff"], depth + 1)}'

        diff += '\n' + str(replacer * spaces_count * (depth - 1)) + '}'
        return diff

    return walk(value, 1) + '\n'


def boolean_transformation(value):

    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
