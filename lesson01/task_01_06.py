"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
while True:
    begin = input("Введите результат начальной пробежки. (Целое положительное число): ")
    if begin.isdigit() and int(begin) > 0:
        break

while True:
    finish = input("Введите желаемый результат (км). (Целое положительное число): ")

    if finish.isdigit() and int(finish) > 0:
        if int(finish) <= int(begin):
            print(f"Конечный результат должен быть больше начального результата - {begin} км.")
            continue
        else:
            break

result = int(begin)
day = 1
while True:
    print(f"{day}-й день: {result:.2f}")
    if result >= int(finish):
        break
    result += result * 0.1
    day += 1

print(f"Ответ: на {day}-й день спортсмен пробежит - не менее {finish} км")
