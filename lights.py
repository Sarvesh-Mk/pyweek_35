import lighting
import math
import pygame


class Lights:
    def __init__(self, screen, offset, map):
        # load the light image
        light_img = pygame.image.load('light.png').convert()

        # define the light box
        self.light_box = lighting.LightBox(screen.get_size())

        # create the lights (mouse_lights will contain a list of the light IDs)
        # just setting a dummy position of [0, 0]. this will be moved later
        self.mouse_lights = [self.light_box.add_light(lighting.Light([0, 0], 80, light_img, (100, 50, 255), 255)) for i in range(9)]
        # light positions relative to the mouse
        self.mouse_light_offsets = [[(i % 3 - 1) * 30, (i // 3 - 1) * 30] for i in range(9)]


        self.visible_walls = self.light_box.render(screen, offset)
        self.light_color = [100, 50, 255]
        lighting.generate_walls(self.light_box, map.data, 25)
        self.moving_box_id = self.light_box.add_dynamic_walls(lighting.box([1200, 100], [20, 20]))
    
    def draw(self, screen, offset):
        self.visible_walls = self.light_box.render(screen, offset)
        # wall lines
        for wall in self.visible_walls:
            wall.render(screen)

    def update(self, timer, offset):
        self.light_box.update_dynamic_walls(self.moving_box_id, lighting.box([1200 + math.sin(timer / 100) * 50, 100 + math.sin(timer / 72) * 100], [(1 + math.sin(timer / 60)) * 50, (1 + math.sin(timer / 65)) * 50]))
        
        # calculate new light color
        light_color = [100 + math.sin(timer / 10) * 100, 50 + math.sin(timer / 25) * 50, 200 + math.sin(timer / 15) * 55]
        # set alpha to 10%
        light_color = [v * 0.2 for v in light_color]

        # Update Lights 
        self.mouse_light_offsets = [[(i % 3 - 1) * math.sin(timer / 40) * 60, (i // 3 - 1) * math.sin(timer / 40) * 60] for i in range(9)]
        mx, my = pygame.mouse.get_pos()
        for i, light in enumerate(self.mouse_lights):
            # True argument overrides light alpha for faster updates
            self.light_box.get_light(light).set_color(light_color, True)
            
            self.light_box.get_light(light).position = [offset[0] + mx + self.mouse_light_offsets[i][0], offset[1] + my + self.mouse_light_offsets[i][1]]
            self.light_box.get_light(light).set_size(int((1 + math.sin(timer / 15)) * 40 + 50))
