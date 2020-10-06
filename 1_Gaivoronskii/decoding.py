import json

from my_elgamal import decode

ONE_SYMBOL_LEN_IN_ALPHABET = 4
UNKNOWN_SYMBOLS_LIMIT = 3


def decoding():
    file_name = 'alphabet.json'
    try:
        with open(file_name, 'r', encoding='utf8') as alphabet_file:
            alphabet = json.load(alphabet_file)['num_char']  # alphabet {char_id: 'char'}
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Кодировка:\n{alphabet}')

    file_name = 'private_key.txt'
    try:
        with open(file_name, 'r') as private_file:
            x = int(private_file.read())
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Закрытый ключ: x = {x}')

    file_name = 'public_key.json'
    try:
        with open(file_name, 'r') as public_file:
            public_key = json.load(public_file)
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    p = public_key['p']
    print(f'Открытый ключ: p = {p}')

    file_name = 'encoded.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as encoded_file:
            encoded_message = encoded_file.read().split(' ')
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Зашифрованное сообщение: {encoded_message}')

    decoded_message = ''
    print('Начало дешифрования...')
    for block in encoded_message:
        if not block:
            continue
        print(f'Дешифрование блока {block}')
        a, b = block.split(',')
        decoded_block = decode((int(a), int(b),), x, p)
        print(f'Дешифрованный блок: {decoded_block}')
        decoded_message = decoded_message + str(decoded_block)
    print(f'Дешифрованное сообщение:\n{decoded_message}')

    non_int_message = ''
    wrong_symbols = 0
    print('Перевод сообщения в символьный вид...')
    while decoded_message:
        int_ch = int(decoded_message[:ONE_SYMBOL_LEN_IN_ALPHABET])
        int_ch_str = str(int_ch)
        non_int_ch = alphabet.get(int_ch_str, None)
        if non_int_ch is None:
            print(f'Символа {int_ch_str} нет в текущей кодировке')
            wrong_symbols = wrong_symbols + 1
            decoded_message = decoded_message[ONE_SYMBOL_LEN_IN_ALPHABET:]
            continue
        print(f'Символ в текущей кодировке: {non_int_ch}')
        decoded_message = decoded_message[ONE_SYMBOL_LEN_IN_ALPHABET:]
        non_int_message = non_int_message + non_int_ch
    if wrong_symbols > UNKNOWN_SYMBOLS_LIMIT:
        non_int_message = 'Внимание! Возможно, сообщение было повреждено!\n' + non_int_message
    print(f'Восстановленное сообщение:\n{non_int_message}')

    file_name = 'output.txt'
    try:
        with open(file_name, 'w', encoding='utf8') as output_file:
            output_file.write(non_int_message)
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return

    print('Расшифрованное сообщение находится в output.txt')


if __name__ == '__main__':
    decoding()
