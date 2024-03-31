from src.color import Color
from src.figures import *



class Board:
    def __init__(self):
        self.__field = []
        self.__color = Color.WHITE
        for _ in range(8):
            self.__field.append([None] * 8)
        self.__fill()

    def __fill(self):
        for col in range(8):
            self.__field[1][col] = Pawn(Color.WHITE)
            self.__field[6][col] = Pawn(Color.BLACK)
        for col in (1, 6):
            self.__field[0][col] = Knight(Color.WHITE)
            self.__field[7][col] = Knight(Color.BLACK)
        for col in (0, 7):
            self.__field[0][col] = Rook(Color.WHITE)
            self.__field[7][col] = Rook(Color.BLACK)
        for col in (2, 5):
            self.__field[0][col] = Rook(Color.WHITE)
            self.__field[7][col] = Rook(Color.BLACK)

        self.__field[0][3] = Queen(Color.WHITE)# Queen(ферзь)
        self.__field[7][3] = Queen(Color.BLACK)

        self.__field[0][4] = King(Color.WHITE)# King(король)
        self.__field[7][4] = King(Color.BLACK)

    @property
    def current_player(self):
        return self.__color

    @property
    def field(self):
        return tuple([tuple(row) for row in self.__field])
    
    def move(self,start, end):
        start_1, start_2 = start
        end_1, end_2 = end
        if self.__field[end_1][end_2] is None:
            self.__field[end_1][end_2] = self.__field[start_1][start_2]
            self.__field[start_1][start_2] = None
            print(self.__field)
            return self.__field
        else:
            raise Exception('Там есть фигура')

    def get_piece(self, row: int, col: int):
        if 1 <= row <= 9 and 1 <= col <= 9:
            return self.field[row - 1][col - 1]
        return None
