import pygame
from settings import *

class Controls:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    
    def keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.right = True
            if event.key == pygame.K_a:
                self.left = True
            if event.key == pygame.K_s:
                self.down = True
            if event.key == pygame.K_w:
                self.up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.right = False
            if event.key == pygame.K_a:
                self.left = False
            if event.key == pygame.K_s:
                self.down = False
            if event.key == pygame.K_w:
                self.up = False

    def mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return 1
            if event.button == 3:
                return 3
        return 0
    
    def collide_group(self, x, y, list, camera):
        l = []
        for g in list:
            l.append(g)
        for instance in reversed(l):
            if instance.id != "wall":
                render_rect = camera.apply(instance)
                iso_x = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF - (render_rect.x//TILESIZE) * TILEHEIGHT_HALF) 
                iso_y = ((render_rect.y//TILESIZE) * TILEWIDTH_HALF + (render_rect.x//TILESIZE) * TILEHEIGHT_HALF)/2
                render_rect.x, render_rect.y = iso_x, iso_y
                if render_rect.collidepoint((x,y)):
                    return instance
        return False