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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class F0(EvaluationFunction):
    """Trivial function that rates all boards as equal."""

    def eval_board(self, board):
        return 0


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def _good_location_1(x, y):
    return (x == 0 and y == 2) or (x == 0 and y == 5) \
           or (x == 7 and y == 2) or (x == 7 and y == 5) \
           or (x == 2 and y == 0) or (x == 5 and y == 0) \
           or (x == 2 and y == 7) or (x == 5 and y == 7)


def _good_location_2(x, y):
    return (x == 2 and y == 2) or (x == 5 and y == 2) \
           or (x == 2 and y == 5) or (x == 5 and y == 5)


class F1(EvaluationFunction):
    """Simple linear static evaluation function."""

    def __init__(self, p0=10, p1=12, p2=11, pm=15):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.pm = pm

    def eval_board(self, board):
        score = 0
        for x in range(8):
            for y in range(8):
                player = board.is_piece(x, y)
                v = self.p0
                v = self.p1 if _good_location_1(x, y) else v
                v = self.p2 if _good_location_2(x, y) else v
                v = self.pm if board.is_permanent(player, x, y) else v
                if player == WHITE:
                    score = score + v
                if player == BLACK:
                    score = score - v
        return score

