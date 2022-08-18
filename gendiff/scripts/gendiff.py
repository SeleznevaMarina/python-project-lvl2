import argparse

def main():
    import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('file1', metavar='first_file')
parser.add_argument('file2', metavar='second_file')
parser.add_argument('-f', '--format', type=str, help='set format of output')

args = parser.parse_args()
print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()
