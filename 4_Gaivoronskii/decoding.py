import same_letters
import bitstring


MAX_LEN_CONTROL_NUMBER = same_letters.MAX_LEN_CONTROL_NUMBER
RU_LETTERS = same_letters.RU_LETTERS
EN_LETTERS = same_letters.EN_LETTERS


def is_same_letter(ch: str) -> bool:
    return ch in RU_LETTERS or ch in EN_LETTERS


def is_ru_letter(ch: str) -> bool:
    return ch in RU_LETTERS


def decoding():
    with_secret_file_name = 'with_secret.txt'
    try:
        with open(with_secret_file_name, 'r', encoding='utf8') as with_secret_file:
            with_secret = with_secret_file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {with_secret_file_name}: {e}\nВыход из программы')
        return
    print('Сообщение выгружено')

    control_number_str = ''
    bits_decoded_message = ''
    index = 0
    control_number = None
    print('Начало дешифрования...')
    for ch in with_secret:
        if not is_same_letter(ch):
            continue
        if control_number is None:
            if is_ru_letter(ch):
                control_number_str = control_number_str + '0'
            else:
                control_number_str = control_number_str + '1'
            index = index + 1
            if index == MAX_LEN_CONTROL_NUMBER:
                control_number = int(control_number_str, 2)
                index = 0
        else:
            if is_ru_letter(ch):
                bits_decoded_message = bits_decoded_message + '0'
            else:
                bits_decoded_message = bits_decoded_message + '1'
            index = index + 1
            if index == control_number:
                break
    print(f'Дешифрованное сообщение в битах:\n{bits_decoded_message}')
    decoded_message = bitstring.Bits(f'0b{bits_decoded_message}').bytes.decode('utf8')
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
