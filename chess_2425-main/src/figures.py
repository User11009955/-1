from src.piece import Piece
from src.color import Color

class Pawn(Piece):
    def char(self):
        return 'P'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if col != col_1:
            return False
        if self.color == Color.WHITE:
            start_row = 2
            direction = 1
        else:
            start_row = 7
            direction = -1
        if row + direction == row_1:
            return True
        if row == start_row \
                and row + 2 * direction == row_1 \
                and board.get_piece(row + direction, col) is None:
            return True
        return False

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if self.color == Color.WHITE:
            direction = 1
        else:
            direction = -1
        return row + direction == row_1 and abs(col - col_1) == 1

class Knight(Piece):
    def char(self):
        return 'N'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_row = abs(row - row_1)
        diff_col = abs(col - col_1)
        return diff_row == 2 and diff_col == 1 or\
            diff_row == 1 and diff_col == 2

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
    
class Rook(Piece):
    def char(self):
        return 'R'
    
    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return row == row_1 or col == col_1

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)

class Bishop(Piece):
    def char(self):
        return 'B'
    
    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return abs(row - row_1) == abs(col - col_1)

    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
    
class Queen(Piece):
    def char(self):
        return 'Q'
    
    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        offsets = [(0, 1), (1, 0), (1, 1)]
        return abs(row - row_1) == abs(col - col_1) or \
            row == row_1 or col == col_1 or \
            (abs(row - row_1), abs(col - col_1)) in offsets
    
    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)
    
class King(Piece):
    def char(self):
        return 'K'
    
    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        offsets = [(0, 1), (1, 0), (1, 1)]
        return (abs(row - row_1), abs(col - col_1)) in offsets
    
    def can_attack(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        return self.can_move(board, row, col, row_1, col_1)