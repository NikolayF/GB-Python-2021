import time

class TrafficLight:

    def __init__(self, color):
        self.color = color

    def __running(self):
        data_color = [['Красный', 2], ['Желтый', 2], ['Зелёный', 4]]
        while True:
            for i in data_color:
                print(i[0])
                time.sleep(i[1])

tl = TrafficLight('Красный')

tl._TrafficLight__running()



