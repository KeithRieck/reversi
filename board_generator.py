#!/usr/bin/env python3
import os
import random
import sys

import eval_functions
from board import Board, BLACK, WHITE

WHITE_TO_MOVE_STATE = 'WHITE_TO_MOVE_STATE'
BLACK_TO_MOVE_STATE = 'BLACK_TO_MOVE_STATE'
GAME_OVER_STATE = 'GAME_OVER_STATE'
DEBUG = False


class RandomGame:
    def __init__(self, start_board=None):
        self.current_board = start_board if start_board is not None else Board()
        self._consecutive_passes = 0
        self.game_state = WHITE_TO_MOVE_STATE
        self.eval_function = eval_functions.F1()

    def next_move(self):
        move = None
        if self.current_board.move_count() > 0:
            n = random.randint(0, self.current_board.move_count() - 1)
            move = self.current_board.get_move(n)
        self.__make_move(move)
        return self.current_board.__hash__()

    def __make_move(self, move):
        # print('\n\n- - - - - - - - - - - - - \n')
        # print(self.current_board.show())
        if move is not None:
            if DEBUG:
                print('Move = %r,%r : %s' % (move.x, move.y, move.player))
            self.current_board = Board(self.current_board, move)
            self._consecutive_passes = 0
        else:
            if DEBUG:
                print('PASS: ' + self.current_board.next_player())
            self.current_board.switch_player()
            self._consecutive_passes = self._consecutive_passes + 1
        self.game_state = BLACK_TO_MOVE_STATE if self.game_state == WHITE_TO_MOVE_STATE else WHITE_TO_MOVE_STATE
        if len(self.current_board) == 64 or self._consecutive_passes >= 2 \
                or self.current_board.count(WHITE) == 0 or self.current_board.count(BLACK) == 0:
            self.game_state = GAME_OVER_STATE
        if DEBUG:
            print(self.current_board.show())
            print('State = ' + self.game_state)
            print('- - - - - - - - - - - - - \n\n')

    def csv_line(self):
        csv = self.current_board.csv_line()
        vector = self.eval_function.eval_vector(self.current_board)
        for v in vector:
            csv = csv + str(v) + ','
        csv = csv + str(self.eval_function.eval_board(self.current_board)) + ','
        return csv


def main(argv=None):
    game_count = int(argv[1]) if argv is not None and len(argv) > 1 else 10
    output_file_name = argv[2] if argv is not None and len(argv) > 2 else 'test.csv'

    with open('data/%s' % output_file_name, 'w') as output_file:
        header_csv = 'ID,move,player'
        for x in range(8):
            for y in range(8):
                header_csv = header_csv + ',d' + str(x) + str(y)
        header_csv = header_csv + ',p0,g1,g2,b3,b4,b5,g6,b7,g8,pm,score_0'
        output_file.write(header_csv + '\n')
        board_set = {32, 33, 41, 57}
        for _ in range(game_count):
            game = RandomGame()
            while game.game_state != GAME_OVER_STATE and game.current_board.move_number < 63:
                b = game.next_move()
                if b not in board_set:
                    output_file.write(game.csv_line() + '\n')
                    board_set.add(b)


if __name__ == '__main__':
    if not os.path.isdir('data'):
        os.mkdir('data')
    main(sys.argv)
