from gendiff import get_input_params, generate_diff


def main():
    """Функция сравнивает два файла и выводит на экран отличия."""
    file1, file2, format_name = get_input_params()
    diff = generate_diff(file1, file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
