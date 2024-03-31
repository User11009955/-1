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


def main():
    board = Board()

    def steps(step):
        row, col = step[0]
        pawn = Pawn('0')
        if str(board.get_piece(row, col))[1] == 'P' and pawn.true_move(step):
            return True
        else:
            raise Exception('Так ходить нельзя')
    
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
                start = convert_step(command[1])
                end = convert_step(command[2])
                if steps((start, end)):
                    board.__field = board.move(start, end)
            except Exception as err:
                print('Ошибка:', err)
            finally:
                continue
        print('Неверная команда. Повторите снова')


main()
