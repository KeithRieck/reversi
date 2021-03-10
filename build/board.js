// Transcrypt'ed from Python, 2021-03-09 20:44:49
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'board';
export var BLACK = 'BLACK';
export var WHITE = 'WHITE';
export var Move =  __class__ ('Move', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, player, x, y) {
		if (typeof player == 'undefined' || (player != null && player.hasOwnProperty ("__kwargtrans__"))) {;
			var player = WHITE;
		};
		if (typeof x == 'undefined' || (x != null && x.hasOwnProperty ("__kwargtrans__"))) {;
			var x = 0;
		};
		if (typeof y == 'undefined' || (y != null && y.hasOwnProperty ("__kwargtrans__"))) {;
			var y = 0;
		};
		self.x = x;
		self.y = y;
		self.player = player;
		self.score = 0;
		self.score_depth = 0;
		self.board = null;
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ('Move(%s, %r, %r)', tuple ([self.player, self.x, self.y]));
	});}
});
export var Board =  __class__ ('Board', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, previous_board, move, csv) {
		if (typeof previous_board == 'undefined' || (previous_board != null && previous_board.hasOwnProperty ("__kwargtrans__"))) {;
			var previous_board = null;
		};
		if (typeof move == 'undefined' || (move != null && move.hasOwnProperty ("__kwargtrans__"))) {;
			var move = null;
		};
		if (typeof csv == 'undefined' || (csv != null && csv.hasOwnProperty ("__kwargtrans__"))) {;
			var csv = null;
		};
		self._player = WHITE;
		self.move_number = 1;
		self._p = [];
		self._r = [];
		self._moves = [];
		for (var x = 0; x < 8; x++) {
			self._p.append ([]);
			self._r.append ([]);
			for (var y = 0; y < 8; y++) {
				self._p [x].append (null);
				self._r [x].append (false);
			}
		}
		if (csv !== null) {
			var f = csv.py_split (',');
			self.move_number = int (f [1]);
			self._player = (f [2] == 'W' ? WHITE : BLACK);
			var n = 2;
			for (var y = 0; y < 8; y++) {
				for (var x = 0; x < 8; x++) {
					var n = n + 1;
					self._p [x] [y] = (f [n] == 'W' ? WHITE : (f [n] == 'B' ? BLACK : null));
				}
			}
			self._calc_perm ();
		}
		else if (previous_board === null) {
			self._p [3] [3] = WHITE;
			self._p [4] [3] = BLACK;
			self._p [3] [4] = BLACK;
			self._p [4] [4] = WHITE;
			self._calc_perm ();
		}
		else {
			for (var x = 0; x < 8; x++) {
				for (var y = 0; y < 8; y++) {
					self._p [x] [y] = previous_board.is_piece (x, y);
				}
			}
			if (move !== null) {
				self._player = move.player;
				self.apply_move (move);
			}
			self.move_number = previous_board.move_number + 1;
		}
		self.__calculate_moves ();
	});},
	get __calculate_moves () {return __get__ (this, function (self) {
		self._moves = [];
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				if (self._p [x] [y] !== null) {
					continue;
				}
				if (self._move_down (self._player, x, y) || self._move_up (self._player, x, y) || self._move_left (self._player, x, y) || self._move_right (self._player, x, y) || self._move_down_right (self._player, x, y) || self._move_down_left (self._player, x, y) || self._move_up_right (self._player, x, y) || self._move_up_left (self._player, x, y)) {
					self._moves.append (Move (self._player, x, y));
				}
			}
		}
	});},
	get __repr__ () {return __get__ (this, function (self) {
		var s = '';
		for (var y = 0; y < 8; y++) {
			if (y != 0) {
				var s = s + ' ';
			}
			for (var x = 0; x < 8; x++) {
				var s = s + self._board_char (x, y);
			}
		}
		return __mod__ ("Board(%s, '%s')", tuple ([self._player, s]));
	});},
	get __hash__ () {return __get__ (this, function (self) {
		var h = (self._player == WHITE ? 0 : 1);
		var m = 1;
		for (var y = 0; y < 8; y++) {
			for (var x = 0; x < 8; x++) {
				var m = __mod__ (m * 2, 4294967296);
				if (self._p [x] [y] == BLACK) {
					var h = __mod__ (h + m, 4294967296);
				}
				if (self._p [x] [__mod__ (y + 4, 8)] == WHITE) {
					var h = __mod__ (h + m, 4294967296);
				}
			}
		}
		return h;
	});},
	get _board_char () {return __get__ (this, function (self, x, y) {
		if (self._p [x] [y] === null) {
			return (self.is_move (x, y) ? '*' : '.');
		}
		if (self._r [x] [y]) {
			return (self._p [x] [y] == WHITE ? 'W' : 'B');
		}
		return (self._p [x] [y] == WHITE ? 'w' : 'b');
	});},
	get __getitem__ () {return __get__ (this, function (self, x) {
		return self._p [x];
	});},
	get __len__ () {return __get__ (this, function (self) {
		var n = 0;
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				if (self._p [x] [y] !== null) {
					var n = n + 1;
				}
			}
		}
		return n;
	});},
	get move_count () {return __get__ (this, function (self) {
		return len (self._moves);
	});},
	get get_move () {return __get__ (this, function (self, n) {
		return self._moves [n];
	});},
	get get_moves () {return __get__ (this, function (self) {
		return self._moves;
	});},
	get apply_move () {return __get__ (this, function (self, move) {
		self._p [move.x] [move.y] = move.player;
		self._player = (move.player == BLACK ? WHITE : BLACK);
		self._move_down (move.player, move.x, move.y, true);
		self._move_up (move.player, move.x, move.y, true);
		self._move_left (move.player, move.x, move.y, true);
		self._move_right (move.player, move.x, move.y, true);
		self._move_down_right (move.player, move.x, move.y, true);
		self._move_down_left (move.player, move.x, move.y, true);
		self._move_up_right (move.player, move.x, move.y, true);
		self._move_up_left (move.player, move.x, move.y, true);
		self._calc_perm ();
	});},
	get is_move () {return __get__ (this, function (self, x, y) {
		if (x < 0 || x > 8 || y < 0 || y > 8) {
			return null;
		}
		for (var move of self._moves) {
			if (move.x == x && move.y == y) {
				return move;
			}
		}
		return null;
	});},
	get next_pending_move () {return __get__ (this, function (self, target_depth) {
		if (typeof target_depth == 'undefined' || (target_depth != null && target_depth.hasOwnProperty ("__kwargtrans__"))) {;
			var target_depth = 0;
		};
		for (var move of self._moves) {
			if (move.board === null) {
				return move;
			}
		}
		for (var move of self._moves) {
			if (move.score_depth < target_depth) {
				return move;
			}
		}
		return null;
	});},
	get best_move () {return __get__ (this, function (self) {
		if (len (self._moves) == 0) {
			return null;
		}
		self.sort_moves ();
		return self._moves [0];
	});},
	get sort_moves () {return __get__ (this, function (self) {
		self._moves.py_sort (__kwargtrans__ ({key: (function __lambda__ (m) {
			return m.score;
		})}));
	});},
	get is_piece () {return __get__ (this, function (self, x, y) {
		if (x === null || y === null || x < 0 || x > 8 || y < 0 || y > 8) {
			return null;
		}
		return self._p [x] [y];
	});},
	get count () {return __get__ (this, function (self, player) {
		var n = 0;
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				if (self._p [x] [y] == player) {
					var n = n + 1;
				}
			}
		}
		return n;
	});},
	get next_player () {return __get__ (this, function (self) {
		return self._player;
	});},
	get switch_player () {return __get__ (this, function (self) {
		self._player = (self._player == WHITE ? BLACK : WHITE);
		self.__calculate_moves ();
		self._calc_perm ();
		return self._player;
	});},
	get show () {return __get__ (this, function (self) {
		for (var y = 0; y < 8; y++) {
			var s = '';
			for (var x = 0; x < 8; x++) {
				var s = (s + self._board_char (x, y)) + ' ';
			}
			if (y == 0) {
				var s = (s + '\t W: ') + str (self.count (WHITE));
			}
			else if (y == 1) {
				var s = (s + '\t B: ') + str (self.count (BLACK));
			}
			else if (y == 2) {
				var s = (s + '\t ') + str (self._player);
			}
			else if (y == 3) {
				var s = (s + '\t ') + str (self.move_number);
			}
			print (s);
		}
		print ();
	});},
	get csv_line () {return __get__ (this, function (self) {
		var s = ((str (self.__hash__ ()) + ',') + str (self.move_number)) + ',';
		var s = (s + (self._player == WHITE ? 'W' : 'B')) + ',';
		for (var y = 0; y < 8; y++) {
			for (var x = 0; x < 8; x++) {
				if (self._p [x] [y] == WHITE) {
					var s = s + 'W,';
				}
				else if (self._p [x] [y] == BLACK) {
					var s = s + 'B,';
				}
				else {
					var s = s + ',';
				}
			}
		}
		return s;
	});},
	get _calc_perm () {return __get__ (this, function (self) {
		for (var n = 0; n < 8; n++) {
			for (var y = 0; y < 8; y++) {
				self._r [n] [y] = false;
			}
		}
		self._r [0] [0] = self._p [0] [0] !== null;
		self._r [0] [7] = self._p [0] [7] !== null;
		self._r [7] [0] = self._p [7] [0] !== null;
		self._r [7] [7] = self._p [7] [7] !== null;
		for (var n = 1; n < 8; n++) {
			if (self._r [n - 1] [0] && self._p [n] [0] == self._p [n - 1] [0]) {
				self._r [n] [0] = true;
			}
			if (self._r [n - 1] [7] && self._p [n] [7] == self._p [n - 1] [7]) {
				self._r [n] [7] = true;
			}
			if (self._r [0] [n - 1] && self._p [0] [n] == self._p [0] [n - 1]) {
				self._r [0] [n] = true;
			}
			if (self._r [7] [n - 1] && self._p [7] [n] == self._p [7] [n - 1]) {
				self._r [7] [n] = true;
			}
			if (self._r [8 - n] [0] && self._p [7 - n] [0] == self._p [8 - n] [0]) {
				self._r [7 - n] [0] = true;
			}
			if (self._r [8 - n] [7] && self._p [7 - n] [7] == self._p [8 - n] [7]) {
				self._r [7 - n] [7] = true;
			}
			if (self._r [0] [8 - n] && self._p [0] [7 - n] == self._p [0] [8 - n]) {
				self._r [0] [7 - n] = true;
			}
			if (self._r [7] [8 - n] && self._p [7] [7 - n] == self._p [7] [8 - n]) {
				self._r [7] [7 - n] = true;
			}
		}
		var done = false;
		while (!(done)) {
			var done = true;
			for (var x = 1; x < 7; x++) {
				for (var y = 1; y < 7; y++) {
					if (self._p [x] [y] === null || self._r [x] [y]) {
						continue;
					}
					if (self._r [x - 1] [y] && self._r [x - 1] [y - 1] && self._r [x] [y - 1] || self._r [x] [y - 1] && self._r [x + 1] [y - 1] && self._r [x + 1] [y] || self._r [x + 1] [y] && self._r [x + 1] [y + 1] && self._r [x] [y + 1] || self._r [x] [y + 1] && self._r [x - 1] [y + 1] && self._r [x - 1] [y]) {
						self._r [x] [y] = true;
						var done = false;
					}
				}
			}
		}
	});},
	get is_permanent () {return __get__ (this, function (self, player, x, y) {
		return self._p [x] [y] == player && self._r [x] [y];
	});},
	get _perm_left () {return __get__ (this, function (self, player, x, y) {
		for (var xx = 0; xx < x + 1; xx++) {
			if (self._p [xx] [y] != player) {
				return false;
			}
		}
		return true;
	});},
	get _perm_right () {return __get__ (this, function (self, player, x, y) {
		for (var xx = x; xx < 8; xx++) {
			if (self._p [xx] [y] != player) {
				return false;
			}
		}
		return true;
	});},
	get _perm_up () {return __get__ (this, function (self, player, x, y) {
		for (var yy = 0; yy < y + 1; yy++) {
			if (self._p [x] [yy] != player) {
				return false;
			}
		}
		return true;
	});},
	get _perm_down () {return __get__ (this, function (self, player, x, y) {
		for (var yy = y; yy < 8; yy++) {
			if (self._p [x] [yy] != player) {
				return false;
			}
		}
		return true;
	});},
	get _move_down () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y + (n + 1) < 8 && self._p [x] [y + (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y + (n + 1) < 8 && self._p [x] [y + (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x] [y + m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_up () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y - (n + 1) >= 0 && self._p [x] [y - (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y - (n + 1) >= 0 && self._p [x] [y - (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x] [y - m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_right () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (x + (n + 1) < 8 && self._p [x + (n + 1)] [y] == other_player) {
			var n = n + 1;
		}
		if (x + (n + 1) < 8 && self._p [x + (n + 1)] [y] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x + m] [y] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_left () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (x - (n + 1) >= 0 && self._p [x - (n + 1)] [y] == other_player) {
			var n = n + 1;
		}
		if (x - (n + 1) >= 0 && self._p [x - (n + 1)] [y] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x - m] [y] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_down_right () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y + (n + 1) < 8 && x + (n + 1) < 8 && self._p [x + (n + 1)] [y + (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y + (n + 1) < 8 && x + (n + 1) < 8 && self._p [x + (n + 1)] [y + (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x + m] [y + m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_down_left () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y + (n + 1) < 8 && x - (n + 1) >= 0 && self._p [x - (n + 1)] [y + (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y + (n + 1) < 8 && x - (n + 1) >= 0 && self._p [x - (n + 1)] [y + (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x - m] [y + m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_up_right () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y - (n + 1) >= 0 && x + (n + 1) < 8 && self._p [x + (n + 1)] [y - (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y - (n + 1) >= 0 && x + (n + 1) < 8 && self._p [x + (n + 1)] [y - (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x + m] [y - m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});},
	get _move_up_left () {return __get__ (this, function (self, player, x, y, do_move) {
		if (typeof do_move == 'undefined' || (do_move != null && do_move.hasOwnProperty ("__kwargtrans__"))) {;
			var do_move = false;
		};
		var other_player = (player == BLACK ? WHITE : BLACK);
		var n = 0;
		while (y - (n + 1) >= 0 && x - (n + 1) >= 0 && self._p [x - (n + 1)] [y - (n + 1)] == other_player) {
			var n = n + 1;
		}
		if (y - (n + 1) >= 0 && x - (n + 1) >= 0 && self._p [x - (n + 1)] [y - (n + 1)] == player) {
			if (do_move) {
				for (var m = 0; m < n + 1; m++) {
					self._p [x - m] [y - m] = player;
				}
			}
			return n;
		}
		else {
			return 0;
		}
	});}
});

//# sourceMappingURL=board.map