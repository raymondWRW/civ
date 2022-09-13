from data.dataGame import *
from coreFunction.dictionaryExtended import *
class Tile:
	def  __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.building = 'none'
		self.housing = 'none'
		self.player_index = 0
		self.population = 0
		self.unit = None
	# resource
	def tile_resource(self):
		temp = {}
		add_value(temp, player[self.player_index].tile[self.name]['resource'])
		add_value(temp, player[self.player_index].building[self.building]['resource'])
		for i in player[self.player_index].tile[self.name]['modifier']['resource']:
			add_value(temp, i(self.pos))
		for i in player[self.player_index].building[self.building]['modifier']['resource']:
			add_value(temp, i(self.pos))
		return temp
	# population
	def max_population(self):
		current_player = player[self.player_index]
		pop = 0
		pop += current_player.tile[self.name]['housing']
		pop += current_player.building[self.building]['housing']
		pop += current_player.building[self.housing]['housing']
		return pop