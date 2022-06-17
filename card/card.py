import pygame
from map.tile import Tile
import template
pygame.init()
import unit,template, material
#cost:	

class Card:
	def  __init__(self, name = 'card', cost = material.Material()):
		self.name = name
		self.image = pygame.image.load("image/cardImage/card.png").convert_alpha()
		self.image.blit(template.CARD_TITLE_FONT.render(self.name, 1, (0,0,0)), (20, 10))
		self.mask = pygame.mask.from_surface(self.image)		
		self.cost = cost
	def draw_pos(self, screen, pos):
		temp = self.image	
		index = 0
		for i in self.cost:
			res = template.cost_image[i[0]]
			for j in range(i[1]):
				pygame.draw.circle(temp,(255,255,255),(10 + index * template.CELL_SIZE + template.CELL_SIZE, 20 + template.CELL_SIZE),template.CELL_SIZE)
				temp.blit(res, (10 + index * template.CELL_SIZE, 20))
				index += 1
		screen.blit(temp, pos)
		# might need to center the text in the future
		# screen.blit(template.CARD_TITLE_FONT.render(self.name, 1, (0,0,0)), (pos[0] + 20, pos[1] + 10))

	def evaluate(self, board, players, visible_screen, order, player_index):
		if players[player_index].material.greater(self.cost):
			players[player_index].material.remove_material(self.cost)
			pass
		players[player_index].hand.remove_card(order[0][2])
		order.clear()
		
class PopulationGrowth(Card):
	def  __init__(self):
		super().__init__('population growth', [('food', 5)])
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'tile':
				if players[player_index].add_population(board, order[1][2]):
					players[player_index].material.remove_material(self.cost)
					players[player_index].hand.remove_card(order[0][2])
					players[player_index].deck.add_card(PopulationGrowth())
			visible_screen['tile_extra'] = 'unit'
			order.clear()

class Warrior(Card):
	def  __init__(self):
		super().__init__('warrior', [('food', 10),('hammer',1),('gold', 5)])
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'tile' and board[order[1][2][0]][order[1][2][1]].unit == None:
				if players[player_index].remove_population(board, order[1][2]):
					board[order[1][2][0]][order[1][2][1]].unit = unit.Unit(template.UNIT_WARRIOR, 'warrior', player_index, players[player_index].unit_stat['warrior'], players[player_index].color)
					players[player_index].unit.append(order[1][2])
					players[player_index].material.remove_material(self.cost)
					players[player_index].hand.remove_card(order[0][2])
					players[player_index].deck.add_card(Warrior())
			visible_screen['tile_extra'] = 'unit'
			order.clear()
   
class Farm(Card):
	def  __init__(self):
		super().__init__('Farm',[('food', 5),('hammer',1)])
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'tile':
				if players[player_index].add_biulding(board, order[1][2], 'farm'):
					players[player_index].material.remove_material(self.cost)
					players[player_index].hand.remove_card(order[0][2])
					players[player_index].deck.add_card(Farm())
			visible_screen['tile_extra'] = 'unit'
			order.clear()
			

    



# technology
"""
military
	1. units are 10% cheaper
	2. mil tech cost 1 less research point
	3. killing unit reward 1/2/3 research point
"""
"""
Science	
	1.whenever population grows draw one card
	2.gain one research point every 5/3/1 turn
	3.
"""

#science
class ScienceAdvancement(Card):
	def  __init__(self):
		super().__init__('ScienceAdvancement',material.Material(0,0,0,0))
	# def evaluate(self, board, players, visible_screen, order, player_index)

# military
class MilitaryAdvancement(Card):
	def  __init__(self):
		super().__init__('MilitaryAdvancement',material.Material(0,0,0,0))