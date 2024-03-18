'''2.	Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд»,
«Автомобиль». Определить время и стоимость перевозки для указанных городов и расстояний'''
class FreightCarrier:
    def __init__(self, name, speed, cost_per_km):
        self.name = name
        self.speed = speed
        self.cost_per_km = cost_per_km

    def calculate_time(self, distance):
        return distance / self.speed

    def calculate_cost(self, distance):
        return distance * self.cost_per_km


class Airplane(FreightCarrier):
    def __init__(self):
        super().__init__("Airplane", 800, 10)


class Train(FreightCarrier):
    def __init__(self):
        super().__init__("Train", 120, 5)


class Car(FreightCarrier):
    def __init__(self):
        super().__init__("Car", 100, 7)


distance = 500

airplane = Airplane()
train = Train()
car = Car()

print(f"Airplane: Time - {airplane.calculate_time(distance)} hours, Cost - {airplane.calculate_cost(distance)} rubles")
print(f"Train: Time - {train.calculate_time(distance)} hours, Cost - {train.calculate_cost(distance)} rubles")
print(f"Car: Time - {car.calculate_time(distance)} hours, Cost - {car.calculate_cost(distance)} rubles")