import unittest
from board import Board, Move, BLACK, WHITE


class BoardTestCase(unittest.TestCase):

    def test_init(self):
        b1 = Board()
        self.assertEqual(WHITE, b1._player)
        self.assertNotEqual(WHITE, b1[4][2])
        self.assertEqual(4, len(b1))
        self.assertEqual(4, len(b1._moves))
        self.assertEqual(2, b1.count(WHITE))
        self.assertEqual(2, b1.count(BLACK))

        m2 = Move(WHITE, 4, 2)
        b2 = Board(b1, m2)
        self.assertEqual(BLACK, b2._player)
        self.assertEqual(WHITE, b2[4][2])
        self.assertEqual(WHITE, b2[4][3])
        self.assertEqual(5, len(b2))
        self.assertEqual(3, len(b2._moves))
        self.assertEqual(4, b2.count(WHITE))
        self.assertEqual(1, b2.count(BLACK))

        b0 = Board(b1, None)
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertNotEqual(WHITE, b0[3][3])
        self.assertEqual(0, len(b0))
        self.assertEqual(0, len(b0._moves))
        self.assertEqual(0, b0.count(WHITE))
        self.assertEqual(0, b0.count(BLACK))

    def test_move_down(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_down(WHITE, 0, 7))

        b0._p[1][7] = BLACK
        self.assertEqual(0, b0._move_down(WHITE, 1, 6))

        b0._p[2][6] = BLACK
        b0._p[2][7] = WHITE
        self.assertEqual(1, b0._move_down(WHITE, 2, 5))

        b0._p[3][5] = BLACK
        b0._p[3][6] = BLACK
        b0._p[3][7] = WHITE
        self.assertEqual(2, b0._move_down(WHITE, 3, 4))

        b0._p[4][5] = BLACK
        b0._p[4][6] = BLACK
        self.assertEqual(0, b0._move_down(WHITE, 4, 4))

        b0._p[5][7] = WHITE
        self.assertEqual(0, b0._move_down(WHITE, 5, 6))

    def test_move_down_do_move(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        b0._p[2][6] = BLACK
        b0._p[2][7] = WHITE
        b0._move_down(WHITE, 2, 5, True)
        self.assertEqual(WHITE, b0._p[2][5])
        self.assertEqual(WHITE, b0._p[2][6])

        b0._p[3][5] = BLACK
        b0._p[3][6] = BLACK
        b0._p[3][7] = WHITE
        b0._move_down(WHITE, 3, 4, True)
        self.assertEqual(WHITE, b0._p[3][4])
        self.assertEqual(WHITE, b0._p[3][5])
        self.assertEqual(WHITE, b0._p[3][6])

    def test_move_up(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_up(WHITE, 0, 0))

        b0._p[1][0] = BLACK
        self.assertEqual(0, b0._move_up(WHITE, 1, 1))

        b0._p[2][0] = WHITE
        b0._p[2][1] = BLACK
        self.assertEqual(1, b0._move_up(WHITE, 2, 2))

        b0._p[3][0] = WHITE
        b0._p[3][1] = BLACK
        b0._p[3][2] = BLACK
        self.assertEqual(2, b0._move_up(WHITE, 3, 3))

        b0._p[4][0] = BLACK
        b0._p[4][1] = BLACK
        self.assertEqual(0, b0._move_up(WHITE, 4, 2))

        b0._p[5][0] = WHITE
        self.assertEqual(0, b0._move_up(WHITE, 5, 1))

    def test_move_right(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_right(WHITE, 7, 0))

        b0._p[7][0] = BLACK
        self.assertEqual(0, b0._move_right(WHITE, 6, 0))

        b0._p[6][1] = BLACK
        b0._p[7][1] = WHITE
        self.assertEqual(1, b0._move_right(WHITE, 5, 1))

        b0._p[5][2] = BLACK
        b0._p[6][2] = BLACK
        b0._p[7][2] = WHITE
        self.assertEqual(2, b0._move_right(WHITE, 4, 2))

        b0._p[6][3] = BLACK
        b0._p[7][3] = BLACK
        self.assertEqual(0, b0._move_right(WHITE, 5, 3))

        b0._p[7][4] = WHITE
        self.assertEqual(0, b0._move_right(WHITE, 6, 4))

    def test_move_left(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_left(WHITE, 0, 0))

        b0._p[0][1] = BLACK
        self.assertEqual(0, b0._move_left(WHITE, 1, 1))

        b0._p[0][2] = WHITE
        b0._p[1][2] = BLACK
        self.assertEqual(1, b0._move_left(WHITE, 2, 2))

        b0._p[0][3] = WHITE
        b0._p[1][3] = BLACK
        b0._p[2][3] = BLACK
        self.assertEqual(2, b0._move_left(WHITE, 3, 3))

        b0._p[0][4] = BLACK
        b0._p[1][4] = BLACK
        self.assertEqual(0, b0._move_left(WHITE, 2, 4))

        b0._p[0][5] = WHITE
        self.assertEqual(0, b0._move_left(WHITE, 1, 5))

    def test_move_down_right(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_down_right(WHITE, 0, 7))
        self.assertEqual(0, b0._move_down_right(WHITE, 7, 7))
        self.assertEqual(0, b0._move_down_right(WHITE, 7, 0))

        b0._p[5][5] = BLACK
        b0._p[6][6] = BLACK
        b0._p[7][7] = WHITE
        self.assertEqual(2, b0._move_down_right(WHITE, 4, 4))

    def test_move_down_left(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_down_left(WHITE, 0, 4))
        self.assertEqual(0, b0._move_down_left(WHITE, 0, 7))
        self.assertEqual(0, b0._move_down_left(WHITE, 4, 7))

        b0._p[0][7] = WHITE
        b0._p[1][6] = BLACK
        b0._p[2][5] = BLACK
        self.assertEqual(2, b0._move_down_left(WHITE, 3, 4))

    def test_move_up_right(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_up_right(WHITE, 4, 0))
        self.assertEqual(0, b0._move_up_right(WHITE, 7, 0))
        self.assertEqual(0, b0._move_up_right(WHITE, 7, 4))

        b0._p[5][2] = BLACK
        b0._p[6][1] = BLACK
        b0._p[7][0] = WHITE
        self.assertEqual(2, b0._move_up_right(WHITE, 4, 3))

    def test_move_up_left(self):
        b0 = Board()
        b0._p[3][3] = None
        b0._p[3][4] = None
        b0._p[4][3] = None
        b0._p[4][4] = None
        b0._moves = []
        self.assertEqual(0, len(b0))

        self.assertEqual(0, b0._move_up_left(WHITE, 4, 0))
        self.assertEqual(0, b0._move_up_left(WHITE, 0, 0))
        self.assertEqual(0, b0._move_up_left(WHITE, 0, 4))

        b0._p[0][0] = WHITE
        b0._p[1][1] = BLACK
        b0._p[2][2] = BLACK
        self.assertEqual(2, b0._move_up_left(WHITE, 3, 3))

    def test_permanent(self):
        b0 = Board()
        b0._moves = []
        b0._p[0][0] = BLACK
        b0._p[1][0] = BLACK
        b0._p[1][1] = BLACK
        b0._p[2][0] = BLACK
        b0._p[4][0] = BLACK
        b0._p[0][1] = BLACK
        b0._p[0][3] = BLACK
        b0._p[0][7] = BLACK
        b0._p[1][6] = BLACK
        b0._p[4][7] = WHITE
        b0._p[6][6] = WHITE
        b0._p[6][7] = WHITE
        b0._p[7][7] = WHITE
        b0._p[7][6] = WHITE
        b0._p[7][5] = WHITE
        b0._p[7][4] = WHITE
        b0._p[7][3] = WHITE
        b0._calc_perm()
        print(b0.show())

        self.assertTrue(b0.is_permanent(BLACK, 0, 0))
        self.assertTrue(b0.is_permanent(BLACK, 0, 7))
        self.assertFalse(b0.is_permanent(BLACK, 7, 7))
        self.assertFalse(b0.is_permanent(BLACK, 7, 0))

        self.assertTrue(b0.is_permanent(BLACK, 1, 0))
        self.assertTrue(b0.is_permanent(BLACK, 2, 0))
        self.assertFalse(b0.is_permanent(BLACK, 3, 0))
        self.assertFalse(b0.is_permanent(BLACK, 4, 0))
        self.assertTrue(b0.is_permanent(BLACK, 0, 1))
        self.assertFalse(b0.is_permanent(BLACK, 0, 2))
        self.assertFalse(b0.is_permanent(BLACK, 0, 3))
        self.assertFalse(b0.is_permanent(BLACK, 0, 4))
        self.assertFalse(b0.is_permanent(BLACK, 0, 6))
        self.assertFalse(b0.is_permanent(BLACK, 1, 7))

        self.assertTrue(b0.is_permanent(WHITE, 6, 7))
        self.assertTrue(b0.is_permanent(WHITE, 7, 5))
        self.assertTrue(b0.is_permanent(WHITE, 7, 3))
        self.assertFalse(b0.is_permanent(WHITE, 7, 2))
        self.assertFalse(b0.is_permanent(WHITE, 5, 7))
        self.assertFalse(b0.is_permanent(WHITE, 4, 7))

    def test_perm(self):
        b0 = Board()
        b0._moves = []
        b0._p[0][0] = BLACK
        b0._p[1][0] = BLACK
        b0._p[1][1] = BLACK
        b0._p[2][0] = BLACK
        b0._p[4][0] = BLACK
        b0._p[0][1] = BLACK
        b0._p[0][3] = BLACK
        b0._p[0][7] = BLACK
        b0._p[1][6] = BLACK
        b0._p[4][7] = WHITE
        b0._p[6][6] = WHITE
        b0._p[6][7] = WHITE
        b0._p[7][7] = WHITE
        b0._p[7][6] = WHITE
        b0._p[7][5] = WHITE
        b0._p[7][4] = WHITE
        b0._p[7][3] = WHITE
        b0._calc_perm()
        print(b0.show())

        self.assertTrue(b0._perm_left(BLACK, 0, 0))
        self.assertTrue(b0._perm_left(BLACK, 1, 0))
        self.assertTrue(b0._perm_left(BLACK, 2, 0))
        self.assertFalse(b0._perm_left(BLACK, 3, 0))
        self.assertFalse(b0._perm_left(BLACK, 4, 0))
        self.assertFalse(b0._perm_left(BLACK, 5, 0))

        self.assertTrue(b0._perm_up(BLACK, 0, 0))
        self.assertTrue(b0._perm_up(BLACK, 0, 1))
        self.assertFalse(b0._perm_up(BLACK, 0, 2))
        self.assertFalse(b0._perm_up(BLACK, 0, 3))
        self.assertFalse(b0._perm_up(BLACK, 0, 4))

        self.assertTrue(b0._perm_right(WHITE, 7, 7))
        self.assertTrue(b0._perm_right(WHITE, 6, 7))
        self.assertFalse(b0._perm_right(WHITE, 5, 7))
        self.assertFalse(b0._perm_right(WHITE, 4, 7))
        self.assertFalse(b0._perm_right(WHITE, 3, 7))

        self.assertTrue(b0._perm_down(WHITE, 7, 7))
        self.assertTrue(b0._perm_down(WHITE, 7, 3))
        self.assertFalse(b0._perm_down(WHITE, 7, 2))

    def test_sort_moves(self):
        b0 = Board()
        b0._moves[0].score = 2
        b0._moves[1].score = 1
        b0._moves[2].score = 3
        b0._moves[3].score = 0

        b0.best_move()

        self.assertEqual(0, b0._moves[0].score)
        self.assertEqual(1, b0._moves[1].score)
        self.assertEqual(2, b0._moves[2].score)
        self.assertEqual(3, b0._moves[3].score)

    def test_moves_1(self):
        b1 = Board()
        b1._moves = []
        b1._p[7][0] = WHITE
        b1._p[5][1] = BLACK
        b1._p[6][1] = WHITE
        b1._p[1][2] = BLACK
        b1._p[2][2] = BLACK
        b1._p[3][2] = BLACK
        b1._p[4][2] = BLACK
        b1._p[5][2] = BLACK
        b1._p[6][2] = BLACK
        b1._p[2][3] = BLACK
        b1._p[3][3] = BLACK
        b1._p[4][3] = BLACK
        b1._p[5][3] = BLACK
        b1._p[6][3] = BLACK
        b1._p[7][3] = BLACK
        b1._p[3][4] = BLACK
        b1._p[4][4] = BLACK
        b1._p[5][4] = BLACK
        b1._p[5][5] = BLACK
        b1._p[5][6] = BLACK
        print(b1.show())

        b2 = Board(b1, Move(WHITE, 2, 5))
        print(b2.show())
        self.assertEqual(6, len(b2._moves))

    def test_moves_2(self):
        b1 = Board()
        b1._moves = []
        b1._p[0][0] = WHITE
        b1._p[1][0] = None
        b1._p[2][0] = WHITE
        b1._p[3][0] = BLACK
        b1._p[4][0] = WHITE
        b1._p[5][0] = WHITE
        b1._p[6][0] = WHITE
        b1._p[7][0] = WHITE
        b1._p[0][1] = BLACK
        b1._p[1][1] = WHITE
        b1._p[2][1] = WHITE
        b1._p[3][1] = BLACK
        b1._p[4][1] = BLACK
        b1._p[5][1] = BLACK
        b1._p[6][1] = WHITE
        b1._p[7][1] = WHITE
        b1._p[0][2] = WHITE
        b1._p[1][2] = WHITE
        b1._p[2][2] = WHITE
        b1._p[3][2] = BLACK
        b1._p[4][2] = BLACK
        b1._p[5][2] = BLACK
        b1._p[6][2] = BLACK
        b1._p[7][2] = WHITE
        b1._p[0][3] = WHITE
        b1._p[1][3] = WHITE
        b1._p[2][3] = BLACK
        b1._p[3][3] = WHITE
        b1._p[4][3] = WHITE
        b1._p[5][3] = WHITE
        b1._p[6][3] = BLACK
        b1._p[7][3] = WHITE
        b1._p[0][4] = WHITE
        b1._p[1][4] = WHITE
        b1._p[2][4] = WHITE
        b1._p[3][4] = WHITE
        b1._p[4][4] = WHITE
        b1._p[5][4] = WHITE
        b1._p[6][4] = WHITE
        b1._p[7][4] = WHITE
        b1._p[0][5] = WHITE
        b1._p[1][5] = WHITE
        b1._p[2][5] = WHITE
        b1._p[3][5] = WHITE
        b1._p[4][5] = BLACK
        b1._p[5][5] = BLACK
        b1._p[6][5] = WHITE
        b1._p[7][5] = WHITE
        b1._p[0][6] = WHITE
        b1._p[1][6] = WHITE
        b1._p[2][6] = WHITE
        b1._p[3][6] = WHITE
        b1._p[4][6] = WHITE
        b1._p[5][6] = WHITE
        b1._p[6][6] = WHITE
        b1._p[7][6] = WHITE
        b1._p[0][7] = WHITE
        b1._p[1][7] = WHITE
        b1._p[2][7] = WHITE
        b1._p[3][7] = WHITE
        b1._p[4][7] = WHITE
        b1._p[5][7] = WHITE
        b1._p[6][7] = WHITE
        b1._p[7][7] = WHITE
        b1.switch_player()
        b1.switch_player()
        print(b1.show())

        self.assertEqual(0, len(b1._moves))

    def test_csv(self):
        b1 = Board()
        csv1 = b1.csv_line()
        b1a = Board(csv=csv1)
        self.assertEqual(b1.__hash__(), b1a.__hash__())

        m2 = Move(WHITE, 4, 2)
        b2 = Board(b1, m2)
        csv2 = b2.csv_line()
        b2a = Board(csv=csv2)
        self.assertEqual(b2.__hash__(), b2a.__hash__())

        b3 = Board(b1, Move(WHITE, 2, 4))
        b3 = Board(b3, Move(BLACK, 2, 5))
        b3 = Board(b3, Move(WHITE, 5, 3))
        b3 = Board(b3, Move(BLACK, 5, 2))
        b3 = Board(b3, Move(WHITE, 4, 2))
        b3 = Board(b3, Move(BLACK, 5, 4))
        b3 = Board(b3, Move(WHITE, 6, 3))
        b3 = Board(b3, Move(BLACK, 3, 2))
        csv3 = b3.csv_line()
        b3a = Board(csv=csv3)
        self.assertEqual(b3.__hash__(), b3a.__hash__())


if __name__ == '__main__':
    unittest.main()
