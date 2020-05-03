// Transcrypt'ed from Python, 2020-05-03 15:34:42
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {WHITE} from './board.js';
import {BLACK} from './board.js';
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
export var F1 =  __class__ ('F1', [EvaluationFunction], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, p0, p1, p2, pm) {
		if (typeof p0 == 'undefined' || (p0 != null && p0.hasOwnProperty ("__kwargtrans__"))) {;
			var p0 = 10;
		};
		if (typeof p1 == 'undefined' || (p1 != null && p1.hasOwnProperty ("__kwargtrans__"))) {;
			var p1 = 12;
		};
		if (typeof p2 == 'undefined' || (p2 != null && p2.hasOwnProperty ("__kwargtrans__"))) {;
			var p2 = 11;
		};
		if (typeof pm == 'undefined' || (pm != null && pm.hasOwnProperty ("__kwargtrans__"))) {;
			var pm = 15;
		};
		self.p0 = p0;
		self.p1 = p1;
		self.p2 = p2;
		self.pm = pm;
	});},
	get eval_board () {return __get__ (this, function (self, board) {
		var score = 0;
		for (var x = 0; x < 8; x++) {
			for (var y = 0; y < 8; y++) {
				var player = board.is_piece (x, y);
				var v = self.p0;
				var v = (_good_location_1 (x, y) ? self.p1 : v);
				var v = (_good_location_2 (x, y) ? self.p2 : v);
				var v = (board.is_permanent (player, x, y) ? self.pm : v);
				if (player == WHITE) {
					var score = score + v;
				}
				if (player == BLACK) {
					var score = score - v;
				}
			}
		}
		return score;
	});}
});

//# sourceMappingURL=eval_functions.map