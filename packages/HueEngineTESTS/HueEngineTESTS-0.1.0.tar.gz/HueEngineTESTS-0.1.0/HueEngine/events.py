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

from HueEngine.core import pg,sys,_ANY
import HueEngine


class Processor:
    priority = 0

    def Process(self, *args: _ANY, **kwargs: _ANY) -> None: raise NotImplementedError

class EventSystem:
    def __init__(self) -> None:
        self.quit = 0

    def _GetEvents(self):
        for event in pg.event.get():
            if (event): return event

    def Post(self, event):  # this doesnt work for some reason
        try:
            pg.event.post(event=event)
        except:
            print(f"Error Posting EVENT: [{event}]")

    def Emit(self, *args: _ANY, **kwargs: _ANY) -> None:
        event = self._GetEvents()
        if (event):
            [listener(event) for listener in HueEngine.LISTENERS.get(event.type, [])]
        
def _registerEvent(eventType):
    if (not HueEngine.LISTENERS.__contains__(eventType)): HueEngine.LISTENERS[eventType] = []
    else: return f"Event {eventType} Already Registered!"

def registerListener(eventType, listener:_ANY):
    _registerEvent(eventType)
    if (not HueEngine.LISTENERS[eventType].__contains__(listener)): HueEngine.LISTENERS[eventType].append(listener)
    else: return f"Listener {listener} Already Registered!"

def QuitListener(event:_ANY) -> None:
    if (event.type == HueEngine.QUIT):
        pg.quit()
        sys.exit()

def registerProcessor(processor:_ANY, stage:str="Fixed"):
    if (not HueEngine.PROCESSORS[stage].__contains__(processor)):
        HueEngine.PROCESSORS[stage].append(processor)
