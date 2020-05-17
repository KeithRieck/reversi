import unittest
from board import Board, Move, BLACK, WHITE
from board_processor import BoardProcessor, MIN_SCORE, MAX_SCORE

TEST_6 = False


class BoardProcessorTestCase(unittest.TestCase):

    def test_minimax_search_1(self):
        b1 = Board()
        b1 = Board(b1, Move(WHITE, 2, 4))
        b1 = Board(b1, Move(BLACK, 2, 5))

        processor = BoardProcessor()
        score0 = processor.eval_function.eval_board(b1)

        s0 = processor.eval_board(b1, depth=0)
        self.assertEqual(score0, s0)
        print('score0 = %r' % s0)

        score1 = MIN_SCORE
        for move1 in b1.get_moves():
            b2 = Board(b1, move1)
            score1 = max(score1, processor.eval_function.eval_board(b2))

        s1 = processor.eval_board(b1, depth=1)
        self.assertEqual(score1, s1)
        print('score1 = %r' % s1)

        score2 = MIN_SCORE
        for move1 in b1.get_moves():
            b2 = Board(b1, move1)
            s_temp = MAX_SCORE
            for move2 in b2.get_moves():
                b3 = Board(b2, move2)
                s_temp = min(s_temp, processor.eval_function.eval_board(b3))
            score2 = max(score2, s_temp)

        s2 = processor.eval_board(b1, depth=2)
        self.assertEqual(score2, s2)
        print('score2 = %r' % s2)

        s3 = processor.eval_board(b1, depth=3)
        self.assertEqual(340, s3)
        print('score3 = %r' % s3)

        s4 = processor.eval_board(b1, depth=4)
        self.assertEqual(20, s4)
        print('score4 = %r\n\n' % s4)

    def test_minimax_search_2(self):
        b1 = Board()
        b1 = Board(b1, Move(WHITE, 2, 4))
        b1 = Board(b1, Move(BLACK, 2, 5))
        b1 = Board(b1, Move(WHITE, 5, 3))
        b1 = Board(b1, Move(BLACK, 5, 2))
        b1 = Board(b1, Move(WHITE, 4, 2))
        b1 = Board(b1, Move(BLACK, 5, 4))
        b1 = Board(b1, Move(WHITE, 6, 3))
        b1 = Board(b1, Move(BLACK, 3, 2))

        processor = BoardProcessor()
        score0 = processor.eval_function.eval_board(b1)

        s0 = processor.eval_board(b1, depth=0)
        self.assertEqual(score0, s0)
        print('score0 = %r' % s0)

        score1 = MIN_SCORE
        for move1 in b1.get_moves():
            b2 = Board(b1, move1)
            score1 = max(score1, processor.eval_function.eval_board(b2))

        s1 = processor.eval_board(b1, depth=1)
        self.assertEqual(score1, s1)
        print('score1 = %r' % s1)

        score2 = MIN_SCORE
        for move1 in b1.get_moves():
            b2 = Board(b1, move1)
            s_temp = MAX_SCORE
            for move2 in b2.get_moves():
                b3 = Board(b2, move2)
                s_temp = min(s_temp, processor.eval_function.eval_board(b3))
            score2 = max(score2, s_temp)

        s2 = processor.eval_board(b1, depth=2)
        self.assertEqual(score2, s2)
        print('score2 = %r\n\n' % s2)

    def test_minimax_search_3(self):
        global TEST_6
        processor = BoardProcessor()
        b1 = Board()
        b1 = Board(b1, Move(WHITE, 3, 5))
        b1 = Board(b1, Move(BLACK, 2, 5))
        self.assertEqual(20, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 2, 4))
        self.assertEqual(120, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 4, 5))
        self.assertEqual(-420, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 5, 2))
        self.assertEqual(120, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 6, 1))
        self.assertEqual(-590, processor.eval_board(b1, depth=4))
        if TEST_6:
            self.assertEqual(-430, processor.eval_board(b1, depth=6))

        b1 = Board(b1, Move(WHITE, 4, 6))
        self.assertEqual(-50, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 2, 3))
        self.assertEqual(-590, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 1, 3))
        self.assertEqual(140, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 4, 7))
        self.assertEqual(-770, processor.eval_board(b1, depth=4))
        if TEST_6:
            self.assertEqual(-770, processor.eval_board(b1, depth=6))

        b1 = Board(b1, Move(WHITE, 2, 2))
        self.assertEqual(-330, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 0, 2))
        self.assertEqual(-940, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 2, 6))
        self.assertEqual(-280, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 1, 5))
        self.assertEqual(-800, processor.eval_board(b1, depth=4))
        if TEST_6:
            self.assertEqual(-810, processor.eval_board(b1, depth=6))

        b1 = Board(b1, Move(WHITE, 5, 5))
        self.assertEqual(-250, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 2, 1))
        self.assertEqual(-420, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 1, 4))
        self.assertEqual(-270, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 6, 6))
        self.assertEqual(-950, processor.eval_board(b1, depth=4))
        if TEST_6:
            self.assertEqual(-920, processor.eval_board(b1, depth=6))

        b1 = Board(b1, Move(WHITE, 7, 0))
        self.assertEqual(-100, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 0, 4))
        self.assertEqual(-920, processor.eval_board(b1, depth=4))

        b1 = Board(b1, Move(WHITE, 0, 3))
        self.assertEqual(-30, processor.eval_board(b1, depth=4))
        b1 = Board(b1, Move(BLACK, 4, 2))
        self.assertEqual(-590, processor.eval_board(b1, depth=4))
        if TEST_6:
            self.assertEqual(-510, processor.eval_board(b1, depth=6))
            self.assertEqual(-450, processor.eval_board(b1, depth=8))


if __name__ == '__main__':
    unittest.main()
