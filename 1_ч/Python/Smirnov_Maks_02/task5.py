# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

arr = [1, 2, 4, 5]
user_num = int(input('Введите цифру: '))
for i, num in enumerate(arr):
    if user_num <= num:
        arr.insert(i, user_num)
        print(arr)
        exit()
    elif user_num > max(arr):
        arr.append(user_num)
        print(arr)
        exit()
    
