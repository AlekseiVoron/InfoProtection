import os

SIGNATURE_SHIFT = 1024
SIGNATURE_LENGTH = 32


def get_signature(path_to_file: str) -> bytes:
    try:
        with open(path_to_file, 'rb') as file:
            data = file.read(SIGNATURE_SHIFT + SIGNATURE_LENGTH)
            if len(data) > SIGNATURE_SHIFT:
                return data[SIGNATURE_SHIFT:]
            elif len(data) > SIGNATURE_LENGTH:
                return data[:SIGNATURE_LENGTH]
            else:
                return data
    except Exception as e:
        raise e


def find_copies_by_signature(sig: bytes, root_dir: str) -> list:
    result = []
    for current_dir, _, files in os.walk(root_dir):
        for f in files:
            path_to_file = current_dir + '\\' + f
            if sig == get_signature(path_to_file):
                result.append(path_to_file)
    return result


def main():
    file_name = ''
    signature = b''
    dir_name = ''
    copies = []
    while True:
        try:
            file_name = input('Введите путь к файлу для считывания сигнатуры: ')
            signature = get_signature(file_name)
            break
        except FileNotFoundError:
            print(f'Нет файла по заданному пути: {file_name}')
        except Exception as e:
            print(str(e))
            break
    while True:
        dir_name = input('Введите начальную директорию для поиска: ')
        if os.path.exists(dir_name):
            if os.path.isfile(dir_name):
                print(f'Указан файл. Пожалуйста, укажите директорию.')
            else:
                copies = find_copies_by_signature(signature, dir_name)
                break
        else:
            print(f'Путь не найден: {dir_name}')
    print('Файлы, найденные по сигнатуре:')
    for c in copies:
        print(c)


if __name__ == '__main__':
    main()
