from abc import ABC, abstractmethod

class Wear:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_rate(self):
        pass

class Coat(Wear):

    def __init__(self, name, v):
        Wear.__init__(self, name)
        self.v = v

    def calc_rate(self):
        print(f'Расход ткани для {self.name} составит: {self.v / 6.5 + 0.5}')

class Costume(Wear):

    def __init__(self, name, h):
        Wear.__init__(self, name)
        self.h = h

    def calc_rate(self):
        print(f'Расход ткани для {self.name} составит: {2 * self.h + 0.3}')

    #@property
    def property_release(self):
        print(f'Эта одежда называется {self.name} и её рост составляет {self.h}')


custom_wear = Wear('Просто одежда')
print(custom_wear.name)


custom_coat = Coat('Пальто зимнее', 6)
custom_coat.calc_rate()

custom_costume = Costume('Костюм спортивный', 6)
custom_costume.calc_rate()
custom_costume.property_release

