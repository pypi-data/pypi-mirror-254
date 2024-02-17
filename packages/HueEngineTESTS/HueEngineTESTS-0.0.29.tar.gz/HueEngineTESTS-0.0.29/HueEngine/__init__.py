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

__version__ = "1.2.0"
__versionTag__ = f"Hue Engine-{__version__}"
__DEV__ = "Setoichi Yumaden <setoichi.dev@gmail.com>"

from .system.events.events import *
from .processors.state import *
from .components.visual import *
from .processors.visual import *
from .components.logical import *
from .components.spatial import *
from .processors.spatial import *
from .processors.logical import *
from .system.events.listeners import *
from .debug.debug import _LOGFUNC, _LOGINTERNAL, _PROCESSTIMES, __DHM__
from .__core__ import os,platform,_TIME,_ANY,_SET,_TYPE,_DICT,_ARRAY,_TUPLE,_OPTION,_TYPEVAR,_COUNT,_NULL

_NULL = None

_COMPONENT = _TYPEVAR("_COMPONENT")
_ECOUNT: "_COUNT[int]" = _COUNT(start=1)
_COMPONENTS: _DICT[_TYPE[_ANY], _SET[_ANY]] = {}
_DEADENTITIES: _SET[int] = set()
_ENTITIES: _DICT[int, _DICT[_TYPE[_ANY], _ANY]] = {}
_LISTENERS: _DICT[_TYPE[EVENT], _ARRAY[_ANY]] = {
    QUIT: [QuitListener]
}
_STOREFETCH: _DICT[int, _DICT[_TYPE[_ANY], _ANY]] = {}
_STOREFETCHALL: _DICT[_TUPLE[_TYPE[_ANY]], _ARRAY[_ANY]] = {}
_PROCESSORS: _ARRAY[Processor] = []
_TEXTLIBRARY = {}


def _freeCache() -> _NULL:
    _STOREFETCH.clear()
    _STOREFETCHALL.clear()

def _freeAll() -> _NULL:
    global _ECOUNT
    _ECOUNT = _COUNT(start=1)
    _COMPONENTS.clear()
    _ENTITIES.clear()
    _DEADENTITIES.clear()
    _freeCache()
def _killEntities() -> _NULL:
    for entity in _DEADENTITIES:
        for componentType in _ENTITIES[entity]:
            _COMPONENTS[componentType].discard(entity)
            if (not _COMPONENTS[componentType]): del _COMPONENTS[componentType]
        del _ENTITIES[entity]
        if (entity in _STOREFETCH): del _STOREFETCH[entity]
    _DEADENTITIES.clear()

@_LOGFUNC
def addProcessor(processor: Processor, priority: int = 0) -> _OPTION[str]:
    processor.priority = priority
    _PROCESSORS.append(processor)
    _PROCESSORS.sort(key=lambda _processor: _processor.priority, reverse=True)

def remProcessor(processorType: _TYPE[Processor]) -> _NULL:
    [_PROCESSORS.remove(processor) for processor in _PROCESSORS if type(processor) is processorType]

@_LOGFUNC
def fetchProcessor(processorType: _TYPE[Processor]) -> _OPTION[Processor]:
    for processor in _PROCESSORS:
        if (type(processor) is processorType):
            return processor 
    else:
        return _NULL

def _Process(*args: _ANY, **kwargs: _ANY) -> _NULL:
    _killEntities()
    for processor in _PROCESSORS:
        if (type(processor) == HueScriptProcessor):
            sp = processor
            funcs = sp.Process()
            if (funcs):
                funcs[0]()
                funcs[1]()
                funcs[2]()
        processor.Process(*args, **kwargs)

def _TimedProcess(*args: _ANY, **kwargs: _ANY) -> _NULL:
    _killEntities()
    for processor in _PROCESSORS:
        _start =  _TIME.process_time()
        if (type(processor) == HueScriptProcessor):
            sp = processor
            onCall,fixedUpdate,postProcessing = sp.Process()
            onCall()
            fixedUpdate()
            postProcessing()
        processor.Process(*args, **kwargs)
        _PROCESSTIMES[processor.__class__.__name__] = int((_TIME.process_time() - _start) * 1000)

@_LOGFUNC
def makeEntity(*component_s:_TYPE[_COMPONENT]|_ARRAY[_TYPE[_COMPONENT]]) -> int:
    e = next(_ECOUNT)
    _ENTITIES[e] = {} if (not _ENTITIES.__contains__(e)) else ...
    for componentInstance in component_s:
        _type = type(componentInstance)
        if (_type not in _COMPONENTS): _COMPONENTS[_type] = set()
        try:
            _COMPONENTS[_type].add(e)
            if (_type == ColliderComponent): 
                componentInstance.entity = e
                componentInstance.__DrawTo__()
        except KeyError:
            return f"Component Not Of Type: _COMPONENT"
        _ENTITIES[e][_type] = componentInstance
        _freeCache()
    return e

def remEntity(entity:int, instant:bool = False) -> _NULL:
    if (instant):
        for _type in _ENTITIES[entity]:
            _COMPONENTS[_type].discard(entity)
            if (not _COMPONENTS[_type]): del _COMPONENTS[_type]
        del _ENTITIES[entity]
        _freeCache()
    else: _DEADENTITIES.add(entity)

