# Importations
import pygame
import sys
from bullet import Bullet
from player import Player

def check_events(the_player, screen, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			print event.key
			# if event.key == 273:
				# the_player.should_move("up", True)
			# elif event.key == 274:
				# the_player.should_move("down", True)
			if event.key == 275:
				the_player.should_move("right", True)
			elif event.key == 276:
				the_player.should_move("left", True)
			elif event.key == 32:
				# User pressed spacebar, fire!
				# for direction in range(1,5):
				new_bullet = Bullet(screen,the_player)
				bullets.add(new_bullet)
			


			 
		elif event.type == pygame.KEYUP:
			# if event.key == 273:
			# 	the_player.should_move("up", False) 
			# if event.key == 274:
			# 	the_player.should_move("down", False) 
			if event.key == 276:
				the_player.should_move("left", False) 
			if event.key == 275:
				the_player.should_move("right", False)


	# Creating the bounderies
	if the_player.x <= 0:
		the_player.x = 0
	if the_player.x >= 908:
		the_player.x =908
