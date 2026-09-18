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
        if sm <= -1.5:
            if sm <= -7.5:
                if sm <= -14.5:
                    if sm <= -22.5:
                        if sm <= -41.0:
                            if sm <= -44.5:
                                if move <= 56.5:
                                    return int(-6200.0)
                                else:
                                    return int(-6300.0)
                            else:
                                if move <= 57.5:
                                    return int(-5000.0)
                                else:
                                    return int(-3900.0)
                        else:
                            if b5 <= -5.5:
                                if sm <= -27.5:
                                    if g8 <= -1.0:
                                        if b4 <= -2.5:
                                            return int(-1475.5555555555557)
                                        else:
                                            return int(-2634.5)
                                    else:
                                        if s0 <= -28.5:
                                            return int(-4636.666666666667)
                                        else:
                                            return int(-3163.3333333333335)
                                else:
                                    if b7 <= -2.5:
                                        if s0 <= -29.0:
                                            return int(-1534.5)
                                        else:
                                            return int(-857.7777777777778)
                                    else:
                                        if s0 <= -27.5:
                                            return int(-1415.0)
                                        else:
                                            return int(-2325.0)
                            else:
                                if sm <= -30.5:
                                    if move <= 57.5:
                                        if g2 <= -3.0:
                                            return int(-3812.8125)
                                        else:
                                            return int(-3314.0625)
                                    else:
                                        if b7 <= -3.0:
                                            return int(-3573.5)
                                        else:
                                            return int(-4882.0)
                                else:
                                    if b4 <= -3.5:
                                        if g6 <= -5.5:
                                            return int(-2929.1666666666665)
                                        else:
                                            return int(-2107.4333333333334)
                                    else:
                                        if s0 <= -21.5:
                                            return int(-2791.987012987013)
                                        else:
                                            return int(-3230.4285714285716)
                    else:
                        if b5 <= -2.5:
                            if b7 <= -3.5:
                                if b4 <= -1.5:
                                    if b7 <= -4.5:
                                        if b3 <= -1.5:
                                            return int(-1274.357142857143)
                                        else:
                                            return int(-556.2941176470588)
                                    else:
                                        if move <= 57.5:
                                            return int(-1306.6923076923076)
                                        else:
                                            return int(-2701.25)
                                else:
                                    if b5 <= -5.5:
                                        if s0 <= -15.5:
                                            return int(-918.5)
                                        else:
                                            return int(-1590.0)
                                    else:
                                        if b3 <= 0.5:
                                            return int(-1884.0350877192982)
                                        else:
                                            return int(-268.5)
                            else:
                                if b5 <= -5.5:
                                    if player <= 0.5:
                                        if s0 <= -12.0:
                                            return int(-1998.25)
                                        else:
                                            return int(-300.0)
                                    else:
                                        if move <= 50.0:
                                            return int(-1931.0)
                                        else:
                                            return int(-1168.1666666666667)
                                else:
                                    if move <= 57.5:
                                        if s0 <= -8.5:
                                            return int(-1938.241573033708)
                                        else:
                                            return int(-3331.0)
                                    else:
                                        if g8 <= -4.0:
                                            return int(-1010.0)
                                        else:
                                            return int(-2817.3333333333335)
                        else:
                            if move <= 50.5:
                                if b4 <= 1.5:
                                    if sm <= -20.5:
                                        if g2 <= 1.0:
                                            return int(-2270.8823529411766)
                                        else:
                                            return int(-3455.0)
                                    else:
                                        if b7 <= 5.5:
                                            return int(-1972.2044198895028)
                                        else:
                                            return int(-2678.5)
                                else:
                                    if sm <= -17.5:
                                        if b5 <= -1.5:
                                            return int(-3983.0)
                                        else:
                                            return int(-3003.125)
                                    else:
                                        if move <= 43.5:
                                            return int(-3088.5)
                                        else:
                                            return int(-2224.181818181818)
                            else:
                                if player <= 0.5:
                                    if move <= 54.5:
                                        if s0 <= -10.0:
                                            return int(-2251.5142857142855)
                                        else:
                                            return int(-2644.0675675675675)
                                    else:
                                        if s0 <= 4.5:
                                            return int(-2934.8009478672984)
                                        else:
                                            return int(-1845.6)
                                else:
                                    if s0 <= -19.5:
                                        if g8 <= -1.5:
                                            return int(-1685.9130434782608)
                                        else:
                                            return int(-2178.825)
                                    else:
                                        if sm <= -19.5:
                                            return int(-2879.449275362319)
                                        else:
                                            return int(-2266.308)
                else:
                    if b5 <= -0.5:
                        if sm <= -11.5:
                            if s0 <= -11.5:
                                if sm <= -13.5:
                                    if b3 <= -0.5:
                                        if g8 <= -5.5:
                                            return int(-3462.8)
                                        else:
                                            return int(-1661.1860465116279)
                                    else:
                                        if move <= 51.5:
                                            return int(-2122.0)
                                        else:
                                            return int(-412.9166666666667)
                                else:
                                    if b4 <= -3.5:
                                        if g1 <= 1.5:
                                            return int(-790.6923076923077)
                                        else:
                                            return int(443.3333333333333)
                                    else:
                                        if s0 <= -17.5:
                                            return int(-1077.7816091954023)
                                        else:
                                            return int(-1523.5114503816794)
                            else:
                                if g6 <= 0.5:
                                    if move <= 55.5:
                                        if b3 <= 2.5:
                                            return int(-1808.3925925925926)
                                        else:
                                            return int(290.0)
                                    else:
                                        if g1 <= -1.5:
                                            return int(-2521.5789473684213)
                                        else:
                                            return int(-1943.0555555555557)
                                else:
                                    if s0 <= -7.5:
                                        if move <= 51.5:
                                            return int(-1221.0)
                                        else:
                                            return int(-668.5)
                                    else:
                                        if b3 <= 0.5:
                                            return int(-1628.9411764705883)
                                        else:
                                            return int(-2351.714285714286)
                        else:
                            if b5 <= -3.5:
                                if move <= 50.5:
                                    if sm <= -9.5:
                                        if sm <= -10.5:
                                            return int(-1047.3076923076924)
                                        else:
                                            return int(-1391.3225806451612)
                                    else:
                                        if b7 <= -1.5:
                                            return int(-819.0294117647059)
                                        else:
                                            return int(-1090.873015873016)
                                else:
                                    if player <= 0.5:
                                        if s0 <= -26.0:
                                            return int(-3980.0)
                                        else:
                                            return int(-943.8524590163935)
                                    else:
                                        if s0 <= -31.0:
                                            return int(-2289.0)
                                        else:
                                            return int(-514.1428571428571)
                            else:
                                if sm <= -9.5:
                                    if g8 <= 7.0:
                                        if b7 <= 1.5:
                                            return int(-1315.0681818181818)
                                        else:
                                            return int(-1683.1649484536083)
                                    else:
                                        return int(2005.0)
                                else:
                                    if b3 <= -0.5:
                                        if move <= 57.5:
                                            return int(-1110.3459302325582)
                                        else:
                                            return int(-1723.5)
                                    else:
                                        if g6 <= -2.5:
                                            return int(-899.7692307692307)
                                        else:
                                            return int(-1414.3854166666667)
                    else:
                        if sm <= -11.5:
                            if s0 <= -10.5:
                                if s0 <= -15.5:
                                    if move <= 53.5:
                                        if g8 <= -1.5:
                                            return int(-1391.3214285714287)
                                        else:
                                            return int(-2003.4285714285713)
                                    else:
                                        if b4 <= 2.5:
                                            return int(-1066.9714285714285)
                                        else:
                                            return int(1210.0)
                                else:
                                    if b7 <= 1.5:
                                        if g1 <= -4.5:
                                            return int(-2222.3125)
                                        else:
                                            return int(-1565.9444444444443)
                                    else:
                                        if g8 <= -7.0:
                                            return int(-3895.0)
                                        else:
                                            return int(-2150.814814814815)
                            else:
                                if move <= 55.5:
                                    if b7 <= -0.5:
                                        if b3 <= -1.5:
                                            return int(-1450.3636363636363)
                                        else:
                                            return int(-1968.0)
                                    else:
                                        if g1 <= -5.5:
                                            return int(-2747.6363636363635)
                                        else:
                                            return int(-2082.402985074627)
                                else:
                                    if player <= 0.5:
                                        if s0 <= 6.0:
                                            return int(-2720.704081632653)
                                        else:
                                            return int(-1967.3076923076924)
                                    else:
                                        if s0 <= 12.0:
                                            return int(-1992.8461538461538)
                                        else:
                                            return int(400.0)
                        else:
                            if move <= 53.5:
                                if b4 <= 0.5:
                                    if sm <= -8.5:
                                        if g8 <= -6.5:
                                            return int(254.0)
                                        else:
                                            return int(-1509.0639534883721)
                                    else:
                                        if move <= 50.5:
                                            return int(-1178.0545454545454)
                                        else:
                                            return int(-1531.9242424242425)
                                else:
                                    if b5 <= 4.5:
                                        if g6 <= -2.5:
                                            return int(-1745.7596153846155)
                                        else:
                                            return int(-1478.4913294797689)
                                    else:
                                        if b3 <= -3.5:
                                            return int(-2342.0)
                                        else:
                                            return int(-1822.0754716981132)
                            else:
                                if player <= 0.5:
                                    if b7 <= 2.5:
                                        if move <= 54.5:
                                            return int(-1588.560975609756)
                                        else:
                                            return int(-1972.3333333333333)
                                    else:
                                        if b4 <= 0.5:
                                            return int(-2382.560606060606)
                                        else:
                                            return int(-1888.0)
                                else:
                                    if b7 <= 1.5:
                                        if s0 <= -9.0:
                                            return int(-826.5217391304348)
                                        else:
                                            return int(-1479.9354838709678)
                                    else:
                                        if b5 <= 3.5:
                                            return int(-1495.016393442623)
                                        else:
                                            return int(-2509.9615384615386)
            else:
                if sm <= -4.5:
                    if b5 <= -0.5:
                        if b3 <= -2.5:
                            if move <= 55.5:
                                if b5 <= -3.5:
                                    if move <= 49.5:
                                        if g1 <= -0.5:
                                            return int(-299.87179487179486)
                                        else:
                                            return int(-1035.7692307692307)
                                    else:
                                        if b4 <= 0.5:
                                            return int(-3.3508771929824563)
                                        else:
                                            return int(-991.7142857142857)
                                else:
                                    if b4 <= -1.5:
                                        if sm <= -6.5:
                                            return int(-662.1176470588235)
                                        else:
                                            return int(-119.47169811320755)
                                    else:
                                        if g8 <= 2.5:
                                            return int(-653.1926605504588)
                                        else:
                                            return int(-1372.5217391304348)
                            else:
                                if s0 <= -1.5:
                                    if g6 <= 2.5:
                                        if s0 <= -12.0:
                                            return int(-645.7222222222222)
                                        else:
                                            return int(-1417.0)
                                    else:
                                        if g8 <= -4.0:
                                            return int(800.0)
                                        else:
                                            return int(110.0)
                                else:
                                    if g8 <= 5.0:
                                        if b3 <= -3.5:
                                            return int(-5000.0)
                                        else:
                                            return int(-2452.5)
                                    else:
                                        return int(200.0)
                        else:
                            if b7 <= -3.5:
                                if sm <= -6.5:
                                    if b3 <= 1.5:
                                        if move <= 55.5:
                                            return int(-897.6792452830189)
                                        else:
                                            return int(-1588.6666666666667)
                                    else:
                                        if s0 <= 1.5:
                                            return int(458.6666666666667)
                                        else:
                                            return int(-180.0)
                                else:
                                    if move <= 54.5:
                                        if g8 <= -0.5:
                                            return int(-406.271186440678)
                                        else:
                                            return int(-685.2444444444444)
                                    else:
                                        if player <= 0.5:
                                            return int(-992.75)
                                        else:
                                            return int(277.3333333333333)
                            else:
                                if move <= 55.5:
                                    if sm <= -6.5:
                                        if b4 <= -3.5:
                                            return int(-525.8571428571429)
                                        else:
                                            return int(-1119.0441988950276)
                                    else:
                                        if b3 <= -1.5:
                                            return int(-681.191235059761)
                                        else:
                                            return int(-878.548623853211)
                                else:
                                    if s0 <= -7.5:
                                        if player <= 0.5:
                                            return int(-1082.6153846153845)
                                        else:
                                            return int(75.83333333333333)
                                    else:
                                        if b4 <= -1.5:
                                            return int(-744.4736842105264)
                                        else:
                                            return int(-1839.3333333333333)
                    else:
                        if move <= 55.5:
                            if b4 <= 1.5:
                                if b3 <= 0.5:
                                    if sm <= -6.5:
                                        if b3 <= -1.5:
                                            return int(-990.9961832061068)
                                        else:
                                            return int(-1315.041095890411)
                                    else:
                                        if b5 <= 1.5:
                                            return int(-863.9013657056146)
                                        else:
                                            return int(-1008.9853157121879)
                                else:
                                    if sm <= -6.5:
                                        if b5 <= 4.5:
                                            return int(-1430.0235294117647)
                                        else:
                                            return int(-1974.3076923076924)
                                    else:
                                        if s0 <= 9.5:
                                            return int(-1202.844155844156)
                                        else:
                                            return int(-823.575)
                            else:
                                if b5 <= 2.5:
                                    if b3 <= 1.5:
                                        if b7 <= -2.5:
                                            return int(-870.9565217391304)
                                        else:
                                            return int(-1170.1831683168316)
                                    else:
                                        if g1 <= -3.5:
                                            return int(-864.5)
                                        else:
                                            return int(-1733.2)
                                else:
                                    if b3 <= -2.5:
                                        if g1 <= -1.5:
                                            return int(-2203.8)
                                        else:
                                            return int(-1667.6666666666667)
                                    else:
                                        if move <= 54.5:
                                            return int(-1453.1628959276018)
                                        else:
                                            return int(-615.8333333333334)
                        else:
                            if player <= 0.5:
                                if b7 <= 1.5:
                                    if g6 <= 5.5:
                                        if sm <= -5.5:
                                            return int(-1779.5438596491229)
                                        else:
                                            return int(-1147.2727272727273)
                                    else:
                                        if sm <= -6.0:
                                            return int(-2990.0)
                                        else:
                                            return int(-3990.0)
                                else:
                                    if move <= 56.5:
                                        if b3 <= 0.5:
                                            return int(-2124.6285714285714)
                                        else:
                                            return int(-1456.6666666666667)
                                    else:
                                        if b5 <= 1.5:
                                            return int(-1941.8181818181818)
                                        else:
                                            return int(-2570.1153846153848)
                            else:
                                if s0 <= 7.5:
                                    if b7 <= 1.5:
                                        if sm <= -6.5:
                                            return int(-961.7692307692307)
                                        else:
                                            return int(-244.1578947368421)
                                    else:
                                        if s0 <= 1.0:
                                            return int(-1035.8333333333333)
                                        else:
                                            return int(-2446.0)
                                else:
                                    if g6 <= 2.5:
                                        return int(-2095.0)
                                    else:
                                        if b3 <= 1.5:
                                            return int(-3030.0)
                                        else:
                                            return int(-3690.0)
                else:
                    if b5 <= -0.5:
                        if b3 <= -1.5:
                            if sm <= -3.5:
                                if g1 <= -0.5:
                                    if b7 <= -0.5:
                                        if move <= 40.5:
                                            return int(-437.46153846153845)
                                        else:
                                            return int(67.39622641509433)
                                    else:
                                        if move <= 55.5:
                                            return int(-394.030303030303)
                                        else:
                                            return int(-1110.0)
                                else:
                                    if b4 <= 0.5:
                                        if g2 <= -0.5:
                                            return int(-630.5769230769231)
                                        else:
                                            return int(-317.0925925925926)
                                    else:
                                        if b5 <= -4.5:
                                            return int(-2090.0)
                                        else:
                                            return int(-711.9354838709677)
                            else:
                                if b5 <= -3.5:
                                    if move <= 53.5:
                                        if g6 <= -3.5:
                                            return int(688.4444444444445)
                                        else:
                                            return int(196.86111111111111)
                                    else:
                                        if s0 <= -8.5:
                                            return int(-711.8888888888889)
                                        else:
                                            return int(423.375)
                                else:
                                    if g6 <= 3.5:
                                        if b3 <= -4.5:
                                            return int(587.1428571428571)
                                        else:
                                            return int(-206.68564356435644)
                                    else:
                                        if g1 <= 2.5:
                                            return int(45.666666666666664)
                                        else:
                                            return int(830.1428571428571)
                        else:
                            if move <= 48.5:
                                if b4 <= -0.5:
                                    if sm <= -2.5:
                                        if g6 <= -5.5:
                                            return int(-1728.0)
                                        else:
                                            return int(-541.7595907928388)
                                    else:
                                        if g6 <= 3.5:
                                            return int(-317.12703583061887)
                                        else:
                                            return int(193.15384615384616)
                                else:
                                    if sm <= -3.5:
                                        if g1 <= 1.5:
                                            return int(-807.139344262295)
                                        else:
                                            return int(-1235.611111111111)
                                    else:
                                        if g8 <= -3.5:
                                            return int(-838.9344262295082)
                                        else:
                                            return int(-553.2684931506849)
                            else:
                                if player <= 0.5:
                                    if g6 <= 7.5:
                                        if move <= 55.0:
                                            return int(-305.3069306930693)
                                        else:
                                            return int(-873.2181818181818)
                                    else:
                                        if b3 <= 1.5:
                                            return int(-3780.0)
                                        else:
                                            return int(-2890.0)
                                else:
                                    if move <= 54.0:
                                        if b5 <= -2.5:
                                            return int(-66.15)
                                        else:
                                            return int(-395.6276595744681)
                                    else:
                                        if g6 <= -2.5:
                                            return int(-111.26923076923077)
                                        else:
                                            return int(379.2)
                    else:
                        if move <= 55.5:
                            if b3 <= -0.5:
                                if sm <= -3.5:
                                    if b5 <= 2.5:
                                        if g6 <= -1.5:
                                            return int(-846.9491525423729)
                                        else:
                                            return int(-652.5331010452961)
                                    else:
                                        if g1 <= -2.5:
                                            return int(-1458.5714285714287)
                                        else:
                                            return int(-834.1830065359477)
                                else:
                                    if b4 <= 0.5:
                                        if move <= 54.5:
                                            return int(-408.85806451612905)
                                        else:
                                            return int(473.53333333333336)
                                    else:
                                        if b7 <= 2.5:
                                            return int(-564.858310626703)
                                        else:
                                            return int(-767.0677966101695)
                            else:
                                if sm <= -2.5:
                                    if b3 <= 0.5:
                                        if b5 <= 6.5:
                                            return int(-757.9287974683544)
                                        else:
                                            return int(-1637.1)
                                    else:
                                        if s0 <= 14.5:
                                            return int(-970.2427983539095)
                                        else:
                                            return int(-1271.8235294117646)
                                else:
                                    if b3 <= 3.5:
                                        if move <= 48.5:
                                            return int(-687.7792378449409)
                                        else:
                                            return int(-458.74074074074076)
                                    else:
                                        if b7 <= 5.0:
                                            return int(-1058.7586206896551)
                                        else:
                                            return int(-2869.5)
                        else:
                            if player <= 0.5:
                                if g1 <= -5.5:
                                    if move <= 57.0:
                                        return int(-1820.0)
                                    else:
                                        if b5 <= 4.5:
                                            return int(-3700.0)
                                        else:
                                            return int(-4500.0)
                                else:
                                    if b7 <= 4.5:
                                        if b5 <= 3.5:
                                            return int(-1253.5533980582525)
                                        else:
                                            return int(-1825.5294117647059)
                                    else:
                                        if s0 <= 11.0:
                                            return int(-2823.846153846154)
                                        else:
                                            return int(-1617.2857142857142)
                            else:
                                if b7 <= 7.0:
                                    if g2 <= 1.0:
                                        if b5 <= 1.5:
                                            return int(-43.774193548387096)
                                        else:
                                            return int(-615.7368421052631)
                                    else:
                                        if g6 <= 3.0:
                                            return int(-1178.611111111111)
                                        else:
                                            return int(861.0)
                                else:
                                    return int(-3697.5)
        else:
            if sm <= 3.5:
                if sm <= 0.5:
                    if b4 <= 0.5:
                        if b3 <= -0.5:
                            if b4 <= -0.5:
                                if sm <= -0.5:
                                    if b5 <= 3.5:
                                        if move <= 55.5:
                                            return int(118.83349561830575)
                                        else:
                                            return int(-485.14285714285717)
                                    else:
                                        if move <= 52.5:
                                            return int(-312.68)
                                        else:
                                            return int(-1891.5714285714287)
                                else:
                                    if b3 <= -1.5:
                                        if b5 <= 7.0:
                                            return int(515.1065830721003)
                                        else:
                                            return int(-2855.0)
                                    else:
                                        if b4 <= -1.5:
                                            return int(400.19597315436243)
                                        else:
                                            return int(258.3535539215686)
                            else:
                                if sm <= -0.5:
                                    if move <= 55.5:
                                        if b7 <= -0.5:
                                            return int(-11.654929577464788)
                                        else:
                                            return int(-216.19163763066203)
                                    else:
                                        if move <= 56.5:
                                            return int(-1361.8333333333333)
                                        else:
                                            return int(-577.5)
                                else:
                                    if move <= 55.5:
                                        if b3 <= -1.5:
                                            return int(223.28571428571428)
                                        else:
                                            return int(73.63138832997988)
                                    else:
                                        if g1 <= -1.0:
                                            return int(-2470.0)
                                        else:
                                            return int(-471.42857142857144)
                        else:
                            if sm <= -0.5:
                                if b3 <= 1.5:
                                    if b4 <= -1.5:
                                        if move <= 44.5:
                                            return int(-51.05882352941177)
                                        else:
                                            return int(285.49411764705883)
                                    else:
                                        if b4 <= -0.5:
                                            return int(-182.4286689419795)
                                        else:
                                            return int(-317.2507204610951)
                                else:
                                    if b4 <= -1.5:
                                        if move <= 48.5:
                                            return int(-300.29801324503313)
                                        else:
                                            return int(387.6190476190476)
                                    else:
                                        if b5 <= -2.5:
                                            return int(-245.625)
                                        else:
                                            return int(-614.5030674846626)
                            else:
                                if b4 <= -0.5:
                                    if player <= 0.5:
                                        if g1 <= -1.5:
                                            return int(-168.84868421052633)
                                        else:
                                            return int(65.38403990024938)
                                    else:
                                        if b4 <= -1.5:
                                            return int(277.4432624113475)
                                        else:
                                            return int(127.06887328652624)
                                else:
                                    if b3 <= 1.5:
                                        if b3 <= 0.5:
                                            return int(2.3785494355114607)
                                        else:
                                            return int(-85.86147757255937)
                                    else:
                                        if player <= 0.5:
                                            return int(-351.79888268156424)
                                        else:
                                            return int(-174.2442996742671)
                    else:
                        if b3 <= 0.5:
                            if sm <= -0.5:
                                if b5 <= 3.5:
                                    if b4 <= 1.5:
                                        if move <= 46.5:
                                            return int(-307.08049535603715)
                                        else:
                                            return int(54.48076923076923)
                                    else:
                                        if g6 <= -4.5:
                                            return int(-1120.6666666666667)
                                        else:
                                            return int(-440.87280701754383)
                                else:
                                    if g1 <= -4.0:
                                        if b7 <= 4.5:
                                            return int(-1083.75)
                                        else:
                                            return int(-3710.0)
                                    else:
                                        if b7 <= 5.5:
                                            return int(-601.8846153846154)
                                        else:
                                            return int(-1204.857142857143)
                            else:
                                if b4 <= 1.5:
                                    if b3 <= -1.5:
                                        if move <= 50.0:
                                            return int(94.68627450980392)
                                        else:
                                            return int(-625.8666666666667)
                                    else:
                                        if player <= 0.5:
                                            return int(-118.63095238095238)
                                        else:
                                            return int(-56.65162311955661)
                                else:
                                    if player <= 0.5:
                                        if move <= 25.0:
                                            return int(-169.1172638436482)
                                        else:
                                            return int(-368.3284671532847)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-192.1159420289855)
                                        else:
                                            return int(50.54189944134078)
                        else:
                            if move <= 31.5:
                                if sm <= -0.5:
                                    if b3 <= 1.5:
                                        if move <= 21.5:
                                            return int(-419.8)
                                        else:
                                            return int(-522.4520547945206)
                                    else:
                                        if g1 <= -3.0:
                                            return int(-357.0)
                                        else:
                                            return int(-647.2857142857143)
                                else:
                                    if b3 <= 1.5:
                                        if b4 <= 1.5:
                                            return int(-252.97237569060775)
                                        else:
                                            return int(-335.0844327176781)
                                    else:
                                        if g1 <= -1.5:
                                            return int(-639.0175438596491)
                                        else:
                                            return int(-399.61007957559684)
                            else:
                                if b4 <= 1.5:
                                    if b3 <= 1.5:
                                        if sm <= -0.5:
                                            return int(-473.90625)
                                        else:
                                            return int(-276.7100977198697)
                                    else:
                                        if sm <= -0.5:
                                            return int(-660.8253012048193)
                                        else:
                                            return int(-497.50621118012424)
                                else:
                                    if player <= 0.5:
                                        if move <= 47.0:
                                            return int(-699.4671968190855)
                                        else:
                                            return int(-968.5982142857143)
                                    else:
                                        if sm <= -0.5:
                                            return int(-713.5454545454545)
                                        else:
                                            return int(-453.6827309236948)
                else:
                    if b4 <= 0.5:
                        if move <= 55.5:
                            if b3 <= -1.5:
                                if g8 <= 5.5:
                                    if sm <= 1.5:
                                        if g6 <= 5.5:
                                            return int(722.8631239935588)
                                        else:
                                            return int(-674.3333333333334)
                                    else:
                                        if b5 <= 4.5:
                                            return int(1028.3333333333333)
                                        else:
                                            return int(-722.6)
                                else:
                                    if move <= 51.5:
                                        if s0 <= -2.5:
                                            return int(1104.0)
                                        else:
                                            return int(482.04347826086956)
                                    else:
                                        if b7 <= 5.0:
                                            return int(-1519.0)
                                        else:
                                            return int(-3000.0)
                            else:
                                if sm <= 1.5:
                                    if b4 <= -0.5:
                                        if b5 <= -2.5:
                                            return int(630.484375)
                                        else:
                                            return int(433.83274021352315)
                                    else:
                                        if b3 <= -0.5:
                                            return int(422.08264462809916)
                                        else:
                                            return int(184.3191763191763)
                                else:
                                    if b3 <= 0.5:
                                        if move <= 49.5:
                                            return int(752.1974448315912)
                                        else:
                                            return int(429.19310344827585)
                                    else:
                                        if b5 <= 0.5:
                                            return int(567.5597826086956)
                                        else:
                                            return int(335.8119469026549)
                        else:
                            if player <= 0.5:
                                if b5 <= 0.5:
                                    if b3 <= 2.5:
                                        if b7 <= -5.0:
                                            return int(850.0)
                                        else:
                                            return int(-235.35802469135803)
                                    else:
                                        if b5 <= -4.5:
                                            return int(2400.0)
                                        else:
                                            return int(242.11111111111111)
                                else:
                                    if b4 <= -1.5:
                                        if b3 <= 2.5:
                                            return int(-172.16666666666666)
                                        else:
                                            return int(-1600.0)
                                    else:
                                        if b3 <= -3.5:
                                            return int(-3400.0)
                                        else:
                                            return int(-945.0217391304348)
                            else:
                                if b5 <= 1.5:
                                    if b3 <= 3.5:
                                        if s0 <= -12.5:
                                            return int(108.44444444444444)
                                        else:
                                            return int(655.8214285714286)
                                    else:
                                        if b3 <= 4.5:
                                            return int(3690.0)
                                        else:
                                            return int(885.0)
                                else:
                                    if b3 <= -3.5:
                                        return int(-3400.0)
                                    else:
                                        if b7 <= 1.0:
                                            return int(597.875)
                                        else:
                                            return int(-328.94736842105266)
                    else:
                        if sm <= 1.5:
                            if b3 <= 0.5:
                                if move <= 55.5:
                                    if b3 <= -0.5:
                                        if b4 <= 1.5:
                                            return int(350.0346385542169)
                                        else:
                                            return int(152.08520179372198)
                                    else:
                                        if b4 <= 1.5:
                                            return int(150.6396866840731)
                                        else:
                                            return int(6.931531531531531)
                                else:
                                    if b5 <= 1.5:
                                        if player <= 0.5:
                                            return int(-853.2142857142857)
                                        else:
                                            return int(352.85714285714283)
                                    else:
                                        if g1 <= 1.5:
                                            return int(-1514.875)
                                        else:
                                            return int(-3060.0)
                            else:
                                if b4 <= 1.5:
                                    if b5 <= 5.5:
                                        if player <= 0.5:
                                            return int(-44.22265625)
                                        else:
                                            return int(118.76076555023923)
                                    else:
                                        if move <= 46.0:
                                            return int(139.33333333333334)
                                        else:
                                            return int(-817.125)
                                else:
                                    if player <= 0.5:
                                        if g1 <= 3.5:
                                            return int(-267.5108359133127)
                                        else:
                                            return int(-853.6315789473684)
                                    else:
                                        if b3 <= 1.5:
                                            return int(34.689189189189186)
                                        else:
                                            return int(-230.88)
                        else:
                            if b5 <= -0.5:
                                if g1 <= -3.5:
                                    if g2 <= 0.5:
                                        if b3 <= 1.5:
                                            return int(669.8333333333334)
                                        else:
                                            return int(-764.0)
                                    else:
                                        if b3 <= -0.5:
                                            return int(-1291.0)
                                        else:
                                            return int(-373.6666666666667)
                                else:
                                    if b3 <= -1.5:
                                        if b4 <= 1.5:
                                            return int(969.6470588235294)
                                        else:
                                            return int(620.9464285714286)
                                    else:
                                        if g6 <= -4.5:
                                            return int(-3.588235294117647)
                                        else:
                                            return int(527.285240464345)
                            else:
                                if move <= 51.5:
                                    if b3 <= 0.5:
                                        if sm <= 2.5:
                                            return int(367.30194805194805)
                                        else:
                                            return int(612.2574850299401)
                                    else:
                                        if b3 <= 2.5:
                                            return int(256.8453453453453)
                                        else:
                                            return int(16.074285714285715)
                                else:
                                    if player <= 0.5:
                                        if move <= 54.5:
                                            return int(-145.2967032967033)
                                        else:
                                            return int(-719.2833333333333)
                                    else:
                                        if move <= 54.5:
                                            return int(-143.15384615384616)
                                        else:
                                            return int(573.5483870967741)
            else:
                if sm <= 11.5:
                    if sm <= 6.5:
                        if move <= 55.5:
                            if b5 <= -0.5:
                                if b3 <= -1.5:
                                    if sm <= 4.5:
                                        if g1 <= -2.5:
                                            return int(1438.695652173913)
                                        else:
                                            return int(1081.654761904762)
                                    else:
                                        if move <= 49.5:
                                            return int(1333.2345679012346)
                                        else:
                                            return int(1763.2884615384614)
                                else:
                                    if sm <= 4.5:
                                        if b4 <= -1.5:
                                            return int(1008.376)
                                        else:
                                            return int(765.9781659388647)
                                    else:
                                        if b4 <= -1.5:
                                            return int(1214.2846441947565)
                                        else:
                                            return int(977.6619718309859)
                            else:
                                if b4 <= 0.5:
                                    if move <= 53.5:
                                        if b3 <= 0.5:
                                            return int(989.520202020202)
                                        else:
                                            return int(763.4486486486486)
                                    else:
                                        if s0 <= 8.5:
                                            return int(718.5)
                                        else:
                                            return int(11.241379310344827)
                                else:
                                    if move <= 49.5:
                                        if b3 <= 0.5:
                                            return int(834.7117647058824)
                                        else:
                                            return int(547.3703703703703)
                                    else:
                                        if b5 <= 3.5:
                                            return int(497.37450199203187)
                                        else:
                                            return int(20.785714285714285)
                        else:
                            if player <= 0.5:
                                if b4 <= -0.5:
                                    if b5 <= 3.0:
                                        if b4 <= -2.5:
                                            return int(-187.69230769230768)
                                        else:
                                            return int(577.2894736842105)
                                    else:
                                        if g6 <= -1.5:
                                            return int(-2200.0)
                                        else:
                                            return int(-538.3333333333334)
                                else:
                                    if b5 <= 3.5:
                                        if s0 <= -16.0:
                                            return int(1680.0)
                                        else:
                                            return int(-291.109756097561)
                                    else:
                                        if g6 <= 0.5:
                                            return int(-1008.6538461538462)
                                        else:
                                            return int(-357.7307692307692)
                            else:
                                if b4 <= 0.5:
                                    if g8 <= -3.0:
                                        if b3 <= -1.5:
                                            return int(415.6666666666667)
                                        else:
                                            return int(1623.25)
                                    else:
                                        if g6 <= 5.5:
                                            return int(907.7333333333333)
                                        else:
                                            return int(-895.0)
                                else:
                                    if g1 <= 1.5:
                                        if s0 <= 4.5:
                                            return int(346.47058823529414)
                                        else:
                                            return int(-485.90909090909093)
                                    else:
                                        if b5 <= -0.5:
                                            return int(1591.0)
                                        else:
                                            return int(596.6)
                    else:
                        if b5 <= 1.5:
                            if move <= 57.5:
                                if b5 <= -1.5:
                                    if sm <= 8.5:
                                        if b4 <= 0.5:
                                            return int(1491.8852459016393)
                                        else:
                                            return int(1176.9333333333334)
                                    else:
                                        if b3 <= 4.5:
                                            return int(1649.5502742230346)
                                        else:
                                            return int(908.4545454545455)
                                else:
                                    if sm <= 7.5:
                                        if move <= 53.5:
                                            return int(1116.5576323987539)
                                        else:
                                            return int(759.8305084745763)
                                    else:
                                        if move <= 55.5:
                                            return int(1343.0644295302013)
                                        else:
                                            return int(950.7551020408164)
                            else:
                                if player <= 0.5:
                                    if g1 <= -2.5:
                                        if b7 <= -3.0:
                                            return int(2200.0)
                                        else:
                                            return int(1406.75)
                                    else:
                                        if b5 <= -2.5:
                                            return int(832.4545454545455)
                                        else:
                                            return int(174.01333333333332)
                                else:
                                    if b5 <= -1.5:
                                        if sm <= 10.5:
                                            return int(3000.0)
                                        else:
                                            return int(2111.0)
                                    else:
                                        if g8 <= 0.0:
                                            return int(-490.0)
                                        else:
                                            return int(1815.0)
                        else:
                            if move <= 55.5:
                                if b5 <= 3.5:
                                    if sm <= 7.5:
                                        if g1 <= 3.5:
                                            return int(940.1933701657458)
                                        else:
                                            return int(238.33333333333334)
                                    else:
                                        if move <= 51.5:
                                            return int(1325.0070921985816)
                                        else:
                                            return int(1030.7931034482758)
                                else:
                                    if g1 <= -1.5:
                                        if b4 <= 1.5:
                                            return int(-1787.5)
                                        else:
                                            return int(68.64285714285714)
                                    else:
                                        if b7 <= 3.5:
                                            return int(938.8297101449275)
                                        else:
                                            return int(435.1195652173913)
                            else:
                                if player <= 0.5:
                                    if b7 <= 4.5:
                                        if g6 <= 6.5:
                                            return int(182.8641975308642)
                                        else:
                                            return int(-1052.0)
                                    else:
                                        if g1 <= 0.5:
                                            return int(-960.0)
                                        else:
                                            return int(-143.65)
                                else:
                                    if g6 <= 2.5:
                                        if g8 <= 5.0:
                                            return int(1287.625)
                                        else:
                                            return int(-47.5)
                                    else:
                                        if g8 <= -3.0:
                                            return int(1143.0)
                                        else:
                                            return int(76.70588235294117)
                else:
                    if sm <= 18.5:
                        if move <= 55.5:
                            if b5 <= -0.5:
                                if sm <= 14.5:
                                    if b5 <= -1.5:
                                        if b7 <= 0.5:
                                            return int(2198.516587677725)
                                        else:
                                            return int(1839.8863636363637)
                                    else:
                                        if move <= 53.5:
                                            return int(1834.7532467532467)
                                        else:
                                            return int(1333.2777777777778)
                                else:
                                    if g2 <= 3.5:
                                        if move <= 49.5:
                                            return int(2126.0793650793653)
                                        else:
                                            return int(2513.3076923076924)
                                    else:
                                        if b7 <= -1.5:
                                            return int(2945.0)
                                        else:
                                            return int(1264.0)
                            else:
                                if sm <= 13.5:
                                    if b5 <= 4.5:
                                        if g1 <= 6.5:
                                            return int(1538.0443786982248)
                                        else:
                                            return int(2955.5)
                                    else:
                                        if g6 <= 0.5:
                                            return int(342.5833333333333)
                                        else:
                                            return int(1073.2702702702702)
                                else:
                                    if g8 <= 5.5:
                                        if b7 <= 1.5:
                                            return int(2083.1462686567165)
                                        else:
                                            return int(1737.0369003690037)
                                    else:
                                        if g1 <= 3.5:
                                            return int(781.1481481481482)
                                        else:
                                            return int(1627.125)
                        else:
                            if player <= 0.5:
                                if b7 <= 3.5:
                                    if sm <= 14.5:
                                        if s0 <= 10.0:
                                            return int(1127.9101123595506)
                                        else:
                                            return int(736.9574468085107)
                                    else:
                                        if move <= 57.5:
                                            return int(1542.7941176470588)
                                        else:
                                            return int(1025.2921348314608)
                                else:
                                    if b5 <= 7.5:
                                        if sm <= 16.5:
                                            return int(263.7236842105263)
                                        else:
                                            return int(816.0869565217391)
                                    else:
                                        if b7 <= 7.0:
                                            return int(-328.57142857142856)
                                        else:
                                            return int(-1700.0)
                            else:
                                if b5 <= 5.5:
                                    if b7 <= -0.5:
                                        if b7 <= -3.5:
                                            return int(2115.173076923077)
                                        else:
                                            return int(2496.5686274509803)
                                    else:
                                        if sm <= 14.5:
                                            return int(1537.9583333333333)
                                        else:
                                            return int(2155.3555555555554)
                                else:
                                    if b7 <= 5.5:
                                        if b7 <= 1.0:
                                            return int(-100.0)
                                        else:
                                            return int(600.0)
                                    else:
                                        if g2 <= 1.0:
                                            return int(-600.0)
                                        else:
                                            return int(-690.0)
                    else:
                        if b5 <= 4.5:
                            if move <= 55.5:
                                if sm <= 20.5:
                                    if b7 <= 5.5:
                                        if b7 <= -2.5:
                                            return int(2793.323529411765)
                                        else:
                                            return int(2290.635714285714)
                                    else:
                                        if g2 <= 1.0:
                                            return int(333.25)
                                        else:
                                            return int(1890.0)
                                else:
                                    if b3 <= 4.5:
                                        if b7 <= 7.5:
                                            return int(2657.451219512195)
                                        else:
                                            return int(997.0)
                                    else:
                                        if b4 <= 3.5:
                                            return int(3307.7868852459014)
                                        else:
                                            return int(2358.3333333333335)
                            else:
                                if player <= 0.5:
                                    if sm <= 25.5:
                                        if b7 <= 7.0:
                                            return int(1738.2181818181818)
                                        else:
                                            return int(-1800.0)
                                    else:
                                        if g6 <= 4.5:
                                            return int(2163.383333333333)
                                        else:
                                            return int(2578.6716417910447)
                                else:
                                    if sm <= 21.5:
                                        if g6 <= 5.5:
                                            return int(2307.5853658536585)
                                        else:
                                            return int(2953.3333333333335)
                                    else:
                                        if move <= 56.5:
                                            return int(4800.0)
                                        else:
                                            return int(2940.014492753623)
                        else:
                            if b3 <= 5.5:
                                if b3 <= 2.5:
                                    if b4 <= 1.5:
                                        if g8 <= 4.5:
                                            return int(2248.5833333333335)
                                        else:
                                            return int(568.75)
                                    else:
                                        if move <= 53.0:
                                            return int(2259.5)
                                        else:
                                            return int(576.4545454545455)
                                else:
                                    if b5 <= 7.5:
                                        if player <= 0.5:
                                            return int(1689.0142857142857)
                                        else:
                                            return int(2430.1)
                                    else:
                                        if sm <= 33.0:
                                            return int(435.0)
                                        else:
                                            return int(2095.0)
                            else:
                                if g1 <= 4.5:
                                    if g8 <= -1.0:
                                        return int(1490.0)
                                    else:
                                        if sm <= 27.5:
                                            return int(2751.0)
                                        else:
                                            return int(3251.0)
                                else:
                                    return int(2076.0)
