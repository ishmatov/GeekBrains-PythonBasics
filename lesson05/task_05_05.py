"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from random import randint
len_list = int(input("Введите длину списка: "))
my_list = [str(randint(-50, 50)) for i in range(len_list)]

filename_out = r"txt\task_05_05.txt"
with open(filename_out, "w+", encoding="utf-8") as f_cool:
    for i in my_list:
        f_cool.write(i + " ")
    f_cool.seek(0)
    str = f_cool.read()
    str_list = str.split(" ")
    print(str)
    nums = [int(item) for item in str_list[:len(str_list)-1]]

print(f"Сумма всех элементов равна: {sum(nums)}")

