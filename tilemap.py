import pygame
from settings import *


class Tile(pygame.sprite.Sprite):

    def __init__(self,game,x,y,image,id,size=TILESIZE,scale=None):
        pygame.sprite.Sprite.__init__(self, game.tiles)
        self.game = game

        self.id = id
        self.image = image
        self.rect = self.image.get_rect()
        
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

    def update(self):
        ...