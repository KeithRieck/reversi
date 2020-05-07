# Bedlam is a trivial game framework.
# It is based, very loosely, on Phaser (see https://phaser.io).
# Copyright (c) 2020, Keith Rieck

# __pragma__('skip')
document = window = Math = Date = console = 0  # Prevent complaints by optional static checker
# __pragma__('noskip')
# __pragma__('noalias', 'clear')


class GameObject:
    """
    Abstract base class for all objects that can be drawn on a Game canvas.
    """

    def __init__(self, game):
        self.game = game

    def update(self, delta_time):
        pass

    def draw(self, ctx):
        pass


class Button(GameObject):
    def __init__(self, game, x, y, width, height, label):
        GameObject.__init__(self, game)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pad = 5
        self.label = label
        self.font = '18pt sans-serif'
        self.fillStyle = 'white'
        self.textStyle = 'black'
        self.strokeStyle = 'black'
        self.disabledStyle = 'gray'
        self.lineWidth = 2
        self.callback = None
        self.enabled = True
        self._clicked = False

    def __repr__(self):
        return "Button(%r,%r, %r,%r, '%s')" % (self.x, self.y, self.width, self.height, self.label)

    def _in_rect(self, x, y):
        return not (x < self.x or x > self.x + self.width
                    or y < self.y or y > self.y + self.height)

    def handle_mousedown(self, event):
        if self._in_rect(event.x, event.y) and self.enabled:
            self._clicked = True

    def handle_mouseup(self, event):
        if self._clicked and self.callback is not None and self._in_rect(event.x, event.y) and self.enabled:
            self.callback()
        self._clicked = False

    def update(self, delta_time):
        pass

    def draw(self, ctx):
        ctx.save()
        ctx.font = self.font
        ctx.fillStyle = self.textStyle if not self._clicked else self.fillStyle
        ctx.fillStyle = ctx.fillStyle if self.enabled else self.disabledStyle
        ctx.fillText(self.label, self.x + self.pad, self.y + self.height - self.pad)
        ctx.beginPath()
        ctx.fillStyle = self.fillStyle if not self._clicked else self.textStyle
        ctx.strokeStyle = self.strokeStyle if self.enabled else self.disabledStyle
        ctx.lineWidth = self.lineWidth
        ctx.rect(self.x, self.y, self.width, self.height)
        ctx.stroke()
        ctx.fillRect(self.x, self.y, self.width, self.height)
        ctx.restore()


class Sprite(GameObject):
    """
    Base object that can be drawn on a game canvas.
    A sprite has an x,y location and also width and height.
    """

    def __init__(self, game, width, height, name=None):
        GameObject.__init__(self, game)
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.name = name if name is not None else str(self)

    def __repr__(self):
        return "Sprite(%r,%r, '%s')" % (self.width, self.height, self.name)

    def update(self, delta_time):
        pass

    def draw(self, ctx):
        pass


class Scene(GameObject):
    """
    One scene to be displayed over the whole game canvas.
    A Scene is a container of GameObjects.
    """

    def __init__(self, game, name=None):
        GameObject.__init__(self, game)
        self.children = []
        self.buttons = []
        self.name = name if name is not None else str(self)

    def __repr__(self):
        return "Scene('%s')" % self.name

    def __len__(self):
        return len(self.children)

    def __getitem__(self, n):
        return self.children[n]

    def __setitem__(self, n, sprite):
        self.children[n] = sprite

    def handle_mousedown(self, event):
        for button in self.buttons:
            button.handle_mousedown(event)

    def handle_mouseup(self, event):
        for button in self.buttons:
            button.handle_mouseup(event)

    def handle_mousemove(self, event):
        pass

    def handle_keydown(self, event):
        pass

    def append(self, obj):
        if isinstance(obj, Button):
            self.buttons.append(obj)
        if isinstance(obj, Sprite):
            self.children.append(obj)
        return obj

    def update(self, delta_time):
        for sprite in self.children:
            sprite.update(delta_time)
        for button in self.buttons:
            button.update(delta_time)

    def _clear_screen(self, ctx):
        ctx.globalCompositeOperation = 'destination-over'
        ctx.clearRect(0, 0, self.game.canvas.width, self.game.canvas.height)

    def draw(self, ctx):
        self._clear_screen(ctx)
        for sprite in self.children:
            sprite.draw(ctx)
        for button in self.buttons:
            button.draw(ctx)


class Game:
    """
    Base class for the overall game and its canvas.
    A Game is a container of Scenes.
    """

    def __init__(self, name=None, loop_time=20):
        self.name = name if name is not None else str(self)
        self.canvasFrame = document.getElementById('canvas_frame')
        self.canvas = document.getElementById('canvas')
        self.scenes = {}
        self.currentScene = None
        self._loop_time = loop_time
        self._prev_time = self.get_time()

    def __get_context(self):
        return self.canvas.getContext('2d')

    def __repr__(self):
        return "Game('%s')" % self.name

    def __len__(self):
        return len(self.scenes)

    def __getitem__(self, name):
        return self.scenes[name]

    def __setitem__(self, name, scene):
        self.scenes[name] = scene
        if self.currentScene is None:
            self.currentScene = scene

    def _prep_event(self, event):
        if event.x:
            return event.x, event.y
        if event.layerX:
            event.x = event.layerX
            event.y = event.layerY
            return event.x, event.y
        event.x = event.offsetX
        event.y = event.offsetY
        return event.x, event.y

    def handle_mousedown(self, event):
        self._prep_event(event)
        if self.currentScene is not None:
            self.currentScene.handle_mousedown(event)

    def handle_mouseup(self, event):
        self._prep_event(event)
        if self.currentScene is not None:
            self.currentScene.handle_mouseup(event)

    def handle_mousemove(self, event):
        self._prep_event(event)
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

    def get_time(self):
        return Date.now()

    def update(self, delta_time):
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
        self._prev_time = current_time
