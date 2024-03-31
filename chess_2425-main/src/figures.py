from src.piece import Piece


class Pawn(Piece):
    def char(self):
        return 'P'
    def true_move(self,steps):
        coord_1, coord_2 = steps
        print(coord_1, coord_2)
        if coord_1[1] == coord_2[1] and (coord_2[0] - coord_1[0]) == 1:
            return True
        else:
            return False

class Knight(Piece):
    def char(self):
        return 'N'
    
class Rook(Piece):
    def char(self):
        return 'R'

class Bishop(Piece):
    def char(self):
        return 'B'
    
class Queen(Piece):
    def char(self):
        return 'Q'
    
class King(Piece):
    def char(self):
        return 'K'