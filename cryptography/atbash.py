ru_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])


def atbash(string: str, alphabet: str = ru_alphabet) -> str:
    if alphabet == '-':
        alphabet = ru_alphabet

    string = string.lower()
    alphabet = alphabet.lower()

    new_str = ''
    for char in string:
        new_str += alphabet[len(alphabet) - alphabet.index(char) - 1]
    return new_str


if __name__ == '__main__':
    try:
        alph = input('Введите алфавит (-, чтобы использовать русский по умолчанию): ')
        s = input('Введите строку для шифрования: ')
        print(f'Результат: {atbash(s, alph)}')
    except KeyboardInterrupt:
        print('\nПрограмма завершена пользователем')
