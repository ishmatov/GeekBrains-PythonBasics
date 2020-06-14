"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
 одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
 типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
 соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V < 50:
            self.__V = 50
        elif V > 210:
            self.__V = 210
        else:
            self.__V = V

    @property
    def tissue_consumption(self):
        return round(self.V / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H < 26:
            self.__H = 26
        elif H > 62:
            self.__H = 62
        else:
            self.__H = H

    @property
    def tissue_consumption(self):
        return round(2 * self.H + 0.3, 2)


coat = Coat(150)
costume = Costume(52)
print(coat.tissue_consumption)
print(costume.tissue_consumption)