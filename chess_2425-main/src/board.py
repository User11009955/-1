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
            self.__field[0][col] = Bishop(Color.WHITE)
            self.__field[7][col] = Bishop(Color.BLACK)

        self.__field[0][3] = Queen(Color.WHITE)
        self.__field[7][3] = Queen(Color.BLACK)

        self.__field[0][4] = King(Color.WHITE)
        self.__field[7][4] = King(Color.BLACK)

    @property
    def current_player(self):
        return self.__color

    @property
    def field(self):
        return tuple([tuple(row) for row in self.__field])

    @staticmethod
    def __validate_coord(row: int, col: int) -> bool:
        return 1 <= row <= 8 and 1 <= col <= 8

    def get_piece(self, row: int, col: int):
        if self.__validate_coord(row, col):
            return self.__field[row - 1][col - 1]
        return None

    def set_piece(self, row, col, piece):
        self.__field[row - 1][col - 1] = piece

    def compare(self, a, b):
        if b > a:
            return 1
        elif b == a:
            return 0
        else:
            return -1

    def move_piece(self, row: int, col: int, row_1: int, col_1: int) -> bool:
        piece = self.get_piece(row, col)
        if piece is None:
            print("Фигура отсутствует на начальной позиции")
            return False
        if piece.color != self.current_player:
            print("Фигура не принадлежит текущему игроку")
            return False
        if not self.__validate_coord(row_1, col_1):
            print("Целевая координата некорректна")
            return False
        if self.get_piece(row_1, col_1) is None:
            if not piece.can_move(self, row, col, row_1, col_1):
                print("Фигура не может переместиться на целевую позицию")
                return False
        elif self.get_piece(row_1, col_1).color != self.current_player:
            if not piece.can_attack(self, row, col, row_1, col_1):
                print("Фигура не может атаковать целевую позицию")
                return False
        else:
            print("Целевая позиция занята фигурой текущего игрока")
            return False
        if isinstance(piece, Knight) or isinstance(piece, Pawn) or isinstance(piece, King):
            pass
        else:
            row_2 = self.compare(row, row_1)
            col_2 = self.compare(col, col_1)
            for i in range(1, abs(row - row_1 if row - row_1 != 0 else col - col_1)):
                if self.get_piece(row + i * row_2, col + i * col_2) is not None:
                    print("На пути движения фигуры находится другая фигура")
                    return False

        self.__field[row - 1][col - 1] = None
        self.__field[row_1 - 1][col_1 - 1] = piece
        self.__color = Color.WHITE if self.__color == Color.BLACK else Color.BLACK
        return True

    def is_in_check(self, color: Color, king_pos) -> bool:

        for row in range(1, 9):
            for col in range(1, 9):
                piece = self.get_piece(row, col)
                if piece and piece.color != color:
                    if piece.can_attack(self, row, col, *king_pos):
                        return True

        return False
