import pygame, sys, csv
import math , init
from pygame.locals import *
import init
import template
def draw_resource(value, image, pos):
	temp = pygame.Surface((100,50))
	temp.fill((255,255,255))
	template.screen.blit(temp,pos)	
	template.screen.blit(image,pos)
	template.screen.blit(template.RESOURCE_FONT.render(str(value), 1, (0,0,0)), (pos[0] + 50, pos[1]))
def draw(player):
	template.screen.fill((255,255,255))
	for key,value in init.visible_screen.items():
		if key == 'tile' and value:
			init.board.draw_map(template.screen, init.players[init.current_player_index].screen_pos)
			#highlight the tile the mouse is hovering over
			index = init.board.get_tile_index(tuple(init.last_mouse_info['pos']), init.players[init.current_player_index].screen_pos)
			init.board.highlight_tile(template.screen, init.players[init.current_player_index].screen_pos, index)
		if key == 'player_tile' and value:
			#loop through all the players
			init.board.draw_player_tile(template.screen, init.players[init.current_player_index].screen_pos, init.players)
		if key == 'tile_extra':
			#1 - population
			#2 - resouurce
			#3 - unit
			#4 biulding
			if pygame.key.get_pressed()[pygame.K_1] == True:
				init.board.draw_population(template.screen, init.players[init.current_player_index].screen_pos)
			elif pygame.key.get_pressed()[pygame.K_2] == True:
				init.board.draw_resource(template.screen, init.players[init.current_player_index].screen_pos, init.players[init.current_player_index])	
			elif pygame.key.get_pressed()[pygame.K_3] == True:
				init.board.draw_unit(template.screen, init.players[init.current_player_index].screen_pos)	
			elif pygame.key.get_pressed()[pygame.K_4] == True:
				init.board.draw_biulding(template.screen, init.players[init.current_player_index].screen_pos)	
			elif value == 'population':
				init.board.draw_population(template.screen, init.players[init.current_player_index].screen_pos)	
			elif value == 'resource':
				init.board.draw_resource(template.screen, init.players[init.current_player_index].screen_pos, init.players[init.current_player_index])	
			elif value == 'unit':
				init.board.draw_unit(template.screen, init.players[init.current_player_index].screen_pos)	
			elif value == 'biulding':
				init.board.draw_biulding(template.screen, init.players[init.current_player_index].screen_pos)	
		if key == 'resource' and value: # draw the resources the player have
			draw_resource(player.material.material['gold'], template.RESOURCE_GOLD_2,(0,0))
			draw_resource(player.material.material['food'], template.RESOURCE_FOOD_2,(0,60))
			draw_resource(player.material.material['hammer'], template.RESOURCE_HAMMER_2,(0,120))
			draw_resource(player.material.material['science'], template.RESOURCE_SCIENCE_2,(0,180))
		if key == 'button' and value:
			#next turn
			init.next_turn_button.draw_Button(template.screen, (0, 300))
			#draw card
			init.draw_card_button.draw_Button(template.screen, (0, 400))
			#deleted
			init.delete_card_button.draw_Button(template.screen, (0, 500))
		if key == 'hand' and value:
			player.hand.draw_hand(template.screen)
			player.hand.draw_hovered_card(template.screen, pygame.mouse.get_pos())
		if key == 'discover' and value != None:
			value.draw(template.screen)
	pygame.display.update()


# def draw(pos):
# 	init.screen.fill((255,255,255))
# 	for key,value in init.visible_screen.items():
# 		if key == 'tile' and value:
# 			map.draw_tile(init.screen, init.screen_pos)	
# 			#highlight the tile the mouse is hovering over
# 			index = map.tile_index((pos[0] - init.screen_pos[0],pos[1] - init.screen_pos[1]))
# 			map.map[index[0]][index[1]].draw_highlight(index, init.screen, init.screen_pos)
# 		if key == 'population' and value:
# 			map.draw_population(init.screen, init.screen_pos)
# 		if key == 'hand' and value:	# idx is the card that the mouse is hovering over
# 			for index,i in enumerate(init.hand):
# 				i.draw(init.screen, index)		
# 			if pos[1] > 600:
# 				for index, i in enumerate(init.hand):
# 					if index * (init.card_width + 20) + 100 < pos[0] and (index + 1) * (init.card_width + 20)+ 100 > pos[0]:
# 						# i.draw(screen, index)
# 						i.draw_pos(init.screen, (index * (init.card_width + 20)+ 100, init.card_height - 130))
# 	pygame.display.update()