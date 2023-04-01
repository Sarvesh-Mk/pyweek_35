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
        
        self.iso_y -= TILEHEIGHT_HALF
        # self.iso_x, self.iso_y = move_x_up(self.iso_x,self.iso_y)
        # self.iso_x, self.iso_y = move_y_up(self.iso_x,self.iso_y)
        #self.iso_x, self.iso_y = move_x_down(self.iso_x,self.iso_y)
        #self.iso_x, self.iso_y = move_y_down(self.iso_x,self.iso_y)

        render_rect.x = self.iso_x# int(self.game.screen.get_rect().x/2 + self.iso_x)
        render_rect.y = self.iso_y# int(self.game.screen.get_rect().y + self.iso_y)
        
        self.game.screen.blit(self.image, render_rect)

