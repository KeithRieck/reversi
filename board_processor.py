#!/usr/bin/env python3

import os
import sys
import time

import eval_functions
from board import Board, WHITE, BLACK

MIN_SCORE = -1000000
MAX_SCORE = 1000000
DEBUG = True


class BoardProcessor:
    def __init__(self):
        self.eval_function = eval_functions.F1()

    def __search(self, board, depth=0, alpha=MIN_SCORE, beta=MAX_SCORE):
        if depth <= 0:
            return self.eval_function.eval_board(board)
        if board.move_count() == 0:
            b = Board(board)
            b.switch_player()
            return self.__search(b, depth - 1)
        score = MIN_SCORE if board.next_player() == WHITE else MAX_SCORE
        for move in board.get_moves():
            move.score = self.__search(Board(board, move), depth - 1, alpha, beta)
            score = max(score, move.score) if board.next_player() == WHITE else min(score, move.score)
            alpha = max(alpha, move.score) if board.next_player() == WHITE else alpha
            beta = min(beta, move.score) if board.next_player() == BLACK else beta
            if alpha >= beta:
                break
        board.sort_moves()
        return score

    def eval_board(self, board, depth=0):
        start_time = time.time()
        score = self.__search(board, depth)
        search_time = time.time() - start_time
        if DEBUG:
            print('%r \t\t depth=%r : search_time=%.2f : score=%r' % (board.__hash__(), depth, search_time, score))
        return score

    def eval_csv(self, csv, max_depth=0):
        start_time = time.time()
        board = Board(csv=csv)
        new_csv = board.csv_line()
        vector = self.eval_function.eval_vector(board)
        for v in vector:
            new_csv = new_csv + str(v) + ','
        for depth in range(0, max_depth + 1, 2):
            score = self.eval_board(board, depth)
            new_csv = new_csv + str(score) + ','
        total_time = time.time() - start_time
        if DEBUG:
            print('%r \t : total_time=%.2f' % (board.__hash__(), total_time))
        return new_csv


def main(argv=None):
    max_depth = int(argv[1]) if argv is not None and len(argv) > 1 else 4
    input_file_name = argv[2] if argv is not None and len(argv) > 2 else 'test.csv'
    output_file_name = argv[3] if argv is not None and len(argv) > 3 else 'processed.csv'

    header_csv = 'ID,move,player'
    for x in range(8):
        for y in range(8):
            header_csv = header_csv + ',d' + str(x) + str(y)
    header_csv = header_csv + ',p0,g1,g2,b3,b4,b5,g6,b7,g8,pm'
    for depth in range(0, max_depth + 1, 2):
        header_csv = header_csv + ',score_' + str(depth)

    processor = BoardProcessor()
    start_time = time.time()
    with open('data/%s' % output_file_name, 'w') as output_file:
        output_file.write(header_csv + '\n')
        with open('data/%s' % input_file_name, 'r') as input_file:
            for csv in input_file:
                if csv.startswith('ID') or len(csv.strip()) == 0:
                    continue
                board = Board(csv=csv)
                if board.move_number < 5 or board.move_number > 58:
                    continue
                new_csv = processor.eval_csv(csv, max_depth)
                output_file.write(new_csv + '\n')
                output_file.flush()

    total_time = time.time() - start_time
    if DEBUG:
        print('TOTAL_TIME=%.2f' % total_time)


if __name__ == '__main__':
    if not os.path.isdir('data'):
        os.mkdir('data')
    main(sys.argv)
