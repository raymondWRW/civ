import pygame
from map.tile import Tile
import template
pygame.init()
import unit,template
#cost:	

class Card:
	def  __init__(self, name = 'card', cost_food = 0, cost_hammer = 0, cost_powerpoint = 0):
		self.image = pygame.image.load("image/cardImage/card.png").convert_alpha()
		self.name = name
		self.mask = pygame.mask.from_surface(self.image)		
		self.cost_food = cost_food
		self.cost_hammer = cost_hammer
		self.cost_powerpoint = cost_powerpoint
	def draw_pos(self, screen, pos):
		screen.blit(self.image, pos)
		# might need to center the text in the future
		screen.blit(template.CARD_TITLE_FONT.render(self.name, 1, (0,0,0)), (pos[0] + 20, pos[1] + 10))
	def evaluate(self, board, players, visible_screen, order, player_index):
		players[player_index].hand.remove_card(order[0][2])
		order.clear()
		
class PopulationGrowth(Card):
	def  __init__(self):
		super().__init__('population growth')
	def evaluate(self, board, players, visible_screen, order, player_index):
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'tile':
				if board[order[1][2][0]][order[1][2][1]].pop.max_pop > board[order[1][2][0]][order[1][2][1]].pop.cur_pop:
					board[order[1][2][0]][order[1][2][1]].pop.cur_pop += 1
					players[player_index].hand.remove_card(order[0][2])
			visible_screen['tile_extra'] = None
			order.clear()

class Warrior(Card):
	def  __init__(self):
		super().__init__('warrior')
	def evaluate(self, board, players, visible_screen, order, player_index):
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'tile':
				# print(board[order[1][2][0]][order[1][2][1]])
				if board[order[1][2][0]][order[1][2][1]].pop.cur_pop > 0 and board[order[1][2][0]][order[1][2][1]].player_index == player_index:
					board[order[1][2][0]][order[1][2][1]].pop.cur_pop -= 1
					board[order[1][2][0]][order[1][2][1]].unit = unit.Unit(template.UNIT_WARRIOR, 'warrior', player_index, players[player_index].unit_stat['warrior'], players[player_index].color)
					players[player_index].hand.remove_card(order[0][2])
					players[player_index].unit.append(order[1][2])
			visible_screen['tile_extra'] = 'unit'
			order.clear()
			
				
    
