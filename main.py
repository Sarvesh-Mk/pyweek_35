import pygame, sys

from os import path

from settings import *
from state import *
from controls import Controls
from enemy import *
from tilemap import *
from lights.lights import Lights
from towers.tower_manager import Tower_manager


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.timer = 0

    
    def new(self):
        self.offset = [WIDTH // 2, HEIGHT // 2]
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.map = Map(100, 50)
        self.camera = Camera(self.map.width, self.map.height)
        
        wall = pygame.image.load("Sprites/wall.png").convert_alpha()
        wall = pygame.transform.scale(wall, (32,32))
        grass = pygame.image.load("Sprites/grass.png").convert_alpha()
        grass = pygame.transform.scale(grass, (32,32)) 

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1' or tile == '0' or tile == 'E':
                    # generate walls here
                    if tile == '1': cur = Tile(self, col, row,grass)
                    elif tile == '0': cur = Tile(self, col, row,wall)
                    elif tile == 'E': 
                        Enemy(self, col, row)
                        cur = Tile(self, col, row,grass)
                    cart_x = row * TILEWIDTH_HALF
                    cart_y = col * TILEHEIGHT_HALF  
                    iso_x = (cart_x - cart_y) 
                    iso_y = (cart_x + cart_y)/2
                    cur.rect.x = self.screen.get_rect().centerx + iso_x
                    cur.rect.y = self.screen.get_rect().centery/2 + iso_y
                    # centered_x = DISPLAYSURF.get_rect().centerx + iso_x
                    # centered_y = DISPLAYSURF.get_rect().centery/2 + iso_y
                # if tile == 'E':
                #     Enemy(self, col, row)
            
        self.lights = Lights(self.screen, self.offset, self.map)
        self.controls = Controls()
        self.tower_manager = Tower_manager()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
            self.events()
            

    def update(self):
        self.timer += 1

        if self.controls.right:
            self.offset[0] += SCROLLSPEED
        if self.controls.left:
            self.offset[0] -= SCROLLSPEED
        if self.controls.up:
            self.offset[1] -= SCROLLSPEED
        if self.controls.down:
            self.offset[1] += SCROLLSPEED

        self.lights.update(self.timer, self.offset)
        self.camera.update(self.offset)
        self.all_sprites.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for sprite in self.tiles:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # for sprite in self.all_sprites:
        #     self.screen.blit(sprite.image, self.camera.apply(sprite))
        
        self.lights.draw(self.screen, self.offset)

        self.tower_manager.draw(self.screen, self.offset)
        pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            self.controls.keyboard_input(event)
            mouse_event = self.controls.mouse_input(event)
            if mouse_event == 1:
                x, y = pygame.mouse.get_pos()
                if self.map.get_tile(x, y, self.offset) == '1':
                    self.tower_manager.add_tower(self.offset, self.lights)

if __name__ == "__main__":               
    g = Game()
    while True:
        g.new()
        g.run()
