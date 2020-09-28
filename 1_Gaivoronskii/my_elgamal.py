import random


def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def mul_by_mod(a: int, b: int, m: int) -> int:  # a * b (mod m)
    res = 0
    a = a % m
    while b:
        if b & 1:  # if b is odd
            res = (res + a) % m
        a = (2 * a) % m
        b >>= 1  # b = b / 2
    return res


def to_binary(n: int) -> list:
    """
    Return binary number as a list.
    :param n: integer, n >= 1
    :return: binary number as a list by 1 digit
    """
    r = []
    while n > 0:
        r.append(n % 2)
        n = n // 2
    r.reverse()
    return r


def witness(a: int, n: int) -> bool:
    """
    Is the number a witness to the fact that the number n is composite?
    :param a: 1 <= a <= n - 1
    :param n: odd integer, n > 2
    :return: True if a is a witness
    """
    b = to_binary(n - 1)
    d = 1
    # calculating d = a ** (n - 1) mod n
    for b_i in b:
        x = d
        d = d ** 2 % n
        # if we have a nontrivial root of 1, then n is composite
        if d == 1 and x != 1 and x != n - 1:
            return True  # composite
        if b_i == 1:
            d = d * a % n
    if d != 1:
        return True  # composite
    return False     # prime


def miller_rabin(n: int, s=50) -> bool:
    """
    Try to find a witness of to the fact that the number n is composite s times.
    :param n: odd integer, n > 2
    :param s: count of attempts (the larger it is, the less chance of mistake)
    :return: True if n is composite (100% chance), False otherwise (probably)
    """
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
    rand_num = random.randint(9999, x)
    while gcd(x, rand_num) != 1:
        rand_num = random.randint(9999, x)
    return rand_num


def encode(m: int, g: int, y: int, p: int) -> tuple:
    """
    Encoding message by ElGamal encryption algorithm.
    :param m: message (int)
    :param g: part of public key (from y=g^x mod p) (int)
    :param y: part of public key (int)
    :param p: part of public key, big prime (int)
    :return: (a: int, b: int) ciphertext
    """
    k = gen_coprime_random(p - 1)  # choose random k coprime with p-1
    print(f'Сгенерированное значение k: {k}')
    a = pow(g, k, p)  # a = g ^ k (mod p)
    print(f'a = {a}')
    b = mul_by_mod(pow(y, k, p), m, p)  # b = y ^ k * m (mod p)
    print(f'b = {b}')
    return a, b


def decode(ciphertext: tuple, x: int, p: int) -> int:
    """
    Decoding message by ElGamal encryption algorithm.
    :param ciphertext: tuple (a: int, b: int)
    :param x: private key (from y=g^x mod p) (int)
    :param p: part of public key, big prime (int)
    :return: original message
    """
    a, b = ciphertext
    # a^-1 = a^(p - 2) (mod p) => a^-x = a^(p - x - 1) (mod p)
    m = mul_by_mod(b, pow(a, p - x - 1, p), p)  # m = b / (a^x) (mod p)
    return m


if __name__ == "__main__":
    # p = gen_prime_random_from_to(pow(10, 7), pow(10, 10))
    p = 1000000009
    g = random.randint(1001, p-1)
    x = random.randint(1001, p-1)
    y = pow(g, x, p)
    msg = 1291117911
    print(f'original msg: {msg}')
    en_msg = encode(msg, g, y, p)
    print(f'ciphertext: {en_msg}')
    dec_msg = decode(en_msg, x, p)
    print(f'decoded msg: {dec_msg}')
