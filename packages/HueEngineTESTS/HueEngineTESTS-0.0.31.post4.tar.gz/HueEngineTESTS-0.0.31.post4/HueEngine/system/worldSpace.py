import HueEngine
from HueEngine.__core__ import pg

class WorldSpace:
    def __init__(self, window:pg.Surface=pg.Surface((800,600)), chunkSize:int=164) -> None:
        self.__zoom__ = 1
        self.window = window
        self.chunkSize:int = chunkSize
        self.worldPos = pg.Vector2()
        self.world = pg.Surface(
            (
                window.get_width()/self.__zoom__,
                window.get_height()/self.__zoom__
            )
        )
        self.MAXCHUNKS = 10_000
        self.chunkCount:tuple = [self.world.get_width() // self.chunkSize,self.world.get_height() // self.chunkSize]
        self.chunks:dict = {(x, y): [] for x in range(self.chunkCount[0]) for y in range(self.chunkCount[1])}
        self.chunkColor = [255, 255, 255]

def drawWorldSpace(window, worldSpace):
    for loc, data in worldSpace.chunks.items():
        x = loc[0] * worldSpace.chunkSize
        y = loc[1] * worldSpace.chunkSize
        pg.draw.rect(window, worldSpace.chunkColor, pg.Rect(x, y, worldSpace.chunkSize, worldSpace.chunkSize), width=1)

def drawChunk(window, pos, worldSpace) -> tuple:
    chunkData = getChunk(pos, worldSpace)
    if (chunkData): pg.draw.rect(window, [0,255,0],pg.Rect(chunkData[0]*worldSpace.chunkSize,chunkData[1]*worldSpace.chunkSize, worldSpace.chunkSize, worldSpace.chunkSize),width=3)
    return chunkData

def getRelevantChunks(pos, worldSpace, chunkRange=1):
    relevantChunks = []
    posX = pos[0]//worldSpace.chunkSize
    posY = pos[1]//worldSpace.chunkSize
    for x in range(int(posX) - chunkRange, int(posX) + chunkRange + 1):
        for y in range(int(posY) - chunkRange, int(posY) + chunkRange + 1):
            if (x, y) in worldSpace.chunks:  # Check if the chunk exists
                relevantChunks.extend(worldSpace.chunks[(x, y)])
    return relevantChunks

def chunkExists(chunk:tuple, worldSpace):
    if (worldSpace.chunks.__contains__(chunk)):
        return chunk

def getChunk(pos:tuple, worldSpace):
    return chunkExists((pos[0]//worldSpace.chunkSize,pos[1]//worldSpace.chunkSize),worldSpace)

def getChunkData(pos:tuple, worldSpace):
    chunk = chunkExists((pos[0]//worldSpace.chunkSize,pos[1]//worldSpace.chunkSize),worldSpace)
    return worldSpace.chunks[chunk]

def remEntityFromChunk(entity, worldSpace):
    entityData = HueEngine.fetchComponent(entity, HueEngine.WorldSpaceComponent)
    for chunk in entityData.prevChunks:
        if (entity in worldSpace.chunks[chunk]):
            worldSpace.chunks[chunk].remove(entity)
    entityData.prevChunks.clear()  # Clear previous chunks after removal

def updateEntityChunk(entity, transform, texture, worldSpace):
    newChunks = set()
    left = transform.x
    top = transform.y
    right = left + texture.texture.rect.width
    bottom = top + texture.texture.rect.height

    startChunkX = int(left // worldSpace.chunkSize)
    endChunkX = int(right // worldSpace.chunkSize)
    startChunkY = int(top // worldSpace.chunkSize)
    endChunkY = int(bottom // worldSpace.chunkSize)

    for chunkX in range(startChunkX, endChunkX + 1):
        for chunkY in range(startChunkY, endChunkY + 1):
            newChunks.add((chunkX, chunkY))
            if (not worldSpace.chunks.__contains__((chunkX, chunkY)) and len(worldSpace.chunks) < worldSpace.MAXCHUNKS and chunkX > 0 and chunkY > 0): worldSpace.chunks[(chunkX, chunkY)] = []
            if (worldSpace.chunks.__contains__((chunkX, chunkY))):
                worldSpace.chunks[(chunkX, chunkY)].append(entity)

    entityData = HueEngine.fetchComponent(entity, HueEngine.WorldSpaceComponent)
    entityData.prevChunks = entityData.chunks
    entityData.chunks = newChunks