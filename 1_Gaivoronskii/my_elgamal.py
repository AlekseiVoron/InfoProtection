import random


def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def mul_by_mod(a: int, b: int, m: int) -> int:
    res = 0
    a = a % m
    while b:
        if b & 1:
            res = (res + a) % m
        a = (2 * a) % m
        b >>= 1
    return res


def gen_primitive(x: int) -> int:
    for a in range(2, x):
        if is_primitive(x, a):
            return a


def is_primitive(x, a):
    for i in range(1, a-1):
        if pow(g, i, x) == 1:
            return False
    return True


def to_binary(n: int) -> list:
    r = []
    while n > 0:
        r.append(n % 2)
        n = n // 2
    r.reverse()
    return r


def witness(a: int, n: int) -> bool:
    b = to_binary(n - 1)
    d = 1
    for b_i in b:
        x = d
        d = d ** 2 % n
        if d == 1 and x != 1 and x != n - 1:
            return True
        if b_i == 1:
            d = d * a % n
    if d != 1:
        return True
    return False


def miller_rabin(n: int, s=50) -> bool:
    for _ in range(s):
        a = random.randint(1, n - 1)
        if witness(a, n):
            return True
    return False


def gen_prime_random_from_to(min: int, max: int) -> int:
    rand_num = random.randint(min, max)
    while miller_rabin(rand_num, 50):
        rand_num = random.randint(min, max)
    return rand_num


def gen_coprime_random(x: int) -> int:
    rand_num = random.randint(1, x)
    while gcd(x, rand_num) != 1:
        rand_num = random.randint(1, x)
    return rand_num


def encode(m: int, g: int, y: int, p: int) -> tuple:
    k = gen_coprime_random(p - 1)
    print(f'Сгенерированное значение k: {k}')
    a = pow(g, k, p)
    print(f'a = {a}')
    b = mul_by_mod(pow(y, k, p), m, p)
    print(f'b = {b}')
    return a, b


def decode(ciphertext: tuple, x: int, p: int) -> int:
    a, b = ciphertext
    m = mul_by_mod(b, pow(a, p - x - 1, p), p)
    return m


if __name__ == "__main__":
    # p = gen_prime_random_from_to(pow(10, 7), pow(10, 10))
    p = 1000000009
    g = gen_primitive(p)
    x = random.randint(1001, p-1)
    y = pow(g, x, p)
    msg = 1291117911
    print(f'original msg: {msg}')
    en_msg = encode(msg, g, y, p)
    print(f'ciphertext: {en_msg}')
    dec_msg = decode(en_msg, x, p)
    print(f'decoded msg: {dec_msg}')
