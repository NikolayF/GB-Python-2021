class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self.title}')


item1 = Pen('Текст для ручки')
item2 = Pencil('Текст для карандаша')
item3 = Handle('Текст для маркера')

item1.draw()
item2.draw()
item3.draw()