# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*arr):
    arr = sorted(arr)
    return int(arr[1]) + int(arr[2])

nums = input('Введите 3 числа через пробел: ').split(' ')

summ = my_func(*nums)

print(summ)