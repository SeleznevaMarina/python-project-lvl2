from gendiff import parse_arguments, generate_diff


def main():
    """Функция сравнивает два файла и выводит на экран отличия."""
    args = parse_arguments()
    diff = generate_diff(args.file1, args.file2, args.formatter)
    print(diff)


if __name__ == '__main__':
    main()
