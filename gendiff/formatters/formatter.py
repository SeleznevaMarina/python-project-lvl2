from gendiff.formatters import stylish, plain, json


def format(content, format_name):

    if format_name == 'stylish':
        return stylish.stringify(content).strip()
    if format_name == 'plain':
        return plain.stringify(content).strip()
    if format_name == 'json':
        return json.stringify(content).strip()
    raise ValueError("Invalid formatter's name!")
