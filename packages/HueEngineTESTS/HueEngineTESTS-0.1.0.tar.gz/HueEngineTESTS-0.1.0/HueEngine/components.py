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

from HueEngine.core import _ANY,HUE_BLUE
from HueEngine.graphics import *
import HueEngine


class Component:
    entity=None
    __compver__:str="0.1.0"
    
    def _init_(self) -> None:
        self.__compver__ = f"{self.__class__.__name__} v{self.__compver__}"

class TextureComponent(Component):
    def __init__(self, size:list|Vector2, color:list=HUE_BLUE, _textureOffset:list|Vector2=None, _renderOffset:list|Vector2=None):
        super()._init_()
        self.size = size
        self.color = color
        self._textureOffset = _textureOffset
        self._renderOffset = _renderOffset

    def SetTexture(self, texture:pg.Surface=pg.Surface((16,16)), fill:bool=False, color:list=HueEngine.HUE_BLUE):
        if (fill): texture.fill(color)
        if (self._textureOffset): self.entity.image.blit(scaleSurface(texture, self.size),[0+self._textureOffset[0],0-self._textureOffset[1]])
        else: self.entity.image.blit(scaleSurface(texture, self.size),[0,0])

    def LoadTexture(self, filePath:str, _ghost:bool=True):
        texture = loadSurface(filePath)
        if (_ghost):
            self.entity.image.set_colorkey([0,0,0])
            self.entity.image.fill([0,0,0])
        if (self._textureOffset): self.entity.image.blit(scaleSurface(texture, self.size),[0+self._textureOffset[0],0-self._textureOffset[1]])
        else: self.entity.image.blit(scaleSurface(texture, self.size),[0,0])

class ScriptComponent(Component):
    def __init__(self, entity, yourScript):
        super()._init_()
        super().__init__()
        self.script = yourScript(entity=entity)

    def Process(self, *args: _ANY, **kwargs: _ANY) -> _ANY:
        return self.script.__onCall__, self.script.__fixedUpdate__, self.script.__post__

class TransformComponent(Component):
    def __init__(self,position:list|Vector2=[0,0]):
        super()._init_()
        self.vX:float=0.0
        self.vY:float=0.0
        self.x:float=position[0]
        self.y:float=position[1]
        
class ColliderComponent(Component,pg.Surface):
    def __init__(self, size:list|Vector2=[16,16],show:bool=False,_color:list=[0,255,0],__offset__:list|Vector2=[0,0]):
        self.show = show
        self.__DRAWN__:bool=False
        super()._init_()
        super().__init__(size)
        self.size = size
        self._color = _color
        self.set_colorkey([0,0,0])
        self.fill([0,0,0])
        self.__offset__ = __offset__
        pg.draw.rect(self,self._color,self.get_rect(),width=1)

    def Rect(self):
        return pg.Rect((self.entity.transform.x, self.entity.transform.y), (self.size[0], self.size[1]))

    def Process(self, *args, dt:float=1.0, **kwargs):...

class PhysicsComponent(Component):
    def __init__(self):
        super()._init_()
        super().__init__()

    def Move(self, dt):
        movement = Vector2(self.entity.transform.vX,self.entity.transform.vY)
        self.entity.transform.x += movement.x * dt
        self.entity.transform.y += movement.y * dt

    def ApplyFriction(self, dt):
        world = self.entity.WORLD
        if (self.entity.transform.vX > 0.0):
            self.entity.transform.vX -= world.FRICTION * dt
            if (self.entity.transform.vX <= 0.0): self.entity.transform.vX = 0.0
        elif (self.entity.transform.vX < 0.0):
            self.entity.transform.vX += world.FRICTION * dt
            if (self.entity.transform.vX >= 0.0): self.entity.transform.vX = 0.0

        if (self.entity.transform.vY > 0.0):
            self.entity.transform.vY -= world.FRICTION * dt
            if (self.entity.transform.vY <= 0.0): self.entity.transform.vY = 0.0
        elif (self.entity.transform.vY < 0.0):
            self.entity.transform.vY += world.FRICTION * dt
            if (self.entity.transform.vY >= 0.0): self.entity.transform.vY = 0.0

    def AABBX(self, dt):
        movement = Vector2(self.entity.transform.vX,self.entity.transform.vY)
        if hasattr(self.entity, 'collider'):
            self.entity.transform.x += movement.x * dt
            entity_rect = self.entity.collider.Rect()
            for rect in self.entity.WORLD.RectsAround(self.entity):
                if entity_rect.colliderect(rect):
                    if movement.x > 0:
                        entity_rect.right = rect.left
                        self.entity.collisions['right'] = True
                    if movement.x < 0:
                        entity_rect.left = rect.right
                        self.entity.collisions['left'] = True
                    self.entity.transform.x = entity_rect.x

    def AABBY(self, dt):
        world = self.entity.WORLD
        movement = Vector2(self.entity.transform.vX,self.entity.transform.vY)
        self.entity.transform.vY += world.GRAVITY * dt
        movement.y = self.entity.transform.vY
        if hasattr(self.entity, 'collider'):
            self.entity.transform.y += movement.y * dt
            entity_rect = self.entity.collider.Rect()
            for rect in self.entity.WORLD.RectsAround(self.entity):
                if entity_rect.colliderect(rect):
                    if movement.y > 0:
                        entity_rect.bottom = rect.top
                        self.entity.collisions['down'] = True
                        self.entity.transform.y = rect.top-entity_rect.height
                    if movement.y < 0:
                        entity_rect.top = rect.bottom
                        self.entity.collisions['up'] = True
                        self.entity.transform.y = rect.bottom

    def Process(self, *args, dt:float=1.0, **kwargs):
        self.ApplyFriction(dt)
        if hasattr(self.entity, 'collider'):
            self.AABBX(dt)
            self.AABBY(dt)
        else: self.Move(dt)



