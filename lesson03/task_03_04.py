"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def check_positive_num(value):
    try:
        if float(value) > 0:
            return True, float(value)
        else:
            print("Число должно быть положительным")
            return False, float(value)
    except ValueError:
        print("Не число. Попробуйте ещё раз")
        return False, -1


def check_negative_num(value):
    try:
        if int(value) < 0:
            return True, int(value)
        else:
            print("Число должно быть отрицательным")
            return False, int(value)
    except ValueError:
        print("Не число. Попробуйте ещё раз")
        return False, -1


def my_func1(x, y):
    return round(x ** y, 4)


def my_func2(x, y):
    i = 1
    result = x
    while i < abs(y):
        result *= x
        i += 1
    return round(1 / result, 4)


while True:
    check, x = check_positive_num(input("Введите положительное число, которое нужно возвести в степень: "))
    if check:
        break
while True:
    check, y = check_negative_num(input(f"Введите отрицательное число, степень в которую будем возводить {x}: "))
    if check:
        break
print(f"С использованием **: {x}^{y} = {my_func1(x, y)}")
print(f"С использованием цикла: {x}^{y} = {my_func2(x, y)}")
