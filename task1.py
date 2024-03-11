'''1.	Создать класс с двумя переменными.
Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных, и функцию которая находит
наибольшее значение из этих двух переменных.'''
class Summ:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_variables(self):
        print(f'Первая переменная х {self.x}, Вторая переменная y {self.y}')

    def set_variables(self, x1: int, x2: int):
        self.x = x1
        self.y = y1

    def summ_variables(self):
        print(f'Сумма введенных переменных = {self.x + self.y}')

    def find_max(self):
        if self.x > self.y:
            print(f'Переменная х = {self.x} больше переменной у = {self.y}')
        else:
            print(f'Переменная y = {self.y} больше переменной x = {self.x}')


object = Summ(12, 7)
object.get_variables()
object.summ_variables()
object.find_max()
