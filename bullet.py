import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, hero):
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, 5, 20)
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		self.color = (0,0,0)
		self.speed = 5
		self.y = self.rect.y
		self.x = self.rect.x
		self.direction = 'up'

	def update(self):
		if self.direction == 'up':
			self.y -= self.speed
			self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)