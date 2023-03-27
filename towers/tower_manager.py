from .tower import Tower
import pygame

class Tower_manager:
    def __init__(self):
        self.tower_list = []

    def add_tower(self, offset, lights):
        mx, my = pygame.mouse.get_pos()
        tower = Tower(mx + offset[0], my + offset[1], 10, (100, 50, 255))
        self.tower_list.append(tower)
        lights.add_entity_light(tower, offset)
    
    def draw(self, screen, offset):
        for tower in self.tower_list:
            tower.draw(screen, offset)
