import pygame, os,sys
import init, draw, evaluate
pygame.init()
while True:
	draw.draw(init.players[init.current_player_index])
	evaluate.mouse_input()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
