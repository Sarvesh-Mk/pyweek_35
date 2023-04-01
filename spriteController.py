from settings import *
import pygame


class SpriteController(pygame.sprite.Sprite):
	def __init__(self):
		self.sprites = {}
		self.sprite_lists = {}
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
		
	def load_sprite_list(self, start, end, filename):
		if filename not in self.sprites_names:
			self.sprites_names.append(filename) 
			l = []
			for x in filename:
				if x == ' ':
					pos = x
					string = filename.split(" ")

			for x in range(start, end):
				l.append(pygame.image.load(str(x).join(string)))
			
			self.sprite_lists[filename] = l
		
		else:
			return self.sprite_lists[filename]