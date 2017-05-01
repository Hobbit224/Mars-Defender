import pygame
from pygame.sprite import Sprite
import math

class Enemy(Sprite):
	def __init__(self, screen, start_x):
		super(Enemy, self).__init__()
		self.image = pygame.image.load('./images/Enemyship1.png')
		self.image = pygame.transform.scale(self.image, (92, 92))
		self.speed = 10
		self.start_x = start_x
		# self.start_y = 0
		self.y = 0
		self.screen = screen
		self.rect = self.image.get_rect()
		self.rect.left = self.start_x
		self.rect.top = self.y

	def draw_me (self):
		self.screen.blit(self.image, [self.start_x, self.y])
		self.rect.left = self.start_x
		self.rect.top = self.y

	def update_me(self):
		self.y += self.speed
