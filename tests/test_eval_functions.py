import unittest
from board import *
import eval_functions


class FunctionTestCase(unittest.TestCase):

    def test_f0(self):
        f0 = eval_functions.F0()
        b1 = Board()
        self.assertEqual(0, f0.eval_board(b1))

    def test_f1_a(self):
        f1 = eval_functions.F1()
        b1 = Board()
        self.assertEqual(0, f1.eval_board(b1))

        b2 = Board(b1, Move(WHITE, 2, 4))
        print(b2.show())
        self.assertEqual(30, f1.eval_board(b2))

        b3a = Board(b2, Move(BLACK, 2, 5))
        print(b3a.show())
        self.assertEqual(-1, f1.eval_board(b3a))

        b3b = Board(b2, Move(BLACK, 2, 3))
        print(b3b.show())
        self.assertEqual(0, f1.eval_board(b3b))


if __name__ == '__main__':
    unittest.main()
