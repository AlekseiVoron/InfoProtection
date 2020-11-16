import bitstring
import same_letters


MAX_LEN_PLAINTEXT = same_letters.MAX_LEN_PLAINTEXT


def encoding():
    container_file_name = 'container.txt'
    try:
        with open(container_file_name, 'r', encoding='utf8') as container_file:
            container_data = container_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {container_file_name}: {e}\nВыход из программы')
        return
    print('Содержимое контейнера выгружено')

    plaintext_file_name = 'plaintext.txt'
    try:
        with open(plaintext_file_name, 'r', encoding='utf8') as plaintext_file:
            plaintext = plaintext_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {plaintext_file_name}: {e}\nВыход из программы')
        return
    print(f'Открытый текст: {plaintext}')

    bits_plaintext = bitstring.Bits(plaintext.encode('utf8')).bin
    print(f'Открытый текст в битах: {bits_plaintext}')
    len_bits_plaintext = len(bits_plaintext)
    binary_len_bits_plaintext = f'{len_bits_plaintext:032b}'
    print(f'Длина бинарного представления открытого текста: {len_bits_plaintext}\n'
          f'(в бинарном виде: {binary_len_bits_plaintext})')
    if len_bits_plaintext >= MAX_LEN_PLAINTEXT:
        print(f'Превышено максимальное кол-во бит в открытом тексте ({MAX_LEN_PLAINTEXT}). Завершение работы')
        return None
    all_binary_data = binary_len_bits_plaintext + bits_plaintext
    print(f'Строка, подлежащая сокрытию: {all_binary_data}')

    ru_letters = same_letters.RU_LETTERS
    en_letters = same_letters.EN_LETTERS
    ru_en_dict = same_letters.ru_en_dict()
    with_secret = ''
    done_plaintext = False
    index_plaintext = 0
    all_binary_len = len_bits_plaintext + len(binary_len_bits_plaintext)
    print('Встраивание открытого текста в контейнер...')
    for ch in container_data:
        if not done_plaintext:
            if ch in en_letters:
                print(f'Пропуск символа {ch} (латинский символ)')
                continue
            if ch in ru_letters:
                bit_plaintext = all_binary_data[index_plaintext]
                if bit_plaintext == '1':
                    with_secret = with_secret + ru_en_dict[ch]
                else:
                    with_secret = with_secret + ch
                index_plaintext = index_plaintext + 1
                if index_plaintext == all_binary_len:
                    done_plaintext = True
                continue
        with_secret = with_secret + ch
    if not done_plaintext:
        print('Размер контейнера слишком мал для данного открытого текста. Завершение работы')
        return None

    with_secret_file_name = 'with_secret.txt'
    try:
        with open(with_secret_file_name, 'w', encoding='utf8') as with_secret_file:
            with_secret_file.write(with_secret)
    except Exception as e:
        print(f'Ошибка при открытии файла {with_secret_file_name}: {e}\nВыход из программы')
        return

    print('Сокрытое сообщение находится в with_secret.txt')


if __name__ == '__main__':
    encoding()
