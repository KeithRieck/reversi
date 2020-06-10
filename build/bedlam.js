// Transcrypt'ed from Python, 2020-06-09 21:22:33
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'bedlam';
export var _in_browser = function () {
	return document != 0;
};
export var _hash_name = function (obj) {
	if (_in_browser ()) {
		return str (obj);
	}
	else {
		return hash (obj);
	}
};
export var GameObject =  __class__ ('GameObject', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game) {
		self.game = game;
		self.enabled = true;
		self.py_name = null;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		// pass;
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		// pass;
	});}
});
export var Button =  __class__ ('Button', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, x, y, width, height, buttonText, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.x = x;
		self.y = y;
		self.width = width;
		self.height = height;
		self.pad = 5;
		self.buttonText = buttonText;
		self.font = '18pt sans-serif';
		self.fillStyle = 'white';
		self.textStyle = 'black';
		self.strokeStyle = 'black';
		self.disabledStyle = 'gray';
		self.lineWidth = 2;
		self.callback = null;
		self._clicked = false;
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Button(%s,%r,%r, %r,%r, '%s', '%s')", tuple ([self.game, self.x, self.y, self.width, self.height, self.buttonText, self.py_name]));
	});},
	get _in_rect () {return __get__ (this, function (self, x, y) {
		return !(x < self.x || x > self.x + self.width || y < self.y || y > self.y + self.height);
	});},
	get handle_mousedown () {return __get__ (this, function (self, event) {
		if (self._in_rect (event.x, event.y) && self.enabled) {
			self._clicked = true;
		}
	});},
	get handle_mouseup () {return __get__ (this, function (self, event) {
		if (self._clicked && self.callback !== null && self._in_rect (event.x, event.y) && self.enabled) {
			self.callback ();
		}
		self._clicked = false;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		// pass;
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		ctx.save ();
		ctx.globalCompositeOperation = 'source-over';
		ctx.beginPath ();
		ctx.fillStyle = (!(self._clicked) ? self.fillStyle : self.textStyle);
		ctx.strokeStyle = (self.enabled ? self.strokeStyle : self.disabledStyle);
		ctx.lineWidth = self.lineWidth;
		ctx.rect (self.x, self.y, self.width, self.height);
		ctx.stroke ();
		ctx.fillRect (self.x, self.y, self.width, self.height);
		ctx.font = self.font;
		ctx.fillStyle = (!(self._clicked) ? self.textStyle : self.fillStyle);
		ctx.fillStyle = (self.enabled ? ctx.fillStyle : self.disabledStyle);
		ctx.fillText (self.buttonText, self.x + self.pad, (self.y + self.height) - self.pad);
		ctx.restore ();
	});}
});
export var Sprite =  __class__ ('Sprite', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, width, height, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.x = 0;
		self.y = 0;
		self.width = width;
		self.height = height;
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Sprite(%s, %r,%r, '%s')", tuple ([self.game, self.width, self.height, self.py_name]));
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		// pass;
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		// pass;
	});}
});
export var Scene =  __class__ ('Scene', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.children = [];
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Scene(%s, '%s')", tuple ([self.game, self.py_name]));
	});},
	get __len__ () {return __get__ (this, function (self) {
		return len (self.children);
	});},
	get __getitem__ () {return __get__ (this, function (self, key) {
		return self.children [key];
	});},
	get __setitem__ () {return __get__ (this, function (self, key, gameobject) {
		self.children [key] = gameobject;
	});},
	get __contains__ () {return __get__ (this, function (self, gameobject) {
		return __in__ (gameobject, self.children);
	});},
	get __iter__ () {return __get__ (this, function* (self) {
		yield* self.children});},
	[Symbol.iterator] () {return this.__iter__ ()},
	get handle_mousedown () {return __get__ (this, function (self, event) {
		for (var button of (function () {
			var __accu0__ = [];
			for (var gameobject of self.children) {
				if (isinstance (gameobject, Button)) {
					__accu0__.append (gameobject);
				}
			}
			return py_iter (__accu0__);
		}) ()) {
			button.handle_mousedown (event);
		}
	});},
	get handle_mouseup () {return __get__ (this, function (self, event) {
		for (var button of (function () {
			var __accu0__ = [];
			for (var gameobject of self.children) {
				if (isinstance (gameobject, Button)) {
					__accu0__.append (gameobject);
				}
			}
			return py_iter (__accu0__);
		}) ()) {
			button.handle_mouseup (event);
		}
	});},
	get handle_mousemove () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get handle_keydown () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get append () {return __get__ (this, function (self, gameobject) {
		self.children.append (gameobject);
		return gameobject;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		for (var gameobject of self.children) {
			gameobject.py_update (delta_time);
		}
	});},
	get _clear_screen () {return __get__ (this, function (self, ctx) {
		ctx.save ();
		ctx.globalCompositeOperation = 'destination-over';
		ctx.clearRect (0, 0, self.game.canvas.width, self.game.canvas.height);
		ctx.restore ();
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		self._clear_screen (ctx);
		for (var gameobject of self.children) {
			gameobject.draw (ctx);
		}
	});}
});
export var Game =  __class__ ('Game', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, py_name, loop_time) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		if (typeof loop_time == 'undefined' || (loop_time != null && loop_time.hasOwnProperty ("__kwargtrans__"))) {;
			var loop_time = 20;
		};
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		if (_in_browser ()) {
			self.canvasFrame = document.getElementById ('canvas_frame');
			self.canvas = document.getElementById ('canvas');
			self._prev_time = self.get_time ();
			self.__get_context ().globalCompositeOperation = 'source-over';
		}
		else {
			self.canvasFrame = null;
			self.canvas = null;
		}
		self.scenes = dict ({});
		self.currentScene = null;
		self._loop_time = loop_time;
	});},
	get __get_context () {return __get__ (this, function (self) {
		return self.canvas.getContext ('2d');
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Game('%s')", self.py_name);
	});},
	get __len__ () {return __get__ (this, function (self) {
		return len (self.scenes);
	});},
	get __getitem__ () {return __get__ (this, function (self, py_name) {
		return self.scenes [py_name];
	});},
	get __setitem__ () {return __get__ (this, function (self, py_name, scene) {
		self.scenes [py_name] = scene;
		if (self.currentScene === null) {
			self.currentScene = scene;
		}
	});},
	get _preprocess_event () {return __get__ (this, function (self, event) {
		if (event.x) {
			return tuple ([event.x, event.y]);
		}
		if (event.layerX) {
			event.x = event.layerX;
			event.y = event.layerY;
			return tuple ([event.x, event.y]);
		}
		event.x = event.offsetX;
		event.y = event.offsetY;
		return tuple ([event.x, event.y]);
	});},
	get handle_mousedown () {return __get__ (this, function (self, event) {
		self._preprocess_event (event);
		if (self.currentScene !== null) {
			self.currentScene.handle_mousedown (event);
		}
	});},
	get handle_mouseup () {return __get__ (this, function (self, event) {
		self._preprocess_event (event);
		if (self.currentScene !== null) {
			self.currentScene.handle_mouseup (event);
		}
	});},
	get handle_mousemove () {return __get__ (this, function (self, event) {
		self._preprocess_event (event);
		if (self.currentScene !== null) {
			self.currentScene.handle_mousemove (event);
		}
	});},
	get handle_keydown () {return __get__ (this, function (self, event) {
		if (self.currentScene !== null) {
			self.currentScene.handle_keydown (event);
		}
	});},
	get append () {return __get__ (this, function (self, scene) {
		self.scenes [scene.py_name] = scene;
		if (self.currentScene === null) {
			self.currentScene = scene;
		}
	});},
	get set_current_scene () {return __get__ (this, function (self, py_name) {
		self.currentScene = self.scenes [py_name];
	});},
	get get_time () {return __get__ (this, function (self) {
		return Date.now ();
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		if (self.currentScene !== null) {
			self.currentScene.py_update (delta_time);
		}
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		if (self.currentScene !== null) {
			self.currentScene.draw (ctx);
		}
	});},
	get start () {return __get__ (this, function (self) {
		window.setInterval (self.__game_loop, self._loop_time);
		window.addEventListener ('mousedown', self.handle_mousedown, false);
		window.addEventListener ('mouseup', self.handle_mouseup, false);
		window.addEventListener ('mousemove', self.handle_mousemove, false);
		window.addEventListener ('keydown', self.handle_keydown, false);
		window.addEventListener ('touchstart', self.handle_mousedown, false);
		window.addEventListener ('touchend', self.handle_mouseup, false);
		window.addEventListener ('touchmove', self.handle_mousemove, false);
	});},
	get __game_loop () {return __get__ (this, function (self) {
		var ctx = self.__get_context ();
		var current_time = self.get_time ();
		var delta_time = current_time - self._prev_time;
		self.py_update (delta_time);
		self.draw (ctx);
		self._prev_time = current_time;
	});}
});

//# sourceMappingURL=bedlam.map