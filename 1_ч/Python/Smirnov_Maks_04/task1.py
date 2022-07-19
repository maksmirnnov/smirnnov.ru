''' Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами. '''

from sys import argv

script_name, output, rate, premium = argv

def salary_calc(output, rate, premium):
    print('Ваша зарплата составляет: ', ((output * rate) + premium))
salary_calc(int(output), int(rate), int(premium))
