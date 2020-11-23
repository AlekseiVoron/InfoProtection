import bitstring

POLY = '00000100110000010001110110110111'  # = 79764919 = 0x04C1 1DB7. Коэффициенты выбранного полинома
# В действительности коэффициенты искомого полинома указаны без учёта старшего единичного бита,
# который не участвует в вычислениях из-за специфики реализации. Полный вид полинома:
# (1)00000100110000010001110110110111
POLY_LEN = 32  # разрядность полинома


def _xor_with_poly(x: list):
    """
    Операция XOR между x и POLY.

    :param x:
    :return:
    """
    for i in range(POLY_LEN):
        if POLY[i] == '1':
            x[i] = '0' if x[i] == '1' else '1'


def _bin_to_decimal(x: str) -> int:
    """
    Перевод двоичного числа из строки в десятичное целое

    :param x: строка - двоичное число
    :return: целое десятичное число
    """
    i = len(x) - 1
    res = 0
    for t in x:
        if t == '1':
            res = res + 2 ** i
        i = i - 1
    return res


def sum_calc():
    file_name = 'input.txt'
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            original_msg = file.read()
    except Exception as e:
        print(f'Ошибка при открытии файла {file_name}: {e}\nВыход из программы')
        return

    msg = bitstring.Bits(original_msg.encode('utf8')).bin  # перевод сообщения в двоичный вид

    msg = msg + '0' * POLY_LEN          # сообщение дополненняется 32мя нулями в младших разрядах
    registry = list('0' * POLY_LEN)     # регистр
    while msg:
        registry.append(msg[0])         # вносим в младший разряд регистра очередной бит сообщения
        msg = msg[1:]                   # убираем бит, внесённый в регистр, из сообщения
        shifting_bit = registry.pop(0)  # "выдвигаем" бит из старшего разряда регистра
        if shifting_bit == '1':         # если этот бит был единицей
            _xor_with_poly(registry)    # производим операцию XOR между регистром и полиномом

    checksum_bin = ''.join(registry)            # контрольная сумма в бинарном виде
    checksum = _bin_to_decimal(checksum_bin)    # контрольная сумма в десятичном виде
    print(f'Контрольная сумма: {checksum} ({checksum_bin})')


if __name__ == '__main__':
    sum_calc()
