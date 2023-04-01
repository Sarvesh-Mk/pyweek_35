import pygame, sys
import pygame_gui
from os import path

from settings import *
from state import *
from controls import Controls
from enemy import *
from spriteController import *
from tilemap import *
from lights import *

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.show_enemies = False
        self.selected = False

    
    def new(self):
        self.offset = [WIDTH // 2, HEIGHT // 2]
        self.all_sprites = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.lights = []
        self.sprites = []
        self.map = Map(100, 100)
        self.camera = Camera(self.map.width, self.map.height)
        self.spriteController = SpriteController()

        for row, tiles in enumerate(self.map.data):
            self.sprites.append([])
            for col, tile in enumerate(tiles):
                if tile == '1': self.sprites[row].append(Tile(self, col, row, self.spriteController.load_sprite("Sprites_all/grass_2.png"),"grass"))
                elif tile == '0': self.sprites[row].append(Tile(self, col, row,self.spriteController.load_sprite("Sprites_all/air.png"),"air"))
                elif tile == 'E': 
                    Enemy(self, col, row,self.spriteController.load_sprite("Sprites_all/enemy.png"))
                    self.sprites[row].append(Tile(self, col, row,self.spriteController.load_sprite("Sprites_all/grass_2.png"),"grass"))

        self.controls = Controls()
        
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(BACKGROUND_COLOR)
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))
        # self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),text='Say Hello',manager=self.manager)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
        
            

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

        self.camera.update(self.offset)
        self.all_sprites.update()
        self.tiles.update()
        self.manager.update(self.dt)


    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.blit(self.background, (0,0))

        render_lighting(self.sprites, self.lights)
        for sprite in self.tiles:
            sprite.render_isometric()
        if self.show_enemies:
            for sprite in self.all_sprites:
                sprite.render_isometric()
        # if self.selected != False:
        #     self.selected.render_isometric()
        
        self.manager.draw_ui(self.screen)
        
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
                if event.key == pygame.K_1:
                    self.show_enemies = not self.show_enemies
            self.controls.keyboard_input(event)
            self.manager.process_events(event)
            mouse_event = self.controls.mouse_input(event)
            if mouse_event == 1 and self.selected:
                self.selected.image = self.spriteController.load_sprite("Sprites_all/light.png")
                self.selected.id = "light"
                self.lights.append(self.selected)
        x, y = pygame.mouse.get_pos()
        if self.selected != False:
            self.selected.selected = False
        self.selected = self.controls.collide_group(x,y,self.tiles,self.camera)
        if self.selected != False:
            self.selected.selected = True

if __name__ == "__main__":               
    g = Game()
    while True:
        g.new()
        g.run()
