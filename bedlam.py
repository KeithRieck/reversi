# Bedlam is a trivial game framework.
# It is based, very loosely, on Phaser (see https://phaser.io).
# Copyright (c) 2020,2021 Keith Rieck


# __pragma__('skip')
from typing import Optional, List, Dict

document = window = Math = Date = console = XMLHttpRequest = JSON = 0  # Prevent complaints by optional static checker


# __pragma__('noskip')

# __pragma__('noalias', 'clear')

def _in_browser() -> bool:
    return document != 0


def _hash_name(obj) -> str:
    if _in_browser():
        return str(obj)
    else:
        return str(hash(obj))


class GameTask:
    """
    Task that a GameObject may execute during its update cycle.
    Every GameObject has a queue in which tasks can be scheduled.
    """

    def __init__(self, game, gameobject, func, time_delay=0, repeat_count=0):
        self.game = game
        self.gameobject = gameobject
        self.func = func
        self.time_delay = time_delay
        self.repeat_count = repeat_count
        self.schedule_time = self.game.get_time() + self.time_delay

    def reschedule(self):
        self.schedule_time = self.game.get_time() + self.time_delay
        self.repeat_count = self.repeat_count - 1

    def is_due(self):
        return self.game.get_time() >= self.schedule_time

    def run(self):
        if self.func is not None:
            self.func()


class GameObject:
    """
    Abstract base class for all objects that can be drawn on a Game canvas.
    """

    def __init__(self, game):
        self.game = game
        self.enabled = True
        self.name = None
        self._sched_queue = []
        self.x = 0
        self.y = 0

    def schedule(self, func, time_delay=0, repeat_count=0):
        if isinstance(func, GameTask):
            self._sched_queue.append(func)
        else:
            self._sched_queue.append(GameTask(self.game, self, func, time_delay, repeat_count))

    def update(self, delta_time: float):
        self._run_schedule()

    def draw(self, ctx):
        pass

    def _run_schedule(self):
        if len(self._sched_queue) == 0:
            return
        new_queue = []
        run_queue = []
        for task in self._sched_queue:
            if task.is_due():
                run_queue.append(task)
                if task.repeat_count > 1:
                    task.reschedule()
                    new_queue.append(task)
            else:
                new_queue.append(task)
        self._sched_queue = new_queue
        for task in run_queue:
            task.run()


class GameImage(GameObject):
    """
    GameObject wrapper around a Javascript canvas Image.
    """

    def __init__(self, game, js_image, width: int = -1, height: int = -1, sx: int = 0, sy: int = 0, ox: int = 0,
                 oy: int = 0, name: Optional[str] = None):
        GameObject.__init__(self, game)
        self.js_image = js_image
        self.name = name if name is not None else _hash_name(self)
        self.sx = sx
        self.sy = sy
        self.originX = ox
        self.originY = oy
        self.angle = 0
        self.global_composition_operation = 'source-over'
        if width < 0 or height < 0:
            self.width = js_image.width
            self.height = js_image.height
        else:
            self.width = width
            self.height = height

    def update(self, delta_time: float):
        GameObject.update(self, delta_time)

    def draw(self, ctx):
        GameObject.draw(self, ctx)
        ctx.save()
        ctx.globalCompositeOperation = self.global_composition_operation
        if self.angle != 0:
            ctx.translate(self.x, self.y)
            ctx.rotate(self.angle * Math.PI / 180.0)
            ctx.translate(-1 * self.originX, -1 * self.originY)
            ctx.drawImage(self.js_image, self.sx, self.sy, self.width, self.height, 0, 0, self.width, self.height)
        else:
            ctx.drawImage(self.js_image, self.sx, self.sy, self.width, self.height, self.x - self.originX,
                          self.y - self.originY, self.width, self.height)
        ctx.restore()


