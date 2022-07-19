# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_answer = int(input('Введите время в секундах: '))
hours = 0
minutes = 0
sec = user_answer

while sec >= 60:
    if sec >= 60:
        minutes += 1
        sec -= 60
    if minutes >= 60:
        hours += 1
        minutes -= 60
if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if sec < 10:
    sec = f'0{sec}'

print('{} секунд это {}:{}:{}'.format(user_answer, hours, minutes, sec))