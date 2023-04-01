import pygame
from settings import *


class Tile(pygame.sprite.Sprite):

    def __init__(self,game,x,y,image,id,size=TILESIZE,scale=None):
        pygame.sprite.Sprite.__init__(self, (game.tiles))
        
        self.game = game

        self.id = id
        self.image = image
        self.rect = self.image.get_rect()
        
        self.selected = False
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

        self.is_shadow = False
        self.shadow =pygame.Surface((image.get_width(), image.get_height()), flags=pygame.SRCALPHA)
        self.shadow.fill((10, 10, 10, 0))
        # image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        # self.iso_x = ((self.rect.y//TILESIZE) * TILEWIDTH_HALF - (self.rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        # self.iso_y = ((self.rect.y//TILESIZE) * TILEWIDTH_HALF + (self.rect.x//TILESIZE) * TILEHEIGHT_HALF)/2

    def update(self):
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE
    
    def render_isometric(self):
        render_rect = self.game.camera.apply(self)
        self.iso_x = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF - (render_rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        self.iso_y = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF + (render_rect.x//TILESIZE) * TILEHEIGHT_HALF)/2
        
        if self.selected:
            self.iso_y -= TILEHEIGHT_HALF

        if self.id == "light":
            self.iso_y -= TILEHEIGHT_HALF

        render_rect.x = self.iso_x# int(self.game.screen.get_rect().x/2 + self.iso_x)
        render_rect.y = self.iso_y# int(self.game.screen.get_rect().y + self.iso_y)
        
        self.game.screen.blit(self.image, render_rect)
        if self.is_shadow:
            self.image.blit(self.shadow, (0,0), special_flags=pygame.BLEND_RGBA_SUB)
        