import pygame

class enemy():
    #initialise all the attributes of the enemy
    HP = 0
    size = 0
    speed = 0
    colour = pygame.Color.r
    def __init__(self,HP,size,speed):
        self.HP = HP
        self.size = size
        self.speed = speed
    def createEnemy(screen,x,y):#this method will draw the enemy on the given screen at the given coordinates
        pygame.draw.rect(screen,colour,pygame.Rect(x,y,size,size))

