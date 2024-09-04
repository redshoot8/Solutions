ru_alphabet = keys={'а':'11', 'б':'12', 'в':'13', 'г':'14',
                    'д':'15', 'е':'16', 'ж':'21', 'з':'22',
                    'и':'23', 'й':'24', 'к':'25', 'л':'26',
                    'м':'31', 'н':'32', 'о':'33', 'п':'34',
                    'р':'35', 'с':'36', 'т':'41', 'у':'42',
                    'ф':'43', 'х':'44', 'ц':'45', 'ч':'46',
                    'ш':'51', 'щ':'52', 'ь':'53', 'ы':'54',
                    'ъ':'55', 'э':'56', 'ю':'61', 'я':'62'}


def polyby_square(string: str, alphabet: dict = ru_alphabet, key: int = 3) -> str:
    string = list(string.lower())

    new_str = ''
    for char in string:
        new_str += ru_alphabet.get(char, char + char) + ' '
    return new_str


if __name__ == '__main__':
    try:
        s = input('Введите строку для шифрования: ')
        print(f'Результат: {polyby_square(s)}')
    except KeyboardInterrupt:
        print('\nПрограмма завершена пользователем')
