''' Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30} '''

import io, re

def my_regexp(obj):
    for keys, values in obj.items():
        key = ''.join(re.findall(r"[^\:]", keys))
        value = re.split('\D', values)
        summ = 0
        for num in value:
            if num:
                summ += int(num)
        new_obj = {key: summ}
        return new_obj

with io.open('txts/text6.txt', encoding='utf-8') as txt:
    my_obj = {}.copy()
    for line in txt:
        line_obj = line.split(' ')
        line_obj = {f'{line_obj[0]}': ''.join(line_obj[1:])}
        my_obj.update(my_regexp(line_obj))
    print(my_obj)
