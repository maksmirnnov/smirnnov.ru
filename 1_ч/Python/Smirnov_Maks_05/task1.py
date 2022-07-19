''' Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка. '''

import os

print(os.getcwd())
user_text = input('Введите данные через пробел: ').split(' ')
def file_writer(mod):
    if not os.path.exists('txts/text1.txt'):
        txt = open('txts/text1.txt', mod)
        for str in user_text:
            txt.writelines(f'{str}\n')
            # print(str, file = txt)    # второй вариант строчки выше
        txt.close()
        print()
    else:
        print('Файл уже существует.')

file_writer('w')
