from gendiff import parsing, generate_diff


def main():
    """Функция сравнивает два файла и выводит на экран отличия."""
    file1, file2, format_name = parsing.parse_files()
    diff = generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
