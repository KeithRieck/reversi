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
        player = 1.0 if board.next_player() == WHITE else 0.0
        return s0, g1, g2, b3, b4, b5, g6, b7, g8, sm, board.move_number, player

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


class F1a(F1):
    """Linear static evaluation function, using weights learned from sklearn's LinearRegression."""

    def __init__(self):
        F1.__init__(self, 28.27866061, -6.37442292, -17.93707242, -64.12435399, -81.42209786,
                    -54.35718033, -20.9621922, -41.92151928, -33.21931113, 120.04270918,
                    -1.46908731, 95.41359195)


class F2(F1):
    """Static evaluation function taken from sklearn's DecisionTreeRegressor."""

    def eval_board(self, board: Board) -> int:
        (s0, g1, g2, b3, b4, b5, g6, b7, g8, sm, move, player) = self.eval_vector(board)
        if sm <= -2.5:
            if sm <= -11.5:
                if sm <= -18.5:
                    if sm <= -31.5:
                        if sm <= -44.5:
                            if move <= 56.5:
                                return int(-5300.0)
                            else:
                                if sm <= -49.5:
                                    return int(-6300.0)
                                else:
                                    return int(-6200.0)
                        else:
                            if b4 <= -3.5:
                                if g6 <= -4.5:
                                    if b3 <= -3.5:
                                        if b5 <= -4.5:
                                            return int(-3595.6666666666665)
                                        else:
                                            return int(-2625.0)
                                    else:
                                        return int(-4205.0)
                                else:
                                    if s0 <= -30.5:
                                        if b3 <= -3.5:
                                            return int(-1820.0)
                                        else:
                                            return int(-1640.0)
                                    else:
                                        return int(-1210.0)
                            else:
                                if g2 <= -0.5:
                                    if g8 <= -2.5:
                                        if sm <= -34.5:
                                            return int(-4008.6923076923076)
                                        else:
                                            return int(-3336.875)
                                    else:
                                        if g1 <= -4.0:
                                            return int(-4357.2307692307695)
                                        else:
                                            return int(-3147.5)
                                else:
                                    if move <= 57.5:
                                        if g6 <= -7.0:
                                            return int(-3021.5)
                                        else:
                                            return int(-2457.5)
                                    else:
                                        if player <= 0.5:
                                            return int(-3520.0)
                                        else:
                                            return int(-4400.0)
                    else:
                        if g1 <= -2.5:
                            if sm <= -22.5:
                                if b4 <= -3.5:
                                    if g8 <= 1.5:
                                        if move <= 53.5:
                                            return int(-2622.4444444444443)
                                        else:
                                            return int(-1767.85)
                                    else:
                                        if b5 <= -1.0:
                                            return int(-2425.714285714286)
                                        else:
                                            return int(-3225.0)
                                else:
                                    if sm <= -26.5:
                                        if b5 <= 1.5:
                                            return int(-3054.2375)
                                        else:
                                            return int(-3833.5)
                                    else:
                                        if s0 <= -25.5:
                                            return int(-2124.8)
                                        else:
                                            return int(-2931.92)
                            else:
                                if s0 <= -19.5:
                                    if g2 <= -2.5:
                                        if s0 <= -22.5:
                                            return int(-1371.3)
                                        else:
                                            return int(-2097.5)
                                    else:
                                        if b4 <= 2.5:
                                            return int(-2261.310344827586)
                                        else:
                                            return int(-1130.0)
                                else:
                                    if move <= 57.5:
                                        if b7 <= -5.5:
                                            return int(-290.0)
                                        else:
                                            return int(-2479.7462686567164)
                                    else:
                                        if b4 <= -1.5:
                                            return int(-2801.157894736842)
                                        else:
                                            return int(-3632.5384615384614)
                        else:
                            if b5 <= -5.5:
                                if b3 <= -1.5:
                                    if move <= 53.5:
                                        if b7 <= -7.0:
                                            return int(-2320.0)
                                        else:
                                            return int(-1820.4)
                                    else:
                                        if b4 <= -1.5:
                                            return int(-1580.1)
                                        else:
                                            return int(-1063.3333333333333)
                                else:
                                    if b7 <= -1.5:
                                        if sm <= -26.5:
                                            return int(-1788.5)
                                        else:
                                            return int(-764.1)
                                    else:
                                        return int(-2400.0)
                            else:
                                if g8 <= -0.5:
                                    if sm <= -23.5:
                                        if b7 <= -3.5:
                                            return int(-2115.714285714286)
                                        else:
                                            return int(-2750.214285714286)
                                    else:
                                        if b7 <= -0.5:
                                            return int(-1893.8865979381444)
                                        else:
                                            return int(-2374.8260869565215)
                                else:
                                    if b4 <= -0.5:
                                        if g1 <= 1.5:
                                            return int(-2333.5857142857144)
                                        else:
                                            return int(-4490.0)
                                    else:
                                        if move <= 56.5:
                                            return int(-2653.4210526315787)
                                        else:
                                            return int(-3422.6666666666665)
                else:
                    if sm <= -14.5:
                        if b5 <= -0.5:
                            if b7 <= -3.5:
                                if move <= 55.5:
                                    if b5 <= -4.5:
                                        if b4 <= -1.5:
                                            return int(-1099.4736842105262)
                                        else:
                                            return int(-1710.7368421052631)
                                    else:
                                        if g8 <= -3.5:
                                            return int(-1596.2727272727273)
                                        else:
                                            return int(-1930.591836734694)
                                else:
                                    if player <= 0.5:
                                        if s0 <= -26.0:
                                            return int(-3800.0)
                                        else:
                                            return int(-1472.9545454545455)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-1003.2666666666667)
                                        else:
                                            return int(103.33333333333333)
                            else:
                                if b7 <= 4.5:
                                    if move <= 57.5:
                                        if b5 <= -5.5:
                                            return int(-1348.7307692307693)
                                        else:
                                            return int(-1839.7721518987341)
                                    else:
                                        if g8 <= -5.0:
                                            return int(-1010.0)
                                        else:
                                            return int(-2328.6666666666665)
                                else:
                                    if b5 <= -3.5:
                                        if b3 <= -3.0:
                                            return int(-1905.0)
                                        else:
                                            return int(-1690.0)
                                    else:
                                        if g8 <= 1.5:
                                            return int(-2436.3333333333335)
                                        else:
                                            return int(-3244.0)
                        else:
                            if move <= 56.5:
                                if b5 <= 0.5:
                                    if s0 <= 3.0:
                                        if g6 <= 1.5:
                                            return int(-1885.7128712871288)
                                        else:
                                            return int(-2882.5)
                                    else:
                                        return int(-310.0)
                                else:
                                    if move <= 50.5:
                                        if b4 <= 1.5:
                                            return int(-1885.8085106382978)
                                        else:
                                            return int(-2186.3888888888887)
                                    else:
                                        if s0 <= -18.5:
                                            return int(-1689.375)
                                        else:
                                            return int(-2181.4025974025976)
                            else:
                                if s0 <= 5.5:
                                    if player <= 0.5:
                                        if s0 <= 2.0:
                                            return int(-2990.086956521739)
                                        else:
                                            return int(-2160.0)
                                    else:
                                        if s0 <= -1.0:
                                            return int(-2385.7291666666665)
                                        else:
                                            return int(-880.0)
                                else:
                                    if g1 <= -2.5:
                                        return int(115.0)
                                    else:
                                        if b4 <= -0.5:
                                            return int(-470.0)
                                        else:
                                            return int(-973.5)
                    else:
                        if b5 <= 0.5:
                            if s0 <= -15.5:
                                if move <= 50.5:
                                    if g2 <= -3.5:
                                        if b4 <= 0.0:
                                            return int(-2096.1428571428573)
                                        else:
                                            return int(-2651.0)
                                    else:
                                        if b3 <= -3.5:
                                            return int(-1866.892857142857)
                                        else:
                                            return int(-1449.8961038961038)
                                else:
                                    if s0 <= -23.5:
                                        if move <= 57.5:
                                            return int(-1496.945945945946)
                                        else:
                                            return int(-3280.0)
                                    else:
                                        if move <= 55.5:
                                            return int(-1359.9893617021276)
                                        else:
                                            return int(-934.5806451612904)
                            else:
                                if move <= 57.5:
                                    if sm <= -13.5:
                                        if b7 <= -5.5:
                                            return int(-848.5)
                                        else:
                                            return int(-1764.1605839416059)
                                    else:
                                        if b4 <= -1.5:
                                            return int(-1372.1007751937984)
                                        else:
                                            return int(-1558.3419913419914)
                                else:
                                    if b5 <= -2.5:
                                        if b3 <= -2.5:
                                            return int(-2384.0)
                                        else:
                                            return int(-1177.0833333333333)
                                    else:
                                        if s0 <= -14.0:
                                            return int(-3261.6666666666665)
                                        else:
                                            return int(-2055.051282051282)
                        else:
                            if move <= 57.5:
                                if b7 <= -2.5:
                                    if b3 <= -4.5:
                                        if b5 <= 2.5:
                                            return int(1210.0)
                                        else:
                                            return int(809.0)
                                    else:
                                        if sm <= -13.5:
                                            return int(-908.25)
                                        else:
                                            return int(-1634.888888888889)
                                else:
                                    if move <= 55.5:
                                        if g1 <= 4.5:
                                            return int(-1727.5528700906345)
                                        else:
                                            return int(-3072.6666666666665)
                                    else:
                                        if s0 <= 11.5:
                                            return int(-2065.7727272727275)
                                        else:
                                            return int(-142.5)
                            else:
                                if g2 <= 3.0:
                                    if b3 <= -4.5:
                                        if b3 <= -5.5:
                                            return int(-3747.5)
                                        else:
                                            return int(-3055.0)
                                    else:
                                        if b3 <= -3.5:
                                            return int(-1742.0)
                                        else:
                                            return int(-2453.823529411765)
                                else:
                                    return int(10.0)
            else:
                if sm <= -6.5:
                    if sm <= -9.5:
                        if b5 <= -3.5:
                            if move <= 51.5:
                                if move <= 41.5:
                                    if player <= 0.5:
                                        if b7 <= -2.5:
                                            return int(-1862.5)
                                        else:
                                            return int(-1473.5)
                                    else:
                                        if b7 <= -2.5:
                                            return int(-1272.125)
                                        else:
                                            return int(-1563.6666666666667)
                                else:
                                    if b7 <= 1.5:
                                        if g1 <= -2.5:
                                            return int(-1248.0)
                                        else:
                                            return int(-943.1034482758621)
                                    else:
                                        if g2 <= 1.0:
                                            return int(-1387.142857142857)
                                        else:
                                            return int(-1854.0)
                            else:
                                if g1 <= 2.5:
                                    if g6 <= -4.5:
                                        if b5 <= -5.5:
                                            return int(-1885.0)
                                        else:
                                            return int(-223.4375)
                                    else:
                                        if g8 <= 1.0:
                                            return int(-758.1836734693877)
                                        else:
                                            return int(-1463.5)
                                else:
                                    if move <= 52.5:
                                        return int(3.0)
                                    else:
                                        if b3 <= 1.5:
                                            return int(246.5)
                                        else:
                                            return int(385.0)
                        else:
                            if move <= 57.5:
                                if b7 <= 1.5:
                                    if b3 <= -6.5:
                                        if s0 <= -17.0:
                                            return int(490.0)
                                        else:
                                            return int(295.0)
                                    else:
                                        if b5 <= 2.5:
                                            return int(-1255.7363636363636)
                                        else:
                                            return int(-1475.7551020408164)
                                else:
                                    if g1 <= -7.5:
                                        if player <= 0.5:
                                            return int(-1109.0)
                                        else:
                                            return int(597.5)
                                    else:
                                        if g6 <= -7.5:
                                            return int(-2966.6666666666665)
                                        else:
                                            return int(-1513.3865546218487)
                            else:
                                if b3 <= 1.5:
                                    if g8 <= 5.0:
                                        if g1 <= -5.5:
                                            return int(-3047.5)
                                        else:
                                            return int(-1941.2115384615386)
                                    else:
                                        if g2 <= 0.0:
                                            return int(-3755.0)
                                        else:
                                            return int(-2280.0)
                                else:
                                    if b5 <= 0.0:
                                        if g8 <= -1.0:
                                            return int(0.0)
                                        else:
                                            return int(-800.0)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-1492.0)
                                        else:
                                            return int(-2000.0)
                    else:
                        if b5 <= -0.5:
                            if b5 <= -3.5:
                                if move <= 52.5:
                                    if b7 <= -5.5:
                                        if g6 <= 1.5:
                                            return int(-61.5)
                                        else:
                                            return int(925.0)
                                    else:
                                        if s0 <= -23.0:
                                            return int(-1534.6)
                                        else:
                                            return int(-925.6969696969697)
                                else:
                                    if s0 <= -32.0:
                                        return int(-3390.0)
                                    else:
                                        if b5 <= -4.5:
                                            return int(-261.97727272727275)
                                        else:
                                            return int(-788.6666666666666)
                            else:
                                if sm <= -7.5:
                                    if move <= 57.5:
                                        if s0 <= -5.5:
                                            return int(-1120.6910299003323)
                                        else:
                                            return int(-979.3214285714286)
                                    else:
                                        if g1 <= 1.5:
                                            return int(-1818.8)
                                        else:
                                            return int(-100.0)
                                else:
                                    if b4 <= -3.5:
                                        if s0 <= -18.5:
                                            return int(-1962.0)
                                        else:
                                            return int(-97.84615384615384)
                                    else:
                                        if b3 <= -3.5:
                                            return int(-693.7435897435897)
                                        else:
                                            return int(-998.913357400722)
                        else:
                            if move <= 57.5:
                                if sm <= -7.5:
                                    if b5 <= 3.5:
                                        if s0 <= -0.5:
                                            return int(-1244.8760330578511)
                                        else:
                                            return int(-1058.3589743589744)
                                    else:
                                        if move <= 46.5:
                                            return int(-1133.1489361702127)
                                        else:
                                            return int(-1487.3475935828876)
                                else:
                                    if b4 <= -1.5:
                                        if b5 <= 3.5:
                                            return int(-866.875)
                                        else:
                                            return int(-350.6363636363636)
                                    else:
                                        if b3 <= -1.5:
                                            return int(-1008.6781115879828)
                                        else:
                                            return int(-1182.3589743589744)
                            else:
                                if b3 <= -5.5:
                                    return int(-3600.0)
                                else:
                                    if player <= 0.5:
                                        if b7 <= -0.5:
                                            return int(-1402.7)
                                        else:
                                            return int(-1826.078431372549)
                                    else:
                                        return int(600.0)
                else:
                    if sm <= -4.5:
                        if move <= 57.5:
                            if b5 <= 0.5:
                                if b3 <= -3.5:
                                    if b4 <= 0.5:
                                        if b7 <= -4.5:
                                            return int(-796.8571428571429)
                                        else:
                                            return int(-302.84033613445376)
                                    else:
                                        if g2 <= 0.5:
                                            return int(-1411.6923076923076)
                                        else:
                                            return int(-425.6)
                                else:
                                    if b7 <= 3.5:
                                        if move <= 51.5:
                                            return int(-743.2273105745212)
                                        else:
                                            return int(-605.4265129682997)
                                    else:
                                        if move <= 56.5:
                                            return int(-853.6418918918919)
                                        else:
                                            return int(-1912.5)
                            else:
                                if b4 <= 1.5:
                                    if g6 <= 3.5:
                                        if s0 <= 5.5:
                                            return int(-886.6880165289256)
                                        else:
                                            return int(-723.3592592592593)
                                    else:
                                        if move <= 53.5:
                                            return int(-1017.3454545454546)
                                        else:
                                            return int(-1588.75)
                                else:
                                    if move <= 54.5:
                                        if b5 <= 4.5:
                                            return int(-1021.4588235294118)
                                        else:
                                            return int(-1345.4833333333333)
                                    else:
                                        if g8 <= -5.0:
                                            return int(1060.0)
                                        else:
                                            return int(-757.7741935483871)
                        else:
                            if b7 <= 2.5:
                                if g2 <= -1.0:
                                    if b3 <= 4.5:
                                        if player <= 0.5:
                                            return int(-381.6666666666667)
                                        else:
                                            return int(320.0)
                                    else:
                                        return int(-3190.0)
                                else:
                                    if b3 <= -4.5:
                                        if b5 <= -3.0:
                                            return int(-505.0)
                                        else:
                                            return int(-20.0)
                                    else:
                                        if g8 <= 3.0:
                                            return int(-1675.7058823529412)
                                        else:
                                            return int(-1050.5)
                            else:
                                if b5 <= -1.0:
                                    if player <= 0.5:
                                        if b3 <= -4.0:
                                            return int(-700.0)
                                        else:
                                            return int(-850.0)
                                    else:
                                        return int(-2185.0)
                                else:
                                    if g1 <= 0.5:
                                        if g1 <= -5.5:
                                            return int(-1966.0)
                                        else:
                                            return int(-2613.076923076923)
                                    else:
                                        if b3 <= -0.5:
                                            return int(-1400.0)
                                        else:
                                            return int(-1285.0)
                    else:
                        if b5 <= 0.5:
                            if b3 <= -1.5:
                                if sm <= -3.5:
                                    if b7 <= -3.5:
                                        if move <= 56.5:
                                            return int(-255.30357142857142)
                                        else:
                                            return int(496.0)
                                    else:
                                        if move <= 55.5:
                                            return int(-452.3392857142857)
                                        else:
                                            return int(-974.2857142857143)
                                else:
                                    if b4 <= -1.5:
                                        if b7 <= 3.5:
                                            return int(-15.63888888888889)
                                        else:
                                            return int(-595.1111111111111)
                                    else:
                                        if move <= 55.5:
                                            return int(-308.7851851851852)
                                        else:
                                            return int(-719.3888888888889)
                            else:
                                if move <= 50.5:
                                    if sm <= -3.5:
                                        if b3 <= 0.5:
                                            return int(-584.6346153846154)
                                        else:
                                            return int(-792.6)
                                    else:
                                        if b4 <= -0.5:
                                            return int(-441.76056338028167)
                                        else:
                                            return int(-562.8582278481013)
                                else:
                                    if player <= 0.5:
                                        if move <= 57.5:
                                            return int(-407.8434782608696)
                                        else:
                                            return int(-908.6206896551724)
                                    else:
                                        if move <= 57.5:
                                            return int(-268.3491124260355)
                                        else:
                                            return int(1019.0)
                        else:
                            if move <= 57.5:
                                if b3 <= 0.5:
                                    if sm <= -3.5:
                                        if g1 <= -6.5:
                                            return int(-2702.5)
                                        else:
                                            return int(-704.1405563689605)
                                    else:
                                        if g1 <= -4.5:
                                            return int(-983.9444444444445)
                                        else:
                                            return int(-477.4188422247446)
                                else:
                                    if b4 <= 3.5:
                                        if b3 <= 3.5:
                                            return int(-828.5281837160752)
                                        else:
                                            return int(-1206.7)
                                    else:
                                        if g1 <= 1.5:
                                            return int(-283.42857142857144)
                                        else:
                                            return int(-1016.0)
                            else:
                                if b3 <= -0.5:
                                    if g1 <= 0.5:
                                        if g1 <= -5.5:
                                            return int(-3357.5)
                                        else:
                                            return int(-2198.076923076923)
                                    else:
                                        if sm <= -3.5:
                                            return int(-1000.0)
                                        else:
                                            return int(-1011.0)
                                else:
                                    if g1 <= -1.5:
                                        if b7 <= -3.0:
                                            return int(-800.0)
                                        else:
                                            return int(-455.0)
                                    else:
                                        if sm <= -3.5:
                                            return int(-1312.2857142857142)
                                        else:
                                            return int(-1982.5)
        else:
            if sm <= 3.5:
                if sm <= 0.5:
                    if sm <= -0.5:
                        if b4 <= -0.5:
                            if sm <= -1.5:
                                if b5 <= -1.5:
                                    if b7 <= 7.5:
                                        if move <= 34.5:
                                            return int(-311.0808080808081)
                                        else:
                                            return int(-59.416666666666664)
                                    else:
                                        return int(-2395.0)
                                else:
                                    if b3 <= -1.5:
                                        if b3 <= -5.5:
                                            return int(756.5)
                                        else:
                                            return int(-197.06299212598427)
                                    else:
                                        if g6 <= 4.5:
                                            return int(-415.00124533001247)
                                        else:
                                            return int(-796.08)
                            else:
                                if b3 <= 0.5:
                                    if b4 <= -1.5:
                                        if b4 <= -2.5:
                                            return int(123.625)
                                        else:
                                            return int(-2.129151291512915)
                                    else:
                                        if b5 <= -3.5:
                                            return int(164.9367088607595)
                                        else:
                                            return int(-118.24778761061947)
                                else:
                                    if move <= 48.5:
                                        if b3 <= 2.5:
                                            return int(-240.77435387673955)
                                        else:
                                            return int(-500.0612244897959)
                                    else:
                                        if g8 <= 3.5:
                                            return int(72.640625)
                                        else:
                                            return int(729.4)
                        else:
                            if b3 <= 1.5:
                                if sm <= -1.5:
                                    if move <= 57.5:
                                        if b5 <= -1.5:
                                            return int(-255.56930693069307)
                                        else:
                                            return int(-506.7916194790487)
                                    else:
                                        if b3 <= -6.0:
                                            return int(-3600.0)
                                        else:
                                            return int(-1273.857142857143)
                                else:
                                    if b4 <= 1.5:
                                        if g1 <= -5.5:
                                            return int(-1997.3333333333333)
                                        else:
                                            return int(-243.5292576419214)
                                    else:
                                        if g6 <= -4.5:
                                            return int(-827.4782608695652)
                                        else:
                                            return int(-413.7900432900433)
                            else:
                                if b3 <= 3.5:
                                    if b5 <= -5.5:
                                        return int(1210.0)
                                    else:
                                        if b7 <= -0.5:
                                            return int(-450.8898550724638)
                                        else:
                                            return int(-558.9656565656566)
                                else:
                                    if move <= 47.5:
                                        if g8 <= -5.0:
                                            return int(188.2)
                                        else:
                                            return int(-669.0952380952381)
                                    else:
                                        if g6 <= -2.5:
                                            return int(-618.875)
                                        else:
                                            return int(-1114.2222222222222)
                    else:
                        if b4 <= -0.5:
                            if b3 <= -0.5:
                                if b3 <= -1.5:
                                    if b5 <= 7.0:
                                        if b3 <= -3.5:
                                            return int(718.3870967741935)
                                        else:
                                            return int(349.8231578947368)
                                    else:
                                        if player <= 0.5:
                                            return int(-1890.0)
                                        else:
                                            return int(-2105.0)
                                else:
                                    if g6 <= 2.5:
                                        if player <= 0.5:
                                            return int(148.85342019543975)
                                        else:
                                            return int(240.48092744951384)
                                    else:
                                        if g1 <= 2.5:
                                            return int(347.744966442953)
                                        else:
                                            return int(958.4166666666666)
                            else:
                                if player <= 0.5:
                                    if g1 <= -1.5:
                                        if b3 <= 1.5:
                                            return int(-118.07664233576642)
                                        else:
                                            return int(-467.0833333333333)
                                    else:
                                        if g6 <= 6.5:
                                            return int(36.49450171821306)
                                        else:
                                            return int(1161.4)
                                else:
                                    if move <= 30.0:
                                        if move <= 22.0:
                                            return int(74.82202957674656)
                                        else:
                                            return int(123.84410256410257)
                                    else:
                                        if g1 <= 6.5:
                                            return int(194.13692162417374)
                                        else:
                                            return int(2590.0)
                        else:
                            if b3 <= 0.5:
                                if b4 <= 0.5:
                                    if b3 <= -1.5:
                                        if player <= 0.5:
                                            return int(89.82005899705015)
                                        else:
                                            return int(253.71393643031786)
                                    else:
                                        if move <= 57.5:
                                            return int(11.968808693319023)
                                        else:
                                            return int(-1198.0)
                                else:
                                    if player <= 0.5:
                                        if b4 <= 1.5:
                                            return int(-81.38916988991372)
                                        else:
                                            return int(-210.1109852774632)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-55.359279141104295)
                                        else:
                                            return int(88.24029126213593)
                            else:
                                if b4 <= 0.5:
                                    if player <= 0.5:
                                        if b3 <= 1.5:
                                            return int(-110.3597232897771)
                                        else:
                                            return int(-275.42432432432435)
                                    else:
                                        if b3 <= 1.5:
                                            return int(-4.798670465337132)
                                        else:
                                            return int(-107.8343949044586)
                                else:
                                    if b3 <= 1.5:
                                        if player <= 0.5:
                                            return int(-248.72406181015452)
                                        else:
                                            return int(-138.9679089026915)
                                    else:
                                        if player <= 0.5:
                                            return int(-420.3847241867044)
                                        else:
                                            return int(-284.3978723404255)
                else:
                    if b4 <= 0.5:
                        if move <= 57.5:
                            if sm <= 1.5:
                                if b3 <= -0.5:
                                    if b3 <= -1.5:
                                        if move <= 54.5:
                                            return int(549.3582966226138)
                                        else:
                                            return int(-85.34615384615384)
                                    else:
                                        if g1 <= 3.5:
                                            return int(389.27784891165174)
                                        else:
                                            return int(-169.61111111111111)
                                else:
                                    if b4 <= -0.5:
                                        if b4 <= -1.5:
                                            return int(402.6653696498054)
                                        else:
                                            return int(284.3541666666667)
                                    else:
                                        if move <= 43.5:
                                            return int(188.6141384388807)
                                        else:
                                            return int(11.944099378881987)
                            else:
                                if b3 <= 0.5:
                                    if move <= 51.5:
                                        if b3 <= -1.5:
                                            return int(808.0901287553648)
                                        else:
                                            return int(612.152719665272)
                                    else:
                                        if b7 <= 2.5:
                                            return int(412.7325581395349)
                                        else:
                                            return int(-222.0188679245283)
                                else:
                                    if b4 <= -1.5:
                                        if g1 <= 5.5:
                                            return int(544.7297297297297)
                                        else:
                                            return int(1828.3333333333333)
                                    else:
                                        if b7 <= 1.5:
                                            return int(430.1304849884527)
                                        else:
                                            return int(243.96464646464648)
                        else:
                            if player <= 0.5:
                                if b5 <= 1.5:
                                    if g6 <= 1.5:
                                        if s0 <= -4.0:
                                            return int(-34.44444444444444)
                                        else:
                                            return int(-569.2222222222222)
                                    else:
                                        if b5 <= -4.5:
                                            return int(-1150.0)
                                        else:
                                            return int(257.8)
                                else:
                                    if b4 <= -1.5:
                                        if sm <= 1.5:
                                            return int(-645.0)
                                        else:
                                            return int(523.0)
                                    else:
                                        if sm <= 1.5:
                                            return int(-1538.0)
                                        else:
                                            return int(-799.1176470588235)
                            else:
                                if g6 <= 1.5:
                                    if g8 <= 1.0:
                                        if g6 <= 0.5:
                                            return int(800.0)
                                        else:
                                            return int(719.0)
                                    else:
                                        if b5 <= 1.0:
                                            return int(1400.0)
                                        else:
                                            return int(1200.0)
                                else:
                                    return int(102.5)
                    else:
                        if sm <= 1.5:
                            if b3 <= -0.5:
                                if move <= 55.5:
                                    if g1 <= -5.5:
                                        if g8 <= 0.5:
                                            return int(-857.0)
                                        else:
                                            return int(-2241.0)
                                    else:
                                        if player <= 0.5:
                                            return int(193.07364975450082)
                                        else:
                                            return int(313.4915887850467)
                                else:
                                    if b7 <= 1.0:
                                        if b5 <= 1.5:
                                            return int(57.36363636363637)
                                        else:
                                            return int(-1200.0)
                                    else:
                                        if b7 <= 5.0:
                                            return int(-850.7142857142857)
                                        else:
                                            return int(-1867.0)
                            else:
                                if move <= 57.5:
                                    if b4 <= 1.5:
                                        if g1 <= 4.5:
                                            return int(112.0640625)
                                        else:
                                            return int(737.0)
                                    else:
                                        if b3 <= 1.5:
                                            return int(23.70985010706638)
                                        else:
                                            return int(-179.37688442211055)
                                else:
                                    if player <= 0.5:
                                        if b3 <= 1.5:
                                            return int(-1324.0)
                                        else:
                                            return int(-234.83333333333334)
                                    else:
                                        return int(1120.0)
                        else:
                            if move <= 57.5:
                                if b3 <= 0.5:
                                    if g1 <= -4.5:
                                        if b5 <= 7.0:
                                            return int(-580.4285714285714)
                                        else:
                                            return int(-1710.0)
                                    else:
                                        if sm <= 2.5:
                                            return int(375.69789983844913)
                                        else:
                                            return int(555.9423558897244)
                                else:
                                    if b5 <= -0.5:
                                        if g1 <= -3.5:
                                            return int(-211.4)
                                        else:
                                            return int(408.2037037037037)
                                    else:
                                        if b3 <= 2.5:
                                            return int(274.76129032258063)
                                        else:
                                            return int(115.89873417721519)
                            else:
                                if player <= 0.5:
                                    if b3 <= -1.5:
                                        if b3 <= -3.0:
                                            return int(-1852.5)
                                        else:
                                            return int(-1001.0)
                                    else:
                                        if b5 <= 2.5:
                                            return int(-311.48)
                                        else:
                                            return int(-1177.5)
                                else:
                                    return int(1800.0)
            else:
                if sm <= 11.5:
                    if sm <= 7.5:
                        if move <= 57.5:
                            if sm <= 5.5:
                                if b3 <= 0.5:
                                    if move <= 53.5:
                                        if b3 <= -1.5:
                                            return int(976.1971326164875)
                                        else:
                                            return int(779.6711041503523)
                                    else:
                                        if b5 <= -0.5:
                                            return int(731.7538461538461)
                                        else:
                                            return int(271.69)
                                else:
                                    if b4 <= 0.5:
                                        if s0 <= -18.5:
                                            return int(-121.0)
                                        else:
                                            return int(697.2063318777292)
                                    else:
                                        if move <= 43.5:
                                            return int(595.837786259542)
                                        else:
                                            return int(405.8390557939914)
                            else:
                                if b5 <= -0.5:
                                    if sm <= 6.5:
                                        if b3 <= -1.5:
                                            return int(1257.5820895522388)
                                        else:
                                            return int(940.3513071895425)
                                    else:
                                        if move <= 52.5:
                                            return int(1083.3078947368422)
                                        else:
                                            return int(1287.9512195121952)
                                else:
                                    if move <= 53.5:
                                        if b5 <= 1.5:
                                            return int(890.8954954954955)
                                        else:
                                            return int(764.0661417322834)
                                    else:
                                        if s0 <= 1.5:
                                            return int(1025.658536585366)
                                        else:
                                            return int(520.2754237288135)
                        else:
                            if player <= 0.5:
                                if g6 <= -2.5:
                                    if s0 <= 2.0:
                                        if sm <= 4.5:
                                            return int(-1403.3333333333333)
                                        else:
                                            return int(85.0)
                                    else:
                                        if g1 <= -2.5:
                                            return int(-1668.0)
                                        else:
                                            return int(-780.0)
                                else:
                                    if b5 <= -5.5:
                                        if b3 <= 0.0:
                                            return int(526.0)
                                        else:
                                            return int(1566.6666666666667)
                                    else:
                                        if s0 <= -6.0:
                                            return int(-807.0)
                                        else:
                                            return int(-44.16417910447761)
                            else:
                                if g6 <= -0.5:
                                    if g1 <= -3.5:
                                        if g1 <= -5.0:
                                            return int(2800.0)
                                        else:
                                            return int(2600.0)
                                    else:
                                        return int(1767.5)
                                else:
                                    if b7 <= -3.0:
                                        return int(2600.0)
                                    else:
                                        if b3 <= 0.5:
                                            return int(633.3333333333334)
                                        else:
                                            return int(-1001.6666666666666)
                    else:
                        if move <= 57.5:
                            if b7 <= 3.5:
                                if b5 <= -1.5:
                                    if sm <= 8.5:
                                        if b3 <= 1.5:
                                            return int(1369.2576687116564)
                                        else:
                                            return int(1080.0594059405942)
                                    else:
                                        if b3 <= 4.5:
                                            return int(1479.4667931688805)
                                        else:
                                            return int(1088.2)
                                else:
                                    if sm <= 10.5:
                                        if b5 <= 3.5:
                                            return int(1188.511652542373)
                                        else:
                                            return int(1024.2362637362637)
                                    else:
                                        if g8 <= 5.5:
                                            return int(1398.3018181818181)
                                        else:
                                            return int(651.75)
                            else:
                                if b5 <= 2.5:
                                    if move <= 54.5:
                                        if sm <= 10.5:
                                            return int(1095.73417721519)
                                        else:
                                            return int(1337.404255319149)
                                    else:
                                        if s0 <= 9.5:
                                            return int(1285.95)
                                        else:
                                            return int(454.43333333333334)
                                else:
                                    if g1 <= -1.5:
                                        if g8 <= 3.0:
                                            return int(-125.15384615384616)
                                        else:
                                            return int(-1447.5)
                                    else:
                                        if move <= 52.5:
                                            return int(934.4827586206897)
                                        else:
                                            return int(561.0327868852459)
                        else:
                            if s0 <= 4.0:
                                if g6 <= 3.0:
                                    if player <= 0.5:
                                        if g2 <= 1.0:
                                            return int(835.4615384615385)
                                        else:
                                            return int(1293.8461538461538)
                                    else:
                                        if b5 <= 3.0:
                                            return int(2255.5)
                                        else:
                                            return int(1675.0)
                                else:
                                    if b5 <= -1.5:
                                        return int(396.0)
                                    else:
                                        return int(-1520.0)
                            else:
                                if sm <= 10.5:
                                    if player <= 0.5:
                                        if b3 <= 1.5:
                                            return int(-226.9814814814815)
                                        else:
                                            return int(295.96153846153845)
                                    else:
                                        if g1 <= 2.5:
                                            return int(2800.0)
                                        else:
                                            return int(1000.0)
                                else:
                                    if g2 <= -1.0:
                                        if s0 <= 9.0:
                                            return int(-705.0)
                                        else:
                                            return int(271.25)
                                    else:
                                        if g6 <= 1.5:
                                            return int(1120.5555555555557)
                                        else:
                                            return int(453.75)
                else:
                    if sm <= 20.5:
                        if move <= 57.5:
                            if sm <= 15.5:
                                if b5 <= 3.5:
                                    if b5 <= -1.5:
                                        if move <= 49.5:
                                            return int(1654.609375)
                                        else:
                                            return int(1871.97583081571)
                                    else:
                                        if sm <= 13.5:
                                            return int(1520.5466377440348)
                                        else:
                                            return int(1707.2151898734178)
                                else:
                                    if b3 <= -1.5:
                                        if b5 <= 6.5:
                                            return int(-250.0)
                                        else:
                                            return int(266.25)
                                    else:
                                        if sm <= 13.5:
                                            return int(1186.439393939394)
                                        else:
                                            return int(1463.1287128712872)
                            else:
                                if b7 <= 5.5:
                                    if g8 <= 4.5:
                                        if b5 <= -0.5:
                                            return int(2258.2096219931273)
                                        else:
                                            return int(2012.215953307393)
                                    else:
                                        if b5 <= 0.5:
                                            return int(1918.842105263158)
                                        else:
                                            return int(1217.4594594594594)
                                else:
                                    if move <= 53.5:
                                        if g2 <= 0.5:
                                            return int(1672.8)
                                        else:
                                            return int(2147.923076923077)
                                    else:
                                        if b4 <= 1.5:
                                            return int(1444.8181818181818)
                                        else:
                                            return int(587.5)
                        else:
                            if player <= 0.5:
                                if sm <= 16.5:
                                    if b7 <= 2.5:
                                        if g6 <= -3.0:
                                            return int(-640.0)
                                        else:
                                            return int(933.2592592592592)
                                    else:
                                        if b3 <= 4.5:
                                            return int(214.2)
                                        else:
                                            return int(1552.5)
                                else:
                                    if s0 <= 16.0:
                                        if b5 <= -2.5:
                                            return int(2292.3333333333335)
                                        else:
                                            return int(1533.2325581395348)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-58.0)
                                        else:
                                            return int(1112.7254901960785)
                            else:
                                if b5 <= 1.0:
                                    if b7 <= -1.0:
                                        if b3 <= 5.5:
                                            return int(2775.625)
                                        else:
                                            return int(3510.0)
                                    else:
                                        if sm <= 13.5:
                                            return int(1687.0)
                                        else:
                                            return int(2543.75)
                                else:
                                    if sm <= 18.5:
                                        if b3 <= 2.5:
                                            return int(3495.0)
                                        else:
                                            return int(2821.6666666666665)
                                    else:
                                        return int(4600.0)
                    else:
                        if move <= 57.5:
                            if sm <= 25.5:
                                if b5 <= 4.5:
                                    if b3 <= 4.5:
                                        if g1 <= 1.5:
                                            return int(2018.34375)
                                        else:
                                            return int(2477.2085561497324)
                                    else:
                                        if g2 <= 3.5:
                                            return int(2852.43661971831)
                                        else:
                                            return int(1992.4285714285713)
                                else:
                                    if s0 <= 34.0:
                                        if b5 <= 5.5:
                                            return int(1285.6)
                                        else:
                                            return int(1972.4375)
                                    else:
                                        if player <= 0.5:
                                            return int(2536.0)
                                        else:
                                            return int(3302.5)
                            else:
                                if sm <= 34.5:
                                    if g2 <= 3.5:
                                        if g6 <= 5.5:
                                            return int(2763.179775280899)
                                        else:
                                            return int(3110.9767441860463)
                                    else:
                                        if b5 <= 1.5:
                                            return int(2851.769230769231)
                                        else:
                                            return int(2056.8125)
                                else:
                                    if b7 <= 7.0:
                                        if b3 <= 3.5:
                                            return int(3342.0)
                                        else:
                                            return int(3867.625)
                                    else:
                                        return int(1100.0)
                        else:
                            if player <= 0.5:
                                if sm <= 25.5:
                                    if s0 <= 18.0:
                                        if s0 <= 12.0:
                                            return int(2707.5714285714284)
                                        else:
                                            return int(1987.92)
                                    else:
                                        if g8 <= 5.0:
                                            return int(1537.6724137931035)
                                        else:
                                            return int(534.0)
                                else:
                                    if g6 <= 2.5:
                                        if g1 <= 1.5:
                                            return int(566.6666666666666)
                                        else:
                                            return int(1865.2307692307693)
                                    else:
                                        if sm <= 32.5:
                                            return int(2274.421875)
                                        else:
                                            return int(2769.5652173913045)
                            else:
                                if g1 <= 3.5:
                                    if g6 <= 4.5:
                                        if b3 <= 2.5:
                                            return int(3242.6666666666665)
                                        else:
                                            return int(2797.8)
                                    else:
                                        if s0 <= 12.0:
                                            return int(3400.0)
                                        else:
                                            return int(3600.0)
                                else:
                                    if b7 <= -1.0:
                                        return int(3280.0)
                                    else:
                                        if b7 <= 1.0:
                                            return int(4620.0)
                                        else:
                                            return int(4495.5)
