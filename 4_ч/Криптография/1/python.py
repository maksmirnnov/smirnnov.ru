# ------------------------------------------ for key, value in person.items()

# person = {
#     "name": "John",
#     "age": 26,
#     "job": "programmer"
# }

# for key, value in person.items():
#     print(f'Key {key} = {value}')

# ------------------------------------------

# arr = [1, 2, 3, 3, 5, 5, 6, 9, 8]
# print( 'unic ', list(set(arr)) )
# print(
#     max(set(arr), key=arr.count)
# )

# for n in set(arr):
#     print(f'{n}: {arr.count(n)}')

# ------------------------------------------ *args **kwargs

# names = ['Maks', 'Jane', 'Masha', 'Alex']

# def say_hello(*name_list):
#     for name in name_list:
#         print(f'Hello, {name}')

# say_hello(*names)

# ------------------------------------------ GLOBAL SCOPE

# number = 1

# def global_scope(some_number):
#     global result
#     result = some_number + 1

# global_scope(number)

# print(number)
# print(result)

# ------------------------------------------ NONLOCAL SCOPE

# def nonlocal_scope():
#     start = 0

#     def nonlocal_scope2():
#         nonlocal start
#         start += 1
    
#     nonlocal_scope2()
    
#     print(start)

# nonlocal_scope()

# ------------------------------------------ COMMENTS

# def hello(world):
#     """
#     :param world: Кого приветствуем
#     :return: Строка приветствия
#     :rtype str
#     """

#     return f'Hello, {world}!!!'

# hello('Maks')


import random

names = ['Maks', 'Jane', 'Masha', 'Alex']

rand_names = random.choice(names)

print(rand_names)
