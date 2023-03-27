import pygame


class Tower:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen, offset):
        pygame.draw.circle(screen, self.color, (self.x - offset[0], self.y - offset[1]), self.radius)
