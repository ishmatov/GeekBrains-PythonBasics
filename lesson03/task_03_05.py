"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""


def sum_list(str_num):
    global result
    for el in str_num:
        if el.isdigit():
            result += int(el)
        else:
            if el == "#":
                return False
    return True


result = 0
while True:
    str_num = list(input("Введите строку чисел через 'пробел', при вводе не числа программа или стоп символа '#' будет завершена: ").split())
    if not sum_list(str_num):
        print(result)
        break
    print(result)