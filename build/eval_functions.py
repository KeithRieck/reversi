from board import Move, Board, BLACK, WHITE


class EvaluationFunction:
    """
    Function for assigning values to Boards, indicating the relative advantage for WHITE.
    Positive values indicate that WHITE is doing well.  Negative values mean that BLACK
    is ahead.
    """

    def eval_board(self, board) -> int:
        """Return the value of a Board."""
        return 0

    def eval_move(self, board: Board, move: Move) -> bool:
        """
        Determine the value of the move leading to this Board.
        If processing is still pending, return False.
        When processing is done, put the score into the Move object and return True.
        """
        move.score = self.eval_board(board)
        move.score_depth = 1
        return True

    def eval_vector(self, board: Board):
        return 0, 0


class F0(EvaluationFunction):
    """Trivial function that rates all boards as equal."""

    def eval_board(self, board: Board):
        return 0


def _good_location_1(x: int, y: int) -> bool:
    return (x == 0 and y == 2) or (x == 0 and y == 5) \
           or (x == 7 and y == 2) or (x == 7 and y == 5) \
           or (x == 2 and y == 0) or (x == 5 and y == 0) \
           or (x == 2 and y == 7) or (x == 5 and y == 7)


def _good_location_2(x: int, y: int) -> bool:
    return (x == 2 and y == 2) or (x == 5 and y == 2) \
           or (x == 2 and y == 5) or (x == 5 and y == 5)


def _bad_location_3(x: int, y: int) -> bool:
    return (x == 0 and y == 1) or (x == 0 and y == 6) \
           or (x == 7 and y == 1) or (x == 7 and y == 6) \
           or (x == 1 and y == 0) or (x == 6 and y == 0) \
           or (x == 1 and y == 7) or (x == 6 and y == 7)


def _bad_location_4(x: int, y: int) -> bool:
    return (x == 1 and y == 1) or (x == 6 and y == 1) \
           or (x == 1 and y == 6) or (x == 6 and y == 6)


def _bad_location_5(x: int, y: int) -> bool:
    return (x == 2 and y == 1) or (x == 1 and y == 2) \
           or (x == 5 and y == 1) or (x == 6 and y == 2) \
           or (x == 1 and y == 5) or (x == 2 and y == 6) \
           or (x == 5 and y == 6) or (x == 6 and y == 5)


def _good_location_6(x: int, y: int) -> bool:
    return (x == 0 and y == 3) or (x == 0 and y == 4) \
           or (x == 7 and y == 3) or (x == 7 and y == 4) \
           or (x == 3 and y == 0) or (x == 4 and y == 0) \
           or (x == 3 and y == 7) or (x == 4 and y == 7)


def _bad_location_7(x: int, y: int) -> bool:
    return (x == 1 and y == 3) or (x == 1 and y == 4) \
           or (x == 6 and y == 3) or (x == 6 and y == 4) \
           or (x == 3 and y == 1) or (x == 4 and y == 1) \
           or (x == 3 and y == 6) or (x == 4 and y == 6)


def _good_location_8(x: int, y: int) -> bool:
    return (x == 2 and y == 3) or (x == 2 and y == 4) \
           or (x == 5 and y == 3) or (x == 5 and y == 4) \
           or (x == 3 and y == 2) or (x == 4 and y == 2) \
           or (x == 3 and y == 5) or (x == 4 and y == 5)


class F1(EvaluationFunction):
    """Simple linear static evaluation function."""

    def __init__(self, p0=1, p1=10, p2=10, p3=-10, p4=-10, p5=1, p6=5, p7=1, p8=5, pm=100, p_move=0,
                 p_player=0):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.pm = pm
        self.p_move = p_move
        self.p_player = p_player

    def eval_vector(self, board):
        s0 = 0
        g1 = 0
        g2 = 0
        b3 = 0
        b4 = 0
        b5 = 0
        g6 = 0
        b7 = 0
        g8 = 0
        sm = 0
        for x in range(8):
            for y in range(8):
                player = board.is_piece(x, y)
                p = 1 if player == WHITE else (-1 if player == BLACK else 0)
                s0 = s0 + p
                g1 = g1 + p if _good_location_1(x, y) else g1
                g2 = g2 + p if _good_location_2(x, y) else g2
                b3 = b3 + p if _bad_location_3(x, y) else b3
                b4 = b4 + p if _bad_location_4(x, y) else b4
                b5 = b5 + p if _bad_location_5(x, y) else b5
                g6 = g6 + p if _good_location_6(x, y) else g6
                b7 = b7 + p if _bad_location_7(x, y) else b7
                g8 = g8 + p if _good_location_8(x, y) else g8
                sm = sm + p if board.is_permanent(player, x, y) else sm
        return s0, g1, g2, b3, b4, b5, g6, b7, g8, sm

    def eval_board(self, board: Board) -> int:
        score = 0
        for x in range(8):
            for y in range(8):
                player = board.is_piece(x, y)
                v = self.p0
                v = self.p1 if _good_location_1(x, y) else v
                v = self.p2 if _good_location_2(x, y) else v
                v = self.p3 if _bad_location_3(x, y) else v
                v = self.p4 if _bad_location_4(x, y) else v
                v = self.p5 if _bad_location_5(x, y) else v
                v = self.p6 if _good_location_6(x, y) else v
                v = self.p7 if _bad_location_7(x, y) else v
                v = self.p8 if _good_location_8(x, y) else v
                v = self.pm if player is not None and board.is_permanent(player, x, y) else v
                if player == WHITE:
                    score = score + v
                if player == BLACK:
                    score = score - v
        score = score + board.move_number * self.p_move
        if board.next_player() == WHITE:
            score = score + self.p_player
        return score


class F2(F1):
    """Linear static evaluation function, using weights learned from sklearn's LinearRegression."""

    def __init__(self):
        F1.__init__(self, 28.27866061, -6.37442292, -17.93707242, -64.12435399, -81.42209786,
                    -54.35718033, -20.9621922, -41.92151928, -33.21931113, 120.04270918,
                    -1.46908731, 95.41359195)
