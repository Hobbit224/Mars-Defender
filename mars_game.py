# Importations
import pygame
from game_functions import check_events
from player import Player
from pygame.sprite import Group, groupcollide
from bullet import Bullet
from baddies import Enemy
from random import randint


# Main Game function

def run_game():
	# Initialize pygame
	pygame.init()
	# Set up tuple for screen size
	screen_size = (1000, 800)
	# Set up a tuple for the bg color
	background_color = (214, 51, 56)

	# Create pygame screen to use
	screen = pygame.display.set_mode(screen_size)
	# Set a title for the game window
	pygame.display.set_caption("Mars Defender")


	baddy_position = randint(0, 900)

	# Instantiate the player
	the_player = Player(screen)
	# Instantiate the bullet
	bullet = Bullet(screen, the_player)
	# Instantiate the enemy
	baddy = Enemy(screen, baddy_position)



	the_player_group = Group()
	the_player_group.add(the_player)
	enemies = Group()
	enemies.add(baddy)
	bullets = Group()
	bullet = Bullet(screen, the_player)

	
	# Main game loop
	while 1:

		# Create background color
		screen.fill(background_color)
		# Draw the player
		for player in the_player_group:
			the_player.draw_me()



		# Draw and update the baddies
		for enemy in enemies:
			baddy.draw_me()
			baddy.update_me()


		# Make the bullets
		for bull in bullets:
			bullet.update()
			bullet.draw_bullet()

			
		# Keep the screen up
		pygame.display.flip()


		



		# Run the functions
		check_events(the_player, screen, bullets)


# Calling the game function
run_game()

