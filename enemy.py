import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    #initialise all the attributes of the enemy
    def __init__(self,game,x,y,image,HP=5,size=TILESIZE,speed=ENEMY_SPEED):
        pygame.sprite.Sprite.__init__(self, game.all_sprites)
        self.game = game

        self.image = image
        self.rect = self.image.get_rect()
        
        self.x, self.y = x, y
        self.HP = HP
        self.size = size
        self.speed = speed
        

    def update(self):
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

    def render_isometric(self):
        render_rect = self.game.camera.apply(self)
        self.iso_x = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF - (render_rect.x//TILESIZE) * TILEHEIGHT_HALF) 
        self.iso_y = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF + (render_rect.x//TILESIZE) * TILEHEIGHT_HALF)/2
        
        render_rect.x = int(self.game.screen.get_rect().centerx/2 + self.iso_x)-TILESIZE+10
        render_rect.y = int(self.game.screen.get_rect().centery + self.iso_y)-TILESIZE+10

        self.game.screen.blit(self.image, render_rect)

