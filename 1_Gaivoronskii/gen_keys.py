import json

from my_elgamal import *


def _input_var(name: str, min_value: int, max_value: int, must_be_prime=False) -> int:
    while True:
        try:
            tmp = int(input(f'Введите {name}: '))
            if tmp <= min_value:
                raise Exception(f'{name} должно быть больше {min_value}')
            if tmp >= max_value:
                raise Exception(f'{name} должно быть меньше {max_value}')
            if must_be_prime:
                if miller_rabin(tmp):
                    raise Exception(f'{name} должно быть простым числом')
            break
        except Exception as e:
            print(f'Ошибка: {e}')
    print(f'{name} = {tmp}')
    return tmp


def gen_keys():
    p = _input_var('часть открытого ключа p', 9, pow(10, 10), True)
    g = gen_primitive(p)
    x = random.randint(1, p-1)
    y = pow(g, x, p)
    print(f'y = {y}')
    public_key = {'p': p, 'g': g, 'y': y}
    with open("public_key.json", "w") as public_file:
        json.dump(public_key, public_file)
    print('Открытый ключ сохранён в public_key.json')
    with open("private_key.txt", "w") as private_file:
        private_file.write(str(x))
    print('Закрытый ключ сохранён в private_key.txt')


if __name__ == '__main__':
    gen_keys()
