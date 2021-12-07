class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self):
        return print(f'{self._Road__length}м * {self._Road__width}м * 25кг * 5см = {self._Road__length * self._Road__width * 25 * 5 / 1000}')

new_road = Road(20, 5000)

new_road.calculate_mass()
