"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """

class NullExepton(Exception):
    def __init__(self, text):
        self.text = text


x = input("Введите делимое: ")
y = input("Введит делитель: ")
try:
    if int(y) == 0:
        raise NullExepton("Делить на '0' нельзя")
    print(int(x)/int(y))
except NullExepton as err:
    print(err)
except ValueError as err:
    print(err)
