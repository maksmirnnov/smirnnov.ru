''' Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
На сколько я понял это задание связано с предыдущим (с task4.py).'''

import task4 as cars_classes

mazda = cars_classes.TownCar(60, 'red', 'mazda')
mazda.show_speed()

lada = cars_classes.WorkCar(41, 'red', 'lada')
lada.show_speed()