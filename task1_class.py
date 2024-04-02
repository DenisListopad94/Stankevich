'''1. Определить класс «Шахматная фигура» с ее координатами на шахматной доске, ее цветом (черный или белый),
виртуальным методом «битья» другой фигуры, и унаследовать от него классы, соответствующие шахматным фигурам 
«Ферзь», «Пешка», «Конь». Написать виртуальные методы «битья» другой фигуры, которые принимают координаты 
другой фигуры и определяют, может ли данная  фигура «бить» фигуру с теми (принятыми) координатами.'''

class ChessPiece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def can_attack(self, x, y):
        raise NotImplementedError


class Queen(ChessPiece):
    def can_attack(self, x, y):
        if self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y):
            return True
        return False


class Pawn(ChessPiece):
    def can_attack(self, x, y):
        if self.color == 'white':
            if x == self.x + 1 and (y == self.y + 1 or y == self.y - 1):
                return True
        elif self.color == 'black':
            if x == self.x - 1 and (y == self.y + 1 or y == self.y - 1):
                return True
        return False


class Knight(ChessPiece):
    def can_attack(self, x, y):
        if (abs(self.x - x) == 2 and abs(self.y - y) == 1) or (abs(self.x - x) == 1 and abs(self.y - y) == 2):
            return True
        return False


queen = Queen("white", 4, 4)
pawn = Pawn("black", 5, 5)
knight = Knight("white", 6, 6)

print(queen.can_attack(5, 5))
print(pawn.can_attack(4, 4))
print(knight.can_attack(8, 7))