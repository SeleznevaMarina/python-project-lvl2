import argparse
from pathlib import Path


def parse_files():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file1', metavar='first_file', type=Path)
    parser.add_argument('file2', metavar='second_file', type=Path)
    parser.add_argument('-f', '--format', dest='formarter', type=str, default='stylish', help='set format of output')

    args = parser.parse_args()
    return (args.file1, args.file2, args.formarter)

    __all__ = ('parse_files')
