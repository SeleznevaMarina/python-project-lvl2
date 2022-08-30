import argparse
from pathlib import Path
from gendiff import compare

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('file1', metavar='first_file', type=Path)
    parser.add_argument('file2', metavar='second_file', type=Path)
    parser.add_argument('-f', '--format', type=str, help='set format of output')

    args = parser.parse_args()
    arg1 = Path().absolute() / 'gendiff' / args.file1
    arg2 = Path().absolute() / 'gendiff' / args.file2

    diff = compare.generate_diff(arg1, arg2)
    print(diff)

if __name__ == '__main__':
    main()
