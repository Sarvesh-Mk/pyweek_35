import pygame
from settings import *

class enemy(pygame.sprite.Sprite):
    #initialise all the attributes of the enemy
    colour = pygame.Color.r
    def __init__(self,game,x,y,HP=5,size=TILESIZE,speed=ENEMY_SPEED):
        pygame.sprite.Sprite.__init__(self, game.all_sprites)
        self.game = game

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.x, self.y = x, y
        self.HP = HP
        self.size = size
        self.speed = speed
        

    def update(self):
        self.rect.x, self.rect.y = self.x * TILESIZE, self.y * TILESIZE

    # def draw(self):
    #     pygame.draw.rect(self.game.screen,enemy.colour,pygame.Rect(self.x,self.y,self.size,self.size))

