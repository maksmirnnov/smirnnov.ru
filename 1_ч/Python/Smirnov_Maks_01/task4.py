num = input('Введите целое положительное число: ')
max_num = '0'
index = 0
while index < len(num):
    if max_num < num[index]:
        max_num = num[index]
    index += 1
print(max_num)
