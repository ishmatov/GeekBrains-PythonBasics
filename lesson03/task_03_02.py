"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user(firsrname, lastname, year, sity, email, tel):
    print(f"{firsrname} {lastname}: |"
          f"Год рождения: {year}, "
          f"Город проживания: {sity}, "
          f"email: {email}, "
          f"tel: {tel}")


firsrname = input("Введите имя: ")
lastname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
sity = input("Введите город проживания: ")
email = input("Введите email: ")
tel = input("Введите телефон: ")

print_user(firsrname, lastname, year, sity, email, tel)
