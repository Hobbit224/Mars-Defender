import pygame
from pygame.sprite import Sprite


# Create the player class

class Player(Sprite):
	def __init__(self, screen):
		super(Player, self).__init__()
		self.image = pygame.image.load('./Images/MDship.png')
		self.image = pygame.transform.scale(self.image, (92, 92))
		self.x = 408
		self.y = 700
		self.speed = 15
		self.screen = screen
		# self.should_move_up = False
		# self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
		self.rect = self.image.get_rect()

	def draw_me(self):
		# if(self.should_move_up):
		# 	self.y -= self.speed
		# elif(self.should_move_down):
		# 	self.y += self.speed
		if(self.should_move_right):
			self.x += self.speed
		elif(self.should_move_left):
			self.x -= self.speed
		self.screen.blit(self.image,[self.x, self.y])
		self.rect.left = self.x
		self.rect.top = self.y

	def should_move(self, direction, true_or_false):
		# if(direction == "up"):
		# 	self.should_move_up = true_or_false
		# elif(direction == "down"):
		# 	self.should_move_down = true_or_false
		if(direction == "left"):
			self.should_move_left = true_or_false
		elif(direction == "right"):
			self.should_move_right = true_or_false

