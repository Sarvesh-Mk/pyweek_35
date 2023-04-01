import pygame
from settings import *

def render_lighting(sprites,lights):
    if lights==[]:
        return 0
    for l in lights:
        for row, tiles in enumerate(sprites):
            for col, tile in enumerate(tiles):
                if (l.x+1) == tile.x and l.y == tile.y:
                    tile.is_shadow = True
                else:
                    tile.is_shadow = False