#  Hue Engine ©️
#  2023-2024 Setoichi Yumaden <setoichi.dev@gmail.com>
#
#  This software is provided 'as-is', without any express or implied
#  warranty.  In no event will the authors be held liable for any damages
#  arising from the use of this software.
#
#  Permission is granted to anyone to use this software for any purpose,
#  including commercial applications, and to alter it and redistribute it
#  freely, subject to the following restrictions:
#
#  1. The origin of this software must not be misrepresented; you must not
#     claim that you wrote the original software. If you use this software
#     in a product, an acknowledgment in the product documentation would be
#     appreciated but is not required.
#  2. Altered source versions must be plainly marked as such, and must not be
#     misrepresented as being the original software.
#  3. This notice may not be removed or altered from any source distribution.

__version__ = "0.1.0"
__HUE_PROMPT__ = False
__versionTag__ = f"Hue Engine-Beta v{__version__}"
__DEV__ = "Setoichi Yumaden <setoichi.dev@gmail.com>"

from HueEngine.core import _GROUP,_COUNT,_DICT
from .graphics import *
from .utils import *
from .events import *
from .systems import *
from .components import *

INIT_ALL = pg.init
INIT_FONTS = pg.font.init
INIT_AUDIO = pg.mixer.init

KEYUP = 769
QUIT = 32787  # Window-Close Event
KEYDOWN = 768
EVENT = pg.event.Event
MOUSEBUTTONUP = 1026
MOUSEBUTTONDOWN = 1025

LISTENERS = {}
E_MAP: _DICT = {}
E_COUNT: "_COUNT[int]" = _COUNT(start=1)
PROCESSORS = {"Pre":[],"Fixed":[],"Post":[]}


class Entity(pg.sprite.Sprite):
    ID:int
    TAG:str
    WORLD = None
    ACTIVE:bool=True

    def __init__(self, size:list, *groups: _GROUP) -> None:
        self.size:list=size
        super().__init__(*groups)
        self.image = pg.Surface(size)
        self.image.fill([255,0,0])
        self.rect = pg.Rect((0,0), (self.size[0], self.size[1]))

    def Rect(self):
        if hasattr(self, 'transform'):
            return pg.Rect((self.transform.x, self.transform.y), (self.size[0], self.size[1]))

    def ProcessComponents(self, *args, renderSurface=None, dt:float=1.0, camera=None, **kwargs):
        if hasattr(self, 'transform'):
            self.rect = pg.Rect((self.transform.x, self.transform.y), (self.size[0], self.size[1]))
        if hasattr(self, 'collider') and self.collider.show and not self.collider.__DRAWN__:
            pos = self.image.get_rect().topleft
            self.image.blit(self.collider, pos)
            self.collider.__DRAWN__ = not self.collider.__DRAWN__
        if hasattr(self, 'physics') and hasattr(self, 'transform'):
            self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
            self.physics.Process(*args, dt=dt, **kwargs)
            if self.collisions["down"]: self.transform.vY = 0.0
        if hasattr(self, 'script'):
            self.script.Process(*args, **kwargs)

