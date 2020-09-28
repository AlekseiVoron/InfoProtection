import json

ALPHABET_STR = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,;:!?&^\t_-—=+-*8/$%#№@"'<>`~(){}[]|\\'''


def make_alphabet_dicts_from_str(s: str, start_num=1111) -> (dict, dict):
    if start_num < 0 or start_num > pow(10, 20):
        raise Exception('Wrong start_num!')
    i = start_num
    num_char = dict()
    char_num = dict()
    for ch in s:
        while '0' in str(i):
            i = i + 1
        num_char[i] = ch
        char_num[ch] = i
        i = i + 1
    return num_char, char_num


if __name__ == '__main__':
    num_char, char_num = make_alphabet_dicts_from_str(ALPHABET_STR)
    data = {
        'num_char': num_char,
        'char_num': char_num
    }
    with open("alphabet.json", "w", encoding='utf8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)
