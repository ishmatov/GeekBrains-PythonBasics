"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


import sys


class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} завелась. Цвет {self.color}")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость - {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - \033[31m{self.speed}\033[0m")
        if self.speed > 60:
            print("\033[31mПревышение скорости!!!\033[0m")


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - \033[31m{self.speed}\033[0m")
        if self.speed > 40:
            print("\033[31mПревышение скорости!!!\033[0m")


class SportCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - \033[31m{self.speed}\033[0m")
        if self.speed > 90:
            print("\033[31mПревышение скорости!!!\033[0m")


class PoliceCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - \033[31m{self.speed}\033[0m")
        if self.speed > 120:
            print("\033[31mОпасная скорость!!!\033[0m")


car_name = {"1": "TownCar", "2": "WorkCar", "3": "SportCar", "4": "PoliceCar"}
car_color = {"1": "Белый", "2": "Чёрный", "3": "Красный", "4": "Жёлтый"}
exit_check = False

print("\033[30m\033[41mNeed for speed на минималках\033[0m")
while True:
    print("Выберите машину")
    print("1 - Городская")
    print("2 - Грузовая")
    print("3 - Спортивная")
    print("4 - Полиция")
    print("0 - Выход")
    car_name_input = input()
    if car_name_input == "0":
        sys.exit()
    elif car_name_input in car_name:
        print(f"Выбрана {car_name.get(car_name_input)}")
        break
    else:
        print("Не верный выбор")

if car_name_input != "4":
    while True:
        print("Выберите цвет машины")
        print("1 - Белый")
        print("2 - Чёрный")
        print("3 - Красный")
        print("4 - Жёлтый")
        print("0 - Выход")
        car_color_input = input()
        if car_color_input == "0":
            sys.exit()
        elif car_color_input in car_color:
            print(f"Выбрана {car_color.get(car_color_input)} цвет")
            break
        else:
            print("Не верный выбор")

if car_name_input == "1":
    car = TownCar(0, car_color.get(car_color_input), car_name.get(car_name_input))
if car_name_input == "2":
    car = WorkCar(0, car_color.get(car_color_input), car_name.get(car_name_input))
if car_name_input == "3":
    car = SportCar(0, car_color.get(car_color_input), car_name.get(car_name_input))
if car_name_input == "4":
    car = PoliceCar(0, "Белый", car_name.get(car_name_input))


car.go()
car.speed += 40
while True:
    car.show_speed()
    q_speed = input("Ускориться? (y/n): ")
    if q_speed == "y":
        car.speed += 10
    elif q_speed == "n":
        car.speed = car.speed
    else:
        print("Неверный выбор. Продолжаем движение с той же скоростью")
    car.show_speed()
    q_turn = input("Перекрёсток. Повернуть? (y/n): ")
    if q_turn == "y":
        q_turn_side = input("Направо (r) / Налево (l): ")
        if q_turn_side == "r":
            car.turn("Направо")
        elif q_turn_side == "l":
            car.turn("Налево")
        else:
            print("Неверный выбор. Продолжаем движение прямо")
    elif q_turn == "n":
        print("Продолжаем движение прямо")
    else:
        print("Неверный выбор. Продолжаем движение прямо")

    q_stop = input("Остановиться? (y/n): ")
    if q_stop == "y":
        car.stop()
        break
    elif q_stop == "n":
        print("Продолжаем движение")
    else:
        print("Неверный выбор. Продолжаем движение")
