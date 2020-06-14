"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex_number((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):
        return Complex_number((self.a - other.a), (self.b - other.b))

    def __str__(self):
        z = "-"
        if self.b > 0:
            z = "+"
        return f"{self.a} {z} {abs(self.b)}i"


c1 = Complex_number(5, -6)
c2 = Complex_number(-3, 2)
print(c1 + c2)
print(c1 - c2)
