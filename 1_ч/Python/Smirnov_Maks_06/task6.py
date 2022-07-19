''' Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра. '''

class Stationery:
    title: str
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    title = 'ручка'
    def draw(self):
        print(f'Это {self.title}')
class Pencil(Stationery):
    title = 'карандаш'
    def draw(self):
        print(f'Это {self.title}')
class Handle(Stationery):
    title = 'маркер'
    def draw(self):
        print(f'Это {self.title}')
my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
