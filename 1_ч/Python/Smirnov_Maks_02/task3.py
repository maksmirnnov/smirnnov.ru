# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

# Пример со списком.

seasons = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
answer = input('Введите номер месяца (1-12): ')
if int(answer) in seasons[0]:
    print(f'Месяц {answer} относится к времени года "{seasons[0][0]}"')
elif int(answer) in seasons[1]:
    print(f'Месяц {answer} относится к времени года "{seasons[1][0]}"')
elif int(answer) in seasons[2]:
    print(f'Месяц {answer} относится к времени года "{seasons[2][0]}"')
elif int(answer) in seasons[3]:
    print(f'Месяц {answer} относится к времени года "{seasons[3][0]}"')

# Пример со словарём
seasons = {'зима':[12, 1, 2], 'весна':[3, 4, 5], 'лето':[6, 7, 8], 'осень':[9, 10, 11]}
answer = input('Введите номер месяца (1-12): ')
for key, value in seasons.items():
    if int(answer) in value:
        print(f'Месяц {answer} относится к времени года "{key}"')
