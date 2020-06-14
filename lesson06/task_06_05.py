"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра. """

import sys


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Пишем ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Выделяем маркером {self.title}")


Stat = {"1": "Ручка", "2": "Карандаш", "3": "Маркер"}
while True:
    print("Возьмите канцелярскую принадлежность")
    print("1 - Ручка")
    print("2 - Карандаш")
    print("3 - Маркер")
    print("0 - Закончить")
    item = input()
    if item == "0":
        sys.exit()
    elif item in Stat:
        if item == "1":
            tool = Pen("Ручка")
        elif item == "2":
            tool = Pencil("Карандаш")
        else:
            tool = Handle("Маркер")
        tool.draw()
        q = input("Закончить (y/n) ")
        if q == "y":
            break
        elif q == "n":
            print("Продолжаем работу")
        else:
            print("Неверный выбор. Продолжаем работу")
    else:
        print("Неверный выбор. Попробуйте ещё раз")
