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
            is_dict = type(value[key]) is dict

            if not(is_dict):
                diff += f'\n{indent}{key}: {value[key]}'
                #diff += '\n' + str(replacer * spaces_count * (depth - 1)) + '}'
                continue

            if 'old' in value[key]:
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}- {key}: {walk(value[key]["old"], depth + 1)}'

            if 'new' in value[key]:
                indent = replacer * (spaces_count * (depth - 1) + 2)
                diff += f'\n{indent}+ {key}: {walk(value[key]["new"], depth + 1)}'

            if 'no_diff' in value[key]:
                diff += f'\n{indent}{key}: {walk(value[key]["no_diff"], depth + 1)}'

            if not 'no_diff' in value[key] and not 'old' in value[key] and not 'new' in value[key]:
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

# - group2: {old: {
#         abc: 12345
#         deep: {
#             id: 45
#         }}
#     }
#   + group3: {new: {
#         deep: {
#             id: {
#                 number: 45
#             }
#         }
#         fee: 100500
#     }}
# }
