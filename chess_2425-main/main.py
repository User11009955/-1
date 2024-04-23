from src import Color, Board
from src.figures import *


def print_board(board: Board):
    print('   +' + '----+' * 8)
    for row in range(8, 0, -1):
        print(f' {row} ', end='')
        for col in range(1, 9):
            print('| ', end='')
            piece = board.get_piece(row, col)
            if piece is None:
                print('  ', end='')
            else:
                print(piece, end='')
            print(' ', end='')
        print('|')
        print('   +' + '----+' * 8)
    print('    ', end='')
    for col in range(8):
        print(f' {chr(65 + col)}   ', end='')
    print()


def convert_step(step: str) -> tuple | Exception:
    if len(step) != 2:
        raise Exception('Неверный формат хода')
    s, n = step[0], step[1]
    if not ord('A') <= ord(s) <= ord('H') :
        raise Exception('Неверный формат столбца')
    if not 1 <= int(n) <= 8:
        raise Exception('Неверный формат строки')
    return int(n), ord(s) - ord('A') + 1

def check(board, color, king_pos):# неработает
    for row in range(1, 9):
        for col in range(1, 9):
            piece = board.get_piece(row, col)
            if piece is not None and piece.color == color:
                if piece.can_move(board, row, col, *king_pos):
                    return False
    return True

def mate(board, color, king_pos):# неработает
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1),(0, 0)]
    result = 0
    for row in range(1, 9):
        for col in range(1, 9):
            piece = board.get_piece(row, col)
            if piece is not None and piece.color == color:
                for offset in offsets:
                    row_1, col_1 = king_pos[0] + offset[0], king_pos[1] + offset[1]
                    if 0 < row_1 > 9 or 0 < col_1 > 9:
                        result += 1
                        continue
                    if piece.can_move(board, row, col, row_1, col_1) or board.get_piece(row_1, col_1) is not None:
                        result += 1
    return True if result == 9 else False

def main():
    board = Board()
    white_king = (1, 5)
    black_king = (8, 5)
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                --выход')
        print('    move <from> <to>    --ход из клетки <from> в клетку <to>')
        if board.current_player == Color.WHITE:
            print('Ход белых')
        else:
            print('Ход черных')
        command =input('Введите команду: ')
        if command == 'exit':
            break
        command = command.split()
        if len(command) == 3 and command[0] == 'move':
            try:
                row, col = convert_step(command[1])
                row_1, col_1 = convert_step(command[2])

                if (row, col) == white_king:
                    white_king = (row_1, col_1)
                elif (row, col) == black_king:
                    black_king = (row_1, col_1)

                if board.move_piece(row, col, row_1, col_1):
                    print('Ход успешен')
                else:
                    print('Неверные координаты. Попробуйте другой ход')
                
                figure = board.get_piece(row_1, col_1)
                if figure.color == Color.WHITE and figure.can_move(board, row_1, col_1, *black_king):
                    if check(board, Color.BLACK, black_king) and mate(board, Color.WHITE, black_king):
                            return 'Игра окончена. Победили Белые.'
                    else:
                        print('Вам Шах, Господин. Бегите.')
                elif figure.color == Color.BLACK and figure.can_move(board, row_1, col_1, *white_king):
                    if check(board, Color.WHITE, white_king) and mate(board, Color.BLACK, white_king):
                            return 'Игра окончена. Победили Чёрные.'
                    else:
                        print('Вам Шах, Господин. Бегите.')
                
            except Exception as err:
                print('Ошибка:', err)
            finally:
                continue
        print('Неверная команда. Повторите снова')


print(main())
