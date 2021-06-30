// Transcrypt'ed from Python, 2021-06-29 21:29:01
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
		var player = (board.next_player () == WHITE ? 1.0 : 0.0);
		return tuple ([s0, g1, g2, b3, b4, b5, g6, b7, g8, sm, board.move_number, player]);
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
export var F1a =  __class__ ('F1a', [F1], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		F1.__init__ (self, 28.27866061, -(6.37442292), -(17.93707242), -(64.12435399), -(81.42209786), -(54.35718033), -(20.9621922), -(41.92151928), -(33.21931113), 120.04270918, -(1.46908731), 95.41359195);
	});}
});
export var F2 =  __class__ ('F2', [F1], {
	__module__: __name__,
	get eval_board () {return __get__ (this, function (self, board) {
		var __left0__ = self.eval_vector (board);
		var s0 = __left0__ [0];
		var g1 = __left0__ [1];
		var g2 = __left0__ [2];
		var b3 = __left0__ [3];
		var b4 = __left0__ [4];
		var b5 = __left0__ [5];
		var g6 = __left0__ [6];
		var b7 = __left0__ [7];
		var g8 = __left0__ [8];
		var sm = __left0__ [9];
		var move = __left0__ [10];
		var player = __left0__ [11];
		if (sm <= -(1.5)) {
			if (sm <= -(7.5)) {
				if (sm <= -(14.5)) {
					if (sm <= -(22.5)) {
						if (sm <= -(41.0)) {
							if (sm <= -(44.5)) {
								if (move <= 56.5) {
									return int (-(6200.0));
								}
								else {
									return int (-(6300.0));
								}
							}
							else if (move <= 57.5) {
								return int (-(5000.0));
							}
							else {
								return int (-(3900.0));
							}
						}
						else if (b5 <= -(5.5)) {
							if (sm <= -(27.5)) {
								if (g8 <= -(1.0)) {
									if (b4 <= -(2.5)) {
										return int (-(1475.5555555555557));
									}
									else {
										return int (-(2634.5));
									}
								}
								else if (s0 <= -(28.5)) {
									return int (-(4636.666666666667));
								}
								else {
									return int (-(3163.3333333333335));
								}
							}
							else if (b7 <= -(2.5)) {
								if (s0 <= -(29.0)) {
									return int (-(1534.5));
								}
								else {
									return int (-(857.7777777777778));
								}
							}
							else if (s0 <= -(27.5)) {
								return int (-(1415.0));
							}
							else {
								return int (-(2325.0));
							}
						}
						else if (sm <= -(30.5)) {
							if (move <= 57.5) {
								if (g2 <= -(3.0)) {
									return int (-(3812.8125));
								}
								else {
									return int (-(3314.0625));
								}
							}
							else if (b7 <= -(3.0)) {
								return int (-(3573.5));
							}
							else {
								return int (-(4882.0));
							}
						}
						else if (b4 <= -(3.5)) {
							if (g6 <= -(5.5)) {
								return int (-(2929.1666666666665));
							}
							else {
								return int (-(2107.4333333333334));
							}
						}
						else if (s0 <= -(21.5)) {
							return int (-(2791.987012987013));
						}
						else {
							return int (-(3230.4285714285716));
						}
					}
					else if (b5 <= -(2.5)) {
						if (b7 <= -(3.5)) {
							if (b4 <= -(1.5)) {
								if (b7 <= -(4.5)) {
									if (b3 <= -(1.5)) {
										return int (-(1274.357142857143));
									}
									else {
										return int (-(556.2941176470588));
									}
								}
								else if (move <= 57.5) {
									return int (-(1306.6923076923076));
								}
								else {
									return int (-(2701.25));
								}
							}
							else if (b5 <= -(5.5)) {
								if (s0 <= -(15.5)) {
									return int (-(918.5));
								}
								else {
									return int (-(1590.0));
								}
							}
							else if (b3 <= 0.5) {
								return int (-(1884.0350877192982));
							}
							else {
								return int (-(268.5));
							}
						}
						else if (b5 <= -(5.5)) {
							if (player <= 0.5) {
								if (s0 <= -(12.0)) {
									return int (-(1998.25));
								}
								else {
									return int (-(300.0));
								}
							}
							else if (move <= 50.0) {
								return int (-(1931.0));
							}
							else {
								return int (-(1168.1666666666667));
							}
						}
						else if (move <= 57.5) {
							if (s0 <= -(8.5)) {
								return int (-(1938.241573033708));
							}
							else {
								return int (-(3331.0));
							}
						}
						else if (g8 <= -(4.0)) {
							return int (-(1010.0));
						}
						else {
							return int (-(2817.3333333333335));
						}
					}
					else if (move <= 50.5) {
						if (b4 <= 1.5) {
							if (sm <= -(20.5)) {
								if (g2 <= 1.0) {
									return int (-(2270.8823529411766));
								}
								else {
									return int (-(3455.0));
								}
							}
							else if (b7 <= 5.5) {
								return int (-(1972.2044198895028));
							}
							else {
								return int (-(2678.5));
							}
						}
						else if (sm <= -(17.5)) {
							if (b5 <= -(1.5)) {
								return int (-(3983.0));
							}
							else {
								return int (-(3003.125));
							}
						}
						else if (move <= 43.5) {
							return int (-(3088.5));
						}
						else {
							return int (-(2224.181818181818));
						}
					}
					else if (player <= 0.5) {
						if (move <= 54.5) {
							if (s0 <= -(10.0)) {
								return int (-(2251.5142857142855));
							}
							else {
								return int (-(2644.0675675675675));
							}
						}
						else if (s0 <= 4.5) {
							return int (-(2934.8009478672984));
						}
						else {
							return int (-(1845.6));
						}
					}
					else if (s0 <= -(19.5)) {
						if (g8 <= -(1.5)) {
							return int (-(1685.9130434782608));
						}
						else {
							return int (-(2178.825));
						}
					}
					else if (sm <= -(19.5)) {
						return int (-(2879.449275362319));
					}
					else {
						return int (-(2266.308));
					}
				}
				else if (b5 <= -(0.5)) {
					if (sm <= -(11.5)) {
						if (s0 <= -(11.5)) {
							if (sm <= -(13.5)) {
								if (b3 <= -(0.5)) {
									if (g8 <= -(5.5)) {
										return int (-(3462.8));
									}
									else {
										return int (-(1661.1860465116279));
									}
								}
								else if (move <= 51.5) {
									return int (-(2122.0));
								}
								else {
									return int (-(412.9166666666667));
								}
							}
							else if (b4 <= -(3.5)) {
								if (g1 <= 1.5) {
									return int (-(790.6923076923077));
								}
								else {
									return int (443.3333333333333);
								}
							}
							else if (s0 <= -(17.5)) {
								return int (-(1077.7816091954023));
							}
							else {
								return int (-(1523.5114503816794));
							}
						}
						else if (g6 <= 0.5) {
							if (move <= 55.5) {
								if (b3 <= 2.5) {
									return int (-(1808.3925925925926));
								}
								else {
									return int (290.0);
								}
							}
							else if (g1 <= -(1.5)) {
								return int (-(2521.5789473684213));
							}
							else {
								return int (-(1943.0555555555557));
							}
						}
						else if (s0 <= -(7.5)) {
							if (move <= 51.5) {
								return int (-(1221.0));
							}
							else {
								return int (-(668.5));
							}
						}
						else if (b3 <= 0.5) {
							return int (-(1628.9411764705883));
						}
						else {
							return int (-(2351.714285714286));
						}
					}
					else if (b5 <= -(3.5)) {
						if (move <= 50.5) {
							if (sm <= -(9.5)) {
								if (sm <= -(10.5)) {
									return int (-(1047.3076923076924));
								}
								else {
									return int (-(1391.3225806451612));
								}
							}
							else if (b7 <= -(1.5)) {
								return int (-(819.0294117647059));
							}
							else {
								return int (-(1090.873015873016));
							}
						}
						else if (player <= 0.5) {
							if (s0 <= -(26.0)) {
								return int (-(3980.0));
							}
							else {
								return int (-(943.8524590163935));
							}
						}
						else if (s0 <= -(31.0)) {
							return int (-(2289.0));
						}
						else {
							return int (-(514.1428571428571));
						}
					}
					else if (sm <= -(9.5)) {
						if (g8 <= 7.0) {
							if (b7 <= 1.5) {
								return int (-(1315.0681818181818));
							}
							else {
								return int (-(1683.1649484536083));
							}
						}
						else {
							return int (2005.0);
						}
					}
					else if (b3 <= -(0.5)) {
						if (move <= 57.5) {
							return int (-(1110.3459302325582));
						}
						else {
							return int (-(1723.5));
						}
					}
					else if (g6 <= -(2.5)) {
						return int (-(899.7692307692307));
					}
					else {
						return int (-(1414.3854166666667));
					}
				}
				else if (sm <= -(11.5)) {
					if (s0 <= -(10.5)) {
						if (s0 <= -(15.5)) {
							if (move <= 53.5) {
								if (g8 <= -(1.5)) {
									return int (-(1391.3214285714287));
								}
								else {
									return int (-(2003.4285714285713));
								}
							}
							else if (b4 <= 2.5) {
								return int (-(1066.9714285714285));
							}
							else {
								return int (1210.0);
							}
						}
						else if (b7 <= 1.5) {
							if (g1 <= -(4.5)) {
								return int (-(2222.3125));
							}
							else {
								return int (-(1565.9444444444443));
							}
						}
						else if (g8 <= -(7.0)) {
							return int (-(3895.0));
						}
						else {
							return int (-(2150.814814814815));
						}
					}
					else if (move <= 55.5) {
						if (b7 <= -(0.5)) {
							if (b3 <= -(1.5)) {
								return int (-(1450.3636363636363));
							}
							else {
								return int (-(1968.0));
							}
						}
						else if (g1 <= -(5.5)) {
							return int (-(2747.6363636363635));
						}
						else {
							return int (-(2082.402985074627));
						}
					}
					else if (player <= 0.5) {
						if (s0 <= 6.0) {
							return int (-(2720.704081632653));
						}
						else {
							return int (-(1967.3076923076924));
						}
					}
					else if (s0 <= 12.0) {
						return int (-(1992.8461538461538));
					}
					else {
						return int (400.0);
					}
				}
				else if (move <= 53.5) {
					if (b4 <= 0.5) {
						if (sm <= -(8.5)) {
							if (g8 <= -(6.5)) {
								return int (254.0);
							}
							else {
								return int (-(1509.0639534883721));
							}
						}
						else if (move <= 50.5) {
							return int (-(1178.0545454545454));
						}
						else {
							return int (-(1531.9242424242425));
						}
					}
					else if (b5 <= 4.5) {
						if (g6 <= -(2.5)) {
							return int (-(1745.7596153846155));
						}
						else {
							return int (-(1478.4913294797689));
						}
					}
					else if (b3 <= -(3.5)) {
						return int (-(2342.0));
					}
					else {
						return int (-(1822.0754716981132));
					}
				}
				else if (player <= 0.5) {
					if (b7 <= 2.5) {
						if (move <= 54.5) {
							return int (-(1588.560975609756));
						}
						else {
							return int (-(1972.3333333333333));
						}
					}
					else if (b4 <= 0.5) {
						return int (-(2382.560606060606));
					}
					else {
						return int (-(1888.0));
					}
				}
				else if (b7 <= 1.5) {
					if (s0 <= -(9.0)) {
						return int (-(826.5217391304348));
					}
					else {
						return int (-(1479.9354838709678));
					}
				}
				else if (b5 <= 3.5) {
					return int (-(1495.016393442623));
				}
				else {
					return int (-(2509.9615384615386));
				}
			}
			else if (sm <= -(4.5)) {
				if (b5 <= -(0.5)) {
					if (b3 <= -(2.5)) {
						if (move <= 55.5) {
							if (b5 <= -(3.5)) {
								if (move <= 49.5) {
									if (g1 <= -(0.5)) {
										return int (-(299.87179487179486));
									}
									else {
										return int (-(1035.7692307692307));
									}
								}
								else if (b4 <= 0.5) {
									return int (-(3.3508771929824563));
								}
								else {
									return int (-(991.7142857142857));
								}
							}
							else if (b4 <= -(1.5)) {
								if (sm <= -(6.5)) {
									return int (-(662.1176470588235));
								}
								else {
									return int (-(119.47169811320755));
								}
							}
							else if (g8 <= 2.5) {
								return int (-(653.1926605504588));
							}
							else {
								return int (-(1372.5217391304348));
							}
						}
						else if (s0 <= -(1.5)) {
							if (g6 <= 2.5) {
								if (s0 <= -(12.0)) {
									return int (-(645.7222222222222));
								}
								else {
									return int (-(1417.0));
								}
							}
							else if (g8 <= -(4.0)) {
								return int (800.0);
							}
							else {
								return int (110.0);
							}
						}
						else if (g8 <= 5.0) {
							if (b3 <= -(3.5)) {
								return int (-(5000.0));
							}
							else {
								return int (-(2452.5));
							}
						}
						else {
							return int (200.0);
						}
					}
					else if (b7 <= -(3.5)) {
						if (sm <= -(6.5)) {
							if (b3 <= 1.5) {
								if (move <= 55.5) {
									return int (-(897.6792452830189));
								}
								else {
									return int (-(1588.6666666666667));
								}
							}
							else if (s0 <= 1.5) {
								return int (458.6666666666667);
							}
							else {
								return int (-(180.0));
							}
						}
						else if (move <= 54.5) {
							if (g8 <= -(0.5)) {
								return int (-(406.271186440678));
							}
							else {
								return int (-(685.2444444444444));
							}
						}
						else if (player <= 0.5) {
							return int (-(992.75));
						}
						else {
							return int (277.3333333333333);
						}
					}
					else if (move <= 55.5) {
						if (sm <= -(6.5)) {
							if (b4 <= -(3.5)) {
								return int (-(525.8571428571429));
							}
							else {
								return int (-(1119.0441988950276));
							}
						}
						else if (b3 <= -(1.5)) {
							return int (-(681.191235059761));
						}
						else {
							return int (-(878.548623853211));
						}
					}
					else if (s0 <= -(7.5)) {
						if (player <= 0.5) {
							return int (-(1082.6153846153845));
						}
						else {
							return int (75.83333333333333);
						}
					}
					else if (b4 <= -(1.5)) {
						return int (-(744.4736842105264));
					}
					else {
						return int (-(1839.3333333333333));
					}
				}
				else if (move <= 55.5) {
					if (b4 <= 1.5) {
						if (b3 <= 0.5) {
							if (sm <= -(6.5)) {
								if (b3 <= -(1.5)) {
									return int (-(990.9961832061068));
								}
								else {
									return int (-(1315.041095890411));
								}
							}
							else if (b5 <= 1.5) {
								return int (-(863.9013657056146));
							}
							else {
								return int (-(1008.9853157121879));
							}
						}
						else if (sm <= -(6.5)) {
							if (b5 <= 4.5) {
								return int (-(1430.0235294117647));
							}
							else {
								return int (-(1974.3076923076924));
							}
						}
						else if (s0 <= 9.5) {
							return int (-(1202.844155844156));
						}
						else {
							return int (-(823.575));
						}
					}
					else if (b5 <= 2.5) {
						if (b3 <= 1.5) {
							if (b7 <= -(2.5)) {
								return int (-(870.9565217391304));
							}
							else {
								return int (-(1170.1831683168316));
							}
						}
						else if (g1 <= -(3.5)) {
							return int (-(864.5));
						}
						else {
							return int (-(1733.2));
						}
					}
					else if (b3 <= -(2.5)) {
						if (g1 <= -(1.5)) {
							return int (-(2203.8));
						}
						else {
							return int (-(1667.6666666666667));
						}
					}
					else if (move <= 54.5) {
						return int (-(1453.1628959276018));
					}
					else {
						return int (-(615.8333333333334));
					}
				}
				else if (player <= 0.5) {
					if (b7 <= 1.5) {
						if (g6 <= 5.5) {
							if (sm <= -(5.5)) {
								return int (-(1779.5438596491229));
							}
							else {
								return int (-(1147.2727272727273));
							}
						}
						else if (sm <= -(6.0)) {
							return int (-(2990.0));
						}
						else {
							return int (-(3990.0));
						}
					}
					else if (move <= 56.5) {
						if (b3 <= 0.5) {
							return int (-(2124.6285714285714));
						}
						else {
							return int (-(1456.6666666666667));
						}
					}
					else if (b5 <= 1.5) {
						return int (-(1941.8181818181818));
					}
					else {
						return int (-(2570.1153846153848));
					}
				}
				else if (s0 <= 7.5) {
					if (b7 <= 1.5) {
						if (sm <= -(6.5)) {
							return int (-(961.7692307692307));
						}
						else {
							return int (-(244.1578947368421));
						}
					}
					else if (s0 <= 1.0) {
						return int (-(1035.8333333333333));
					}
					else {
						return int (-(2446.0));
					}
				}
				else if (g6 <= 2.5) {
					return int (-(2095.0));
				}
				else if (b3 <= 1.5) {
					return int (-(3030.0));
				}
				else {
					return int (-(3690.0));
				}
			}
			else if (b5 <= -(0.5)) {
				if (b3 <= -(1.5)) {
					if (sm <= -(3.5)) {
						if (g1 <= -(0.5)) {
							if (b7 <= -(0.5)) {
								if (move <= 40.5) {
									return int (-(437.46153846153845));
								}
								else {
									return int (67.39622641509433);
								}
							}
							else if (move <= 55.5) {
								return int (-(394.030303030303));
							}
							else {
								return int (-(1110.0));
							}
						}
						else if (b4 <= 0.5) {
							if (g2 <= -(0.5)) {
								return int (-(630.5769230769231));
							}
							else {
								return int (-(317.0925925925926));
							}
						}
						else if (b5 <= -(4.5)) {
							return int (-(2090.0));
						}
						else {
							return int (-(711.9354838709677));
						}
					}
					else if (b5 <= -(3.5)) {
						if (move <= 53.5) {
							if (g6 <= -(3.5)) {
								return int (688.4444444444445);
							}
							else {
								return int (196.86111111111111);
							}
						}
						else if (s0 <= -(8.5)) {
							return int (-(711.8888888888889));
						}
						else {
							return int (423.375);
						}
					}
					else if (g6 <= 3.5) {
						if (b3 <= -(4.5)) {
							return int (587.1428571428571);
						}
						else {
							return int (-(206.68564356435644));
						}
					}
					else if (g1 <= 2.5) {
						return int (45.666666666666664);
					}
					else {
						return int (830.1428571428571);
					}
				}
				else if (move <= 48.5) {
					if (b4 <= -(0.5)) {
						if (sm <= -(2.5)) {
							if (g6 <= -(5.5)) {
								return int (-(1728.0));
							}
							else {
								return int (-(541.7595907928388));
							}
						}
						else if (g6 <= 3.5) {
							return int (-(317.12703583061887));
						}
						else {
							return int (193.15384615384616);
						}
					}
					else if (sm <= -(3.5)) {
						if (g1 <= 1.5) {
							return int (-(807.139344262295));
						}
						else {
							return int (-(1235.611111111111));
						}
					}
					else if (g8 <= -(3.5)) {
						return int (-(838.9344262295082));
					}
					else {
						return int (-(553.2684931506849));
					}
				}
				else if (player <= 0.5) {
					if (g6 <= 7.5) {
						if (move <= 55.0) {
							return int (-(305.3069306930693));
						}
						else {
							return int (-(873.2181818181818));
						}
					}
					else if (b3 <= 1.5) {
						return int (-(3780.0));
					}
					else {
						return int (-(2890.0));
					}
				}
				else if (move <= 54.0) {
					if (b5 <= -(2.5)) {
						return int (-(66.15));
					}
					else {
						return int (-(395.6276595744681));
					}
				}
				else if (g6 <= -(2.5)) {
					return int (-(111.26923076923077));
				}
				else {
					return int (379.2);
				}
			}
			else if (move <= 55.5) {
				if (b3 <= -(0.5)) {
					if (sm <= -(3.5)) {
						if (b5 <= 2.5) {
							if (g6 <= -(1.5)) {
								return int (-(846.9491525423729));
							}
							else {
								return int (-(652.5331010452961));
							}
						}
						else if (g1 <= -(2.5)) {
							return int (-(1458.5714285714287));
						}
						else {
							return int (-(834.1830065359477));
						}
					}
					else if (b4 <= 0.5) {
						if (move <= 54.5) {
							return int (-(408.85806451612905));
						}
						else {
							return int (473.53333333333336);
						}
					}
					else if (b7 <= 2.5) {
						return int (-(564.858310626703));
					}
					else {
						return int (-(767.0677966101695));
					}
				}
				else if (sm <= -(2.5)) {
					if (b3 <= 0.5) {
						if (b5 <= 6.5) {
							return int (-(757.9287974683544));
						}
						else {
							return int (-(1637.1));
						}
					}
					else if (s0 <= 14.5) {
						return int (-(970.2427983539095));
					}
					else {
						return int (-(1271.8235294117646));
					}
				}
				else if (b3 <= 3.5) {
					if (move <= 48.5) {
						return int (-(687.7792378449409));
					}
					else {
						return int (-(458.74074074074076));
					}
				}
				else if (b7 <= 5.0) {
					return int (-(1058.7586206896551));
				}
				else {
					return int (-(2869.5));
				}
			}
			else if (player <= 0.5) {
				if (g1 <= -(5.5)) {
					if (move <= 57.0) {
						return int (-(1820.0));
					}
					else if (b5 <= 4.5) {
						return int (-(3700.0));
					}
					else {
						return int (-(4500.0));
					}
				}
				else if (b7 <= 4.5) {
					if (b5 <= 3.5) {
						return int (-(1253.5533980582525));
					}
					else {
						return int (-(1825.5294117647059));
					}
				}
				else if (s0 <= 11.0) {
					return int (-(2823.846153846154));
				}
				else {
					return int (-(1617.2857142857142));
				}
			}
			else if (b7 <= 7.0) {
				if (g2 <= 1.0) {
					if (b5 <= 1.5) {
						return int (-(43.774193548387096));
					}
					else {
						return int (-(615.7368421052631));
					}
				}
				else if (g6 <= 3.0) {
					return int (-(1178.611111111111));
				}
				else {
					return int (861.0);
				}
			}
			else {
				return int (-(3697.5));
			}
		}
		else if (sm <= 3.5) {
			if (sm <= 0.5) {
				if (b4 <= 0.5) {
					if (b3 <= -(0.5)) {
						if (b4 <= -(0.5)) {
							if (sm <= -(0.5)) {
								if (b5 <= 3.5) {
									if (move <= 55.5) {
										return int (118.83349561830575);
									}
									else {
										return int (-(485.14285714285717));
									}
								}
								else if (move <= 52.5) {
									return int (-(312.68));
								}
								else {
									return int (-(1891.5714285714287));
								}
							}
							else if (b3 <= -(1.5)) {
								if (b5 <= 7.0) {
									return int (515.1065830721003);
								}
								else {
									return int (-(2855.0));
								}
							}
							else if (b4 <= -(1.5)) {
								return int (400.19597315436243);
							}
							else {
								return int (258.3535539215686);
							}
						}
						else if (sm <= -(0.5)) {
							if (move <= 55.5) {
								if (b7 <= -(0.5)) {
									return int (-(11.654929577464788));
								}
								else {
									return int (-(216.19163763066203));
								}
							}
							else if (move <= 56.5) {
								return int (-(1361.8333333333333));
							}
							else {
								return int (-(577.5));
							}
						}
						else if (move <= 55.5) {
							if (b3 <= -(1.5)) {
								return int (223.28571428571428);
							}
							else {
								return int (73.63138832997988);
							}
						}
						else if (g1 <= -(1.0)) {
							return int (-(2470.0));
						}
						else {
							return int (-(471.42857142857144));
						}
					}
					else if (sm <= -(0.5)) {
						if (b3 <= 1.5) {
							if (b4 <= -(1.5)) {
								if (move <= 44.5) {
									return int (-(51.05882352941177));
								}
								else {
									return int (285.49411764705883);
								}
							}
							else if (b4 <= -(0.5)) {
								return int (-(182.4286689419795));
							}
							else {
								return int (-(317.2507204610951));
							}
						}
						else if (b4 <= -(1.5)) {
							if (move <= 48.5) {
								return int (-(300.29801324503313));
							}
							else {
								return int (387.6190476190476);
							}
						}
						else if (b5 <= -(2.5)) {
							return int (-(245.625));
						}
						else {
							return int (-(614.5030674846626));
						}
					}
					else if (b4 <= -(0.5)) {
						if (player <= 0.5) {
							if (g1 <= -(1.5)) {
								return int (-(168.84868421052633));
							}
							else {
								return int (65.38403990024938);
							}
						}
						else if (b4 <= -(1.5)) {
							return int (277.4432624113475);
						}
						else {
							return int (127.06887328652624);
						}
					}
					else if (b3 <= 1.5) {
						if (b3 <= 0.5) {
							return int (2.3785494355114607);
						}
						else {
							return int (-(85.86147757255937));
						}
					}
					else if (player <= 0.5) {
						return int (-(351.79888268156424));
					}
					else {
						return int (-(174.2442996742671));
					}
				}
				else if (b3 <= 0.5) {
					if (sm <= -(0.5)) {
						if (b5 <= 3.5) {
							if (b4 <= 1.5) {
								if (move <= 46.5) {
									return int (-(307.08049535603715));
								}
								else {
									return int (54.48076923076923);
								}
							}
							else if (g6 <= -(4.5)) {
								return int (-(1120.6666666666667));
							}
							else {
								return int (-(440.87280701754383));
							}
						}
						else if (g1 <= -(4.0)) {
							if (b7 <= 4.5) {
								return int (-(1083.75));
							}
							else {
								return int (-(3710.0));
							}
						}
						else if (b7 <= 5.5) {
							return int (-(601.8846153846154));
						}
						else {
							return int (-(1204.857142857143));
						}
					}
					else if (b4 <= 1.5) {
						if (b3 <= -(1.5)) {
							if (move <= 50.0) {
								return int (94.68627450980392);
							}
							else {
								return int (-(625.8666666666667));
							}
						}
						else if (player <= 0.5) {
							return int (-(118.63095238095238));
						}
						else {
							return int (-(56.65162311955661));
						}
					}
					else if (player <= 0.5) {
						if (move <= 25.0) {
							return int (-(169.1172638436482));
						}
						else {
							return int (-(368.3284671532847));
						}
					}
					else if (g1 <= 0.5) {
						return int (-(192.1159420289855));
					}
					else {
						return int (50.54189944134078);
					}
				}
				else if (move <= 31.5) {
					if (sm <= -(0.5)) {
						if (b3 <= 1.5) {
							if (move <= 21.5) {
								return int (-(419.8));
							}
							else {
								return int (-(522.4520547945206));
							}
						}
						else if (g1 <= -(3.0)) {
							return int (-(357.0));
						}
						else {
							return int (-(647.2857142857143));
						}
					}
					else if (b3 <= 1.5) {
						if (b4 <= 1.5) {
							return int (-(252.97237569060775));
						}
						else {
							return int (-(335.0844327176781));
						}
					}
					else if (g1 <= -(1.5)) {
						return int (-(639.0175438596491));
					}
					else {
						return int (-(399.61007957559684));
					}
				}
				else if (b4 <= 1.5) {
					if (b3 <= 1.5) {
						if (sm <= -(0.5)) {
							return int (-(473.90625));
						}
						else {
							return int (-(276.7100977198697));
						}
					}
					else if (sm <= -(0.5)) {
						return int (-(660.8253012048193));
					}
					else {
						return int (-(497.50621118012424));
					}
				}
				else if (player <= 0.5) {
					if (move <= 47.0) {
						return int (-(699.4671968190855));
					}
					else {
						return int (-(968.5982142857143));
					}
				}
				else if (sm <= -(0.5)) {
					return int (-(713.5454545454545));
				}
				else {
					return int (-(453.6827309236948));
				}
			}
			else if (b4 <= 0.5) {
				if (move <= 55.5) {
					if (b3 <= -(1.5)) {
						if (g8 <= 5.5) {
							if (sm <= 1.5) {
								if (g6 <= 5.5) {
									return int (722.8631239935588);
								}
								else {
									return int (-(674.3333333333334));
								}
							}
							else if (b5 <= 4.5) {
								return int (1028.3333333333333);
							}
							else {
								return int (-(722.6));
							}
						}
						else if (move <= 51.5) {
							if (s0 <= -(2.5)) {
								return int (1104.0);
							}
							else {
								return int (482.04347826086956);
							}
						}
						else if (b7 <= 5.0) {
							return int (-(1519.0));
						}
						else {
							return int (-(3000.0));
						}
					}
					else if (sm <= 1.5) {
						if (b4 <= -(0.5)) {
							if (b5 <= -(2.5)) {
								return int (630.484375);
							}
							else {
								return int (433.83274021352315);
							}
						}
						else if (b3 <= -(0.5)) {
							return int (422.08264462809916);
						}
						else {
							return int (184.3191763191763);
						}
					}
					else if (b3 <= 0.5) {
						if (move <= 49.5) {
							return int (752.1974448315912);
						}
						else {
							return int (429.19310344827585);
						}
					}
					else if (b5 <= 0.5) {
						return int (567.5597826086956);
					}
					else {
						return int (335.8119469026549);
					}
				}
				else if (player <= 0.5) {
					if (b5 <= 0.5) {
						if (b3 <= 2.5) {
							if (b7 <= -(5.0)) {
								return int (850.0);
							}
							else {
								return int (-(235.35802469135803));
							}
						}
						else if (b5 <= -(4.5)) {
							return int (2400.0);
						}
						else {
							return int (242.11111111111111);
						}
					}
					else if (b4 <= -(1.5)) {
						if (b3 <= 2.5) {
							return int (-(172.16666666666666));
						}
						else {
							return int (-(1600.0));
						}
					}
					else if (b3 <= -(3.5)) {
						return int (-(3400.0));
					}
					else {
						return int (-(945.0217391304348));
					}
				}
				else if (b5 <= 1.5) {
					if (b3 <= 3.5) {
						if (s0 <= -(12.5)) {
							return int (108.44444444444444);
						}
						else {
							return int (655.8214285714286);
						}
					}
					else if (b3 <= 4.5) {
						return int (3690.0);
					}
					else {
						return int (885.0);
					}
				}
				else if (b3 <= -(3.5)) {
					return int (-(3400.0));
				}
				else if (b7 <= 1.0) {
					return int (597.875);
				}
				else {
					return int (-(328.94736842105266));
				}
			}
			else if (sm <= 1.5) {
				if (b3 <= 0.5) {
					if (move <= 55.5) {
						if (b3 <= -(0.5)) {
							if (b4 <= 1.5) {
								return int (350.0346385542169);
							}
							else {
								return int (152.08520179372198);
							}
						}
						else if (b4 <= 1.5) {
							return int (150.6396866840731);
						}
						else {
							return int (6.931531531531531);
						}
					}
					else if (b5 <= 1.5) {
						if (player <= 0.5) {
							return int (-(853.2142857142857));
						}
						else {
							return int (352.85714285714283);
						}
					}
					else if (g1 <= 1.5) {
						return int (-(1514.875));
					}
					else {
						return int (-(3060.0));
					}
				}
				else if (b4 <= 1.5) {
					if (b5 <= 5.5) {
						if (player <= 0.5) {
							return int (-(44.22265625));
						}
						else {
							return int (118.76076555023923);
						}
					}
					else if (move <= 46.0) {
						return int (139.33333333333334);
					}
					else {
						return int (-(817.125));
					}
				}
				else if (player <= 0.5) {
					if (g1 <= 3.5) {
						return int (-(267.5108359133127));
					}
					else {
						return int (-(853.6315789473684));
					}
				}
				else if (b3 <= 1.5) {
					return int (34.689189189189186);
				}
				else {
					return int (-(230.88));
				}
			}
			else if (b5 <= -(0.5)) {
				if (g1 <= -(3.5)) {
					if (g2 <= 0.5) {
						if (b3 <= 1.5) {
							return int (669.8333333333334);
						}
						else {
							return int (-(764.0));
						}
					}
					else if (b3 <= -(0.5)) {
						return int (-(1291.0));
					}
					else {
						return int (-(373.6666666666667));
					}
				}
				else if (b3 <= -(1.5)) {
					if (b4 <= 1.5) {
						return int (969.6470588235294);
					}
					else {
						return int (620.9464285714286);
					}
				}
				else if (g6 <= -(4.5)) {
					return int (-(3.588235294117647));
				}
				else {
					return int (527.285240464345);
				}
			}
			else if (move <= 51.5) {
				if (b3 <= 0.5) {
					if (sm <= 2.5) {
						return int (367.30194805194805);
					}
					else {
						return int (612.2574850299401);
					}
				}
				else if (b3 <= 2.5) {
					return int (256.8453453453453);
				}
				else {
					return int (16.074285714285715);
				}
			}
			else if (player <= 0.5) {
				if (move <= 54.5) {
					return int (-(145.2967032967033));
				}
				else {
					return int (-(719.2833333333333));
				}
			}
			else if (move <= 54.5) {
				return int (-(143.15384615384616));
			}
			else {
				return int (573.5483870967741);
			}
		}
		else if (sm <= 11.5) {
			if (sm <= 6.5) {
				if (move <= 55.5) {
					if (b5 <= -(0.5)) {
						if (b3 <= -(1.5)) {
							if (sm <= 4.5) {
								if (g1 <= -(2.5)) {
									return int (1438.695652173913);
								}
								else {
									return int (1081.654761904762);
								}
							}
							else if (move <= 49.5) {
								return int (1333.2345679012346);
							}
							else {
								return int (1763.2884615384614);
							}
						}
						else if (sm <= 4.5) {
							if (b4 <= -(1.5)) {
								return int (1008.376);
							}
							else {
								return int (765.9781659388647);
							}
						}
						else if (b4 <= -(1.5)) {
							return int (1214.2846441947565);
						}
						else {
							return int (977.6619718309859);
						}
					}
					else if (b4 <= 0.5) {
						if (move <= 53.5) {
							if (b3 <= 0.5) {
								return int (989.520202020202);
							}
							else {
								return int (763.4486486486486);
							}
						}
						else if (s0 <= 8.5) {
							return int (718.5);
						}
						else {
							return int (11.241379310344827);
						}
					}
					else if (move <= 49.5) {
						if (b3 <= 0.5) {
							return int (834.7117647058824);
						}
						else {
							return int (547.3703703703703);
						}
					}
					else if (b5 <= 3.5) {
						return int (497.37450199203187);
					}
					else {
						return int (20.785714285714285);
					}
				}
				else if (player <= 0.5) {
					if (b4 <= -(0.5)) {
						if (b5 <= 3.0) {
							if (b4 <= -(2.5)) {
								return int (-(187.69230769230768));
							}
							else {
								return int (577.2894736842105);
							}
						}
						else if (g6 <= -(1.5)) {
							return int (-(2200.0));
						}
						else {
							return int (-(538.3333333333334));
						}
					}
					else if (b5 <= 3.5) {
						if (s0 <= -(16.0)) {
							return int (1680.0);
						}
						else {
							return int (-(291.109756097561));
						}
					}
					else if (g6 <= 0.5) {
						return int (-(1008.6538461538462));
					}
					else {
						return int (-(357.7307692307692));
					}
				}
				else if (b4 <= 0.5) {
					if (g8 <= -(3.0)) {
						if (b3 <= -(1.5)) {
							return int (415.6666666666667);
						}
						else {
							return int (1623.25);
						}
					}
					else if (g6 <= 5.5) {
						return int (907.7333333333333);
					}
					else {
						return int (-(895.0));
					}
				}
				else if (g1 <= 1.5) {
					if (s0 <= 4.5) {
						return int (346.47058823529414);
					}
					else {
						return int (-(485.90909090909093));
					}
				}
				else if (b5 <= -(0.5)) {
					return int (1591.0);
				}
				else {
					return int (596.6);
				}
			}
			else if (b5 <= 1.5) {
				if (move <= 57.5) {
					if (b5 <= -(1.5)) {
						if (sm <= 8.5) {
							if (b4 <= 0.5) {
								return int (1491.8852459016393);
							}
							else {
								return int (1176.9333333333334);
							}
						}
						else if (b3 <= 4.5) {
							return int (1649.5502742230346);
						}
						else {
							return int (908.4545454545455);
						}
					}
					else if (sm <= 7.5) {
						if (move <= 53.5) {
							return int (1116.5576323987539);
						}
						else {
							return int (759.8305084745763);
						}
					}
					else if (move <= 55.5) {
						return int (1343.0644295302013);
					}
					else {
						return int (950.7551020408164);
					}
				}
				else if (player <= 0.5) {
					if (g1 <= -(2.5)) {
						if (b7 <= -(3.0)) {
							return int (2200.0);
						}
						else {
							return int (1406.75);
						}
					}
					else if (b5 <= -(2.5)) {
						return int (832.4545454545455);
					}
					else {
						return int (174.01333333333332);
					}
				}
				else if (b5 <= -(1.5)) {
					if (sm <= 10.5) {
						return int (3000.0);
					}
					else {
						return int (2111.0);
					}
				}
				else if (g8 <= 0.0) {
					return int (-(490.0));
				}
				else {
					return int (1815.0);
				}
			}
			else if (move <= 55.5) {
				if (b5 <= 3.5) {
					if (sm <= 7.5) {
						if (g1 <= 3.5) {
							return int (940.1933701657458);
						}
						else {
							return int (238.33333333333334);
						}
					}
					else if (move <= 51.5) {
						return int (1325.0070921985816);
					}
					else {
						return int (1030.7931034482758);
					}
				}
				else if (g1 <= -(1.5)) {
					if (b4 <= 1.5) {
						return int (-(1787.5));
					}
					else {
						return int (68.64285714285714);
					}
				}
				else if (b7 <= 3.5) {
					return int (938.8297101449275);
				}
				else {
					return int (435.1195652173913);
				}
			}
			else if (player <= 0.5) {
				if (b7 <= 4.5) {
					if (g6 <= 6.5) {
						return int (182.8641975308642);
					}
					else {
						return int (-(1052.0));
					}
				}
				else if (g1 <= 0.5) {
					return int (-(960.0));
				}
				else {
					return int (-(143.65));
				}
			}
			else if (g6 <= 2.5) {
				if (g8 <= 5.0) {
					return int (1287.625);
				}
				else {
					return int (-(47.5));
				}
			}
			else if (g8 <= -(3.0)) {
				return int (1143.0);
			}
			else {
				return int (76.70588235294117);
			}
		}
		else if (sm <= 18.5) {
			if (move <= 55.5) {
				if (b5 <= -(0.5)) {
					if (sm <= 14.5) {
						if (b5 <= -(1.5)) {
							if (b7 <= 0.5) {
								return int (2198.516587677725);
							}
							else {
								return int (1839.8863636363637);
							}
						}
						else if (move <= 53.5) {
							return int (1834.7532467532467);
						}
						else {
							return int (1333.2777777777778);
						}
					}
					else if (g2 <= 3.5) {
						if (move <= 49.5) {
							return int (2126.0793650793653);
						}
						else {
							return int (2513.3076923076924);
						}
					}
					else if (b7 <= -(1.5)) {
						return int (2945.0);
					}
					else {
						return int (1264.0);
					}
				}
				else if (sm <= 13.5) {
					if (b5 <= 4.5) {
						if (g1 <= 6.5) {
							return int (1538.0443786982248);
						}
						else {
							return int (2955.5);
						}
					}
					else if (g6 <= 0.5) {
						return int (342.5833333333333);
					}
					else {
						return int (1073.2702702702702);
					}
				}
				else if (g8 <= 5.5) {
					if (b7 <= 1.5) {
						return int (2083.1462686567165);
					}
					else {
						return int (1737.0369003690037);
					}
				}
				else if (g1 <= 3.5) {
					return int (781.1481481481482);
				}
				else {
					return int (1627.125);
				}
			}
			else if (player <= 0.5) {
				if (b7 <= 3.5) {
					if (sm <= 14.5) {
						if (s0 <= 10.0) {
							return int (1127.9101123595506);
						}
						else {
							return int (736.9574468085107);
						}
					}
					else if (move <= 57.5) {
						return int (1542.7941176470588);
					}
					else {
						return int (1025.2921348314608);
					}
				}
				else if (b5 <= 7.5) {
					if (sm <= 16.5) {
						return int (263.7236842105263);
					}
					else {
						return int (816.0869565217391);
					}
				}
				else if (b7 <= 7.0) {
					return int (-(328.57142857142856));
				}
				else {
					return int (-(1700.0));
				}
			}
			else if (b5 <= 5.5) {
				if (b7 <= -(0.5)) {
					if (b7 <= -(3.5)) {
						return int (2115.173076923077);
					}
					else {
						return int (2496.5686274509803);
					}
				}
				else if (sm <= 14.5) {
					return int (1537.9583333333333);
				}
				else {
					return int (2155.3555555555554);
				}
			}
			else if (b7 <= 5.5) {
				if (b7 <= 1.0) {
					return int (-(100.0));
				}
				else {
					return int (600.0);
				}
			}
			else if (g2 <= 1.0) {
				return int (-(600.0));
			}
			else {
				return int (-(690.0));
			}
		}
		else if (b5 <= 4.5) {
			if (move <= 55.5) {
				if (sm <= 20.5) {
					if (b7 <= 5.5) {
						if (b7 <= -(2.5)) {
							return int (2793.323529411765);
						}
						else {
							return int (2290.635714285714);
						}
					}
					else if (g2 <= 1.0) {
						return int (333.25);
					}
					else {
						return int (1890.0);
					}
				}
				else if (b3 <= 4.5) {
					if (b7 <= 7.5) {
						return int (2657.451219512195);
					}
					else {
						return int (997.0);
					}
				}
				else if (b4 <= 3.5) {
					return int (3307.7868852459014);
				}
				else {
					return int (2358.3333333333335);
				}
			}
			else if (player <= 0.5) {
				if (sm <= 25.5) {
					if (b7 <= 7.0) {
						return int (1738.2181818181818);
					}
					else {
						return int (-(1800.0));
					}
				}
				else if (g6 <= 4.5) {
					return int (2163.383333333333);
				}
				else {
					return int (2578.6716417910447);
				}
			}
			else if (sm <= 21.5) {
				if (g6 <= 5.5) {
					return int (2307.5853658536585);
				}
				else {
					return int (2953.3333333333335);
				}
			}
			else if (move <= 56.5) {
				return int (4800.0);
			}
			else {
				return int (2940.014492753623);
			}
		}
		else if (b3 <= 5.5) {
			if (b3 <= 2.5) {
				if (b4 <= 1.5) {
					if (g8 <= 4.5) {
						return int (2248.5833333333335);
					}
					else {
						return int (568.75);
					}
				}
				else if (move <= 53.0) {
					return int (2259.5);
				}
				else {
					return int (576.4545454545455);
				}
			}
			else if (b5 <= 7.5) {
				if (player <= 0.5) {
					return int (1689.0142857142857);
				}
				else {
					return int (2430.1);
				}
			}
			else if (sm <= 33.0) {
				return int (435.0);
			}
			else {
				return int (2095.0);
			}
		}
		else if (g1 <= 4.5) {
			if (g8 <= -(1.0)) {
				return int (1490.0);
			}
			else if (sm <= 27.5) {
				return int (2751.0);
			}
			else {
				return int (3251.0);
			}
		}
		else {
			return int (2076.0);
		}
	});}
});

//# sourceMappingURL=eval_functions.map