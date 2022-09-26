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

            cond_1 = 'old' in value[key]
            cond_2 = 'new' in value[key]
            cond_3 = 'no_diff' in value[key]

            if cond_1:
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}- {key}: {walk(value[key]["old"], depth + 1)}'

            if cond_2:
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}+ {key}: {walk(value[key]["new"], depth + 1)}'

            if cond_3:
                diff += f'\n{indent}{key}: {walk(value[key]["no_diff"], depth + 1)}'

            if not cond_1 and not cond_2 and not cond_3:
                diff += f'\n{indent}{key}: {walk(value[key], depth + 1)}'

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
