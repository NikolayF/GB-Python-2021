class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} движется прямо')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена!')
        else:
            print(f'Скорость {self.name}: {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена!')
        else:
            print(f'Скорость {self.name}: {self.speed}')


car1 = TownCar(70, 'Черный', 'Уаз')
car2 = SportCar(370, 'Красный', 'Мерседес')
car3 = WorkCar(45, 'Синий', 'Заз')
car4 = PoliceCar(250, 'Белый', 'Ваз', True)
car1.turn('налево')
car2.go()
car3.show_speed()
print(car4.is_police)
