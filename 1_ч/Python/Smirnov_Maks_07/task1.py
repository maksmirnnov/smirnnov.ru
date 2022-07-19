''' Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д. '''

from itertools import zip_longest

class Matrix:
    main_list: list
    def __init__(self, main_list):
        self.main_list = main_list
    def __str__(self):
        return f'{self.main_list[0]}\n{self.main_list[1]}\n{self.main_list[2]}\n'
    def __add__(self, other):
        summed_list = []
        for other_x_ind, self_x in enumerate(self.main_list):
            summed_list.append([x + y for x, y in zip_longest(other.main_list[other_x_ind], self_x, fillvalue = 0)])
        return Matrix(summed_list)

matrix_1 = Matrix([[10, 20, 30], [4, 5, 6], [70, 80, 90]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]][::-1])
print(matrix_1 + matrix_2)




