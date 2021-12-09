class Cell:

    def __init__(self, cells):
        self.cells = '*' * cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        len_new = len(self.cells) - len(other.cells)
        if len_new > 0:
            return '*' * len_new
        else:
            return 'Клетка погибла'

    def __mul__(self, other):
        return '*' * (len(self.cells) * len(other.cells))

    def __truediv__(self, other):
        return '*' * (len(self.cells) // len(other.cells))

    def make_order(self, order):
        a_list = list(self.cells)
        output = []
        start = 1
        for i in a_list:
            if start % order == 0:
                output.append(i)
                output.append('\n')
            else:
                output.append(i)
            start += 1
        return "".join(output)

c1 = Cell(5)
c2 = Cell(2)
c3 = Cell(15)
print(f'Клетка №1: {c1.cells}')
print(f'Клетка №2: {c2.cells}')
print(f'Клетка №3: {c3.cells}')
print(f'Сложение клетки №1 и клетки №2 = {c1 + c2}')
print(f'Вычитание клетки №1 и клетки №2 = {c1 - c2}')
print(f'Умножение клетки №1 и клетки №2 = {c1 * c2}')
print(f'Деление клетки №1 и клетки №2 = {c1 / c2}')
print(f'Сортировка клетки №3:\n{c3.make_order(4)}')



