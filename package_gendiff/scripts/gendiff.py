from package_gendiff import gendiff, parsing
#from gendiff import generate_diff


def main():
    """Функция сравнивает два файла и выводит на экран отличия."""
    file1, file2, format_name = parsing.parse_files()
    diff = gendiff.generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
