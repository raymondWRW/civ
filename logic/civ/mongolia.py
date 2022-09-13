from logic.civ.civ import Civ
from coreFunction.dictionaryExtended import add_value
from logic.modifier import modPasture
class Mongolia(Civ):
	def __init__(self, player_index):
		super().__init__(player_index, (0,102,179))
		self.name = 'Mongolia'
	def start_game(self):
		super().start_game()
		self.tile['plain']['modifier']['resource'].append(modPasture)
		self.tech['pasture'].researched = True
		self.unit['cavalry']['max movement'] += 1

  