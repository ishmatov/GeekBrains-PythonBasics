"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т """


class Road:
    __length = None
    __width = None
    __mass = None
    __thickness = None

    def __init__(self, length, width, mass=25, thickness=5):
        if length <= 0:
            raise TypeError("Длина дороги не может быть меньше 0")
        if width <= 0:
            raise TypeError("Ширина дороги не может быть меньше 0")
        if mass <= 0:
            raise TypeError("Масса не может быть меньше 0")
        if thickness <= 0:
            raise TypeError("Толщина не может быть меньше 0")
        self.__length = length
        self.__width = width
        self.__mass = mass
        self.__thickness = thickness

    def payment(self):
        return f"{(self.__length * self.__width * self.__mass * self.__thickness)/1000} т."


road = Road(5000, 20)
print(road.payment())