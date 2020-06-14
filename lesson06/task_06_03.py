"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров). """


class Worker:
    name = None
    surname = None

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Worker):
    position = None
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname)
        self.position = position
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

    def get_full_name(self):
        print(f"{self.name} {self.surname}: {self.position}")

    def get_total_income(self):
        return sum(self.__income.values())


p_1 = Position("Руслан", "Ишматов", "Ведущий инженер-программист", 10000, 2000)
p_1.get_full_name()
print(p_1.get_total_income())
