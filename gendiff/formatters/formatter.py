from gendiff.formatters import stylish, plain, json


def format(compare_dict, format_name):

    if format_name == 'stylish':
        return stylish.stringify(compare_dict, ' ', 4).strip()
    if format_name == 'plain':
        return plain.stringify(compare_dict).strip()
    if format_name == 'json':
        return json.stringify(compare_dict).strip()
    else:
        raise IOError("Invalid formatter's name!")
