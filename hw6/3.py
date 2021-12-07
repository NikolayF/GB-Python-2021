class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'Имя и отчетсво сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учётом премии: {self._Worker__income["wage"] + self._Worker__income["bonus"]}')

user1 = Position('Иван', 'Иванов', 'Простой работник', 50000, 30000)
user2 = Position('Петр', 'Петров', 'Работник', 100000, 50000)
user3 = Position('Сидр', 'Сидоров', 'Старший работник', 150000, 80000)

user1.get_full_name()
user1.get_total_income()
user2.get_full_name()
user2.get_total_income()
user3.get_full_name()
user3.get_total_income()
