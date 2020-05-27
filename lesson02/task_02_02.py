"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
result_list = []
while True:
    el = input(f"({len(result_list)}) Введите элемент списка. Для выхода введите 0: ")
    if el != "0":
        result_list.append(el)
    else:
        break

print(result_list)
i = 0

while i < len(result_list)-1:
    temp = result_list[i]
    result_list[i] = result_list[i + 1]
    result_list[i + 1] = temp
    i += 2

print(result_list)
