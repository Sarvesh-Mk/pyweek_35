from settings import *
import pygame


class SpriteController(pygame.sprite.Sprite):
	def __init__(self):
		self.sprites = {}
		self.sprites_names = []

	def load_sprite(self, filename):
		if filename not in self.sprites_names:
			self.sprites_names.append(filename)
			image = pygame.image.load(filename).convert_alpha()
			image = pygame.transform.scale(image, (TILESIZE,TILESIZE))
			self.sprites[filename] = image
			return image
		else: 
			return self.sprites[filename]