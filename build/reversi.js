// Transcrypt'ed from Python, 2021-03-09 20:44:48
var eval_functions = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {WHITE} from './board.js';
import {Board} from './board.js';
import {BLACK} from './board.js';
import {Scene} from './bedlam.js';
import {Game} from './bedlam.js';
import {Button} from './bedlam.js';
import * as __module_eval_functions__ from './eval_functions.js';
__nest__ (eval_functions, '', __module_eval_functions__);
var __name__ = '__main__';
export var WHITE_TO_MOVE_STATE = 'WHITE_TO_MOVE_STATE';
export var BLACK_TO_MOVE_STATE = 'BLACK_TO_MOVE_STATE';
export var GAME_OVER_STATE = 'GAME_OVER_STATE';
export var MIN_SCORE = -(1000000);
export var MAX_SCORE = 1000000;
export var THINK_TIME = 2 * 1000;
export var DISPLAY_TIME = 3 * 1000;
export var HIGHLIGHT_TIME = 4 * 1000;
export var TARGET_DEPTH = 4;
export var DEBUG = false;
export var VERSION = '2.0';
export var ReversiScene =  __class__ ('ReversiScene', [Scene], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, py_name) {
		Scene.__init__ (self, game, py_name);
		self.current_board = null;
		self.target_depth = TARGET_DEPTH;
		self.radius = 20;
		self.padding = 8;
		self.px = 10;
		self.py = 20;
		self.eval_function = eval_functions.F2 ();
		self.game_state = WHITE_TO_MOVE_STATE;
		self._hoverX = null;
		self._hoverY = null;
		self._think_until = -(1);
		self._display_until = -(1);
		self._display = '';
		self._consecutive_passes = 0;
		self._highlightX = 0;
		self._highlightY = 0;
		self._highlight_until = -(1);
		var r = 2 * self.radius + 2 * self.padding;
		self.reset_button = self.append (Button (self.game, 9 * r, 8 * r, 75, 30, 'Reset'));
		self.reset_button.callback = self.__reset_game;
		self.tag1 = '';
		self.tag2 = '';
	});},
	get set_current_board () {return __get__ (this, function (self, board) {
		self.current_board = board;
		self.game_state = WHITE_TO_MOVE_STATE;
	});},
	get __find_cell () {return __get__ (this, function (self, mouse_x, mouse_y) {
		var r = 2 * self.radius + 2 * self.padding;
		var x = Math.floor (((mouse_x - self.px) - self.padding) / r);
		var y = Math.floor (((mouse_y - self.py) - self.padding) / r);
		if (x < 0 || x >= 8 || y < 0 || y >= 8) {
			return tuple ([null, null]);
		}
		return tuple ([x, y]);
	});},
	get __reset_game () {return __get__ (this, function (self) {
		self.set_current_board (Board ());
	});},
	get handle_mouseup () {return __get__ (this, function (self, event) {
		Scene.handle_mouseup (self, event);
		var __left0__ = self.__find_cell (event.x, event.y);
		var x = __left0__ [0];
		var y = __left0__ [1];
		if (DEBUG) {
			console.log ((((('click:  cell=' + x) + ',') + y) + '    ') + self.current_board.is_piece (x, y));
		}
		if (self.game_state == WHITE_TO_MOVE_STATE) {
			var move = self.current_board.is_move (x, y);
			if (DEBUG) {
				self.__display_message (((' ' + x) + ',') + y);
			}
			if (move !== null) {
				self.__make_move (move);
			}
		}
	});},
	get handle_mousemove () {return __get__ (this, function (self, event) {
		Scene.handle_mousemove (self, event);
		if (self.game_state == WHITE_TO_MOVE_STATE) {
			var __left0__ = self.__find_cell (event.x, event.y);
			self._hoverX = __left0__ [0];
			self._hoverY = __left0__ [1];
		}
		else {
			var __left0__ = tuple ([null, null]);
			self._hoverX = __left0__ [0];
			self._hoverY = __left0__ [1];
		}
	});},
	get __make_move () {return __get__ (this, function (self, move) {
		if (DEBUG) {
			console.log ('\n\n- - - - - - - - - - - - - \n');
			console.log (self.current_board.show ());
		}
		if (move !== null) {
			if (DEBUG) {
				console.log ((((('Move = ' + move.x) + ',') + move.y) + '  : ') + move.player);
			}
			self.current_board = Board (self.current_board, move);
			self._consecutive_passes = 0;
			self._highlightX = move.x;
			self._highlightY = move.y;
			self._highlight_until = self.game.get_time () + HIGHLIGHT_TIME;
		}
		else {
			if (DEBUG) {
				console.log ((('PASS: ' + self.current_board.next_player ()) + ' consecutive_passes=') + self._consecutive_passes);
			}
			self.__display_message ('PASS: ' + self.current_board.next_player ());
			self.current_board.switch_player ();
			self._consecutive_passes = self._consecutive_passes + 1;
		}
		self.game_state = (self.game_state == WHITE_TO_MOVE_STATE ? BLACK_TO_MOVE_STATE : WHITE_TO_MOVE_STATE);
		self._think_until = -(1);
		if (len (self.current_board) == 64 || self._consecutive_passes >= 2 || self.current_board.count (WHITE) == 0 || self.current_board.count (BLACK) == 0) {
			self.__display_message ('Game over');
			self.game_state = GAME_OVER_STATE;
		}
		if (DEBUG) {
			console.log (self.current_board.show ());
			console.log ('State = ' + self.game_state);
			console.log ('- - - - - - - - - - - - - \n\n');
		}
	});},
	get __display_message () {return __get__ (this, function (self, message) {
		self._display_until = self.game.get_time () + DISPLAY_TIME;
		self._display = message;
	});},
	get __draw_board () {return __get__ (this, function (self, ctx) {
		var r = 2 * self.radius + 2 * self.padding;
		var bsize = 8 * r + self.padding;
		ctx.save ();
		ctx.globalCompositeOperation = 'source-over';
		ctx.fillStyle = 'green';
		ctx.fillRect (self.px, self.py, self.px + bsize, self.py + bsize);
		ctx.strokeStyle = '#666666';
		ctx.lineWidth = 1;
		ctx.beginPath ();
		for (var n = 0; n < 8 + 1; n++) {
			ctx.moveTo (self.px + self.padding, (self.py + self.padding) + n * r);
			ctx.lineTo ((self.px + self.padding) + 8 * r, (self.py + self.padding) + n * r);
			ctx.moveTo ((self.px + self.padding) + n * r, self.py + self.padding);
			ctx.lineTo ((self.px + self.padding) + n * r, (self.py + self.padding) + 8 * r);
		}
		ctx.stroke ();
		ctx.strokeStyle = 'black';
		ctx.lineWidth = 2;
		if (self.current_board !== null) {
			for (var x = 0; x < 8; x++) {
				for (var y = 0; y < 8; y++) {
					if (self.current_board.is_piece (x, y) === null) {
						continue;
					}
					ctx.beginPath ();
					ctx.fillStyle = (self.current_board.is_piece (x, y) == BLACK ? '#000000' : '#CCCCCC');
					ctx.arc (((x + 1) * r - self.padding) - 1, (y + 1) * r - 1, self.radius, 0, 2 * Math.PI);
					ctx.fill ();
				}
			}
		}
		if (self._hoverX !== null && self.current_board.is_move (self._hoverX, self._hoverY)) {
			ctx.strokeStyle = '#CCCCCC';
			ctx.beginPath ();
			ctx.moveTo (((self._hoverX + 1) * r + self.radius) - self.padding, (self._hoverY + 1) * r);
			ctx.arc ((self._hoverX + 1) * r - self.padding, (self._hoverY + 1) * r, self.radius, 0, 2 * Math.PI);
			ctx.stroke ();
		}
		if (self._highlight_until > 0) {
			ctx.strokeStyle = '#999999';
			ctx.strokeRect ((((1 + self.px) + self._highlightX * r) + self.radius) - self.padding, (((1 + self.py) + self._highlightY * r) + self.radius) - self.padding, (r - self.padding) - 2, (r - self.padding) - 2);
			if (self.game.get_time () > self._highlight_until) {
				self._highlight_until = -(1);
			}
		}
		ctx.fillStyle = 'black';
		ctx.font = '18pt sans-serif';
		var tx = (self.px + bsize) + 20;
		var ty = (self.py + r) - 10;
		ctx.fillText ('WHITE: ' + self.current_board.count (WHITE), tx, ty);
		var ty = ty + 32;
		ctx.fillText ('BLACK: ' + self.current_board.count (BLACK), tx, ty);
		var ty = ty + 32;
		if (self.game_state == GAME_OVER_STATE) {
			if (self.current_board.count (WHITE) > self.current_board.count (BLACK)) {
				ctx.fillText ('WHITE wins', tx, ty);
			}
			else {
				ctx.fillText ('BLACK wins', tx, ty);
			}
		}
		else {
			ctx.fillText (self.current_board.next_player () + ' to play', tx, ty);
		}
		var ty = ty + 32;
		if (self._display_until > 0) {
			ctx.fillText (self._display, tx, ty);
			if (self.game.get_time () > self._display_until) {
				self._display_until = -(1);
			}
		}
		ctx.font = '10pt sans-serif';
		ctx.fillText (self.tag1, 9 * r + 100, 8 * r + 10);
		ctx.fillText (self.tag2, 9 * r + 130, 8 * r + 10);
		ctx.fillText ('v' + VERSION, 9 * r + 100, 8 * r + 27);
		ctx.restore ();
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		Scene.draw (self, ctx);
		self.__draw_board (ctx);
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		Scene.py_update (self, delta_time);
		if (self.game_state == BLACK_TO_MOVE_STATE) {
			if (self._think_until < 0) {
				self._think_until = self.game.get_time () + THINK_TIME;
			}
			if (self.game.get_time () < self._think_until) {
				self.__search_for_best_move (self.current_board);
				return ;
			}
			if (self.current_board.move_count () == 0) {
				self.__make_move (null);
				return ;
			}
			var best_move = self.__search_for_best_move (self.current_board);
			if (best_move !== null) {
				self.__make_move (best_move);
			}
		}
		else if (self.current_board.move_count () == 0) {
			self.__make_move (null);
		}
	});},
	get __search_for_best_move () {return __get__ (this, function (self, board) {
		var move = board.next_pending_move (self.target_depth);
		if (move !== null) {
			if (move.board === null) {
				move.board = Board (self.current_board, move);
			}
			move.score = self.__search (move.board, self.target_depth);
			move.score_depth = self.target_depth;
			return null;
		}
		else {
			return board.best_move ();
		}
	});},
	get __search () {return __get__ (this, function (self, board, depth, alpha, beta) {
		if (typeof depth == 'undefined' || (depth != null && depth.hasOwnProperty ("__kwargtrans__"))) {;
			var depth = 0;
		};
		if (typeof alpha == 'undefined' || (alpha != null && alpha.hasOwnProperty ("__kwargtrans__"))) {;
			var alpha = MIN_SCORE;
		};
		if (typeof beta == 'undefined' || (beta != null && beta.hasOwnProperty ("__kwargtrans__"))) {;
			var beta = MAX_SCORE;
		};
		if (depth <= 0) {
			return self.eval_function.eval_board (board);
		}
		if (board.move_count () == 0) {
			var b = Board (board);
			b.switch_player ();
			return self.__search (b, depth - 1);
		}
		var score = (board.next_player () == WHITE ? MIN_SCORE : MAX_SCORE);
		for (var move of board.get_moves ()) {
			move.score = self.__search (Board (board, move), depth - 1, alpha, beta);
			var score = (board.next_player () == WHITE ? max (score, move.score) : min (score, move.score));
			var alpha = (board.next_player () == WHITE ? max (alpha, move.score) : alpha);
			var beta = (board.next_player () == BLACK ? min (beta, move.score) : beta);
			if (alpha >= beta) {
				break;
			}
		}
		board.sort_moves ();
		return score;
	});}
});
export var ReversiGame =  __class__ ('ReversiGame', [Game], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, loop_time) {
		if (typeof loop_time == 'undefined' || (loop_time != null && loop_time.hasOwnProperty ("__kwargtrans__"))) {;
			var loop_time = 20;
		};
		Game.__init__ (self, 'Reversi', loop_time);
		var scene = ReversiScene (self, 'REVERSI');
		self.append (scene);
		var b = Board ();
		scene.set_current_board (b);
	});},
	get set_debug () {return __get__ (this, function (self, b) {
		if (b !== null && b == 'true') {
			DEBUG = true;
		}
	});},
	get set_depth () {return __get__ (this, function (self, n) {
		if (n !== null) {
			self.currentScene.target_depth = int (n);
			self.currentScene.tag2 = n;
		}
	});},
	get set_version () {return __get__ (this, function (self, n) {
		if (n !== null) {
			if (n == '0') {
				self.currentScene.eval_function = eval_functions.F0 ();
				self.currentScene.tag1 = 'F0';
			}
			if (n == '1') {
				self.currentScene.eval_function = eval_functions.F1 ();
				self.currentScene.tag1 = 'F1';
			}
			if (n == '2') {
				self.currentScene.eval_function = eval_functions.F2 ();
				self.currentScene.tag1 = 'F2';
			}
		}
	});}
});

//# sourceMappingURL=reversi.map