# Importations
import pygame
from game_functions import check_events
from player import Player
from pygame.sprite import Group, groupcollide
from bullet import Bullet
from baddies import Enemy
from random import randint
import time


# Set up tuple for screen size
screen_size = (1000, 800)
# Set up a tuple for the bg color
background_color = (214, 51, 56)

# Create pygame screen to use
screen = pygame.display.set_mode(screen_size)
# Set a title for the game window
pygame.display.set_caption("Mars Defender")

clock = pygame.time.Clock()

# Colors
black = (0,0,0)
white = (255,255,255)
mars_red = (214, 51, 56)
red = (200,0,0)
bright_red = (255,0,0)
green = (0, 200, 0)
bright_green =(0, 255, 0)

def title_text(text, font):
	textSurface = font.render(text, True, mars_red)
	return textSurface, textSurface.get_rect()

def button_text(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()


	# (message, x, y, width, height, inactive color, active color)
def button_function(msg,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
		# Green start
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen, ac, (x, y, w, h))
		if click[0] == 1 and action != None:
			if action == "play":
				run_game()
			elif action == "quit":
				pygame.quit()

	else:
		pygame.draw.rect(screen, ic, (x, y, w, h))

	# Making the start button text
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	text_surf1, text_rect1 = button_text(msg, small_text)
	text_rect1.center = ((x+(w/2)), (y+(h/2)))
	screen.blit(text_surf1, text_rect1)







def game_intro():

	# Initialize pygame
	pygame.init()
	

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		screen.fill(black)
		large_text = pygame.font.Font('freesansbold.ttf', 115)
		TextSurf, TextRect = title_text("Mars Defender", large_text)
		TextRect.center = ((500),(400))
		screen.blit(TextSurf, TextRect)


		button_function("Defend Mars!",200,550,100,50,green,bright_green,"play")
		button_function("Quit",700,550,100,50,red,bright_red,"quit")
		




		pygame.display.update()
		clock.tick(15)


# Main Game function

def run_game():


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
			bull.update()
			bull.draw_bullet()




		# Run the functions
		check_events(the_player, screen, bullets)

		# Check for collisions
		hero_died = groupcollide(the_player_group, enemies, True, False)
		enemy_died = groupcollide(bullets, enemies, True, True)

		# Make new enemies
		if enemy_died:
			baddy_position = randint(0, 900)

			baddy = Enemy(screen, baddy_position)
			enemies.add(baddy)


		# Keep the screen up
		pygame.display.flip()


# Calling the game function
game_intro()

