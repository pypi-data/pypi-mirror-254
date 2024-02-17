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

__version__ = "1.2.0"
__versionTag__ = f"Hue Engine-{__version__}"
import os, sys
import tkinter as tk
from tkinter import filedialog
from typing import Any as _ANY
from typing import Set as _SET
from typing import Type as _TYPE
from typing import Dict as _DICT
from typing import List as _ARRAY
from typing import Tuple as _TUPLE
from typing import Optional as _OPTION
from typing import TypeVar as _TYPEVAR
from itertools import count as _COUNT
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(True)
import pygame as pg,time as _TIME,platform,psutil,pygetwindow as gw,random,re,math
from screeninfo import get_monitors
pgRect = pg.Rect
pgEvent = pg.Event
pgSurface = pg.Surface
pgSprite = pg.sprite.Sprite
Vector2 = pg.math.Vector2
_NULL = None
THEMES = {
    "light theme": {
        "main": (0,0,0),
        "accent": (255,255,255),
        "secondary": (80,80,80),
        "background": (255, 255, 255),
        "grid": (125,125,125),
        "text": (255, 255, 255),
        "button color": (0, 128, 255),
        "menu slots": (125,125,125),
        "menu border": (125,125,125),
        "menu background": (125,125,125),
    },
    "dark theme": {
        "main": (0,0,0),
        "accent": (0,0,0),
        "secondary": (0,0,0),
        "background": (0, 0, 0),
        "grid": (0,0,0),
        "text": (255, 255, 255),
        "button color": (255, 128, 0),
        "menu slots": (125,125,125),
        "menu border": (125,125,125),
        "menu background": (125,125,125),
    }
}
