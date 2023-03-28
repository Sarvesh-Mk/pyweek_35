import pygame

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
        for instance in list:
            if instance.id == "wall" and camera.apply(instance).collidepoint((x,y)):
                return True
        return False