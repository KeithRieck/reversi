# Bedlam is a trivial game framework.
# It is based, very loosely, on Phaser (see https://phaser.io).
# Copyright (c) 2020, Keith Rieck


# __pragma__('skip')
from typing import Optional, List, Dict

document = window = Math = Date = console = 0  # Prevent complaints by optional static checker


# __pragma__('noskip')

# __pragma__('noalias', 'clear')

def _in_browser() -> bool:
    return document != 0


def _hash_name(obj) -> str:
    if _in_browser():
        return str(obj)
    else:
        return str(hash(obj))


class GameObject:
    """
    Abstract base class for all objects that can be drawn on a Game canvas.
    """

    def __init__(self, game):
        self.game = game
        self.enabled = True
        self.name = None

    def update(self, delta_time: float):
        pass

    def draw(self, ctx):
        pass


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
        if self._in_rect(event.x, event.y) and self.enabled:
            self._clicked = True

    def handle_mouseup(self, event):
        if self._clicked and self.callback is not None and self._in_rect(event.x, event.y) and self.enabled:
            self.callback()
        self._clicked = False

    def update(self, delta_time: float):
        pass

    def draw(self, ctx):
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

    def __repr__(self) -> str:
        return "Sprite(%s, %r,%r, '%s')" % (self.game, self.width, self.height, self.name)

    def in_rect(self, x: int, y: int) -> bool:
        return not (x < self.x or x > self.x + self.width
                    or y < self.y or y > self.y + self.height)

    def collides_with(self, sprite) -> bool:
        return not (self.x + self.width < sprite.x or self.x > sprite.x + sprite.width
                    or self.y + self.height < sprite.y or self.y > sprite.y + sprite.height)

    def update(self, delta_time: float) -> str:
        pass

    def draw(self, ctx):
        pass


class ImageSprite(Sprite):
    """
    Base Sprite object that draws an Image object onto a game canvas.
    """

    def __init__(self, game, width: int, height: int, image, name: Optional[str] = None):
        Sprite.__init__(self, game, width, height, name)
        self.image = image
        self.angle = 0
        self.originX = 0
        self.originY = 0

    def draw(self, ctx):
        Sprite.draw(self, ctx)
        ctx.save()
        ctx.globalCompositeOperation = 'source-over'
        if self.angle != 0:
            ctx.translate(self.x, self.y)
            ctx.rotate(self.angle * Math.PI / 180.0)
            ctx.translate(-1 * self.originX, -1 * self.originY)
            ctx.drawImage(self.image, 0, 0)
        else:
            ctx.drawImage(self.image, self.x - self.originX, self.y - self.originY)
        ctx.restore()


class Scene(GameObject):
    """
    One scene to be displayed over the whole game canvas.
    A Scene is a container of GameObjects.
    """

    def __init__(self, game, name: Optional[str] = None):
        GameObject.__init__(self, game)
        self.name = name if name is not None else _hash_name(self)
        self.children: List[GameObject] = []

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
        return gameobject

    def update(self, delta_time: float):
        for gameobject in self.children:
            gameobject.update(delta_time)

    def _clear_screen(self, ctx):
        ctx.save()
        ctx.globalCompositeOperation = 'destination-over'
        ctx.clearRect(0, 0, self.game.canvas.width, self.game.canvas.height)
        ctx.restore()

    def draw(self, ctx):
        self._clear_screen(ctx)
        for gameobject in self.children:
            gameobject.draw(ctx)


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
        return document.getElementById(image_id)

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
