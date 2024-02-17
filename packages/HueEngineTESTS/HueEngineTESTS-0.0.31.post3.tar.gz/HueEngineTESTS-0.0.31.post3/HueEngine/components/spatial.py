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
import HueEngine
from HueEngine.__core__ import pg,_NULL,_ARRAY

class TransformComponent:
    def __init__(self, x:float=0.0, y:float=0.0) -> _NULL:
        self.x = x
        self.y = y
        self.rotation = 0

class VelocityComponent:
    vX = 0.0
    vY = 0.0

class WorldSpaceComponent:
    chunks:set=set()
    prevChunks:set=set()

class ColliderComponent(pg.sprite.Sprite):
    def __init__(self, position:_ARRAY[int]=(0,0), size:_ARRAY[int]=[16,32], color:_ARRAY[int]=[0,255,0], dynamic:bool=False) -> _NULL:
        super().__init__()
        self.entity = None
        self._width = 5
        self.size = size
        self.color = color
        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.image.fill((0, 0, 0))
        pg.draw.rect(self.image, self.color, self.rect, width=self._width)
        self.SetDynamic(dynamic)
        
    def SetDynamic(self, isDynamic:bool=False):
        self.dynamic = isDynamic

    def SetColor(self, color:_ARRAY[int]=[142,50,67]) -> _NULL:
        self.color = color
        pg.draw.rect(self.texture.image, self.color, self.texture.rect, width=self._width)
