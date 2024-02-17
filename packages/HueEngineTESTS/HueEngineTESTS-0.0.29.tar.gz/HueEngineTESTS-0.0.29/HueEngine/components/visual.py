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

from HueEngine.debug.debug import _LOGFUNC
from HueEngine.__core__ import _NULL, _ARRAY, pg


class TextureComponent:
    def __init__(self, color:_ARRAY[int]=[53,20,62]) -> _NULL:
        self.color = color
        self.texture = pg.sprite.Sprite()
        self.texture.image = pg.Surface((32,32))
        self.texture.image.fill(self.color)
        self.texture.rect = self.texture.image.get_rect()

    def Refresh(self):
        self.texture = pg.sprite.Sprite()
        self.texture.image = pg.Surface((32,32))
        self.texture.image.fill(self.color)
        self.texture.rect = self.texture.image.get_rect()

    def SetColor(self, color:_ARRAY[int]=[53,20,62]) -> _NULL:
        self.Refresh()
        self.color = color
        self.texture.image.fill(self.color)

    @_LOGFUNC
    def Load(self, fp:str):
        try:
            image = pg.image.load(fp)
            self._ogriginalImage = image
            self.texture.image.blit(image,(0,0))
            self.texture.image.set_colorkey(self.color)
        except:
            return "Error Loading Texture!\n"
