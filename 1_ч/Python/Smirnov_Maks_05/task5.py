''' Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. '''

numbers = input('Введите числа через пробел: ')
with open('txts/text5.txt', 'w+') as txt:
    print(numbers, file = txt)
    txt.seek(0)
    text = txt.readline().split(' ')
    summ = 0
    for num in text:
        summ += int(num)
    print(summ)
