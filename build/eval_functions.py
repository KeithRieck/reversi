from board import BLACK
from board import WHITE


class EvaluationFunction:
    """
    Function for assigning values to Boards, indicating the relative advantage for WHITE.
    Positive values indicate that WHITE is doing well.  Negative values mean that BLACK
    is ahead.
    """

    def eval_board(self, board):
        """Return the value of a Board."""
        return 0

    def eval_move(self, board, move):
        """
        Determine the value of the move leading to this Board.
        If processing is still pending, return False.
        When processing is done, put the score into the Move object and return True.
        """
        move.score = self.eval_board(board)
        move.score_depth = 1
        return True

    def eval_vector(self, board):
        return 0, 0


class F0(EvaluationFunction):
    """Trivial function that rates all boards as equal."""

    def eval_board(self, board):
        return 0


def _good_location_1(x, y):
    return (x == 0 and y == 2) or (x == 0 and y == 5) \
           or (x == 7 and y == 2) or (x == 7 and y == 5) \
           or (x == 2 and y == 0) or (x == 5 and y == 0) \
           or (x == 2 and y == 7) or (x == 5 and y == 7)


def _good_location_2(x, y):
    return (x == 2 and y == 2) or (x == 5 and y == 2) \
           or (x == 2 and y == 5) or (x == 5 and y == 5)


def _bad_location_3(x, y):
    return (x == 0 and y == 1) or (x == 0 and y == 6) \
           or (x == 7 and y == 1) or (x == 7 and y == 6) \
           or (x == 1 and y == 0) or (x == 6 and y == 0) \
           or (x == 1 and y == 7) or (x == 6 and y == 7)


def _bad_location_4(x, y):
    return (x == 1 and y == 1) or (x == 6 and y == 1) \
           or (x == 1 and y == 6) or (x == 6 and y == 6)


class F1(EvaluationFunction):
    """Simple linear static evaluation function."""

    def __init__(self, p0=100, p1=120, p2=110, p3=70, p4=50, pm=150):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.pm = pm

    def eval_vector(self, board):
        s0 = 0
        g1 = 0
        g2 = 0
        b3 = 0
        b4 = 0
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
                sm = sm + p if board.is_permanent(player, x, y) else sm
        return s0, g1, g2, b3, b4, sm

    def eval_board(self, board):
        score = 0
        for x in range(8):
            for y in range(8):
                player = board.is_piece(x, y)
                v = self.p0
                v = self.p1 if _good_location_1(x, y) else v
                v = self.p2 if _good_location_2(x, y) else v
                v = self.p3 if _bad_location_3(x, y) else v
                v = self.p4 if _bad_location_4(x, y) else v
                v = self.pm if board.is_permanent(player, x, y) else v
                if player == WHITE:
                    score = score + v
                if player == BLACK:
                    score = score - v
        return score
