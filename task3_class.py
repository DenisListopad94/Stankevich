'''3.	Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет. Представитель каждого
класса может умереть, если достигнет определенного возраста или для него не будет еды.
Напишите виртуальные методы поедания и определения состояния живого существа (живой или нет,
в зависимости от достижения предельного возраста и наличия еды (входной параметр)).'''
class LivingThing:
    def __init__(self, age_limit):
        self.age = 0
        self.age_limit = age_limit
        self.alive = True

    def eat(self):
        pass

    def check_status(self, food_available):
        if self.age >= self.age_limit or not food_available:
            self.alive = False
            print(f" {self.__class__.__name__} умирает.")
        else:
            print(f"This {self.__class__.__name__} остается живым.")


class Fox(LivingThing):
    def eat(self, prey):
        print(f"Лиса ест {prey.__class__.__name__}.")
        prey.alive = False


class Rabbit(LivingThing):
    def eat(self, food):
        if isinstance(food, Plant):
            print(f"Кролик ест {food.__class__.__name__}.")
            food.available = False
        else:
            print("Кролик ест только растения!")


class Plant(LivingThing):
    def __init__(self, age_limit):
        super().__init__(age_limit)
        self.available = True

    def eat(self):
        print("Растение поглощает солнечный свет.")


fox = Fox(age_limit=5)
rabbit = Rabbit(age_limit=3)
plant = Plant(age_limit=10)

print("Initial statuses:")
fox.check_status(food_available=True)
rabbit.check_status(food_available=True)
plant.check_status(food_available=True)

print("\nЛиса ест кролика:")
fox.eat(rabbit)
rabbit.check_status(food_available=True)

print("\nКролик ест растение:")
rabbit.eat(plant)
plant.check_status(food_available=True)

print("\nРастение питается солнечным светом:")
plant.eat()
