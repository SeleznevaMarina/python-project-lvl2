def stringify(value, replacer=' ', spaces_count=1):

    return walk(value, 1, replacer, spaces_count) + '\n'


def walk(value, depth, replacer, spaces_count):
    diff = ['{']

    if type(value) is not dict:
        return convert_to_string(value)

    for key in value:
        indent = replacer * spaces_count * depth
        value[key] = convert_to_string(value[key])

        if type(value[key]) is not dict:
            diff.append(f'{indent}{key}: {value[key]}')
            continue

        if 'type' not in value[key]:
            diff.append(f'{indent}{key}: {walk(value[key], depth + 1, replacer, spaces_count)}')

        elif value[key]['type'] == 'removed':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}- {key}: {walk(value[key]["old"], depth + 1, replacer, spaces_count)}')

        elif value[key]['type'] == 'added':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}+ {key}: {walk(value[key]["new"], depth + 1, replacer, spaces_count)}')

        elif value[key]['type'] == 'updated':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}- {key}: {walk(value[key]["old"], depth + 1, replacer, spaces_count)}')
            diff.append(f'{indent}+ {key}: {walk(value[key]["new"], depth + 1, replacer, spaces_count)}')

        elif value[key]['type'] == 'nested':
            diff.append(f'{indent}{key}: {walk(value[key]["no_diff"], depth + 1, replacer, spaces_count)}')

    diff.append(str(replacer * spaces_count * (depth - 1)) + '}')
    return '\n'.join(diff)


def convert_to_string(value):

    if isinstance(value, bool):

        if value is True:
            return 'true'
        else:
            return 'false'

    if value is None:
        return 'null'
    else:
        return value
