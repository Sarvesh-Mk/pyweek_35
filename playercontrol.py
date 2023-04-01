import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.a]:
            self.x -= self.speed
        elif keys[pygame.d]:
            self.x += self.speed
        elif keys[pygame.w]:
            self.y -= self.speed
        elif keys[pygame.s]:
            self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), 20)
       
