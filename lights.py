import pygame
from settings import *

def render_lighting(sprites,lights):
    if lights==[]:
        return 0
    for l in lights:
        for row, tiles in enumerate(sprites):
            for col, tile in enumerate(tiles):
                ...
                    