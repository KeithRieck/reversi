BLACK = "BLACK"
WHITE = "WHITE"


class Move:

    def __init__(self, player=WHITE, x=0, y=0):
        self.x = x
        self.y = y
        self.player = player
        self.score = 0
        self.score_depth = 0
        self.board = None

    def __repr__(self):
        return 'Move(%s, %r, %r)' % (self.player, self.x, self.y)


class Board:

    def __init__(self, previous_board=None, move=None, csv=None):
        self._player = WHITE
        self.move_number = 1
        self._p = []
        self._r = []
        self._moves = []
        for x in range(8):
            self._p.append([])
            self._r.append([])
            for y in range(8):
                self._p[x].append(None)
                self._r[x].append(False)
        if csv is not None:
            f = csv.split(',')
            self.move_number = int(f[1])
            self._player = WHITE if f[2] == 'W' else BLACK
            n = 2
            for y in range(8):
                for x in range(8):
                    n = n + 1
                    self._p[x][y] = WHITE if f[n] == 'W' else (BLACK if f[n] == 'B' else None)
            self._calc_perm()
        elif previous_board is None:
            self._p[3][3] = WHITE
            self._p[4][3] = BLACK
            self._p[3][4] = BLACK
            self._p[4][4] = WHITE
            self._calc_perm()
        else:
            for x in range(8):
                for y in range(8):
                    self._p[x][y] = previous_board.is_piece(x, y)
            if move is not None:
                self._player = move.player
                self.apply_move(move)
            self.move_number = previous_board.move_number + 1
        self.__calculate_moves()

    def __calculate_moves(self):
        self._moves = []
        for x in range(8):
            for y in range(8):
                if self._p[x][y] is not None:
                    continue
                if self._move_down(self._player, x, y) \
                        or self._move_up(self._player, x, y) \
                        or self._move_left(self._player, x, y) \
                        or self._move_right(self._player, x, y) \
                        or self._move_down_right(self._player, x, y) \
                        or self._move_down_left(self._player, x, y) \
                        or self._move_up_right(self._player, x, y) \
                        or self._move_up_left(self._player, x, y):
                    self._moves.append(Move(self._player, x, y))

    def __repr__(self):
        s = ''
        for y in range(8):
            if y != 0:
                s = s + ' '
            for x in range(8):
                s = s + self._board_char(x, y)
        return "Board(%s, '%s')" % (self._player, s)

    def __hash__(self):
        h = 0 if self._player == WHITE else 1
        m = 1
        for y in range(8):
            for x in range(8):
                m = (m * 2) % 4294967296
                if self._p[x][y] == BLACK:
                    h = (h + m) % 4294967296
                if self._p[x][(y + 4) % 8] == WHITE:
                    h = (h + m) % 4294967296
        return h

    def _board_char(self, x, y):
        if self._p[x][y] is None:
            return '*' if self.is_move(x, y) else '.'
        if self._r[x][y]:
            return 'W' if self._p[x][y] == WHITE else 'B'
        return 'w' if self._p[x][y] == WHITE else 'b'

    def __getitem__(self, x):
        return self._p[x]

    def __len__(self):
        n = 0
        for x in range(8):
            for y in range(8):
                if self._p[x][y] is not None:
                    n = n + 1
        return n

    def move_count(self):
        return len(self._moves)

    def get_move(self, n):
        return self._moves[n]

    def get_moves(self):
        return self._moves

    def apply_move(self, move):
        self._p[move.x][move.y] = move.player
        self._player = WHITE if move.player == BLACK else BLACK
        self._move_down(move.player, move.x, move.y, True)
        self._move_up(move.player, move.x, move.y, True)
        self._move_left(move.player, move.x, move.y, True)
        self._move_right(move.player, move.x, move.y, True)
        self._move_down_right(move.player, move.x, move.y, True)
        self._move_down_left(move.player, move.x, move.y, True)
        self._move_up_right(move.player, move.x, move.y, True)
        self._move_up_left(move.player, move.x, move.y, True)
        self._calc_perm()

    def is_move(self, x, y):
        if x < 0 or x > 8 or y < 0 or y > 8:
            return None
        for move in self._moves:
            if move.x == x and move.y == y:
                return move
        return None

    def next_pending_move(self, target_depth=0):
        for move in self._moves:
            if move.board is None:
                # move.board = Board(self, move)
                return move
        for move in self._moves:
            if move.score_depth < target_depth:
                return move
        return None

    def best_move(self):
        if len(self._moves) == 0:
            return None
        self.sort_moves()
        return self._moves[0]

    def sort_moves(self):
        self._moves.sort(key=lambda m: m.score)

    def is_piece(self, x, y):
        if x is None or y is None or x < 0 or x > 8 or y < 0 or y > 8:
            return None
        return self._p[x][y]

    def count(self, player):
        n = 0
        for x in range(8):
            for y in range(8):
                if self._p[x][y] == player:
                    n = n + 1
        return n

    def next_player(self):
        return self._player

    def switch_player(self):
        self._player = BLACK if self._player == WHITE else WHITE
        self.__calculate_moves()
        self._calc_perm()
        return self._player

    def show(self):
        for y in range(8):
            s = ''
            for x in range(8):
                s = s + self._board_char(x, y) + ' '
            if y == 0:
                s = s + '\t W: ' + str(self.count(WHITE))
            elif y == 1:
                s = s + '\t B: ' + str(self.count(BLACK))
            elif y == 2:
                s = s + '\t ' + str(self._player)
            elif y == 3:
                s = s + '\t ' + str(self.move_number)
            print(s)
        print()

    def csv_line(self):
        s = str(self.__hash__()) + ',' + str(self.move_number) + ','
        s = s + ('W' if self._player == WHITE else 'B') + ','
        for y in range(8):
            for x in range(8):
                if self._p[x][y] == WHITE:
                    s = s + 'W,'
                elif self._p[x][y] == BLACK:
                    s = s + 'B,'
                else:
                    s = s + ','
        return s

    def _calc_perm(self):
        for n in range(8):
            for y in range(8):
                self._r[n][y] = False
        self._r[0][0] = self._p[0][0] is not None
        self._r[0][7] = self._p[0][7] is not None
        self._r[7][0] = self._p[7][0] is not None
        self._r[7][7] = self._p[7][7] is not None
        for n in range(1, 8):
            if self._r[n - 1][0] and self._p[n][0] == self._p[n - 1][0]:
                self._r[n][0] = True
            if self._r[n - 1][7] and self._p[n][7] == self._p[n - 1][7]:
                self._r[n][7] = True
            if self._r[0][n - 1] and self._p[0][n] == self._p[0][n - 1]:
                self._r[0][n] = True
            if self._r[7][n - 1] and self._p[7][n] == self._p[7][n - 1]:
                self._r[7][n] = True
            if self._r[8 - n][0] and self._p[7 - n][0] == self._p[8 - n][0]:
                self._r[7 - n][0] = True
            if self._r[8 - n][7] and self._p[7 - n][7] == self._p[8 - n][7]:
                self._r[7 - n][7] = True
            if self._r[0][8 - n] and self._p[0][7 - n] == self._p[0][8 - n]:
                self._r[0][7 - n] = True
            if self._r[7][8 - n] and self._p[7][7 - n] == self._p[7][8 - n]:
                self._r[7][7 - n] = True
        done = False
        while not done:
            done = True
            for x in range(1, 7):
                for y in range(1, 7):
                    if self._p[x][y] is None or self._r[x][y]:
                        continue
                    if self._r[x - 1][y] and self._r[x - 1][y - 1] and self._r[x][y - 1] \
                            or self._r[x][y - 1] and self._r[x + 1][y - 1] and self._r[x + 1][y] \
                            or self._r[x + 1][y] and self._r[x + 1][y + 1] and self._r[x][y + 1] \
                            or self._r[x][y + 1] and self._r[x - 1][y + 1] and self._r[x - 1][y]:
                        self._r[x][y] = True
                        done = False

    def is_permanent(self, player, x, y):
        return self._p[x][y] == player and self._r[x][y]

    def _perm_left(self, player, x, y):
        for xx in range(x + 1):
            if self._p[xx][y] != player:
                return False
        return True

    def _perm_right(self, player, x, y):
        for xx in range(x, 8):
            if self._p[xx][y] != player:
                return False
        return True

    def _perm_up(self, player, x, y):
        for yy in range(y + 1):
            if self._p[x][yy] != player:
                return False
        return True

    def _perm_down(self, player, x, y):
        for yy in range(y, 8):
            if self._p[x][yy] != player:
                return False
        return True

    def _move_down(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y + (n + 1)) < 8 and self._p[x][y + (n + 1)] == other_player:
            n = n + 1
        if (y + (n + 1)) < 8 and self._p[x][y + (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x][y + m] = player
            return n
        else:
            return 0

    def _move_up(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y - (n + 1)) >= 0 and self._p[x][y - (n + 1)] == other_player:
            n = n + 1
        if (y - (n + 1)) >= 0 and self._p[x][y - (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x][y - m] = player
            return n
        else:
            return 0

    def _move_right(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (x + (n + 1)) < 8 and self._p[x + (n + 1)][y] == other_player:
            n = n + 1
        if (x + (n + 1)) < 8 and self._p[x + (n + 1)][y] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x + m][y] = player
            return n
        else:
            return 0

    def _move_left(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y] == other_player:
            n = n + 1
        if (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x - m][y] = player
            return n
        else:
            return 0

    def _move_down_right(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y + (n + 1)) < 8 and (x + (n + 1)) < 8 and self._p[x + (n + 1)][y + (n + 1)] == other_player:
            n = n + 1
        if (y + (n + 1)) < 8 and (x + (n + 1)) < 8 and self._p[x + (n + 1)][y + (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x + m][y + m] = player
            return n
        else:
            return 0

    def _move_down_left(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y + (n + 1)) < 8 and (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y + (n + 1)] == other_player:
            n = n + 1
        if (y + (n + 1)) < 8 and (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y + (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x - m][y + m] = player
            return n
        else:
            return 0

    def _move_up_right(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y - (n + 1)) >= 0 and (x + (n + 1)) < 8 and self._p[x + (n + 1)][y - (n + 1)] == other_player:
            n = n + 1
        if (y - (n + 1)) >= 0 and (x + (n + 1)) < 8 and self._p[x + (n + 1)][y - (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x + m][y - m] = player
            return n
        else:
            return 0

    def _move_up_left(self, player, x, y, do_move=False):
        other_player = WHITE if player == BLACK else BLACK
        n = 0
        while (y - (n + 1)) >= 0 and (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y - (n + 1)] == other_player:
            n = n + 1
        if (y - (n + 1)) >= 0 and (x - (n + 1)) >= 0 and self._p[x - (n + 1)][y - (n + 1)] == player:
            if do_move:
                for m in range(n + 1):
                    self._p[x - m][y - m] = player
            return n
        else:
            return 0
