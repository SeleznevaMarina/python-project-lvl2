from pathlib import Path
import json
import yaml


def get_data(path):

    with open(Path().absolute() / 'gendiff' / path, "r") as f:
        return parse(f, Path(path).suffix[1:])


def parse(content, format_name):

    if format_name == 'yaml' or format_name == 'yml':
        return yaml.load(content, Loader=yaml.FullLoader)
    else:
        return json.load(content)
    raise ValueError("Invalid file format!")
