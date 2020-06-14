"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список
сохранить в виде json-объекта в соответствующий файл. Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000,
"firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


firms_profit = {}
average_profit = {}
total_profit = 0
count_profit_firms = 0
try:
    filename = r"txt\task_05_07.txt"
    with open(filename, "r", encoding="utf-8") as f_cool:
        for s in f_cool:
            profit = 0
            item = s.split(" ")
            profit = int(item[2]) - int(item[3])
            if profit > 0:
                total_profit += profit
                count_profit_firms += 1
            firms_profit[item[0]] = profit
        average_profit["average_profit"] = total_profit / count_profit_firms

    total = [firms_profit, average_profit]
    with open(r"txt\task_05_07_out.json", "w", encoding="utf-8") as f_total:
        json.dump(total, f_total, indent=4, ensure_ascii=False)
except IOError:
    print("Такого файла не существует")
