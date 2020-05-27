"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def check_num(value):
    try:
        return True, float(value)
    except ValueError:
        print("Не число. Попробуйте ещё раз")
        return False, -1


while True:
    check, a = check_num(input("Введите делимое: "))
    if check:
        break
while True:
    check, b = check_num(input("Введите делитель: "))
    if check:
        break
try:
    print(a / b)
except ZeroDivisionError:
    print("На 0 делить нельзя")
