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
from HueEngine.system.worldSpace import addEntityToChunk,remEntityFromChunk,updateEntityChunk
from .__init__ import Processor

class TransformProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def Move(self, transform, velocity, dt):
        transform.x += velocity.vX * dt
        transform.y += velocity.vY * dt

    def ApplyFriction(self, velocity, dt):
        if (velocity.vX > 0.0):
            velocity.vX -= 75 * dt
            if (velocity.vX <= 0.0): velocity.vX = 0.0
        elif (velocity.vX < 0.0):
            velocity.vX += 75 * dt
            if (velocity.vX >= 0.0): velocity.vX = 0.0

        if (velocity.vY > 0.0):
            velocity.vY -= 75 * dt
            if (velocity.vY <= 0.0): velocity.vY = 0.0
        elif (velocity.vY < 0.0):
            velocity.vY += 75 * dt
            if (velocity.vY >= 0.0): velocity.vY = 0.0

    def ApplyGravity(self, velocity, dt):
        velocity.vY += 300 * dt

    def Process(self, *args, dt:float=1.0, **kwargs) -> None:
        for entity, transform in HueEngine.fetchAllTypes(HueEngine.TransformComponent):
            velocity = HueEngine.fetchComponent(entity, HueEngine.VelocityComponent)
            if transform and velocity:
                self.ApplyGravity(velocity, dt)
                self.Move(transform, velocity, dt)
                self.ApplyFriction(velocity, dt)

class WorldSpaceProcessor(Processor): 
    def __init__(self) -> None:
        super().__init__()

    def Process(self, *args, worldSpace:dict={}, **kwargs) -> None:
        for e,c in HueEngine.fetchAllTypes(HueEngine.WorldSpaceComponent):
            updateEntityChunk(e,worldSpace)
            remEntityFromChunk(e,worldSpace)
            pos = HueEngine.fetchComponent(e, HueEngine.TransformComponent)
            addEntityToChunk(e,pos,worldSpace)

class ColliderProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def Process(self, *args, **kwargs) -> None:
        for entity, component in HueEngine.fetchAllTypes(HueEngine.ColliderComponent):
            transform = HueEngine.fetchComponent(entity, HueEngine.TransformComponent)
            if transform and component:
                component.rect.x = transform.x
                component.rect.y = transform.y

class CollisionProcessor(Processor):
    def __init__(self) -> None:
        super().__init__()

    def AABBNegX(self, collider1, collider2, velocity, transform) -> bool:
        if ( int(collider1.rect.topleft[0]) == int(collider2.rect.topright[0]) and ( collider1.rect.topleft[1] <= collider2.rect.bottomright[1] and collider1.rect.bottomleft[1] >= collider2.rect.topleft[1] ) ):
            transform.x = collider2.rect.x + collider2.rect.w + 1
            velocity.x = 0.0
            return True
        return False
    
    def AABBPosX(self, collider1, collider2, velocity, transform) -> bool:
        if ( int(collider1.rect.topright[0]) == int(collider2.rect.topleft[0]) and ( collider1.rect.topright[1] <= collider2.rect.bottomleft[1] and collider1.rect.bottomright[1] >= collider2.rect.topright[1] ) ):
            transform.x = collider2.rect.x - collider1.rect.w - 1
            velocity.x = 0.0
            return True
        return False

    def AABBNegY(self, collider1, collider2, velocity, transform) -> bool:
        if ( int(collider1.rect.topleft[1]) == int(collider2.rect.bottomleft[1]) and ( collider1.rect.topleft[0] < collider2.rect.bottomright[0] and collider1.rect.topright[0] > collider2.rect.bottomleft[0] ) ):
            transform.y = collider2.rect.y + collider2.rect.h + 1
            velocity.y = 0.0
            return True
        return False

    def AABBPosY(self, collider1, collider2, velocity, transform) -> bool:
        if ( int(collider1.rect.bottomleft[1]) == int(collider2.rect.topleft[1]) and ( collider1.rect.bottomleft[0] < collider2.rect.topright[0] and collider1.rect.bottomright[0] > collider2.rect.topleft[0] ) ):
            transform.y = collider2.rect.y - collider1.rect.h - 1
            velocity.y = 0.0
            return True
        return False

    def AABB(self) -> None:
        for entity1, collider1 in HueEngine.fetchAllTypes(HueEngine.HueEngine.ColliderComponent):
            transform = HueEngine.fetchComponent(entity1, HueEngine.TransformComponent)
            velocity = HueEngine.fetchComponent(entity1, HueEngine.HueEngine.VelocityComponent)
            for entity2, collider2 in HueEngine.fetchAllTypes(HueEngine.HueEngine.ColliderComponent):
                if (velocity and velocity.vX < 0.0): self.AABBNegX(collider1, collider2, velocity, transform)
                elif (velocity and velocity.vX > 0.0): self.AABBPosX(collider1, collider2, velocity, transform)
                if (velocity and velocity.vY < 0.0): self.AABBNegY(collider1, collider2, velocity, transform)
                elif (velocity and velocity.vY > 0.0): self.AABBPosY(collider1, collider2, velocity, transform)

    def Process(self, *args, dt:float=1.0, **kwargs) -> None:
        for step in range(12):
            self.AABB()