import pygame
from settings import *
from world_gen import GenerateMap

class Map:
    def __init__(self, width, height):
        # with open(filename, 'rt') as f:
        #     for line in f:
        #         self.data.append(line.strip())
        map_name = 'generated_map_1.txt'
        self.save_map(map_name, GenerateMap(width, height))
        self.data = self.load_map_from_file(map_name)

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

    def save_map(self, filename, map):
        str_map = ''
        for row in map:
            for col in row:
                str_map += col
            str_map += '\n'
        with open(filename, 'wt') as f:
            f.write(str_map)
                        
    def load_map_from_file(self, filename):
        with open(filename, 'rt') as f:
            data = f.read()
        tile_list = []
        y = 0
        for row in data.split('\n'):
            x = 0
            for col in row:
                if col == '0':
                    tile_list.append([x, y])
                x += 1
            y += 1
        self.data = tile_list
        return tile_list

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        #limit scrolling to map size
        #x = min(0, x)  # left
        #y = min(0, y)  # top
        #x = max(-(self.width - WIDTH), x)  # right
        #y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)