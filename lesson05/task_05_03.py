"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников. """

employees = []
count_emp = 0
common_sum = 0
try:
    filename = r"txt\task_05_03.txt"
    with open(filename, "r", encoding="utf-8") as f_cool:
        for i in f_cool:
            count_emp += 1
            salary = float(i.split(" ")[1])
            fio = i.split(" ")[0]
            common_sum += salary
            if salary < 20000:
                employees.append(fio)
    if len(employees) > 0:
        print(f"Сотрудники у которых ЗП меньше 20 т.р.:")
        for i in employees:
            print(i)
    print(f"Средняя ЗП сотрудников {common_sum/count_emp:.2f}")
except IOError:
    print("Такого файла не существует")
