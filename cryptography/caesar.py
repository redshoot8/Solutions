ru_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])


def caesar(string: str, alphabet: str = ru_alphabet, key: int = 3) -> str:
    if alphabet == '-':
        alphabet = ru_alphabet

    string = string.lower()
    alphabet = alphabet.lower()

    new_str = ''
    for char in string:
        new_str += alphabet[(alphabet.index(char) + key) % len(alphabet)]
    return new_str


if __name__ == '__main__':
    try:
        alph = input('Введите алфавит (-, чтобы использовать русский по умолчанию): ')
        s = input('Введите строку для шифрования: ')
        k = int(input('Введите ключ (число): '))
        print(f'Результат: {caesar(s, alph, k)}')
    except KeyboardInterrupt:
        print('\nПрограмма завершена пользователем')
