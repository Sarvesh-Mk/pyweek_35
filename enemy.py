import pygame

class enemy():
    #initialise all the attributes of the enemy
    HP = 0
    size = 0
    speed = 0
    colour = pygame.Color.r
    def __init__(self,HP,size,speed):

        #Hp
        self.HP = HP

        #size
        self.size = size

        #speed of the enemy
        self.speed = speed

    def createEnemy(x,y,screen):#this method will draw the enemy on the given screen at the given coordinates
        pygame.draw.rect(screen,colour,pygame.Rect(x,y,size,size))

