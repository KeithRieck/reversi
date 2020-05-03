# Bedlam is a trivial game framework.
# It is based, very loosely, on Phaser (see https://phaser.io).

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
        return "Sprite(%r, %r, '%s')" % (self.width, self.height, self.name)

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
        self.name = name if name is not None else str(self)

    def __repr__(self):
        return "Scene('%s')" % self.name

    def __len__(self):
        return len(self.children)

    def __getitem__(self, n):
        return self.children[n]

    def __setitem__(self, n, sprite):
        self.children[n] = sprite

    def __handle_mousedown(self, event):
        pass

    def __handle_mouseup(self, event):
        pass

    def __handle_mousemove(self, event):
        pass

    def __handle_keydown(self, event):
        pass

    def append(self, sprite):
        self.children.append(sprite)

    def update(self, delta_time):
        for sprite in self.children:
            sprite.update(delta_time)

    def __clear_screen(self, ctx):
        ctx.globalCompositeOperation = 'destination-over'
        ctx.clearRect(0, 0, self.game.canvas.width, self.game.canvas.height)

    def draw(self, ctx):
        self.__clear_screen(ctx)
        for sprite in self.children:
            sprite.draw(ctx)


class Game:
    """
    Base class for the overall game and its canvas.
    A Game is a container of Scenes.
    """

    def __init__(self, name=None, loop_time=20):
        self.name = name if name is not None else str(self)
        self.loop_time = loop_time
        self.canvasFrame = document.getElementById('canvas_frame')
        self.canvas = document.getElementById('canvas')
        self.prev_time = self.get_time()
        self.scenes = {}
        self.currentScene = None

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

    def __handle_mousedown(self, event):
        if self.currentScene is not None:
            self.currentScene.__handle_mousedown(event)

    def __handle_mouseup(self, event):
        if self.currentScene is not None:
            self.currentScene.__handle_mouseup(event)

    def __handle_mousemove(self, event):
        if self.currentScene is not None:
            self.currentScene.__handle_mousemove(event)

    def __handle_keydown(self, event):
        if self.currentScene is not None:
            self.currentScene.__handle_keydown(event)

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
        window.setInterval(self.__game_loop, self.loop_time);
        window.addEventListener('mousedown', self.__handle_mousedown, False)
        window.addEventListener('mouseup', self.__handle_mouseup, False)
        window.addEventListener('mousemove', self.__handle_mousemove, False)
        window.addEventListener('keydown', self.__handle_keydown, False)

    def __game_loop(self):
        ctx = self.__get_context()
        current_time = self.get_time()
        delta_time = current_time - self.prev_time
        self.update(delta_time)
        self.draw(ctx)
        self.prev_time = current_time
        # console.log("update(" + delta_time + ")  : ")
