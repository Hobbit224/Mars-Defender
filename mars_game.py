# Importations
import pygame
from game_functions import check_events
from player import Player
from pygame.sprite import Group, groupcollide
from bullet import Bullet


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



	# Instantiate the player
	the_player = Player(screen)
	# bad_guy = Enemy(screen)
	the_player_group = Group()
	the_player_group.add(the_player)
	enemies = Group()
	# enemies.add(bad_guy)
	bullets = Group()

	# Instantiate the bullet
	bullet = Bullet(screen, the_player)
	# Main game loop
	while 1:

		# Create background color
		screen.fill(background_color)
		# Draw the player
		for player in the_player_group:
			the_player.draw_me()


		# Keep the screen up
		pygame.display.flip()


		# Make the bullets
		for bullet in bullets:
			bullet.update()
			bullet.draw_bullet()
			


		# Run the functions
		check_events(the_player, screen, bullets)


# Calling the game function
run_game()
