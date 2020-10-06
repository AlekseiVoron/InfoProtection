import json

from my_elgamal import encode


def encoding():
    file_name = 'alphabet.json'
    try:
        with open(file_name, 'r', encoding='utf8') as alphabet_file:
            alphabet = json.load(alphabet_file)['char_num']  # alphabet {'char': char_id}
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Кодировка:\n{alphabet}')

    file_name = 'public_key.json'
    try:
        with open(file_name, 'r', encoding='utf8') as public_file:
            public_key = json.load(public_file)
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    g = public_key['g']
    y = public_key['y']
    p = public_key['p']
    print(f'Открытый ключ: p = {p}, g = {g}, y = {y}')

    file_name = 'input.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as input_file:
            original_message = input_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print(f'Исходное сообщение: {original_message}')

    int_message = ''
    print('Перевод символов в целые числа...')
    for ch in original_message:
        ch = ch.lower()
        print(f'Кодирование символа {ch}')
        int_ch = alphabet.get(ch, None)
        if int_ch is None:
            print(f'Символа {ch} нет в текущей кодировке')
            continue
        print(f'ID символа в текущей кодировке: {int_ch}')
        int_message = int_message + str(int_ch)
    print(f'Исходный текст в виде кодов символов:\n{int_message}')

    encoded_message = ''
    print('Начало разбиения на блоки < p и шифрования...')
    while int_message:
        i = 1
        current_block = int(int_message[:i])
        while True:
            if current_block >= p or i > len(int_message):
                i = i - 1
                current_block = int(int_message[:i])
                break
            i = i + 1
            current_block = int(int_message[:i])
        print(f'Текущий блок: {current_block}')
        a, b = encode(current_block, g, y, p)
        print(f'Зашифрованный блок: {a},{b}')
        encoded_message = encoded_message + f'{a},{b} '
        int_message = int_message[i:]
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
