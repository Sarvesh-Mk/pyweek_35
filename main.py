import pygame, sys

from os import path

import lighting
from settings import *
from state import *
from controls import *

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.offset = [0, 0]

        # map
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, "levels/mapexample.txt"))
        self.map.load_map(path.join(game_folder, "levels/mapexample.txt"))

        # lighting
        self.light_box = lighting.LightBox(self.screen.get_size())
        self.visible_walls = self.light_box.render(self.screen, self.offset)
        self.light_color = [100, 50, 255]
        lighting.generate_walls(self.light_box, self.map.data, 25)
        self.moving_box_id = self.light_box.add_dynamic_walls(lighting.box([1200, 100], [20, 20]))

        # controls
        self.controls = controls()

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
            self.events()

    def update(self):
        if self.controls.right:
            self.offset[0] += 2
        if self.controls.left:
            self.offset[0] -= 2
        if self.controls.up:
            self.offset[1] -= 2
        if self.controls.down:
            self.offset[1] += 2
        self.all_sprites.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.visible_walls = self.light_box.render(self.screen, self.offset)
        # wall lines
        for wall in self.visible_walls:
            wall.render(self.screen)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            self.controls.keyboard_input(event)
            

g = Game()
while True:
    g.new()
    g.run()
