import random

from gen_table import gen_table

FREQUENCY_OF_ZEROS = 0.3  # should be in [0;1) (if it will be 1 or greater, you will have an infinity loop)


def add_in_random_index(s: str, ch: str = '0') -> str:
    """
    Put some substring into s with some frequency.
    :param s: original string
    :param ch: substring for putting
    :return: string after with substrings
    """
    i = 0
    while i < len(s):
        if random.random() < FREQUENCY_OF_ZEROS:    # random.random() give float in [0;1)
            s = s[:i] + ch + s[i:]
        i = i + 1
    return s


def encoding():
    if FREQUENCY_OF_ZEROS >= 1:
        print('Недопустимая частота незначащих нулей в шифротексте. Значение должно быть меньше 1')
        return
    file_name = 'input.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as input_file:
            original_message = input_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Исходное сообщение: {original_message}')

    table = gen_table()  # input the key and generation of the table

    int_message = ''
    table_0 = table[0]
    table_1 = table[1]
    table_2 = table[2]
    print('Шифрование...')
    for ch in original_message:
        ch = ch.upper()  # all letters must be in uppercase
        print(f'Шифрование символа {ch}')
        if ch in table_0:  # if 1st line of the table contains ch
            column = table_0.index(ch) + 1  # second digit is serial number of letter in the table
            line = random.randint(4, 9)  # first digit of the code will be randomly generated from 4-9 range
        elif ch in table_1:  # almost same as in the 1st case
            column = table_1.index(ch) + 1
            line = random.randint(2, 3)
        elif ch in table_2:  # almost same as in the 1st case
            column = table_2.index(ch) + 1
            line = 1
        else:
            print(f'Символа {ch} нет в алфавите, пропуск символа')
            continue
        code = str(line) + str(column)
        print(f'Код символа: {code}')
        int_message = int_message + code
    print(f'Зашифрованные символы:\n{int_message}')

    print('Добавление незначащих нулей...')
    encoded_message = add_in_random_index(int_message, '0')
    print(f'Шифротекст:\n{encoded_message}')

    file_name = 'encoded.txt'
    try:
        with open(file_name, 'w', encoding='utf8') as output_file:
            output_file.write(encoded_message)
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return

    print('Зашифрованное сообщение находится в encoded.txt')


if __name__ == '__main__':
    encoding()