class SpriteSheet:
    """
    A collection of GameImage objects, typically loaded from a JSON file.
    """

    def __init__(self, game, name: Optional[str] = None):
        self.game = game
        self._frames = {}
        self.name = name if name is not None else _hash_name(self)

    def add_image(self, name: str, js_image, width: int, height: int, sx: int, sy: int):
        game_image = GameImage(self.game, js_image, width, height, sx, sy)
        game_image.name = name
        self._frames[name] = game_image

    def frames(self, key_list=None):
        if key_list is None:
            key_list = sorted(self._frames.keys())
        return [self._frames[k] for k in key_list]

    def __len__(self) -> int:
        return len(self._frames)

    def __getitem__(self, name: str) -> GameImage:
        return self._frames[name]

    def __setitem__(self, name: str, game_image: GameImage):
        self.scenes[name] = game_image


class Animation(GameObject):
    """
    A sequence of GameImage objects that can be displayed, started, and stoppped.
    """

    def __init__(self, game, frame_list=[], mspf: int = 100, rpt: int = -1, name: Optional[str] = None):
        GameObject.__init__(self, game)
        self.msPerFrame = mspf
        self.repeat = rpt
        self.name = name if name is not None else _hash_name(self)
        self.x = 0
        self.y = 0
        self.angle = 0
        self._time_in_frame = 0
        self._repeat_count = 0
        self._running = False
        self._current_frame = 0
        self.width = 0
        self.height = 0
        self._frame = []
        self.set_frame_list(frame_list)

    def set_frame_list(self, frame_list):
        self._frame = frame_list
        for game_image in self._frame:
            if game_image.width > self.width:
                self.width = game_image.width
            if game_image.height > self.height:
                self.height = game_image.height

    @property
    def originX(self):
        if len(self._frame) == 0:
            return 0
        else:
            return self._frame[0].originX

    @originX.setter
    def originX(self, value):
        for game_image in self._frame:
            game_image.originX = value

    @property
    def originY(self):
        if len(self._frame) == 0:
            return 0
        else:
            return self._frame[0].originY

    @originY.setter
    def originY(self, value):
        for game_image in self._frame:
            game_image.originY = value

    def start(self):
        self._time_in_frame = 0
        self._repeat_count = 0
        self._running = True

    def stop(self):
        self._time_in_frame = 0
        self._repeat_count = 0
        self._running = False

    def update(self, delta_time: float):
        GameObject.update(self, delta_time)
        self._time_in_frame = self._time_in_frame + delta_time
        if self._running and self._time_in_frame > self.msPerFrame:
            self._time_in_frame = 0
            self._current_frame = self._current_frame + 1
            if self._current_frame >= len(self._frame):
                self._repeat_count = self._repeat_count + 1
                if (self.repeat > 0) and (self._repeat_count >= self.repeat):
                    self._running = False
                else:
                    self._current_frame = 0

    def draw(self, ctx):
        GameObject.draw(self, ctx)
        game_image = self._frame[self._current_frame]
        game_image.x = self.x
        game_image.y = self.y
        game_image.angle = self.angle
        game_image.draw(ctx)


