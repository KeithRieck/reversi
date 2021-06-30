// Transcrypt'ed from Python, 2021-06-29 21:29:00
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
		return str (hash (obj));
	}
};
export var GameTask =  __class__ ('GameTask', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, gameobject, func, time_delay, repeat_count) {
		if (typeof time_delay == 'undefined' || (time_delay != null && time_delay.hasOwnProperty ("__kwargtrans__"))) {;
			var time_delay = 0;
		};
		if (typeof repeat_count == 'undefined' || (repeat_count != null && repeat_count.hasOwnProperty ("__kwargtrans__"))) {;
			var repeat_count = 0;
		};
		self.game = game;
		self.gameobject = gameobject;
		self.func = func;
		self.time_delay = time_delay;
		self.repeat_count = repeat_count;
		self.schedule_time = self.game.get_time () + self.time_delay;
	});},
	get reschedule () {return __get__ (this, function (self) {
		self.schedule_time = self.game.get_time () + self.time_delay;
		self.repeat_count = self.repeat_count - 1;
	});},
	get is_due () {return __get__ (this, function (self) {
		return self.game.get_time () >= self.schedule_time;
	});},
	get run () {return __get__ (this, function (self) {
		if (self.func !== null) {
			self.func ();
		}
	});}
});
export var GameObject =  __class__ ('GameObject', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game) {
		self.game = game;
		self.enabled = true;
		self.py_name = null;
		self._sched_queue = [];
		self.x = 0;
		self.y = 0;
	});},
	get schedule () {return __get__ (this, function (self, func, time_delay, repeat_count) {
		if (typeof time_delay == 'undefined' || (time_delay != null && time_delay.hasOwnProperty ("__kwargtrans__"))) {;
			var time_delay = 0;
		};
		if (typeof repeat_count == 'undefined' || (repeat_count != null && repeat_count.hasOwnProperty ("__kwargtrans__"))) {;
			var repeat_count = 0;
		};
		if (isinstance (func, GameTask)) {
			self._sched_queue.append (func);
		}
		else {
			self._sched_queue.append (GameTask (self.game, self, func, time_delay, repeat_count));
		}
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		self._run_schedule ();
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		// pass;
	});},
	get _run_schedule () {return __get__ (this, function (self) {
		if (len (self._sched_queue) == 0) {
			return ;
		}
		var new_queue = [];
		var run_queue = [];
		for (var task of self._sched_queue) {
			if (task.is_due ()) {
				run_queue.append (task);
				if (task.repeat_count > 1) {
					task.reschedule ();
					new_queue.append (task);
				}
			}
			else {
				new_queue.append (task);
			}
		}
		self._sched_queue = new_queue;
		for (var task of run_queue) {
			task.run ();
		}
	});}
});
export var GameImage =  __class__ ('GameImage', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, js_image, width, height, sx, sy, ox, oy, py_name) {
		if (typeof width == 'undefined' || (width != null && width.hasOwnProperty ("__kwargtrans__"))) {;
			var width = -(1);
		};
		if (typeof height == 'undefined' || (height != null && height.hasOwnProperty ("__kwargtrans__"))) {;
			var height = -(1);
		};
		if (typeof sx == 'undefined' || (sx != null && sx.hasOwnProperty ("__kwargtrans__"))) {;
			var sx = 0;
		};
		if (typeof sy == 'undefined' || (sy != null && sy.hasOwnProperty ("__kwargtrans__"))) {;
			var sy = 0;
		};
		if (typeof ox == 'undefined' || (ox != null && ox.hasOwnProperty ("__kwargtrans__"))) {;
			var ox = 0;
		};
		if (typeof oy == 'undefined' || (oy != null && oy.hasOwnProperty ("__kwargtrans__"))) {;
			var oy = 0;
		};
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.js_image = js_image;
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.sx = sx;
		self.sy = sy;
		self.originX = ox;
		self.originY = oy;
		self.angle = 0;
		self.global_composition_operation = 'source-over';
		if (width < 0 || height < 0) {
			self.width = js_image.width;
			self.height = js_image.height;
		}
		else {
			self.width = width;
			self.height = height;
		}
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		GameObject.py_update (self, delta_time);
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		GameObject.draw (self, ctx);
		ctx.save ();
		ctx.globalCompositeOperation = self.global_composition_operation;
		if (self.angle != 0) {
			ctx.translate (self.x, self.y);
			ctx.rotate ((self.angle * Math.PI) / 180.0);
			ctx.translate (-(1) * self.originX, -(1) * self.originY);
			ctx.drawImage (self.js_image, self.sx, self.sy, self.width, self.height, 0, 0, self.width, self.height);
		}
		else {
			ctx.drawImage (self.js_image, self.sx, self.sy, self.width, self.height, self.x - self.originX, self.y - self.originY, self.width, self.height);
		}
		ctx.restore ();
	});}
});
export var SpriteSheet =  __class__ ('SpriteSheet', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, py_name) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		self.game = game;
		self._frames = dict ({});
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
	});},
	get add_image () {return __get__ (this, function (self, py_name, js_image, width, height, sx, sy) {
		var game_image = GameImage (self.game, js_image, width, height, sx, sy);
		game_image.py_name = py_name;
		self._frames [py_name] = game_image;
	});},
	get frames () {return __get__ (this, function (self, key_list) {
		if (typeof key_list == 'undefined' || (key_list != null && key_list.hasOwnProperty ("__kwargtrans__"))) {;
			var key_list = null;
		};
		if (key_list === null) {
			var key_list = sorted (self._frames.py_keys ());
		}
		return (function () {
			var __accu0__ = [];
			for (var k of key_list) {
				__accu0__.append (self._frames [k]);
			}
			return __accu0__;
		}) ();
	});},
	get __len__ () {return __get__ (this, function (self) {
		return len (self._frames);
	});},
	get __getitem__ () {return __get__ (this, function (self, py_name) {
		return self._frames [py_name];
	});},
	get __setitem__ () {return __get__ (this, function (self, py_name, game_image) {
		self.scenes [py_name] = game_image;
	});}
});
export var Animation =  __class__ ('Animation', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, frame_list, mspf, rpt, py_name) {
		if (typeof frame_list == 'undefined' || (frame_list != null && frame_list.hasOwnProperty ("__kwargtrans__"))) {;
			var frame_list = [];
		};
		if (typeof mspf == 'undefined' || (mspf != null && mspf.hasOwnProperty ("__kwargtrans__"))) {;
			var mspf = 100;
		};
		if (typeof rpt == 'undefined' || (rpt != null && rpt.hasOwnProperty ("__kwargtrans__"))) {;
			var rpt = -(1);
		};
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		GameObject.__init__ (self, game);
		self.msPerFrame = mspf;
		self.repeat = rpt;
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.x = 0;
		self.y = 0;
		self.angle = 0;
		self._time_in_frame = 0;
		self._repeat_count = 0;
		self._running = false;
		self._current_frame = 0;
		self.width = 0;
		self.height = 0;
		self._frame = [];
		self.set_frame_list (frame_list);
	});},
	get set_frame_list () {return __get__ (this, function (self, frame_list) {
		self._frame = frame_list;
		for (var game_image of self._frame) {
			if (game_image.width > self.width) {
				self.width = game_image.width;
			}
			if (game_image.height > self.height) {
				self.height = game_image.height;
			}
		}
	});},
	get _get_originX () {return __get__ (this, function (self) {
		if (len (self._frame) == 0) {
			return 0;
		}
		else {
			return self._frame [0].originX;
		}
	});},
	get _set_originX () {return __get__ (this, function (self, value) {
		for (var game_image of self._frame) {
			game_image.originX = value;
		}
	});},
	get _get_originY () {return __get__ (this, function (self) {
		if (len (self._frame) == 0) {
			return 0;
		}
		else {
			return self._frame [0].originY;
		}
	});},
	get _set_originY () {return __get__ (this, function (self, value) {
		for (var game_image of self._frame) {
			game_image.originY = value;
		}
	});},
	get start () {return __get__ (this, function (self) {
		self._time_in_frame = 0;
		self._repeat_count = 0;
		self._running = true;
	});},
	get stop () {return __get__ (this, function (self) {
		self._time_in_frame = 0;
		self._repeat_count = 0;
		self._running = false;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		GameObject.py_update (self, delta_time);
		self._time_in_frame = self._time_in_frame + delta_time;
		if (self._running && self._time_in_frame > self.msPerFrame) {
			self._time_in_frame = 0;
			self._current_frame = self._current_frame + 1;
			if (self._current_frame >= len (self._frame)) {
				self._repeat_count = self._repeat_count + 1;
				if (self.repeat > 0 && self._repeat_count >= self.repeat) {
					self._running = false;
				}
				else {
					self._current_frame = 0;
				}
			}
		}
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		GameObject.draw (self, ctx);
		var game_image = self._frame [self._current_frame];
		game_image.x = self.x;
		game_image.y = self.y;
		game_image.angle = self.angle;
		game_image.draw (ctx);
	});}
});
Object.defineProperty (Animation, 'originY', property.call (Animation, Animation._get_originY, Animation._set_originY));
Object.defineProperty (Animation, 'originX', property.call (Animation, Animation._get_originX, Animation._set_originX));;
export var Button =  __class__ ('Button', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, x, y, width, height, button_text, py_name) {
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
		self.buttonText = button_text;
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
		if (self._in_rect (event.mouseX, event.mouseY) && self.enabled) {
			self._clicked = true;
		}
	});},
	get handle_mouseup () {return __get__ (this, function (self, event) {
		if (self._clicked && self.callback !== null && self._in_rect (event.mouseX, event.mouseY) && self.enabled) {
			self.callback ();
		}
		self._clicked = false;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		GameObject.py_update (self, delta_time);
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		GameObject.draw (self, ctx);
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
		self.dx = 0;
		self.dy = 0;
		self.mass = 0;
		self.bounce = 0;
		self.num = 0;
		self.at_rest = false;
	});},
	get __repr__ () {return __get__ (this, function (self) {
		return __mod__ ("Sprite(%s, %r,%r, '%s')", tuple ([self.game, self.width, self.height, self.py_name]));
	});},
	get in_rect () {return __get__ (this, function (self, x, y) {
		return !(x < self.x || x > self.x + self.width || y < self.y || y > self.y + self.height);
	});},
	get collides_with () {return __get__ (this, function (self, sprite) {
		return !(self.x + self.width < sprite.x || self.x > sprite.x + sprite.width || self.y + self.height < sprite.y || self.y > sprite.y + sprite.height);
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		GameObject.py_update (self, delta_time);
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		GameObject.draw (self, ctx);
	});}
});
export var ImageSprite =  __class__ ('ImageSprite', [Sprite], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, game_image, w, h, py_name) {
		if (typeof w == 'undefined' || (w != null && w.hasOwnProperty ("__kwargtrans__"))) {;
			var w = -(1);
		};
		if (typeof h == 'undefined' || (h != null && h.hasOwnProperty ("__kwargtrans__"))) {;
			var h = -(1);
		};
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		var width = w;
		var height = h;
		if (width < 0 || height < 0) {
			var width = game_image.width;
			var height = game_image.height;
		}
		Sprite.__init__ (self, game, width, height, py_name);
		self.game_image = game_image;
		self.animation = null;
	});},
	get set_animation () {return __get__ (this, function (self, animation) {
		self.animation = animation;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		Sprite.py_update (self, delta_time);
		if (self.animation !== null) {
			self.animation.py_update (delta_time);
		}
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		Sprite.draw (self, ctx);
		if (self.animation !== null) {
			self.animation.x = self.x;
			self.animation.y = self.y;
			self.animation.angle = self.angle;
			self.animation.draw (ctx);
		}
		else {
			self.game_image.x = self.x;
			self.game_image.y = self.y;
			self.game_image.angle = self.angle;
			self.game_image.draw (ctx);
		}
	});}
});
export var GamePhysics =  __class__ ('GamePhysics', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, c_left, c_right, c_up, c_down) {
		if (typeof c_left == 'undefined' || (c_left != null && c_left.hasOwnProperty ("__kwargtrans__"))) {;
			var c_left = false;
		};
		if (typeof c_right == 'undefined' || (c_right != null && c_right.hasOwnProperty ("__kwargtrans__"))) {;
			var c_right = false;
		};
		if (typeof c_up == 'undefined' || (c_up != null && c_up.hasOwnProperty ("__kwargtrans__"))) {;
			var c_up = false;
		};
		if (typeof c_down == 'undefined' || (c_down != null && c_down.hasOwnProperty ("__kwargtrans__"))) {;
			var c_down = false;
		};
		self.game = game;
		self.collide_left = c_left;
		self.collide_right = c_right;
		self.collide_up = c_up;
		self.collide_down = c_down;
		self.children = [];
	});},
	get __len__ () {return __get__ (this, function (self) {
		return len (self.children);
	});},
	get __getitem__ () {return __get__ (this, function (self, key) {
		return self.children [key];
	});},
	get __setitem__ () {return __get__ (this, function (self, key, sprite) {
		self.children [key] = sprite;
	});},
	get __contains__ () {return __get__ (this, function (self, sprite) {
		return __in__ (sprite, self.children);
	});},
	get __iter__ () {return __get__ (this, function* (self) {
		yield* self.children});},
	[Symbol.iterator] () {return this.__iter__ ()},
	get _calc_angle () {return __get__ (this, function (self, sprite1, sprite2) {
		if (sprite1.y == sprite2.y) {
			return (sprite1.x < sprite2.x ? 0.5 * Math.PI : -(0.5) * Math.PI);
		}
		var angle = Math.atan ((sprite1.x - sprite2.x) / (sprite1.y - sprite2.y));
		if (sprite2.y < sprite1.y) {
			var angle = angle + Math.PI;
		}
		if (angle > Math.PI) {
			var angle = angle - 2 * Math.PI;
		}
		return angle;
	});},
	get append () {return __get__ (this, function (self, sprite) {
		sprite.num = len (self.children);
		self.children.append (sprite);
		return sprite;
	});},
	get collide () {return __get__ (this, function (self, sprite1, sprite2, angle) {
		// pass;
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		for (var sprite1 of self.children) {
			for (var sprite2 of self.children) {
				if (sprite1.num <= sprite2.num) {
					continue;
				}
				if (sprite1.collides_with (sprite2)) {
					var angle = self._calc_angle (sprite1, sprite2);
					self.collide (sprite1, sprite2, angle);
				}
			}
			if (self.collide_left && sprite1.x < 0) {
				self.collide (sprite1, 'LEFT', 0);
			}
			else if (self.collide_right && sprite1.x + sprite1.width >= self.game.canvas.width) {
				self.collide (sprite1, 'RIGHT', 0);
			}
			else if (self.collide_up && sprite1.y < 0) {
				self.collide (sprite1, 'UP', 0);
			}
			else if (self.collide_down && sprite1.y + sprite1.height >= self.game.canvas.height) {
				self.collide (sprite1, 'DOWN', 0);
			}
		}
		// pass;
	});}
});
export var Scene =  __class__ ('Scene', [GameObject], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, game, py_name, physics) {
		if (typeof py_name == 'undefined' || (py_name != null && py_name.hasOwnProperty ("__kwargtrans__"))) {;
			var py_name = null;
		};
		if (typeof physics == 'undefined' || (physics != null && physics.hasOwnProperty ("__kwargtrans__"))) {;
			var physics = null;
		};
		GameObject.__init__ (self, game);
		self.py_name = (py_name !== null ? py_name : _hash_name (self));
		self.children = [];
		self.physics = physics;
		self.background_color = null;
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
		gameobject.scene = self;
		return gameobject;
	});},
	get extend () {return __get__ (this, function (self, container) {
		for (var gameobject of container) {
			self.children.append (gameobject);
		}
	});},
	get remove () {return __get__ (this, function (self, gameobject) {
		gameobject.scene = null;
		self.children.remove (gameobject);
	});},
	get py_update () {return __get__ (this, function (self, delta_time) {
		GameObject.py_update (self, delta_time);
		if (self.physics !== null) {
			self.physics.py_update (delta_time);
		}
		for (var gameobject of self.children) {
			gameobject.py_update (delta_time);
		}
	});},
	get _clear_screen () {return __get__ (this, function (self, ctx) {
		ctx.save ();
		if (self.background_color !== null) {
			ctx.globalCompositeOperation = 'copy';
			ctx.fillStyle = self.background_color;
			ctx.fillRect (0, 0, self.game.canvas.width, self.game.canvas.height);
		}
		else {
			ctx.globalCompositeOperation = 'destination-over';
			ctx.clearRect (0, 0, self.game.canvas.width, self.game.canvas.height);
		}
		ctx.restore ();
	});},
	get _draw_children () {return __get__ (this, function (self, ctx) {
		for (var gameobject of self.children) {
			gameobject.draw (ctx);
		}
	});},
	get draw () {return __get__ (this, function (self, ctx) {
		GameObject.draw (self, ctx);
		self._clear_screen (ctx);
		self._draw_children (ctx);
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
		if (event.mouseX) {
			return tuple ([event.mouseX, event.mouseY]);
		}
		if (event.clientX) {
			event.mouseX = event.clientX - self.canvas.offsetLeft;
			event.mouseY = event.clientY - self.canvas.offsetTop;
			return tuple ([event.mouseX, event.mouseY]);
		}
		if (event.layerX) {
			event.mouseX = event.layerX;
			event.mouseY = event.layerY;
			return tuple ([event.mouseX, event.mouseY]);
		}
		event.mouseX = event.offsetX;
		event.mouseY = event.offsetY;
		return tuple ([event.mouseX, event.mouseY]);
	});},
	get __load_json () {return __get__ (this, function (self, json_url) {
		var xhr = new XMLHttpRequest ();
		xhr.open ('GET', json_url, false);
		xhr.send ();
		if (xhr.status != 200) {
			console.log ('unable to load {}'.format (json_url));
			return null;
		}
		return JSON.parse (xhr.responseText);
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
	get load_image () {return __get__ (this, function (self, image_id) {
		var js_image = document.getElementById (image_id);
		return GameImage (self, js_image);
	});},
	get load_audio () {return __get__ (this, function (self, audio_id) {
		return document.getElementById (audio_id);
	});},
	get load_spritesheet () {return __get__ (this, function (self, json_url, image_id) {
		var js_image = document.getElementById (image_id);
		var json_data = self.__load_json (json_url);
		if (json_data === null) {
			return null;
		}
		var spritesheet = SpriteSheet (self);
		for (var f of json_data ['frames']) {
			spritesheet.add_image (f.filename, js_image, f.frame.w, f.frame.h, f.frame.x, f.frame.y);
		}
		return spritesheet;
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
		self._prev_time = self.get_time ();
	});}
});

//# sourceMappingURL=bedlam.map