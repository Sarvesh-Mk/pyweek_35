import math
import pygame

from . import lighting


class Lights:
    def __init__(self, screen, offset, map):
        # load the light image
        self.light_img = pygame.image.load('lights/light.png').convert()

        # define the light box
        self.light_box = lighting.LightBox(screen.get_size())

        # create the lights (mouse_lights will contain a list of the light IDs)
        # just setting a dummy position of [0, 0]. this will be moved later
        # self.mouse_lights = [self.light_box.add_light(lighting.Light([0, 0], 80, light_img, (100, 50, 255), 255)) for i in range(9)]
        self.mouse_lights = [self.light_box.add_light(lighting.Light([0, 0], 80, self.light_img, (100, 50, 255), 255))]
        # light positions relative to the mouse
        # self.mouse_light_offsets = [[(i % 3 - 1) * 30, (i // 3 - 1) * 30] for i in range(9)]
        self.mouse_light_offsets = [[0,0]]
        self.visible_walls = self.light_box.render(screen, offset)
        self.light_color = [100, 50, 255]
        lighting.generate_walls(self.light_box, map.light_data, 25)

        # A list of lights that will be used to light up entities
        self.entity_lights = []

    def add_entity_light(self, entity, offset):
        # create a light for the entity
        light = lighting.Light([entity.x + offset[0], entity.y + offset[1]], 80, self.light_img, entity.light_color, 255)
        # add the light to the light box
        light_id = self.light_box.add_light(light)
        # add the light to the list of entity lights
        self.entity_lights.append([entity, light_id])
        

    def draw(self, screen, offset):
        mx, my = pygame.mouse.get_pos()
        self.visible_walls = self.light_box.render(screen, offset)
        # wall lines
        # for wall in self.visible_walls:
        #     wall.render(screen)
        
        # dots for light
        for m in self.mouse_light_offsets:
            pygame.draw.circle(screen, (255, 0, 0), (mx + m[0], my + m[1]), 3)
        

    def update(self, timer, offset):
        # calculate new light color
        light_color = [100 + math.sin(timer / 10) * 100, 50 + math.sin(timer / 25) * 50, 200 + math.sin(timer / 15) * 55]
        # set alpha to 10%
        light_color = [v * 0.2 for v in light_color]

        # Update Lights 
        # self.mouse_light_offsets = [[(i % 3 - 1) * math.sin(timer / 40) * 60, (i // 3 - 1) * math.sin(timer / 40) * 60] for i in range(9)]
        mx, my = pygame.mouse.get_pos()
        for i, light in enumerate(self.mouse_lights):
            # True argument overrides light alpha for faster updates
            self.light_box.get_light(light).set_color(light_color, True)
            
            self.light_box.get_light(light).position = [offset[0] + mx + self.mouse_light_offsets[i][0], offset[1] + my + self.mouse_light_offsets[i][1]]
            self.light_box.get_light(light).set_size(50)
            # self.light_box.get_light(light).set_size(int((1 + math.sin(timer / 15)) * 40 + 50))

        for entity, light in self.entity_lights:
            self.light_box.get_light(light).position = [entity.x, entity.y]
            self.light_box.get_light(light).set_size(entity.light_size)
            self.light_box.get_light(light).set_color(entity.light_color, True)