def HueScript(*componentTypes):
    def decorator(cls):
        class Wrapped(cls):
            def __init__(self, entity, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.entity = entity
                # Automatically fetch and assign component references
                for componentType in componentTypes:
                    setattr(self, _getComponentTypeAttr(componentType), fetchComponent(entity, componentType))
            def getComponent(self, componentType):
                return fetchComponent(self.entity, componentType.__name__)
        return Wrapped
    return decorator

def createEntity(world, renderer, renderLayer:str="foreground", size:list|Vector2=[16,16]):
    entity = Entity(size=size)
    entity.WORLD = world
    entity.ID = next(E_COUNT)
    if (not E_MAP.__contains__(entity.ID)): E_MAP[entity.ID] = entity
    renderer.addToScope(visual=entity,layer=renderLayer)
    return entity

def remEntity(entityID):
    entity = E_MAP.pop(entityID, None)
    if entity:
        entity.kill()

def _getComponentTypeAttr(componentType):
    return f"{componentType.__name__.lower().removesuffix("component")}"

def _getComponentAttr(component):
    return f"{component.__class__.__name__.lower().removesuffix("component")}"

def fetchComponent(entity, componentType):
    if hasattr(entity, _getComponentTypeAttr(componentType)):
        return getattr(entity, _getComponentTypeAttr(componentType))

def attachComponent(entity, component):
    if not hasattr(entity, _getComponentAttr(component)):
        component.entity = entity
        setattr(entity, _getComponentAttr(component), component)

def attachComponents(entity, *components):
    for component in components:
        if not hasattr(entity, _getComponentAttr(component)):
            component.entity = entity
            setattr(entity, _getComponentAttr(component), component)

def remComponent(entity, componentType):
    attr = _getComponentTypeAttr(componentType)
    if hasattr(entity, attr):
        delattr(entity, attr)


class Engine:
    camera = None
    renderer = None
    worldGROUP:_GROUP=pg.sprite.Group()
    entityGROUP:_GROUP=pg.sprite.Group()
    eventSystem:EventSystem=EventSystem()

    def __init__(self, FPS:int=144, winSize:list[int]|Vector2=[800,600]) -> None:
        self._Config()
        self.dt = 0.0
        self.FPS = FPS
        self.zoom = .5
        self._maxZoom = 3
        self._minZoom = 0.2
        self._postScriptCalls_ = []
        self.clock = pg.time.Clock()
        self.screen = pg.Surface((winSize[0]*self.zoom,winSize[1]*self.zoom))
        self.window = pg.display.set_mode((winSize[0],winSize[1]))
        setTitle(f"{__versionTag__}")
        _cDir = os.path.dirname(__file__)
        _aDir = os.path.join(_cDir, 'assets')
        _ico = os.path.join(_aDir, 'icon.ico')
        setIcon(_ico)

    def _Config(self):
        registerListener(QUIT, QuitListener)

    def SetCamera(self, camera:Camera):
        if (type(camera) == Camera): self.camera = camera
        else:
            self.camera = None
            print("Failed To Add Camera!\nThe Object Was Of The Wrong Type!")
    
    def SetRenderer(self, renderer:Renderer):
        if (type(renderer) == Renderer): self.renderer = renderer
        else:
            self.renderer = None
            print("Failed To Add Renderer!\nThe Object Was Of The Wrong Type!")

    def PreProcessing(self, *args, **kwargs):
        self.zoom = clamp(self.zoom, self._minZoom, self._maxZoom)
        for processor in sorted(PROCESSORS["Pre"], key=lambda p: p.priority): processor.Process(*args, **kwargs)

    def Process(self, *args, **kwargs):
        self.dt = tickGetDeltaTime(self.clock, self.FPS)
        for ID in E_MAP:
            if (hasattr(E_MAP[ID], "script")):
                onCall,fixedUpdate,post = E_MAP[ID].script.Process(*args, **kwargs)
                onCall(*args, **kwargs)
                E_MAP[ID].ProcessComponents(*args, renderSurface=self.screen, dt=self.dt, **kwargs)
                fixedUpdate(*args, **kwargs)
                self._postScriptCalls_.append(post)
            else: E_MAP[ID].ProcessComponents(*args, renderSurface=self.screen, dt=self.dt, **kwargs)
        if (self.camera): self.camera.Process(*args,dt=self.dt,**kwargs)
        for processor in sorted(PROCESSORS["Fixed"], key=lambda p: p.priority): processor.Process(*args, **kwargs)

    def PostProcessing(self, *args, **kwargs):
        for processor in sorted(PROCESSORS["Post"], key=lambda p: p.priority): processor.Process(*args, **kwargs)
        scroll = self.camera.GetPosition() if (self.camera) else [0,0]
        if (self.renderer):
            self.renderer.Sblit(
                self.window,
                self.screen,
                scroll,
                self.zoom,
                fillColor=HUE_BLUE
            )
        for call in self._postScriptCalls_: call(*args,**kwargs)
    
    def SendFrame(self):
        pg.display.flip()




if "HueEngine_HIDE_PROMPT" not in os.environ and not __HUE_PROMPT__:
    print(
        f"{__versionTag__} (pygame-ce {pg.ver}, SDL2 {'.'.join(map(str, pg.get_sdl_version()))}, Python {platform.python_version()})\n"
    )
    __HUE_PROMPT__ = not __HUE_PROMPT__
