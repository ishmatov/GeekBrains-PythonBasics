"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


class Date:
    def __init__(self, date="01-01-1970"):
        self.date = date

    @classmethod
    def get(cls, date, t):
        d = list(map(int, date.split("-")))
        if t == "d" or t == "D":
            result = d[0]
        elif t == "m" or t == "M":
            result = d[1]
        elif t == "y" or t == "Y":
            result = d[2]
        return result

    @staticmethod
    def check(date):
        day = Date.get(date, "d")
        month = Date.get(date, "m")
        year = Date.get(date, "y")

        if month <= 0 or month > 12:
            return False
        if year < 1900 or year > 9999:
            return False
        if 1 <= day <= 31:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                return True
            elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30:
                return True
            elif month == 2:
                if Date.__check_leap_year(year):
                    if day <= 29:
                        return True
                elif day <= 28:
                    return True
            else:
                return False
        else:
            return False

    @staticmethod
    def __check_leap_year(year):
        if year % 4 != 0:
            return False
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True


print(Date.get("23-04-1984", "d"))
print(Date.get("23-04-1984", "m"))
print(Date.get("23-04-1984", "y"))

if Date.check("29-02-2020"):
    print("OK")
else:
    print("Bad")