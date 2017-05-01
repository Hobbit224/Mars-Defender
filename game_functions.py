# Importations
import pygame
import sys
from bullet import Bullet
from player import Player
import time



# screen_size = (1000, 800)
# screen = pygame.display.set_mode(screen_size)


def check_events(the_player, screen, bullets):


	paused = False

	# Colors
	black = (0,0,0)
	white = (255,255,255)
	mars_red = (214, 51, 56)
	red = (200,0,0)
	bright_red = (255,0,0)
	green = (0, 200, 0)
	bright_green =(0, 255, 0)



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
				elif action == "pause":
					pause()
				elif action == "unpause":
					unpause()




	def pause_text(text, font):
		textSurface = font.render(text, True, mars_red)
		return textSurface, textSurface.get_rect()


	def unpause():
		# global paused 
		paused = False

	def pause():	
		paused = True
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			screen.fill(black)
			large_text = pygame.font.Font('freesansbold.ttf', 115)
			TextSurf, TextRect = pause_text("Paused", large_text)
			TextRect.center = ((500),(400))
			screen.blit(TextSurf, TextRect)
			


			# button_function("Continue",200,550,100,50,green,bright_green,"unpause")
			# button_function("Quit",700,550,100,50,red,bright_red,"quit")

			pygame.display.update()



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
			elif event.key == 112 and paused == False:
				pause()
			elif event.key == 112 and paused == True:
				unpause()
					


			 
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


	
