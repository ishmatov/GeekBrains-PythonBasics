"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
списка. Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_f(itog, el_1):
    return itog * el_1


my_list = [el for el in range(100, 1001) if el % 2 == 0]
#my_list = [el for el in range(100, 1001, 2)]  Шаг 2 - будем получать чётные
print(my_list)

print(reduce(my_f, my_list))



print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))