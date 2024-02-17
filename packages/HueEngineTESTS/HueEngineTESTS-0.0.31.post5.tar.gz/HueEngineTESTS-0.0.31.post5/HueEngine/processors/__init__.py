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

from HueEngine.__core__ import pg,_ANY,_NULL

class Processor:
    priority = 0

    def Process(self, *args: _ANY, **kwargs: _ANY) -> _NULL: raise NotImplementedError

from .visual import *
from .spatial import *
from .logical import *
from .state import *

class Quadtree:
    def __init__(self, depthLevel:int=0, spatialBoundry:pg.Rect=pg.Rect(0,0,800,600)):
        """
        Initializes a Quadtree node.

        Args:
            depthLevel (int): The current depth depthLevel of the Quadtree node.
            spatialBoundry (pg.Rect): The rectangular spatialBoundry of this Quadtree node.
        """
        self.MAXLEVELS = 5
        self.MAXENTITIES = 10

        self.entities = []
        self.depthLevel = depthLevel
        self.spatialBoundry = spatialBoundry
        self.nodes = [_NULL, _NULL, _NULL, _NULL]

    def Split(self) -> _NULL:
        """
        Splits the node into 4 subnodes by dividing the node into four equal parts.
        """
        subWidth = self.spatialBoundry.width / 2
        subHeight = self.spatialBoundry.height / 2
        x = self.spatialBoundry.x
        y = self.spatialBoundry.y

        self.nodes[0] = Quadtree(self.depthLevel + 1, pg.Rect(x + subWidth, y, subWidth, subHeight))
        self.nodes[1] = Quadtree(self.depthLevel + 1, pg.Rect(x, y, subWidth, subHeight))
        self.nodes[2] = Quadtree(self.depthLevel + 1, pg.Rect(x, y + subHeight, subWidth, subHeight))
        self.nodes[3] = Quadtree(self.depthLevel + 1, pg.Rect(x + subWidth, y + subHeight, subWidth, subHeight))
