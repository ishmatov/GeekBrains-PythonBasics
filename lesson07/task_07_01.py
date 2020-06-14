"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
from random import randint

x = randint()


class Matrix:
    def __init__(self, my_m):
        self.my_m = my_m

    def __add__(self, other):
        m = []
        i = 0
        while i < len(self.my_m):
            j = 0
            mm = []
            while j < len(self.my_m[i]):
                mm.append(self.my_m[i][j] + other.my_m[i][j])
                j += 1
            m.append(mm)
            i += 1
        return Matrix(m)

    def __str__(self):
        s = ""
        for row in self.my_m:
            for el in row:
                s += str(el) + "\t"
            s += "\n"
        return s


class MatrixNew:
    my_m = []

    def __init__(self, rows, columns):
        if columns <= 0 or rows <= 0:
            raise TypeError("Размерность матрицы должна быть положительной")
        i = 0
        m = []
        while i < columns:
            r = []
            j = 0
            while j < rows:
                r.append(randint(-10, 10))
                j += 1
            m.append(r)
            i += 1
        self.my_m = m

    def __str__(self):
        s = ""
        for row in self.my_m:
            for el in row:
                s += str(el) + "\t"
            s += "\n"
        return s

    def __add__(self, other):
        m = []
        i = 0
        while i < len(self.my_m):
            j = 0
            mm = []
            while j < len(self.my_m[i]):
                mm.append(self.my_m[i][j] + other.my_m[i][j])
                j += 1
            m.append(mm)
            i += 1
        return Matrix(m)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[6, 5], [4, 3], [2, 1]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

m1 = MatrixNew(5, 5)
m2 = MatrixNew(5, 5)
print(m1)
print(m2)
print(m1 + m2)