def isAlive(entity:int) -> bool:
    """Check if a given Entity is alive.

    Blank Entities ( has no components ) and dead Entities ( killed with
    remEntity() ) will not count as "live" ones.
    """
    return _ENTITIES.__contains__(entity) and not _DEADENTITIES.__contains__(entity)

def addComponent(entity:int, *component_s:_TYPE[_COMPONENT]|_ARRAY[_TYPE[_COMPONENT]]) -> _NULL:
    for c in component_s:
        _type = type(c)
        if (_type not in _COMPONENTS): _COMPONENTS[_type] = set()
        _COMPONENTS[_type].add(entity)
        if (_type == ColliderComponent): 
            c.entity = entity
            c.__DrawTo__()
        _ENTITIES[entity][_type] = c
        if (_STOREFETCH.__contains__(entity)): _STOREFETCH[entity][_type] = c
    _freeCache()

@_LOGFUNC
def remComponent(entity:int, componentType:_TYPE[_COMPONENT]|_ARRAY[_TYPE[_COMPONENT]], all:_OPTION[bool]=False) -> _OPTION[_COMPONENT]:
    try:
        _COMPONENTS[componentType].discard(entity)
        if (not _COMPONENTS[componentType] and all): del _COMPONENTS[componentType]
        _freeCache()
        return _ENTITIES[entity].pop(componentType)
    except KeyError:
        return _NULL

@_LOGFUNC
def _fetchComponent(entity: int, componentType: _TYPE[_COMPONENT]) -> _OPTION[_COMPONENT]:
    if (entity in _ENTITIES and componentType in _ENTITIES[entity]):
        return _ENTITIES[entity][componentType]
    return _NULL

@_LOGFUNC
def fetchComponent(entity: int, componentType: _TYPE[_COMPONENT]) -> _OPTION[_COMPONENT]:
    if (not _STOREFETCH.__contains__(entity)):
        _LOGINTERNAL("single component never fetched adding to cache")
        _STOREFETCH[entity] = {}
    if (not _STOREFETCH[entity].__contains__(componentType)):
        _STOREFETCH[entity][componentType] = _fetchComponent(entity, componentType)
        return _STOREFETCH[entity][componentType]
    
    _LOGINTERNAL("single component fetched using cache")
    return _STOREFETCH[entity][componentType]

@_LOGFUNC
def _fetchAllTypes(componentType: _TYPE[_COMPONENT]) -> _ARRAY[_TUPLE[int, _COMPONENT]]:
    return [(entity, _ENTITIES[entity][componentType]) for entity in _COMPONENTS.get(componentType, []) if componentType in _ENTITIES[entity]]

@_LOGFUNC
def fetchAllTypes(componentType: _TYPE[_COMPONENT]) -> _ARRAY[_TUPLE[int, _COMPONENT]]:
    if not _STOREFETCHALL.__contains__(componentType):
        _STOREFETCHALL[componentType] = _fetchAllTypes(componentType)
    return _STOREFETCHALL[componentType]

@_LOGFUNC
def __componentFor__(entity:int, componentType: _TYPE[_COMPONENT]) -> _OPTION[_COMPONENT]:
    try:
        return _ENTITIES[entity][componentType]
    except:
        _LOGINTERNAL(f"Entity {entity} does not have Component {componentType}!\n")
        return _NULL

@_LOGFUNC
def __componentsFor__(entity:int) -> _OPTION[_ARRAY[_TYPE[_COMPONENT]]]:
    try:
        return list(_ENTITIES[entity].values())
    except:
        _LOGINTERNAL(f"Entity {entity} does not exist or is dead!\n")
        return _NULL

@_LOGFUNC
def hasComponent(entity:int, componentType: _TYPE[_COMPONENT]) -> bool:
    return componentType in _ENTITIES[entity]

@_LOGFUNC
def hasComponents(entity:int, *componentTypes: _TYPE[_COMPONENT]) -> bool:
    return all(_type in _ENTITIES[entity] for _type in componentTypes)

@_LOGFUNC
def registerEvent(eventType:EVENT):
    if (not _LISTENERS.__contains__(eventType)): _LISTENERS[eventType] = []
    else: return f"Event {eventType} Already Registered!"

@_LOGFUNC
def registerListener(eventType:EVENT, listener:_ANY):
    if (not _LISTENERS.__contains__(eventType)): _LISTENERS[eventType] = []
    if (not _LISTENERS[eventType].__contains__(listener)): _LISTENERS[eventType].append(listener)
    else: return f"Listener {listener} Already Registered!"

def init():
    addProcessor(EventProcessor(), 999)
    addProcessor(RenderProcessor(), 1)
    addProcessor(TextureProcessor(), 1)
    addProcessor(TransformProcessor(), 2)
    addProcessor(ColliderProcessor(), 2)
    addProcessor(WorldSpaceProcessor(), 2)
    #addProcessor(CollisionProcessor(), 3)
    addProcessor(HueScriptProcessor(), 4)

if "HueEngine_HIDE_PROMPT" not in os.environ and not __DHM__:
    print(
        f"{__versionTag__} (pygame-ce {pg.ver}, SDL2 {'.'.join(map(str, pg.get_sdl_version()))}, Python {platform.python_version()})\n"
    )
    __DHM__ = not __DHM__

from .system.mgmt import *
from .system.worldSpace import *
from .decorators.decorators import *
from .hgl.hgl import *
from .utils import *
pg.font.init()
pg.mixer.init()