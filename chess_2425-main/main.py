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


def convert_step(step: str) -> tuple:
    if len(step) != 2:
        raise Exception('Неверный формат хода')
    s, n = step[0], step[1]
    if not ord('A') <= ord(s) <= ord('H'):
        raise Exception('Неверный формат столбца')
    if not '1' <= n <= '8':
        raise Exception('Неверный формат строки')
    return int(n), ord(s) - ord('A') + 1


def mate(board, color, king_pos):
    opponent_color = Color.BLACK if color == Color.WHITE else Color.WHITE

    def is_safe(king_pos):
        for row in range(1, 9):
            for col in range(1, 9):
                piece = board.get_piece(row, col)
                if piece is not None and piece.color == opponent_color:
                    if piece.can_attack(board, row, col, *king_pos):
                        return False
        return True
    
    def is_safe_king_move():
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        for offset in offsets:
            new_pos = (king_pos[0] + offset[0], king_pos[1] + offset[1])
            if 1 <= new_pos[0] <= 8 and 1 <= new_pos[1] <= 8:
                if board.get_piece(*new_pos) is None:
                    if is_safe(new_pos):
                        return True
        return False

    def can_piece_defend():
        for row in range(1, 9):
            for col in range(1, 9):
                piece = board.get_piece(row, col)
                if piece is not None and piece.color == color:
                    for r in range(1, 9):
                        for c in range(1, 9):
                            if piece.can_move(board, row, col, r, c):
                                clon__fill = board.__field
                                board.move_piece(row, col, r, c)
                                if is_safe(king_pos):
                                    board.__field = clon__fill  # Отменяем ход
                                    return True
                                board.__field = clon__fill  # Отменяем ход
        return False
    
    if not is_safe(king_pos):
        if not is_safe_king_move() and not can_piece_defend():
            return True
    return False

def main():
    board = Board()
    white_king = (1, 5)
    black_king = (8, 5)
    king_pos = white_king
    color = board.current_player
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                --выход')
        print('    move <from> <to>    --ход из клетки <from> в клетку <to>')
        if board.current_player == Color.WHITE:
            print('Ход белых')
        else:
            print('Ход черных')
        command = input('Введите команду: ')
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

                # clon__fill = board.__field

                if board.move_piece(row, col, row_1, col_1):
                    king_pos = white_king if color == Color.WHITE else black_king
                    # Не сыпь мне соль на рану...
                    # if not board.is_in_check(color, king_pos):
                    #     print('Ход успешен')
                    # else:
                    #     board.__field = clon__fill  # Отменяем ход
                    #     print_board(board)
                    #     print('Ход невозможен. Шах!')
                    #     continue

                    # if mate(board, color, king_pos):
                    #     winner = 'Белые' if color == Color.BLACK else 'Черные'
                    #     print(f'Игра окончена. Победили {winner}.')
                    #     break
                    # if color == Color.WHITE and board.is_in_check(Color.BLACK, black_king):
                    #     print('Черному королю шах.')
                    # if color == Color.BLACK and board.is_in_check(Color.WHITE, white_king):
                    #     print('Белому королю шах.')
                else:
                    print('Неверные координаты. Попробуйте другой ход')
                    continue
                
                color = board.current_player

            except Exception as err:
                print('Ошибка:', err)
        else:
            print('Неверная команда. Повторите снова')

main()
