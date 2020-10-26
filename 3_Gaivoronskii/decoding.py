from gen_table import gen_table

AVAILABLE_DIGITS = '123456789'


def _get_letter_by_code(table: list, first_dig: str, second_dig: str) -> str:
    """
    Get letter from the table by two digits of code.
    :param table: list with 2 dimensions
    :param first_dig: string, but probably int
    :param second_dig: string, but probably int
    :return: found letter or nothing
    """
    try:
        if first_dig == '1':
            return table[2][int(second_dig) - 1]
        elif first_dig == '2' or first_dig == '3':
            return table[1][int(second_dig) - 1]
        else:
            return table[0][int(second_dig) - 1]
    except IndexError:
        print(f'Неизвестный символ с кодом {first_dig}{second_dig}')
        return ''


def decoding():
    table = gen_table()  # generation of the table by key from key.txt
    if not table:
        print('Таблица по ключу не сгенерированна. Завершение работы.')
        return

    file_name = 'encoded.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as encoded_file:
            encoded_message = encoded_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Зашифрованное сообщение: {encoded_message}')

    decoded_message = ''
    print('Начало дешифрования...')
    i = 0
    len_encoded = len(encoded_message)
    first_digit = ''  # 1st digit of two-digits code
    while i < len_encoded:
        cur_digit = encoded_message[i]  # next digit from ciphertext
        i = i + 1
        if cur_digit not in AVAILABLE_DIGITS:  # skip the zeros and other symbols
            print(f'Пропуск символа {cur_digit} в шифрограмме')
            continue
        if not bool(first_digit):
            first_digit = cur_digit  # if we don't have a first digit, this one will be the first digit
            continue
        decoded_char = _get_letter_by_code(table, first_digit, cur_digit)
        first_digit = ''
        if not bool(decoded_char):
            continue
        print(f'Дешифрованный символ: {decoded_char}')
        decoded_message = decoded_message + decoded_char
    print(f'Дешифрованное сообщение:\n{decoded_message}')

    file_name = 'output.txt'
    try:
        with open(file_name, 'w', encoding='utf8') as output_file:
            output_file.write(decoded_message)
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return

    print('Расшифрованное сообщение находится в output.txt')


if __name__ == '__main__':
    decoding()
