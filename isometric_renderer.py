import pygame
from settings import *

def render_isometric(screen,sprites,camera):
    for sprite in sprites:
        render_rect = camera.apply(sprite)
        iso_x = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF - (render_rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        iso_y = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF + (render_rect.x//TILESIZE) * TILEHEIGHT_HALF)/2
        
        render_rect.x = int(screen.get_rect().centerx/2 + iso_x)
        render_rect.y = int(screen.get_rect().centery + iso_y)
        screen.blit(sprite.image, render_rect)