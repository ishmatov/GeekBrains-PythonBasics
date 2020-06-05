"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint
len_list = int(input("Введите длину списка: "))
my_list = [randint(0, 300) for i in range(len_list)]
print(my_list)

new_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        new_list.append(my_list[i])

print(new_list)
# --------------------------------------------------------------------------------------------------------
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)