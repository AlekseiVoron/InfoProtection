import bitstring
RU_LETTERS = 'АВСЕТХКРМНОУауоехрск'
EN_LETTERS = 'ABCETXKPMHOYayoexpck'
MAX_LEN_CONTROL_NUMBER = 32
MAX_LEN_PLAINTEXT = 2**MAX_LEN_CONTROL_NUMBER


def ru_en_dict() -> dict:
    result = dict()
    for i in range(len(RU_LETTERS)):
        result[RU_LETTERS[i]] = EN_LETTERS[i]
    return result


if __name__ == '__main__':
    b = f'{11:032b}'
    i = int(b, 2)
    pass
