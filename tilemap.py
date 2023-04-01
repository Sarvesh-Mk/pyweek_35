import pygame
from settings import *


class Tile(pygame.sprite.Sprite):

    def __init__(self,game,x,y,image,id,size=TILESIZE,scale=None):
        pygame.sprite.Sprite.__init__(self, (game.tiles,game.all_sprites))
        self.game = game

        self.id = id
        self.image = image
        self.rect = self.image.get_rect()
        
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

        # self.iso_x = ((self.rect.y//TILESIZE) * TILEWIDTH_HALF - (self.rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        # self.iso_y = ((self.rect.y//TILESIZE) * TILEWIDTH_HALF + (self.rect.x//TILESIZE) * TILEHEIGHT_HALF)/2

    def update(self):
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE
    
    def render_isometric(self):
        render_rect = self.game.camera.apply(self)
        self.iso_x = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF - (render_rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        self.iso_y = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF + (render_rect.x//TILESIZE) * TILEHEIGHT_HALF)/2
        
        render_rect.x = int(self.game.screen.get_rect().centerx/2 + self.iso_x)
        render_rect.y = int(self.game.screen.get_rect().centery + self.iso_y)
        
        self.game.screen.blit(self.image, render_rect)