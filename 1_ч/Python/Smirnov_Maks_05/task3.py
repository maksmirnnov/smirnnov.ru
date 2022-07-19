''' Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32 '''

from statistics import mean

with open('txts/text3.txt') as txt:
    salaries = []
    for ind, line in enumerate(txt):
        user = {'name': line.split(' ')[0], 'salary': line.split(' ')[1]}
        if float(user['salary']) < 20000.00:
            print(user['name'])
        salaries.append(float(user['salary']))
    print(f'{mean(salaries):.2f}')
