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
	for key,value in init.visible_screen.items():
		if key == 'tile' and value:
			init.board.draw_map(template.screen, init.screen_pos)
			#highlight the tile the mouse is hovering over
			index = init.board.get_tile_index(tuple(init.last_mouse_info['pos']), init.screen_pos)
			init.board.highlight_tile(template.screen, init.screen_pos, index)
		if key == 'player_tile' and value:
			#loop through all the players
			for i in init.players:
				for j in i.tile:
					init.board.draw_edge_tile(template.screen, init.screen_pos, j, i.color)
		if key == 'tile_extra':
			if value == 'population':
				init.board.draw_population(template.screen, init.screen_pos)	
			elif value == 'resource':
				init.board.draw_resource(template.screen, init.screen_pos)	
			elif value == 'unit':
				init.board.draw_unit(template.screen, init.screen_pos)	
			elif value == 'biulding':
				init.board.draw_biulding(template.screen, init.screen_pos)	
		if key == 'resource' and value: # draw the resources the player have
			draw_resource(player.material.gold, template.RESOURCE_GOLD_2,(0,0))
			draw_resource(player.material.food, template.RESOURCE_FOOD_2,(0,80))
			draw_resource(player.material.science, template.RESOURCE_SCIENCE_2,(0,160))
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