class Button(GameObject):
    """
    Button on a Scene that can execute a callback function.
    """

    def __init__(self, game, x: int, y: int, width: int, height: int, button_text: str, name: Optional[str] = None):
        GameObject.__init__(self, game)
        self.name = name if name is not None else _hash_name(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pad = 5
        self.buttonText = button_text
        self.font = '18pt sans-serif'
        self.fillStyle = 'white'
        self.textStyle = 'black'
        self.strokeStyle = 'black'
        self.disabledStyle = 'gray'
        self.lineWidth = 2
        self.callback = None
        self._clicked = False

    def __repr__(self) -> str:
        return "Button(%s,%r,%r, %r,%r, '%s', '%s')" \
               % (self.game, self.x, self.y, self.width, self.height, self.buttonText, self.name)

    def _in_rect(self, x: int, y: int) -> bool:
        return not (x < self.x or x > self.x + self.width
                    or y < self.y or y > self.y + self.height)

    def handle_mousedown(self, event):
        if self._in_rect(event.mouseX, event.mouseY) and self.enabled:
            self._clicked = True

    def handle_mouseup(self, event):
        if self._clicked and self.callback is not None and self._in_rect(event.mouseX, event.mouseY) and self.enabled:
            self.callback()
        self._clicked = False

    def update(self, delta_time: float):
        GameObject.update(self, delta_time)

    def draw(self, ctx):
        GameObject.draw(self, ctx)
        ctx.save()
        ctx.globalCompositeOperation = 'source-over'
        ctx.beginPath()
        ctx.fillStyle = self.fillStyle if not self._clicked else self.textStyle
        ctx.strokeStyle = self.strokeStyle if self.enabled else self.disabledStyle
        ctx.lineWidth = self.lineWidth
        ctx.rect(self.x, self.y, self.width, self.height)
        ctx.stroke()
        ctx.fillRect(self.x, self.y, self.width, self.height)
        ctx.font = self.font
        ctx.fillStyle = self.textStyle if not self._clicked else self.fillStyle
        ctx.fillStyle = ctx.fillStyle if self.enabled else self.disabledStyle
        ctx.fillText(self.buttonText, self.x + self.pad, self.y + self.height - self.pad)
        ctx.restore()


class Sprite(GameObject):
    """
    Base object that can be drawn on a game canvas.
    A sprite has an x,y location and also width and height.
    """

    def __init__(self, game, width: int, height: int, name: Optional[str] = None):
        GameObject.__init__(self, game)
        self.name = name if name is not None else _hash_name(self)
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.mass = 0
        self.bounce = 0
        self.num = 0
        self.at_rest = False

    def __repr__(self) -> str:
        return "Sprite(%s, %r,%r, '%s')" % (self.game, self.width, self.height, self.name)

    def in_rect(self, x: int, y: int) -> bool:
        return not (x < self.x or x > self.x + self.width
                    or y < self.y or y > self.y + self.height)

    def collides_with(self, sprite) -> bool:
        return not (self.x + self.width < sprite.x or self.x > sprite.x + sprite.width
                    or self.y + self.height < sprite.y or self.y > sprite.y + sprite.height)

    def update(self, delta_time: float):
        GameObject.update(self, delta_time)

    def draw(self, ctx):
        GameObject.draw(self, ctx)


class ImageSprite(Sprite):
    """
    Base Sprite object that draws an Image object onto a game canvas.
    """

    def __init__(self, game, game_image: GameImage, w: int = -1, h: int = -1, name: Optional[str] = None):
        width = w
        height = h
        if width < 0 or height < 0:
            width = game_image.width
            height = game_image.height
        Sprite.__init__(self, game, width, height, name)
        self.game_image = game_image
        self.animation = None

    def set_animation(self, animation):
        self.animation = animation

    def update(self, delta_time: float):
        Sprite.update(self, delta_time)
        if self.animation is not None:
            self.animation.update(delta_time)

    def draw(self, ctx):
        Sprite.draw(self, ctx)
        if self.animation is not None:
            self.animation.x = self.x
            self.animation.y = self.y
            self.animation.angle = self.angle
            self.animation.draw(ctx)
        else:
            self.game_image.x = self.x
            self.game_image.y = self.y
            self.game_image.angle = self.angle
            self.game_image.draw(ctx)


class GamePhysics:
    """
    Base class for other physics engines.
    Physics engines move sprites and handle collisions.
    """

    def __init__(self, game, c_left=False, c_right=False, c_up=False, c_down=False):
        self.game = game
        self.collide_left = c_left
        self.collide_right = c_right
        self.collide_up = c_up
        self.collide_down = c_down
        self.children = []

    def __len__(self):
        return len(self.children)

    def __getitem__(self, key: int):
        return self.children[key]

    def __setitem__(self, key: int, sprite: Sprite):
        self.children[key] = sprite

    def __contains__(self, sprite: Sprite) -> bool:
        return sprite in self.children

    def __iter__(self) -> Sprite:
        yield from self.children

    def _calc_angle(self, sprite1: Sprite, sprite2: Sprite) -> float:
        """
        Calculate sprite collision angle in radians.
        Straight up is 0 and Straight right is PI/2
        Straight down is PI and straight left is -PI/2.
        """
        if sprite1.y == sprite2.y:
            return 0.5 * Math.PI if sprite1.x < sprite2.x else -0.5 * Math.PI
        angle = Math.atan((sprite1.x - sprite2.x) / (sprite1.y - sprite2.y))
        if sprite2.y < sprite1.y:
            angle = angle + Math.PI
        if angle > Math.PI:
            angle = angle - 2 * Math.PI
        return angle

    def append(self, sprite: Sprite) -> Sprite:
        sprite.num = len(self.children)
        self.children.append(sprite)
        return sprite

    def collide(self, sprite1: Sprite, sprite2, angle: float):
        pass

    def update(self, delta_time: float):
        for sprite1 in self.children:
            for sprite2 in self.children:
                if sprite1.num <= sprite2.num:
                    continue
                if sprite1.collides_with(sprite2):
                    angle = self._calc_angle(sprite1, sprite2)
                    self.collide(sprite1, sprite2, angle)
            if self.collide_left and sprite1.x < 0:
                self.collide(sprite1, "LEFT", 0)
            elif self.collide_right and (sprite1.x + sprite1.width) >= self.game.canvas.width:
                self.collide(sprite1, "RIGHT", 0)
            elif self.collide_up and sprite1.y < 0:
                self.collide(sprite1, "UP", 0)
            elif self.collide_down and (sprite1.y + sprite1.height) >= self.game.canvas.height:
                self.collide(sprite1, "DOWN", 0)
        pass


class Scene(GameObject):
    """
    One scene to be displayed over the whole game canvas.
    A Scene is a container of GameObjects.
    """

    def __init__(self, game, name: Optional[str] = None, physics: GamePhysics = None):
        GameObject.__init__(self, game)
        self.name = name if name is not None else _hash_name(self)
        self.children: List[GameObject] = []
        self.physics = physics
        self.background_color = None

    def __repr__(self):
        return "Scene(%s, '%s')" % (self.game, self.name)

    def __len__(self):
        return len(self.children)

    def __getitem__(self, key: int):
        return self.children[key]

    def __setitem__(self, key: int, gameobject: GameObject):
        self.children[key] = gameobject

    def __contains__(self, gameobject: GameObject) -> bool:
        return gameobject in self.children

    def __iter__(self):
        yield from self.children

    def handle_mousedown(self, event):
        for button in (gameobject for gameobject in self.children if isinstance(gameobject, Button)):
            button.handle_mousedown(event)

    def handle_mouseup(self, event):
        for button in (gameobject for gameobject in self.children if isinstance(gameobject, Button)):
            button.handle_mouseup(event)

    def handle_mousemove(self, event):
        pass

    def handle_keydown(self, event):
        pass

    def append(self, gameobject):
        self.children.append(gameobject)
        gameobject.scene = self
        return gameobject

    def extend(self, container):
        for gameobject in container:
            self.children.append(gameobject)

    def remove(self, gameobject):
        gameobject.scene = None
        self.children.remove(gameobject)

    def update(self, delta_time: float):
        GameObject.update(self, delta_time)
        if self.physics is not None:
            self.physics.update(delta_time)
        for gameobject in self.children:
            gameobject.update(delta_time)

    def _clear_screen(self, ctx):
        ctx.save()
        if self.background_color is not None:
            ctx.globalCompositeOperation = 'copy'
            ctx.fillStyle = self.background_color
            ctx.fillRect(0, 0, self.game.canvas.width, self.game.canvas.height)
        else:
            ctx.globalCompositeOperation = 'destination-over'
            ctx.clearRect(0, 0, self.game.canvas.width, self.game.canvas.height)
        ctx.restore()

    def _draw_children(self, ctx):
        for gameobject in self.children:
            gameobject.draw(ctx)

    def draw(self, ctx):
        GameObject.draw(self, ctx)
        self._clear_screen(ctx)
        self._draw_children(ctx)


class Game:
    """
    Base class for the overall game and its canvas.
    A Game is a container of Scenes.
    """

    def __init__(self, name: str = None, loop_time: int = 20):
        self.name = name if name is not None else _hash_name(self)
        if _in_browser():
            self.canvasFrame = document.getElementById('canvas_frame')
            self.canvas = document.getElementById('canvas')
            self._prev_time = self.get_time()
            self.__get_context().globalCompositeOperation = 'source-over'
        else:
            self.canvasFrame = None
            self.canvas = None
        self.scenes: Dict[str, Scene] = {}
        self.currentScene: Optional[Scene] = None
        self._loop_time = loop_time

    def __get_context(self):
        return self.canvas.getContext('2d')

    def __repr__(self) -> str:
        return "Game('%s')" % self.name

    def __len__(self) -> int:
        return len(self.scenes)

    def __getitem__(self, name: str) -> Scene:
        return self.scenes[name]

    def __setitem__(self, name: str, scene: Scene):
        self.scenes[name] = scene
        if self.currentScene is None:
            self.currentScene = scene

    def _preprocess_event(self, event):
        if event.mouseX:
            return event.mouseX, event.mouseY
        if event.clientX:
            event.mouseX = event.clientX - self.canvas.offsetLeft
            event.mouseY = event.clientY - self.canvas.offsetTop
            return event.mouseX, event.mouseY
        if event.layerX:
            event.mouseX = event.layerX
            event.mouseY = event.layerY
            return event.mouseX, event.mouseY
        event.mouseX = event.offsetX
        event.mouseY = event.offsetY
        return event.mouseX, event.mouseY

    def __load_json(self, json_url):
        xhr = __new__(XMLHttpRequest())
        xhr.open('GET', json_url, False)
        xhr.send()
        if xhr.status != 200:
            console.log("unable to load {}".format(json_url))
            return None
        return JSON.parse(xhr.responseText)

    def handle_mousedown(self, event):
        self._preprocess_event(event)
        if self.currentScene is not None:
            self.currentScene.handle_mousedown(event)

    def handle_mouseup(self, event):
        self._preprocess_event(event)
        if self.currentScene is not None:
            self.currentScene.handle_mouseup(event)

    def handle_mousemove(self, event):
        self._preprocess_event(event)
        if self.currentScene is not None:
            self.currentScene.handle_mousemove(event)

    def handle_keydown(self, event):
        if self.currentScene is not None:
            self.currentScene.handle_keydown(event)

    def append(self, scene):
        self.scenes[scene.name] = scene
        if self.currentScene is None:
            self.currentScene = scene

    def set_current_scene(self, name):
        self.currentScene = self.scenes[name]

    def get_time(self) -> float:
        return Date.now()

    def load_image(self, image_id):
        js_image = document.getElementById(image_id)
        return GameImage(self, js_image)

    def load_audio(self, audio_id):
        return document.getElementById(audio_id)

    def load_spritesheet(self, json_url, image_id):
        js_image = document.getElementById(image_id)
        json_data = self.__load_json(json_url)
        if json_data is None:
            return None
        spritesheet = SpriteSheet(self)
        for f in json_data['frames']:
            spritesheet.add_image(f.filename, js_image, f.frame.w, f.frame.h, f.frame.x, f.frame.y)
        return spritesheet

    def update(self, delta_time: float):
        if self.currentScene is not None:
            self.currentScene.update(delta_time)

    def draw(self, ctx):
        if self.currentScene is not None:
            self.currentScene.draw(ctx)

    def start(self):
        window.setInterval(self.__game_loop, self._loop_time)
        window.addEventListener('mousedown', self.handle_mousedown, False)
        window.addEventListener('mouseup', self.handle_mouseup, False)
        window.addEventListener('mousemove', self.handle_mousemove, False)
        window.addEventListener('keydown', self.handle_keydown, False)
        window.addEventListener('touchstart', self.handle_mousedown, False)
        window.addEventListener('touchend', self.handle_mouseup, False)
        window.addEventListener('touchmove', self.handle_mousemove, False)

    def __game_loop(self):
        ctx = self.__get_context()
        current_time = self.get_time()
        delta_time = current_time - self._prev_time
        self.update(delta_time)
        self.draw(ctx)
        self._prev_time = self.get_time()
