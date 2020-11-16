import bitstring

POLY = 0b100000100110000010001110110110111  # 4 374 732 215. Но старший бит не учитывается (обозначает)
POLY_LEN = 32
DIVIDER = 0b100110000010001110110110111  # = POLY без старшего бита 0x04C1 1DB7, это число используется в алгоритме


def sum_calc():
    file_name = 'input.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            msg = file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return
    print('Содержимое контейнера выгружено')

    msg = bitstring.Bits(msg.encode('utf8'))#.bin
    print(f'Сообщение в битах: {msg}')
    msg2 = (msg.int << 1) & 10
    msg3 = msg[0:3]

    msg = msg + '0' * POLY_LEN  # сообщение, дополненное 32мя нулями в конце
    registry = '0' * POLY_LEN  # регистр
    while msg:
        registry = registry + msg[0]
        shifting_bit = registry[0]



if __name__ == '__main__':
    sum_calc()
