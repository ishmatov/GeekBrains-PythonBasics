"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number_inp = int(input("Enter an integer: "))
max_num = number_inp % 10
tmp_num = number_inp // 10
while tmp_num > 0:
    if max_num < tmp_num % 10:
        max_num = tmp_num % 10
    if max_num == 9:
        break
    tmp_num //= 10

print(f'In integer \'{number_inp}\' max number - {max_num}')
