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

from HueEngine.core import *
from HueEngine.graphics import *
import HueEngine


class World:
    assetCache:dict={}
    GRAVITY:float=980.0
    FRICTION:float=250.0
    NEIGHBOR_OFFSETS = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
        (1, -1),
        (-1, 1)
    ]

    def __init__(self, engine, worldDataPath):
        self.world = {}
        self.engine = engine
        self.LoadWorld(worldDataPath)
        self.SetUpCache()

    def LoadWorld(self, filePath:str):
        with open(filePath, "r") as savefile:
            data = json.load(savefile)

        self.world = data["WORLD"]
        self.WORLD_DATA = data["WORLD DATA"]
        self.name = self.WORLD_DATA["NAME"]
        self.tileSize = self.WORLD_DATA["TILE SIZE"]
        
        self.WORLD_DATA["WORLD SIZE"],self.WORLD_DATA["WORLD SIZE IN TILES"] = self.CalcWorldSize()

    def SetFriction(self, FRICTION:int|float=250.0):
        self.FRICTION = FRICTION
    
    def SetGravity(self, GRAVITY:int|float=980.0):
        self.GRAVITY = GRAVITY

    def CalcWorldSize(self):
        size = [0,0]
        sizeT = [0,0]
        for location in self.world:
            x, y = map(int, location.split(';'))
            sizeT[0] = max(sizeT[0], x)
            sizeT[1] = max(sizeT[1], y)
            size[0] = max(size[0], (x*self.tileSize)+self.tileSize)
            size[1] = max(size[1], (y*self.tileSize)+self.tileSize)
        return size,sizeT

    def SetUpCache(self):
        layers = {}
        for tileCoord,tile in self.world.items():
            textures = loadSurfaceCutout(self.world[tileCoord]["path"],self.tileSize)
            self.assetCache[tileCoord] = textures[int(tile["ID"])]
            if (not layers.__contains__(self.world[tileCoord]["layer"])):
                layers[self.world[tileCoord]["layer"]] = []
            rawPos = self.world[tileCoord]["position"]
            posX,posY = rawPos.split(",")
            layers[self.world[tileCoord]["layer"]].append((self.assetCache[tileCoord],(int(posX)*self.tileSize,int(posY)*self.tileSize)))

    def TilesAround(self, position:list|Vector2, size:list|Vector2):
        tiles = []
        # Calculate the entity's bounding box in tile coordinates
        minX = int(position[0] // self.tileSize)
        maxX = int((position[0] + size[0]) // self.tileSize)
        minY = int(position[1] // self.tileSize)
        maxY = int((position[1] + size[1]) // self.tileSize)

        # Check all tiles that intersect with the entity's bounding box
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                check_location = f"{x};{y}"
                if check_location in self.world:
                    tiles.append(self.world[check_location])
        return tiles

    def RectsAround(self, entity):
        rects = []
        if hasattr(entity, "transform") and hasattr(entity, "collider"):
            entityPos = [entity.transform.x,entity.transform.y]
            entitySize = [entity.collider.size[0], entity.collider.size[0]]
            for tile in self.TilesAround(entityPos, entitySize):
                if tile["collisions"] == "True":
                    position = [0,0]
                    position[0],position[1] = map(int, tile["position"].split(','))
                    rect = pg.Rect(
                        [int(position[0]) * self.tileSize, int(position[1]) * self.tileSize],
                        (self.tileSize, self.tileSize)
                    )
                    rects.append(rect)
            return rects

    def _ExportPNG(self, savePath):
        # Get the map size in pixels
        map_size = self.WORLD_DATA["WORLD SIZE"]

        # Create a surface to render the map
        export_surface = pg.Surface(map_size)

        # Fill the surface with a background color (e.g., white)
        export_surface.fill((255, 255, 255))

        # Render each tile onto the surface
        for location in self.world:
            tile = self.world[location]
            tile_image = self.assetCache[location]
            position = [0,0]
            position[0],position[1] = map(int, location.split(';'))
            position = (position[0] * self.tileSize, position[1] * self.tileSize)
            export_surface.blit(tile_image, position)

        # Create the full path for saving the image
        export_filename = f'{self.WORLD_DATA["NAME"]}.png'
        full_export_path = os.path.join(savePath, export_filename)

        # Save the surface as a PNG image
        pg.image.save(export_surface, full_export_path)
        print(f"Map exported as {full_export_path}")

class Camera:
    
    def __init__(self, world, speed, interpolation):
        self.world = world
        self.DEADZONE = 100
        self.target = None
        self.speed = speed
        self.scroll = Vector2(0, 0)
        self.interpolation = interpolation
        self.levelSize = Vector2(self.world.WORLD_DATA["WORLD SIZE"])
        self.screenSize = Vector2(self.world.engine.screen.get_size())

        # panning config
        self.panning = False
        self.panPosition = None
        self.panTarget = None
        self.panSpeed = speed/2

    def StartPan(self, position:list|Vector2=[0,0]):
        self.panPosition = position
        self.panning = True

    def StopPan(self):
        self.panPosition = None
        self.panning = False
        self.SetTarget(self.target)
        
    def SetTarget(self, target):
        if type(target) == HueEngine.Entity: self.target = target
        else:
            self.target = None
            print("Target Not An Entity!\nTry Using Camera.Pan() To Scroll Over To A Desired Position!")

    def Scroll(self, dt):
        desired_scroll = Vector2(
            self.target.transform.x - self.screenSize.x // 2,
            self.target.transform.y - self.screenSize.y // 2
        )
        distance_to_target = (self.scroll - desired_scroll).length()

        # If the camera is outside the deadzone, follow self.target normally
        if distance_to_target >= self.DEADZONE:
            self.scroll += ((desired_scroll - self.scroll) * self.speed) // self.interpolation * dt

    def Pan(self):
        desired_scroll = Vector2(
            self.panPosition[0] - self.screenSize.x // 2,
            self.panPosition[1] - self.screenSize.y // 2
        )
        self.scroll += ((desired_scroll - self.scroll) * self.panSpeed) / self.interpolation * self.world.engine.dt

    def Process(self, *args, dt:float=1.0, **kwargs):
        # Calculate the desired camera position
        if (not self.panning and self.target != None):
            self.Scroll(dt)
        elif (self.panning and self.panPosition):
            self.Pan()

        # Constrain camera within the level bounds
        self.scroll.x = max(0, min(self.scroll.x, self.levelSize.x - self.screenSize.x))
        self.scroll.y = max(0, min(self.scroll.y, self.levelSize.y - self.screenSize.y))

    def GetPosition(self):
        return Vector2(int(self.scroll.x), int(self.scroll.y))

class Renderer:
    assetCache:dict={}

    def __init__(self, world):
        """
        Initializes the Renderer object, setting up layers for rendering sprites.

        Attributes:
            scope (dict): A dictionary containing different layers of sprites, categorized as
                          'background', 'midground', and 'foreground'.
        """
        self.world = world
        self.visibleArea = pg.sprite.Sprite()
        self.layers = {
            "background": pg.sprite.Group(),
            "midground": pg.sprite.Group(),
            "foreground": pg.sprite.Group()
        }
        self.WorldConfig()

    def WorldConfig(self):
        for tileCoord,tile in self.world.world.items():
            textures = loadSurfaceCutout(self.world.world[tileCoord]["path"],self.world.tileSize)
            self.assetCache[tileCoord] = textures[int(tile["ID"])]
            rawPos = self.world.world[tileCoord]["position"]
            posX,posY = rawPos.split(",")

            tile = pg.sprite.Sprite(self.layers[self.world.world[tileCoord]["layer"]])
            tile.rect = pg.Rect([int(posX)*self.world.tileSize,int(posY)*self.world.tileSize],[self.world.tileSize,self.world.tileSize])
            tile.image = self.assetCache[tileCoord]
            
    def addToScope(self, visual:pg.Surface|pg.sprite.Sprite|pg.Rect, position:pg.math.Vector2|tuple|list=[0,0], layer:str=None):
        """
        Adds a sprite or Engine Object to a specific rendering layer within the Renderer's scope.

        Args:
            sprite (pg.sprite.Sprite | Object): A valid pg Sprite object, either custom or created using the Engine Object class.
            layer (str, optional): The rendering layer to add the sprite to. Options are "background", "midground", "foreground". Defaults to "midground" if not specified.
        """
        if layer is not None and layer in self.layers:
            if not isinstance(visual, pg.sprite.Sprite):
                s = pg.sprite.Sprite()
                if isinstance(visual, pg.Surface):
                    s.image = visual 
                elif isinstance(visual, pg.Rect):
                    s.image = pg.Surface(visual.w, visual.h)
                    s.rect = visual
                s.rect = pg.Rect(position[0],position[1],s.image.get_width(),s.image.get_height()) if not hasattr(visual, "rect") else visual.rect
                self.layers[layer].add(s) if s not in self.layers[layer] else None
            else:
                self.layers[layer].add(visual) if visual not in self.layers[layer] else None
        else:
            if not isinstance(visual, pg.sprite.Sprite):
                s = pg.sprite.Sprite()
                if isinstance(visual, pg.Surface):
                    s.image = visual 
                elif isinstance(visual, pg.Rect):
                    s.image = pg.Surface(visual.w, visual.h)
                    s.rect = visual
                s.rect = pg.Rect(position[0],position[1],s.image.get_width(),s.image.get_height()) if not hasattr(visual, "rect") else visual.rect
                self.layers["midground"].add(s) if s not in self.layers["midground"] else None
            else:
                self.layers["midground"].add(visual) if visual not in self.layers["midground"] else None

    def popFromScope(self, visual:pg.sprite.Sprite=None):
        if not visual:
            self.layers.pop()
        else:
            for scope in self.layers:
                try:
                    self.layers[scope].remove(visual)
                except:
                    print('error popFromScope')

    def Sblit(self, displaySurface:pg.Surface, blitSurface:pg.Surface, scrollOffset:list|tuple|pg.math.Vector2=pg.math.Vector2(), zoomValue:int|float=1.0, scaleSurface:bool=True, fill:bool=True, fillDisplay:bool=True, fillColor:list|tuple=[10,30,80], fillDisplayColor:list|tuple=[10,30,80]):
        """
        Performs a 'speed blit' operation, which is less computationally expensive but may result in slightly less accurate positioning due to zoom and scroll offsets. ( HIGHLY recommended for tilemap rendering and any large group of sprites. )

        Args:
            displaySurface (pg.Surface): The main display surface of the game.
            blitSurface (pg.Surface): The surface onto which sprites are drawn before being transferred to the display surface.
            scrollOffset (list | tuple | pg.math.Vector2, optional): The offset for scrolling effect in the game. Defaults to pg.math.Vector2().
            zoomValue (int | float, optional): The zoom effect value in the game. Defaults to 0.0.
            fill (bool, optional): Whether to clear the blitSurface each pg. Defaults to True.
            fillColor (list | tuple, optional): The color used to clear the blitSurface, if fill is True. Defaults in RGB format to [10,30,80].
        """
        if scaleSurface:
            blitSurface = pg.transform.scale(blitSurface, (displaySurface.get_size()[0]/zoomValue, displaySurface.get_size()[1]/zoomValue))
        self.visibleArea.rect = pg.Rect(0,0, displaySurface.get_width()+int(scrollOffset[0]), displaySurface.get_height()+scrollOffset[1])
        if fill:
            blitSurface.fill(fillColor)
        if fillDisplay:
            displaySurface.fill(fillDisplayColor)
        for scope in self.layers:
            visibleScope = pg.sprite.spritecollide(self.visibleArea, self.layers[scope], False)
            for sprite in visibleScope:
                if hasattr(sprite, "texture") and sprite.texture._renderOffset is not None:
                    sprite.rect.move_ip(sprite.texture._renderOffset[0], sprite.texture._renderOffset[1])
                if any(value > 0 for value in scrollOffset):
                    sprite.rect.move_ip(-int(scrollOffset[0]), -scrollOffset[1]) if hasattr(sprite, "collider") else sprite.rect.move_ip(-int(scrollOffset[0]), -scrollOffset[1])
            self.layers[scope].draw(surface=blitSurface)
            for sprite in visibleScope:
                if hasattr(sprite, "texture") and sprite.texture._renderOffset is not None:
                    sprite.rect.move_ip(-sprite.texture._renderOffset[0], -sprite.texture._renderOffset[1])
                sprite.rect.move_ip(int(scrollOffset[0]), scrollOffset[1]) if hasattr(sprite, "collider") else sprite.rect.move_ip(int(scrollOffset[0]), scrollOffset[1])
        if scaleSurface:
            displaySurface.blit(pg.transform.scale(blitSurface, displaySurface.get_size()), (0,0))
        else:
            displaySurface.blit(blitSurface, (0,0)) if not hasattr(blitSurface,"position") else displaySurface.blit(blitSurface, blitSurface.position)
