''' Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров). '''

class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage": int, "bonus": int}
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus
class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')
    def get_total_income(self):
        print(f'Доход: {(self._income["wage"] + self._income["bonus"])}')
petya = Position('Petya', 'Ivanov', 30000, 5000)
petya.get_full_name()
petya.get_total_income()