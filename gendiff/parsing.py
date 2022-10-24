from pathlib import Path
import json
import yaml


def get_data(path):

    with open(Path().absolute() / 'gendiff' / path, "r") as f:
        return parse_data(f, Path(path).suffix[1:])


def parse_data(raw_data, format_file):

    if format_file == 'yaml' or format_file == 'yml':
        return yaml.load(raw_data, Loader=yaml.FullLoader)
    elif format_file == 'json':
        return json.load(raw_data)
    else:
        raise IOError('Invalid file format!')
