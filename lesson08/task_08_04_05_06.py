"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""
import os
ID = 0

all_items = {}


class Storage:
    def __init__(self, title):
        self.title = title
        self.items = {"printer": {1: 5, 2: 3}, "scanner": {}, "copier": {}}
        # self.save_items = []

    def add(self, obj, count):
        if obj.type in self.items:
            if obj.ID in self.items[obj.type]:
                self.items[obj.type][obj.ID] += count
            else:
                self.items[obj.type][obj.ID] = count
            print("Добавленно")
        else:
            print("Это хранится на другом складе")

    def add_id(self, id, count):
        t = all_items[id].get("type")
        if id in self.items[t]:
            self.items[t][id] += count
        else:
            self.items[t][id] = count
        print("Добавленно")


    def __str__(self):
        s = ""
        for item in self.items:
            if len(self.items[item]) > 0:
                print(item)
                for i in self.items[item].keys():
                    if self.items[item].get(i) > 0:
                        print(f"ID[{i}]", end=" - ")
                        print(all_items.get(i), end=":\t ")
                        print(self.items[item].get(i), "шт.")
        return s

    def transfer_to(self, id, count):
        t = all_items[id].get("type")
        if id in self.items[t]:
            self.items[t][id] -= count
        print("Товар передан")

    @property
    def count(self):
        return len(self.save_items)


class Office_equipment:
    def __init__(self, title, creator):
        global ID
        ID += 1
        self.ID = ID
        self.title = title
        self.creator = creator

    @staticmethod
    def info(ID):
        print(all_items.get(ID))


class Printer(Office_equipment):
    def __init__(self, title, creator, is_color):
        super().__init__(title, creator)
        self.type = "printer"
        self.is_color = is_color
        all_items[self.ID] = {"title": self.title, "creator": self.creator, "type": self.type,
                              "is_color": self.is_color}


class Scanner(Office_equipment):
    def __init__(self, title, creator, speed_scan, dpi):
        super().__init__(title, creator)
        self.type = "scanner"
        self.speed_scan = speed_scan
        self.dpi = dpi
        all_items[self.ID] = {"title": self.title, "creator": self.creator, "type": self.type,
                              "speed_scan": self.speed_scan, "dpi": self.dpi}


class Copier(Office_equipment):
    def __init__(self, title, creator, is_color, speed_copy):
        super().__init__(title, creator)
        self.type = "copier"
        self.is_color = is_color
        self.speed_copy = speed_copy
        all_items[self.ID] = {"title": self.title, "creator": self.creator, "type": self.type,
                              "is_color": self.is_color, "speed_copy": self.speed_copy}


def add_new_product():
    while True:
        print("1 - Принтер")
        print("2 - Сканер")
        print("3 - Ксерокс")
        print("0 - В главное меню")
        menu = input()
        if menu == "1":
            title = input("Введите название: ")
            creator = input("Введите производителя: ")
            is_color = input("Цветной (1) / Ч/Б (2): ")
            if is_color == "1":
                is_color = True
            elif is_color == "1":
                is_color = False
            else:
                is_color = False
            print("Добавлен новый принтере")
            return Printer(title, creator, is_color)
        elif menu == "2":
            title = input("Введите название: ")
            creator = input("Введите производителя: ")
            speed_scan = int(input("Введите скорость сканирования: "))
            dpi = int(input("Введите DPI: "))
            print("Добавлен новый сканер")
            return Scanner(title, creator, speed_scan, dpi)
        elif menu == "3":
            title = input("Введите название: ")
            creator = input("Введите производителя: ")
            is_color = input("Цветной (1) / Ч/Б (2): ")
            if is_color == "1":
                is_color = True
            elif is_color == "1":
                is_color = False
            else:
                is_color = False
            speed_copy = int(input("Введите скорость копирования: "))
            print("Добавлен новый ксерокс")
            return Copier(title, creator, is_color, speed_copy)
        elif menu == "0":
            return 0
        else:
            print("Не верный пункт меню")


storage = Storage("Главный склад")
p1 = Printer("5050", "HP", False)
p2 = Printer("M123", "LG", True)
s1 = Scanner("789", "Samsung", 24, 1600)
s2 = Scanner("102", "HP", 12, 800)
c1 = Copier("X800", "Xerox", False, 80)
c2 = Copier("MN4578", "Samsung", True, 24)

storage.add(p1, 5)
storage.add(p2, 3)
storage.add(s1, 1)
storage.add(s2, 2)
storage.add(c1, 7)
storage.add(c2, 8)

while True:
    print("1 - Добавить новый товар")
    print("2 - Передать товар на склад")
    print("3 - Передать товар в подразделение")
    print("4 - Информация о товарах на складе")
    print("0 - Выход")
    menu = input("Выбери пункт меню: ")
    if menu == "1":
        add_new_product()
    elif menu == "2":
        for item in all_items:
            print(f"{item}  - {all_items.get(item)}")
        id = int(input("Выберите ID элемента, который поступил на склад. Для выхода введите '0': "))
        if id != 0 and id in all_items.keys():
            count = int(input("Введите кол-во этого товара поступившего на склад: "))
            if count > 0:
                storage.add_id(id, count)
    elif menu == "3":
        print(storage)
        id = int(input("Введите ID товара, который будет передана, для выхода введите '0': "))
        if id != 0:
            count = int(input("Введите кол-во передаваемого товара: "))
            storage.transfer_to(id, count)
    elif menu == "4":
        print(storage)
    elif menu == "0":
        break
    else:
        print("Не верный пункт меню")