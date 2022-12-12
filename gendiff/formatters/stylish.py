import json


def stringify(value):

    return walk(value)


def walk(value, depth=1, replacer=' ', spaces_count=4):
    diff = ['{']

    for key in value:
        indent = replacer * spaces_count * depth

        if value[key]['type'] == 'same':
            diff.append(f'{indent}{key}: {convert_to_string(value[key]["children"], depth)}')

        elif value[key]['type'] == 'removed':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}- {key}: {convert_to_string(value[key]["old"], depth)}')

        elif value[key]['type'] == 'added':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}+ {key}: {convert_to_string(value[key]["new"], depth)}')

        elif value[key]['type'] == 'updated':
            indent = replacer * (spaces_count * (depth - 1) + 2)
            diff.append(f'{indent}- {key}: {convert_to_string(value[key]["old"], depth)}')
            diff.append(f'{indent}+ {key}: {convert_to_string(value[key]["new"], depth)}')

        elif value[key]['type'] == 'nested':
            diff.append(f'{indent}{key}: {walk(value[key]["children"], depth + 1, replacer, spaces_count)}')

    diff.append(str(replacer * spaces_count * (depth - 1)) + '}')
    return '\n'.join(diff)


def convert_to_string(value, depth):

    if type(value) is not dict:

        if isinstance(value, bool):
            return str(value).lower()

        if value is None:
            return 'null'

        return value
    add_indent = '    ' * depth
    return json.dumps(value, indent=4).replace('"', '').replace(',', '').replace('\n', f'\n{add_indent}')
