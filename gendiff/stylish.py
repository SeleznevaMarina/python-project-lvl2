def stringify(value, replacer=' ', spaces_count=1):

    if type(value) is not dict:
        return str(value)


    def walk(value, depth):
        diff = '{'
        indent = replacer * spaces_count * depth

        for key in value:

            value[key] = boolean_transformation(value[key])

            if type(value[key]) is not dict:

                if str(value[key]).startswith(' + ') or str(value[key]).startswith(' - '):
                    indent = indent - 3

                diff += f'\n{indent}{key}: {value[key]}'

            else:
                diff += f"\n{indent}{key}: {walk(value[key], depth + 1)}"
                diff += '\n' + str(indent) + '}'

        return diff

    return walk(value, 1) + '\n}'

def boolean_transformation(value):

    if value == True:
        return 'true'
    elif value == False:
        return 'false'
    elif value == None:
        return 'null'
    else:
        return value
