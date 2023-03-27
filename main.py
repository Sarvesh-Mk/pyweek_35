import pygame, sys

from os import path

from settings import *
from state import *
from controls import Controls
from lights import Lights

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.timer = 0

        self.offset = [0, 0]

        # map
        game_folder = path.dirname(__file__)
        self.map = Map(100, 40)
        # self.map.load_map(path.join(game_folder, "levels/mapexample.txt"))

        # lighting
        self.lights = Lights(self.screen, self.offset, self.map)

        # controls
        self.controls = Controls()

    
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
        self.timer += 1

        if self.controls.right:
            self.offset[0] += 2
        if self.controls.left:
            self.offset[0] -= 2
        if self.controls.up:
            self.offset[1] -= 2
        if self.controls.down:
            self.offset[1] += 2

        self.lights.update(self.timer, self.offset)
        self.all_sprites.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.lights.draw(self.screen, self.offset)

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
