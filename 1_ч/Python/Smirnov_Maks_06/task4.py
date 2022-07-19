''' Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости. '''

class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула {direction}')
    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость = {self.speed}')
        else:
            print(f'Внимание, превышена скорость!\n Текущая скорость = {self.speed}')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость = {self.speed}')
        else:
            print(f'Внимание, пр превышена скорость!\n Текущая скорость = {self.speed}')
class PoliceCar(Car):
    is_police = True
