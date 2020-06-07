// Transcrypt'ed from Python, 2020-06-07 16:27:50
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {BLACK, Board, Move, WHITE} from './board.js';
var __name__ = 'eval_functions';
export var EvaluationFunction =  __class__ ('EvaluationFunction', [object], {
	__module__: __name__,
	get eval_board () {return __get__ (this, function (self, board) {
		return 0;
	});},
	get eval_move () {return __get__ (this, function (self, board, move) {
		move.score = self.eval_board (board);
		move.score_depth = 1;
		return true;
	});},
	get eval_vector () {return __get__ (this, function (self, board) {
		return tuple ([0, 0]);
	});}
});
export var F0 =  __class__ ('F0', [EvaluationFunction], {
	__module__: __name__,
	get eval_board () {return __get__ (this, function (self, board) {
		return 0;
	});}
});
export var _good_location_1 = function (x, y) {
	return x == 0 && y == 2 || x == 0 && y == 5 || x == 7 && y == 2 || x == 7 && y == 5 || x == 2 && y == 0 || x == 5 && y == 0 || x == 2 && y == 7 || x == 5 && y == 7;
};
export var _good_location_2 = function (x, y) {
	return x == 2 && y == 2 || x == 5 && y == 2 || x == 2 && y == 5 || x == 5 && y == 5;
};
export var _bad_location_3 = function (x, y) {
	return x == 0 && y == 1 || x == 0 && y == 6 || x == 7 && y == 1 || x == 7 && y == 6 || x == 1 && y == 0 || x == 6 && y == 0 || x == 1 && y == 7 || x == 6 && y == 7;
};
export var _bad_location_4 = function (x, y) {
	return x == 1 && y == 1 || x == 6 && y == 1 || x == 1 && y == 6 || x == 6 && y == 6;
};
export var _bad_location_5 = function (x, y) {
	return x == 2 && y == 1 || x == 1 && y == 2 || x == 5 && y == 1 || x == 6 && y == 2 || x == 1 && y == 5 || x == 2 && y == 6 || x == 5 && y == 6 || x == 6 && y == 5;
};
export var _good_location_6 = function (x, y) {
	return x == 0 && y == 3 || x == 0 && y == 4 || x == 7 && y == 3 || x == 7 && y == 4 || x == 3 && y == 0 || x == 4 && y == 0 || x == 3 && y == 7 || x == 4 && y == 7;
};
export var _bad_location_7 = function (x, y) {
	return x == 1 && y == 3 || x == 1 && y == 4 || x == 6 && y == 3 || x == 6 && y == 4 || x == 3 && y == 1 || x == 4 && y == 1 || x == 3 && y == 6 || x == 4 && y == 6;
};
export var _good_location_8 = function (x, y) {
	return x == 2 && y == 3 || x == 2 && y == 4 || x == 5 && y == 3 || x == 5 && y == 4 || x == 3 && y == 2 || x == 4 && y == 2 || x == 3 && y == 5 || x == 4 && y == 5;
};
export var F1 =  __class__ ('F1', [EvaluationFunction], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, p0, p1, p2, p3, p4, p5, p6, p7, p8, pm, p_move, p_player) {
		if (typeof p0 == 'undefined' || (p0 != null && p0.hasOwnProperty ("__kwargtrans__"))) {;
			var p0 = 1;
		};
		if (typeof p1 == 'undefined' || (p1 != null && p1.hasOwnProperty ("__kwargtrans__"))) {;
			var p1 = 10;
		};
		if (typeof p2 == 'undefined' || (p2 != null && p2.hasOwnProperty ("__kwargtrans__"))) {;
			var p2 = 10;
		};
		if (typeof p3 == 'undefined' || (p3 != null && p3.hasOwnProperty ("__kwargtrans__"))) {;
			var p3 = -(10);
		};
		if (typeof p4 == 'undefined' || (p4 != null && p4.hasOwnProperty ("__kwargtrans__"))) {;
			var p4 = -(10);
		};
		if (typeof p5 == 'undefined' || (p5 != null && p5.hasOwnProperty ("__kwargtrans__"))) {;
			var p5 = 1;
		};
		if (typeof p6 == 'undefined' || (p6 != null && p6.hasOwnProperty ("__kwargtrans__"))) {;
			var p6 = 5;
		};
		if (typeof p7 == 'undefined' || (p7 != null && p7.hasOwnProperty ("__kwargtrans__"))) {;
			var p7 = 1;
		};
		if (typeof p8 == 'undefined' || (p8 != null && p8.hasOwnProperty ("__kwargtrans__"))) {;
			var p8 = 5;
		};
		if (typeof pm == 'undefined' || (pm != null && pm.hasOwnProperty ("__kwargtrans__"))) {;
			var pm = 100;
		};
		if (typeof p_move == 'undefined' || (p_move != null && p_move.hasOwnProperty ("__kwargtrans__"))) {;
			var p_move = 0;
		};
		if (typeof p_player == 'undefined' || (p_player != null && p_player.hasOwnProperty ("__kwargtrans__"))) {;
			var p_player = 0;
		};
		self.p0 = p0;
		self.p1 = p1;
		self.p2 = p2;
		self.p3 = p3;
		self.p4 = p4;
		self.p5 = p5;
		self.p6 = p6;
		self.p7 = p7;
		self.p8 = p8;
		self.pm = pm;
		self.p_move = p_move;
		self.p_player = p_player;
	});},
	get eval_vector () {return __get__ (this, function (self, board) {
		var s0 = 0;
		var g1 = 0;
		var g2 = 0;
		var b3 = 0;
		var b4 = 0;
		var b5 = 0;
		var g6 = 0;
		var b7 = 0;
		var g8 = 0;
		var sm = 0;
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				var player = board.is_piece (x, y);
				var p = (player == WHITE ? 1 : (player == BLACK ? -(1) : 0));
				var s0 = s0 + p;
				var g1 = (_good_location_1 (x, y) ? g1 + p : g1);
				var g2 = (_good_location_2 (x, y) ? g2 + p : g2);
				var b3 = (_bad_location_3 (x, y) ? b3 + p : b3);
				var b4 = (_bad_location_4 (x, y) ? b4 + p : b4);
				var b5 = (_bad_location_5 (x, y) ? b5 + p : b5);
				var g6 = (_good_location_6 (x, y) ? g6 + p : g6);
				var b7 = (_bad_location_7 (x, y) ? b7 + p : b7);
				var g8 = (_good_location_8 (x, y) ? g8 + p : g8);
				var sm = (board.is_permanent (player, x, y) ? sm + p : sm);
			}
		}
		return tuple ([s0, g1, g2, b3, b4, b5, g6, b7, g8, sm]);
	});},
	get eval_board () {return __get__ (this, function (self, board) {
		var score = 0;
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				var player = board.is_piece (x, y);
				var v = self.p0;
				var v = (_good_location_1 (x, y) ? self.p1 : v);
				var v = (_good_location_2 (x, y) ? self.p2 : v);
				var v = (_bad_location_3 (x, y) ? self.p3 : v);
				var v = (_bad_location_4 (x, y) ? self.p4 : v);
				var v = (_bad_location_5 (x, y) ? self.p5 : v);
				var v = (_good_location_6 (x, y) ? self.p6 : v);
				var v = (_bad_location_7 (x, y) ? self.p7 : v);
				var v = (_good_location_8 (x, y) ? self.p8 : v);
				var v = (player !== null && board.is_permanent (player, x, y) ? self.pm : v);
				if (player == WHITE) {
					var score = score + v;
				}
				if (player == BLACK) {
					var score = score - v;
				}
			}
		}
		var score = score + board.move_number * self.p_move;
		if (board.next_player () == WHITE) {
			var score = score + self.p_player;
		}
		return score;
	});}
});
export var F2 =  __class__ ('F2', [F1], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		F1.__init__ (self, 28.27866061, -(6.37442292), -(17.93707242), -(64.12435399), -(81.42209786), -(54.35718033), -(20.9621922), -(41.92151928), -(33.21931113), 120.04270918, -(1.46908731), 95.41359195);
	});}
});

//# sourceMappingURL=eval_functions.map