with open('6.txt', 'r') as file:
    in_hex_arr = file.read().splitlines()

with open('text.txt', 'r') as file:
    readed_file = file.read()


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def get_unhexly_str(hexly_str):
    '''
    Функция декодирует HEX-строку в байты, после чего возвращает строку.
    :rtype str
    '''
    return bytearray.fromhex(hexly_str)

def get_xored_str(unhexly_str, key):
    '''
    Функция выполняет побайтовую операцию XOR строки и ключа.
    :return: Строка, получившаяся в результации выполнения операции XOR двух переданных аргументов.
    :rtype str
    '''
    return ''.join(map(lambda sub_str: chr(sub_str ^ key), unhexly_str))


def get_uncipher_texts_arr(in_hex_str):
    '''
    Функция выполняет XOR двух строк и возвращает массив HEX-дешифрованных строк.
    :return: Массив строк.
    :rtype arr
    '''
    uncipher_texts_arr = []
    for letter in range(0, 255):
        result = get_xored_str(get_unhexly_str(in_hex_str), letter)
        uncipher_texts_arr.append(f'{result}')
    return uncipher_texts_arr


def get_histogram_count_obj(raw_text):
    '''
    Функция считает сколько раз буква встречается в тексте.
    :return: Объект, где ключ - буква, значение - сколько раз в тексте встречается
    :rtype obj
    '''
    histogram_count = {}
    for char in alphabet:
        histogram_count[char] = raw_text.count(char)
    return histogram_count


def get_histogram_percent_obj(raw_text):
    '''
    Функция считает процент, занимаемый буквой в тексте.
    :return: Объект, где ключ - буква, значение - какой процент в тексте она занимает
    :rtype obj
    '''
    histogram_percent = {}
    for key, value in get_histogram_count_obj(raw_text).items():
        histogram_percent[key] = (value / len(raw_text)) * 100
    return histogram_percent


def get_compared_obj(percent_obj1, percent_obj2):
    '''
    Функция считает разницу нормальной процентной гистограммы c проверяемой в %.
    :return: Объект, где ключ - буква, значение - разница нормальной процентной гистограммы c проверяемой в %.
    :rtype obj
    '''
    compared_obj = {}
    for key in alphabet:
        compared_obj[key] = abs(float(percent_obj1[key]) - float(percent_obj2[key]))
    return compared_obj


def get_uncipher_str(in_hex_str):
    letter_percent_values_array = []
    for text in get_uncipher_texts_arr(in_hex_str):
        normal_obj = get_histogram_percent_obj(readed_file)
        check_obj = get_histogram_percent_obj(text)

        letter_percent_value = 0
        for key in get_compared_obj(normal_obj, check_obj):
            letter_percent_value += get_compared_obj(normal_obj, check_obj)[key]

        letter_percent_values_array.append(letter_percent_value)
    return get_uncipher_texts_arr(in_hex_str)[letter_percent_values_array.index(min(letter_percent_values_array))]


def get_uncipher_str2():
    uncipher_text_array = []
    letter_percent_values_array = []

    for line in in_hex_arr:
        uncipher_text_array.append(get_uncipher_str(line))
        print(get_uncipher_str(line))

    for text in uncipher_text_array:
        normal_obj = get_histogram_percent_obj(readed_file)
        check_obj = get_histogram_percent_obj(text)

        letter_percent_value = 0
        for key in get_compared_obj(normal_obj, check_obj):
            letter_percent_value += get_compared_obj(normal_obj, check_obj)[key]

        letter_percent_values_array.append(letter_percent_value)
    print(uncipher_text_array[letter_percent_values_array.index(min(letter_percent_values_array))])

get_uncipher_str2()
