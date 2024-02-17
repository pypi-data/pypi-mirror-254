import HueEngine
from HueEngine.__core__ import pg

class _ViewPort:
    area:pg.Rect=pg.Rect((100,75),(200,150))
    border:list[int,list]=[3,[255,255,0]]

    def CalcWithin(self, transform, texture) -> bool:
        if (transform.x < self.area.right and transform.x+texture.rect.width > self.area.left and transform.y+texture.rect.height > self.area.top and transform.y < self.area.bottom):
            return True
        else: return False

    def Resize(self, sizeX:int=100, sizeY:int=75):
        self.area:pg.Rect=pg.Rect((sizeX,sizeY),(200,150))
    
    def ReLocate(self, posX:int=100, posY:int=75):
        self.area:pg.Rect=pg.Rect(self.area.size(),(posX,posY))

HueEngineViewPort = _ViewPort()
