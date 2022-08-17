import argparse

def main():
    import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('name', metavar='first_file')
parser.add_argument('name', metavar='second file')

args = parser.parse_args()
print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()
