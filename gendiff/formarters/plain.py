def plain_formarter(value):

    if type(value) is not dict:
        return str(value)


    def walk(value, depth):
        diff = ''
        keys = list(map(startswith(('+', '-')), value.keys()))

        for (key, index) in enumerate(keys):
            value[key] = boolean_transformation(value[key])

            if key[index][1:] == key[index + 1][1:]:
                diff += f"Property {path} was updated. From {value[key]} to {value[key[index +1]]}"
        return diff

    return walk(value, 1)


def boolean_transformation(value):

    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
