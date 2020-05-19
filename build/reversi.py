import eval_functions
from bedlam import Button
from bedlam import Game
from bedlam import Scene
from board import BLACK
from board import Board
from board import WHITE

# __pragma__('skip')
document = window = Math = Date = console = 0  # Prevent complaints by optional static checker
# __pragma__('noskip')
# __pragma__('noalias', 'clear')

WHITE_TO_MOVE_STATE = 'WHITE_TO_MOVE_STATE'
BLACK_TO_MOVE_STATE = 'BLACK_TO_MOVE_STATE'
GAME_OVER_STATE = 'GAME_OVER_STATE'
MIN_SCORE = -1000000
MAX_SCORE = 1000000
THINK_TIME = 2 * 1000
DISPLAY_TIME = 3 * 1000
HIGHLIGHT_TIME = 1 * 1000
DEBUG = True


class ReversiScene(Scene):
    def __init__(self, game, name):
        Scene.__init__(self, game, name)
        self.current_board = None
        self.target_depth = 2
        self.radius = 20
        self.padding = 8
        self.px = 10
        self.py = 20
        self.eval_function = eval_functions.F1(1, 10, 10, -10, -10, 100)
        self.game_state = WHITE_TO_MOVE_STATE
        self._hoverX = None
        self._hoverY = None
        self._think_until = -1
        self._display_until = -1
        self._display = ''
        self._consecutive_passes = 0
        self._highlightX = 0
        self._highlightY = 0
        self._highlight_until = -1
        r = 2 * self.radius + 2 * self.padding
        self.reset_button = self.append(Button(self.game, 9 * r, 8 * r, 75, 30, 'Reset'))
        self.reset_button.callback = self.__reset_game

    def set_current_board(self, board):
        self.current_board = board
        self.game_state = WHITE_TO_MOVE_STATE

    def __find_cell(self, mouse_x, mouse_y):
        r = 2 * self.radius + 2 * self.padding
        x = Math.floor((mouse_x - self.px - self.padding) / r)
        y = Math.floor((mouse_y - self.py - self.padding) / r)
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return None, None
        return x, y

    def __reset_game(self):
        self.set_current_board(Board())

    def handle_mouseup(self, event):
        Scene.handle_mouseup(self, event)
        x, y = self.__find_cell(event.x, event.y)
        if DEBUG:
            console.log('click:  cell=' + x + ',' + y + '    ' + self.current_board.is_piece(x, y))
        if self.game_state == WHITE_TO_MOVE_STATE:
            move = self.current_board.is_move(x, y)
            if DEBUG:
                self.__display_message(" " + x + "," + y)
            if move is not None:
                self.__make_move(move)

    def handle_mousemove(self, event):
        Scene.handle_mousemove(self, event)
        if self.game_state == WHITE_TO_MOVE_STATE:
            self._hoverX, self._hoverY = self.__find_cell(event.x, event.y)
        else:
            self._hoverX, self._hoverY = None, None

    def __make_move(self, move):
        if DEBUG:
            console.log('\n\n- - - - - - - - - - - - - \n')
            console.log(self.current_board.show())
        if move is not None:
            if DEBUG:
                console.log('Move = ' + move.x + ',' + move.y + '  : ' + move.player)
            self.current_board = Board(self.current_board, move)
            self._consecutive_passes = 0
            self._highlightX = move.x
            self._highlightY = move.y
            self._highlight_until = self.game.get_time() + HIGHLIGHT_TIME
        else:
            if DEBUG:
                console.log('PASS: ' + self.current_board.next_player())
            self.__display_message('PASS: ' + self.current_board.next_player())
            self.current_board.switch_player()
            self._consecutive_passes = self._consecutive_passes + 1
        self.game_state = BLACK_TO_MOVE_STATE if self.game_state == WHITE_TO_MOVE_STATE else WHITE_TO_MOVE_STATE
        self._think_until = -1
        if len(self.current_board) == 64 or self._consecutive_passes >= 2 \
                or self.current_board.count(WHITE) == 0 or self.current_board.count(BLACK) == 0:
            self.__display_message('Game over')
            self.game_state = GAME_OVER_STATE
        if DEBUG:
            console.log(self.current_board.show())
            console.log('State = ' + self.game_state)
            console.log('- - - - - - - - - - - - - \n\n')

    def __display_message(self, message):
        self._display_until = self.game.get_time() + DISPLAY_TIME
        self._display = message

    def __draw_board(self, ctx):
        r = 2 * self.radius + 2 * self.padding
        bsize = 8 * r + self.padding
        ctx.save()
        ctx.globalCompositeOperation = 'source-over'
        ctx.fillStyle = 'green'
        ctx.fillRect(self.px, self.py, self.px + bsize, self.py + bsize)
        ctx.strokeStyle = '#666666'
        ctx.lineWidth = 1
        ctx.beginPath()
        for n in range(8 + 1):
            ctx.moveTo(self.px + self.padding, self.py + self.padding + n * r)
            ctx.lineTo(self.px + self.padding + 8 * r, self.py + self.padding + n * r)
            ctx.moveTo(self.px + self.padding + n * r, self.py + self.padding)
            ctx.lineTo(self.px + self.padding + n * r, self.py + self.padding + 8 * r)
        ctx.stroke()
        ctx.strokeStyle = 'black'
        ctx.lineWidth = 2
        if self.current_board is not None:
            for x in range(8):
                for y in range(8):
                    if self.current_board.is_piece(x, y) is None:
                        continue
                    ctx.beginPath()
                    ctx.fillStyle = '#000000' if self.current_board.is_piece(x, y) == BLACK else '#CCCCCC'
                    ctx.arc((x + 1) * r - self.padding - 1, (y + 1) * r - 1, self.radius, 0, 2 * Math.PI)
                    ctx.fill()
        if self._hoverX is not None and self.current_board.is_move(self._hoverX, self._hoverY):
            ctx.strokeStyle = '#CCCCCC'
            ctx.beginPath()
            ctx.moveTo((self._hoverX + 1) * r + self.radius - self.padding, (self._hoverY + 1) * r)
            ctx.arc((self._hoverX + 1) * r - self.padding, (self._hoverY + 1) * r, self.radius, 0, 2 * Math.PI)
            ctx.stroke()
        if self._highlight_until > 0:
            ctx.strokeStyle = '#999999'
            ctx.strokeRect(1 + self.px + self._highlightX * r + self.radius - self.padding,
                           1 + self.py + self._highlightY * r + self.radius - self.padding,
                           r - self.padding - 2, r - self.padding - 2)
            if self.game.get_time() > self._highlight_until:
                self._highlight_until = -1
        ctx.fillStyle = 'black'
        ctx.font = '18pt sans-serif'
        tx = self.px + bsize + 20
        ty = self.py + r - 10
        ctx.fillText('WHITE: ' + self.current_board.count(WHITE), tx, ty)
        ty = ty + 32
        ctx.fillText('BLACK: ' + self.current_board.count(BLACK), tx, ty)
        ty = ty + 32
        if self.game_state == GAME_OVER_STATE:
            if self.current_board.count(WHITE) > self.current_board.count(BLACK):
                ctx.fillText('WHITE wins', tx, ty)
            else:
                ctx.fillText('BLACK wins', tx, ty)
        else:
            ctx.fillText(self.current_board.next_player() + ' to play', tx, ty)
        ty = ty + 32
        if self._display_until > 0:
            ctx.fillText(self._display, tx, ty)
            if self.game.get_time() > self._display_until:
                self._display_until = -1
        ctx.restore()

    def draw(self, ctx):
        Scene.draw(self, ctx)
        self.__draw_board(ctx)

    def update(self, delta_time):
        Scene.update(self, delta_time)
        if self.game_state == BLACK_TO_MOVE_STATE:
            if self._think_until < 0:
                self._think_until = self.game.get_time() + THINK_TIME
            if self.game.get_time() < self._think_until:
                self.__search_for_best_move(self.current_board)
                return
            if self.current_board.move_count() == 0:
                self.__make_move(None)
                return
            best_move = self.__search_for_best_move(self.current_board)
            if best_move is not None:
                self.__make_move(best_move)

    def __search_for_best_move(self, board):
        move = board.next_pending_move(self.target_depth)
        if move is not None:
            if move.board is None:
                move.board = Board(self.current_board, move)
            move.score = self.__search(move.board, self.target_depth)
            move.score_depth = self.target_depth
            return None
        else:
            return board.best_move()

    def __search(self, board, depth=0, alpha=MIN_SCORE, beta=MAX_SCORE):
        if depth <= 0:
            return self.eval_function.eval_board(board)
        if board.move_count() == 0:
            b = Board(board)
            b.switch_player()
            return self.__search(b, depth - 1)
        score = MIN_SCORE if board.next_player() == WHITE else MAX_SCORE
        for move in board.get_moves():
            move.score = self.__search(Board(board, move), depth - 1, alpha, beta)
            score = max(score, move.score) if board.next_player() == WHITE else min(score, move.score)
            alpha = max(alpha, move.score) if board.next_player() == WHITE else alpha
            beta = min(beta, move.score) if board.next_player() == BLACK else beta
            if alpha >= beta:
                break
        board.sort_moves()
        return score


class ReversiGame(Game):
    def __init__(self, loop_time=20):
        Game.__init__(self, 'Reversi', loop_time)
        scene = ReversiScene(self, 'REVERSI')
        self.append(scene)
        b = Board()
        scene.set_current_board(b)
