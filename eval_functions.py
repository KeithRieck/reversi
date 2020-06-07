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


class F2(F1):
    """Linear static evaluation function, using weights learned from sklearn's LinearRegression."""

    def __init__(self):
        F1.__init__(self, 28.27866061, -6.37442292, -17.93707242, -64.12435399, -81.42209786,
                    -54.35718033, -20.9621922, -41.92151928, -33.21931113, 120.04270918,
                    -1.46908731, 95.41359195)


class F3(F1):
    """Static evaluation function taken from sklearn's DecisionTreeRegressor."""

    def eval_board(self, board: Board) -> int:
        (s0, g1, g2, b3, b4, b5, g6, b7, g8, sm, move, player) = self.eval_vector(board)
        if sm <= -2.5:
            if sm <= -11.5:
                if sm <= -18.5:
                    if sm <= -31.5:
                        if sm <= -44.5:
                            if b5 <= -5.0:
                                return int(-6250.0)
                            else:
                                return int(-5300.0)
                        else:
                            if b4 <= -3.5:
                                return int(-2665.1666666666665)
                            else:
                                return int(-3824.404761904762)
                    else:
                        if g1 <= -2.5:
                            if sm <= -22.5:
                                return int(-2792.609756097561)
                            else:
                                return int(-2413.3021582733813)
                        else:
                            if b5 <= -5.5:
                                return int(-1375.96875)
                            else:
                                return int(-2276.8656126482215)
                else:
                    if sm <= -14.5:
                        if b5 <= -0.5:
                            if b7 <= -3.5:
                                return int(-1509.7212121212121)
                            else:
                                return int(-1866.1932114882507)
                        else:
                            if move <= 56.5:
                                return int(-2036.166163141994)
                            else:
                                return int(-2534.96261682243)
                    else:
                        if b5 <= 0.5:
                            if s0 <= -15.5:
                                return int(-1392.7564935064936)
                            else:
                                return int(-1603.6410714285714)
                        else:
                            if move <= 57.5:
                                return int(-1750.6438923395444)
                            else:
                                return int(-2402.6875)
            else:
                if sm <= -6.5:
                    if sm <= -9.5:
                        if b5 <= -3.5:
                            if move <= 51.5:
                                return int(-1186.3055555555557)
                            else:
                                return int(-740.702380952381)
                        else:
                            if move <= 57.5:
                                return int(-1365.8311944718657)
                            else:
                                return int(-1977.6129032258063)
                    else:
                        if b5 <= -0.5:
                            if b5 <= -3.5:
                                return int(-811.0282685512367)
                            else:
                                return int(-1022.3094944512947)
                        else:
                            if move <= 57.5:
                                return int(-1160.6668526785713)
                            else:
                                return int(-1701.150684931507)
                else:
                    if sm <= -4.5:
                        if move <= 57.5:
                            if b5 <= 0.5:
                                return int(-707.6208378088078)
                            else:
                                return int(-903.3123486682808)
                        else:
                            if b7 <= 2.5:
                                return int(-1275.6724137931035)
                            else:
                                return int(-2127.9166666666665)
                    else:
                        if b5 <= 0.5:
                            if b3 <= -1.5:
                                return int(-349.4884568651276)
                            else:
                                return int(-514.6022727272727)
                        else:
                            if move <= 57.5:
                                return int(-644.1261904761905)
                            else:
                                return int(-1810.5483870967741)
        else:
            if sm <= 3.5:
                if sm <= 0.5:
                    if sm <= -0.5:
                        if b4 <= -0.5:
                            if sm <= -1.5:
                                return int(-315.8522642910171)
                            else:
                                return int(-105.63129074315515)
                        else:
                            if b3 <= 1.5:
                                return int(-335.4826254826255)
                            else:
                                return int(-540.2414507772021)
                    else:
                        if b4 <= -0.5:
                            if b3 <= -0.5:
                                return int(260.64928633847944)
                            else:
                                return int(73.67454721415733)
                        else:
                            if b3 <= 0.5:
                                return int(-9.602133950379226)
                            else:
                                return int(-181.58042813455657)
                else:
                    if b4 <= 0.5:
                        if move <= 57.5:
                            if sm <= 1.5:
                                return int(338.2530003243594)
                            else:
                                return int(510.9832116788321)
                        else:
                            if player <= 0.5:
                                return int(-422.32394366197184)
                            else:
                                return int(817.7142857142857)
                    else:
                        if sm <= 1.5:
                            if b3 <= -0.5:
                                return int(229.01535836177473)
                            else:
                                return int(49.86499794829709)
                        else:
                            if move <= 57.5:
                                return int(345.3444350758853)
                            else:
                                return int(-524.5135135135135)
            else:
                if sm <= 11.5:
                    if sm <= 7.5:
                        if move <= 57.5:
                            if sm <= 5.5:
                                return int(682.9570720968629)
                            else:
                                return int(896.2982257455643)
                        else:
                            if player <= 0.5:
                                return int(-126.40350877192982)
                            else:
                                return int(1166.6666666666667)
                    else:
                        if move <= 57.5:
                            if b7 <= 3.5:
                                return int(1274.4775179856115)
                            else:
                                return int(911.3606138107417)
                        else:
                            if s0 <= 4.0:
                                return int(1056.225806451613)
                            else:
                                return int(187.63945578231292)
                else:
                    if sm <= 20.5:
                        if move <= 57.5:
                            if sm <= 15.5:
                                return int(1615.0720257234727)
                            else:
                                return int(2021.670704845815)
                        else:
                            if player <= 0.5:
                                return int(950.8625429553265)
                            else:
                                return int(2725.782608695652)
                    else:
                        if move <= 57.5:
                            if sm <= 25.5:
                                return int(2447.935975609756)
                            else:
                                return int(2848.16)
                        else:
                            if player <= 0.5:
                                return int(1998.5707070707072)
                            else:
                                return int(3400.5714285714284)
