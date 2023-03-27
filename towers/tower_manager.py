from .tower import Tower
import pygame

class Tower_manager:
    def __init__(self):
        self.tower_list = []

    def add_tower(self, offset):
        mx, my = pygame.mouse.get_pos()
        tower = Tower(mx + offset[0], my + offset[1], 10, (255, 0, 0))
        self.tower_list.append(tower)
    
    def draw(self, screen, offset):
        for tower in self.tower_list:
            tower.draw(screen, offset)