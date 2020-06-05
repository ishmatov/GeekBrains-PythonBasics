"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами. """

from sys import argv

name, production, rate, bonus = argv
#production, rate, bonus = map(int, argv[1:])
changes = True
for i in range(1, len(argv)):
    if not argv[i].isdigit():
        changes = False
        print(f"Параметер № {i} ({argv[i]}) - не является числом")

if changes:
    wage = (int(production) * int(rate)) + int(bonus)
    print(wage)



