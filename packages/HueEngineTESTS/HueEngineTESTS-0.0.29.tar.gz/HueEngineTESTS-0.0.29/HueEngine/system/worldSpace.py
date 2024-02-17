import HueEngine
from HueEngine.__core__ import pg

class WorldSpace:
    def __init__(self, worldSize:tuple, chunkSize:int) -> None:
        self.chunkSize:int = chunkSize
        self.size:tuple = [worldSize[0] // self.chunkSize,worldSize[1] // self.chunkSize]
        self.grid:dict = {(x, y): [] for x in range(self.size[0]) for y in range(self.size[1])}

def drawWorldSpace(window, worldSpace):
    chunkCount = 0
    gridColor = [25, 25, 25]
    for loc, data in worldSpace.grid.items():
        chunkCount += 1
        x = loc[0] * worldSpace.chunkSize
        y = loc[1] * worldSpace.chunkSize
        pg.draw.rect(window, gridColor, pg.Rect(x, y, worldSpace.chunkSize, worldSpace.chunkSize), width=1)

def drawChunk(window, pos, worldSpace) -> tuple:
    chunkData = getChunk(pos, worldSpace)
    if (chunkData): pg.draw.rect(window, [0,0,255],pg.Rect(chunkData[0]*worldSpace.chunkSize,chunkData[1]*worldSpace.chunkSize, worldSpace.chunkSize, worldSpace.chunkSize),width=1)
    return chunkData

def getRelevantChunks(pos, worldSpace, chunkRange=1):
    relevant_chunks = []
    posX = pos[0]//worldSpace.chunkSize
    posY = pos[1]//worldSpace.chunkSize
    for x in range(posX - chunkRange, posX + chunkRange + 1):
        for y in range(posY - chunkRange, posY + chunkRange + 1):
            if (x, y) in WorldSpace:  # Check if the chunk exists
                relevant_chunks.extend(WorldSpace[(x, y)])
    return relevant_chunks

def chunkExists(chunk:tuple, worldSpace):
    if worldSpace.grid.__contains__(chunk):
        return chunk

def getChunk(pos:tuple, worldSpace):
    return chunkExists((pos[0]//worldSpace.chunkSize,pos[1]//worldSpace.chunkSize),worldSpace)

def getChunkData(pos:tuple, worldSpace):
    chunk = chunkExists((pos[0]//worldSpace.chunkSize,pos[1]//worldSpace.chunkSize),worldSpace)
    return worldSpace.grid[chunk]

def addEntityToChunk(entity, transform, worldSpace):
    chunkX = transform.x // worldSpace.chunkSize
    chunkY = transform.y // worldSpace.chunkSize
    if (entity not in worldSpace.grid[(chunkX,chunkY)]):
        worldSpace.grid[(chunkX,chunkY)].append(entity)

def remEntityFromChunk(entity, worldSpace):
    entityData = HueEngine.fetchComponent(entity, HueEngine.WorldSpaceComponent)
    if entityData.prevChunk != entityData.chunk:
        try:
            worldSpace.grid[tuple(entityData.prevChunk)].remove(entity)
        except ValueError:
            pass  # Entity was not in the previous chunk; ignore

def updateEntityChunk(entity, worldSpace):
    pos = HueEngine.fetchComponent(entity, HueEngine.TransformComponent)
    newChunk = getChunk((pos.x, pos.y), worldSpace)
    entityData = HueEngine.fetchComponent(entity, HueEngine.WorldSpaceComponent)
    entityData.prevChunk = entityData.chunk
    entityData.chunk = newChunk