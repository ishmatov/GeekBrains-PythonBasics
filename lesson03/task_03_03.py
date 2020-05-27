"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def check_num(value):
    try:
        return True, int(value)
    except ValueError:
        print("Не число. Попробуйте ещё раз")
        return False, -1


def sum_doble_max(num1, num2, num3):
    return max(num1 + num2, num1 + num3, num2 + num3)


i = 0
list_num = []
while True and i < 3:
    check, num = check_num(input(f"{i + 1} - Введите целое число: "))
    if check:
        list_num.append(num)
        i += 1

print(f"Сумма из двух максимальных числе из {list_num} = ", sum_doble_max(list_num[0], list_num[1], list_num[2]))
