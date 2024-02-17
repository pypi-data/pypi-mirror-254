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

from HueEngine import fetchComponent

def HueScript(*componentTypes):
    def decorator(cls):
        class Wrapped(cls):
            def __init__(self, entity, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.entity = entity
                # Automatically fetch and assign component references
                for componentType in componentTypes:
                    setattr(self, componentType.__name__, fetchComponent(entity, componentType))
            def getComponent(self, componentType):
                return fetchComponent(self.entity, componentType.__name__)
        return Wrapped
    return decorator
