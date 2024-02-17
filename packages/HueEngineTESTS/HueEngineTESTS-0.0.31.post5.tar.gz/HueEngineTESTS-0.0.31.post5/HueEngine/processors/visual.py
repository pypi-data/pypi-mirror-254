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
from .__init__ import Processor
from HueEngine.__core__ import pg,_ANY,_NULL,pgSurface
from HueEngine.system.viewport import HueEngineViewPort

class RenderProcessor(Processor):
    def __init__(self) -> _NULL:
        super().__init__()
        self.viewport = HueEngineViewPort
        self._showColliders = False
        self.showViewPort = True
        self.showChunks = True
        self.spriteGroup = pg.sprite.Group()

    def ShowColliders(self):
        if (not self._showColliders):
            for entity, component in HueEngine.fetchAllTypes(HueEngine.ColliderComponent):
                self.spriteGroup.add(component)
                print(("showing"))
        self._showColliders = True
    
    def HideColliders(self):
        if (self._showColliders):
            for entity, component in HueEngine.fetchAllTypes(HueEngine.ColliderComponent):
                print(("hiding"))
                self.spriteGroup.remove(component)
        self._showColliders = False

    def Process(self, window:pgSurface=None, worldSpace=None, interface=None, *args: _ANY, **kwargs: _ANY) -> _NULL:
        if (not worldSpace): worldSpace = HueEngine.WorldSpace()
        HueEngine.fillSurface(worldSpace.world, [50,50,50,])
        for entity, component in HueEngine.fetchAllTypes(HueEngine.TextureComponent):
            texture = component.texture
            transform = HueEngine.fetchComponent(entity, HueEngine.TransformComponent)
            if (self.viewport.CalcWithin(transform,texture)):self.spriteGroup.add(texture)
            else: self.spriteGroup.remove(texture)
        self.spriteGroup.draw(worldSpace.world)
        if (self.showChunks): 
            HueEngine.drawWorldSpace(worldSpace.world, worldSpace)
            pos = HueEngine.getMousePosition()
            pos = (pos[0]-worldSpace.worldPos[0], pos[1]-worldSpace.worldPos[1])
            hoveredChunk = HueEngine.drawChunk(worldSpace.world, pos, worldSpace)
        if (self.showViewPort): pg.draw.rect(worldSpace.world,self.viewport.border[1],self.viewport.area,width=self.viewport.border[0])
        HueEngine.fillSurface(window, [50,50,50])
        window.blit(
        pg.transform.scale(worldSpace.world,(window.get_width(),window.get_height())), 
        worldSpace.worldPos
        )
        if (self.showChunks and interface): interface.addToInterface(f"Chunk: {hoveredChunk}")
        if (interface): 
            interface.displaySurface = window
            interface.visualOutput()

        HueEngine.sendFrame()

class TextureProcessor(Processor):
    def __init__(self) -> _NULL:
        super().__init__()

    def Process(self, *args: _ANY, **kwargs: _ANY) -> _NULL:
        for entity, component in HueEngine.fetchAllTypes(HueEngine.TextureComponent):
            texture = component.texture
            transform = HueEngine.fetchComponent(entity, HueEngine.TransformComponent)
            if (transform and texture):
                if (HueEngineViewPort.CalcWithin(transform,texture)):
                    component.texture.rect.x = transform.x
                    component.texture.rect.y = transform.y    

