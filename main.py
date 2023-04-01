import pygame, sys

from os import path

from settings import *
from state import *
from controls import Controls
from enemy import *
from spriteController import *
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
        self.spriteController = SpriteController()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1': Tile(self, col, row, self.spriteController.load_sprite("Sprites_all/grass_2.png"),"grass")
                elif tile == '0': Tile(self, col, row,self.spriteController.load_sprite("Sprites_all/wall.png"),"wall")
                elif tile == 'E': 
                    Enemy(self, col, row,self.spriteController.load_sprite("Sprites_all/enemy.png"))
                    Tile(self, col, row,self.spriteController.load_sprite("Sprites_all/grass_2.png"),"grass")
            
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
            self.offset[0] -= SCROLLSPEED
        elif self.controls.left:
            self.offset[0] += SCROLLSPEED
        elif self.controls.up:
            self.offset[1] -= SCROLLSPEED
        elif self.controls.down:
            self.offset[1] += SCROLLSPEED

        self.lights.update(self.timer, self.offset)
        self.camera.update(self.offset)
        self.all_sprites.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        for sprite in self.all_sprites:
            sprite.render_isometric()
        
        # self.lights.draw(self.screen, self.offset)

        # self.tower_manager.draw(self.screen, self.offset)
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
                if not self.controls.collide_group(x,y,self.tiles,self.camera):
                    self.tower_manager.add_tower(self.offset, self.lights)

if __name__ == "__main__":               
    g = Game()
    while True:
        g.new()
        g.run()
