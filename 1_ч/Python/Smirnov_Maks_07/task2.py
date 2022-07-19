''' Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property. '''

from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
    def __add__(self, other):
        return (f'Общий расход ткани составляет: {float(self.get_expance) + float(other.get_expance):.2f}')
    @abstractmethod
    def get_expance(self):
        pass

class ClothesCoatType(Clothes):
    def __str__(self):
        return self.type
    def __init__(self, size: int):
        self.size = size
        self.type = 'Пальто'
    @property
    def get_expance(self):
        return f'Расход ткани на пальто составляет: {self.size / 6.5 + 0.5:.2f}'

class ClothesCostumeType(Clothes):
    def __str__(self):
        return self.type
    def __init__(self, height: int):
        self.type = 'Костюм'
        self.height = height
    @property
    def get_expance(self):
        return f'Расход ткани на костюм составляет: {2 * self.height + 0.3:.2f}'

coat = ClothesCoatType(42)
print(coat.get_expance)

costume = ClothesCostumeType(42)
print(costume.get_expance)

print(coat + costume)