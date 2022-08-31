import argparse
from pathlib import Path
from gendiff import compare


def main():

    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file1', metavar='first_file', type=Path)
    parser.add_argument('file2', metavar='second_file', type=Path)
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()

    diff = compare.generate_diff(args.file1, args.file2)
    print(diff)


if __name__ == '__main__':
    main()
