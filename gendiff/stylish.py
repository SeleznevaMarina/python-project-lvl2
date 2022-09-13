def stringify(value, replacer=' ', spaces_count=1):

    if type(value) is not dict:
        return str(value)

    def walk(value, depth):
        diff = '{'

        for key in value:
            indent = replacer * spaces_count * depth

            if key.startswith('+') or key.startswith('-'):
                indent = replacer * (spaces_count * (depth - 1) + 2)

            value[key] = boolean_transformation(value[key])

            if type(value[key]) is not dict:

                diff += f'\n{indent}{key}: {value[key]}'

            else:
                diff += f"\n{indent}{key}: {walk(value[key], depth + 1)}"
                diff += '\n' + str(replacer * spaces_count * depth) + '}'

        return diff

    return walk(value, 1) + '\n}\n'


def boolean_transformation(value):

    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
