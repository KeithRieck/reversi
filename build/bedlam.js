// Transcrypt'ed from Python, 2020-05-03 15:34:42
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'bedlam';
export var GameObject =  __class__ ('GameObject', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game) {
		self.game = game;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		// pass;
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		// pass;
	});}
});
export var Sprite =  __class__ ('Sprite', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, width, height, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.x = 0;
		self.y = 0;
		self.width = width;
		self.height = height;
		self.py_name = (py_name !== null ? py_name : str (self));
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Sprite(%r, %r, '%s')", tuple ([self.width, self.height, self.py_name]));
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
		self.children = [];
		self.py_name = (py_name !== null ? py_name : str (self));
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Scene('%s')", self.py_name);
	});},
	get __len__ () {return __get__ (this, function (self) {
		return len (self.children);
	});},
	get __getitem__ () {return __get__ (this, function (self, n) {
		return self.children [n];
	});},
	get __setitem__ () {return __get__ (this, function (self, n, sprite) {
		self.children [n] = sprite;
	});},
	get __handle_mousedown () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get __handle_mouseup () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get __handle_mousemove () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get __handle_keydown () {return __get__ (this, function (self, event) {
		// pass;
	});},
	get append () {return __get__ (this, function (self, sprite) {
		self.children.append (sprite);
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		for (var sprite of self.children) {
			sprite.py_update (delta_time);
		}
	});},
	get __clear_screen () {return __get__ (this, function (self, ctx) {
		ctx.globalCompositeOperation = 'destination-over';
		ctx.clearRect (0, 0, self.game.canvas.width, self.game.canvas.height);
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		self.__clear_screen (ctx);
		for (var sprite of self.children) {
			sprite.draw (ctx);
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
		self.py_name = (py_name !== null ? py_name : str (self));
		self.loop_time = loop_time;
		self.canvasFrame = document.getElementById ('canvas_frame');
		self.canvas = document.getElementById ('canvas');
		self.prev_time = self.get_time ();
		self.scenes = dict ({});
		self.currentScene = null;
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
	get __handle_mousedown () {return __get__ (this, function (self, event) {
		if (self.currentScene !== null) {
			self.currentScene.__handle_mousedown (event);
		}
	});},
	get __handle_mouseup () {return __get__ (this, function (self, event) {
		if (self.currentScene !== null) {
			self.currentScene.__handle_mouseup (event);
		}
	});},
	get __handle_mousemove () {return __get__ (this, function (self, event) {
		if (self.currentScene !== null) {
			self.currentScene.__handle_mousemove (event);
		}
	});},
	get __handle_keydown () {return __get__ (this, function (self, event) {
		if (self.currentScene !== null) {
			self.currentScene.__handle_keydown (event);
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
		window.setInterval (self.__game_loop, self.loop_time);
		window.addEventListener ('mousedown', self.__handle_mousedown, false);
		window.addEventListener ('mouseup', self.__handle_mouseup, false);
		window.addEventListener ('mousemove', self.__handle_mousemove, false);
		window.addEventListener ('keydown', self.__handle_keydown, false);
	});},
	get __game_loop () {return __get__ (this, function (self) {
		var ctx = self.__get_context ();
		var current_time = self.get_time ();
		var delta_time = current_time - self.prev_time;
		self.py_update (delta_time);
		self.draw (ctx);
		self.prev_time = current_time;
	});}
});

//# sourceMappingURL=bedlam.map