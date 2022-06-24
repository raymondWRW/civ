import card.card, card.hand
import material
"""
Science	
	1.whenever population grows draw one card
	2.drawing card cost one less
	3.removing card gain one extra science
"""
class Administration(card.card.Card):
	def __init__(self):
		super().__init__('administration')
	def evaluate(self, board, players, visible_screen, order, player_index):
		players[player_index].sciencebonus = 'administration'
		return 1
	def valid (self, finished):
		return True

class EfficiantProduction(card.card.Card):
	def __init__(self):
		super().__init__('scientific conversation')
	def evaluate(self, board, players, visible_screen, order, player_index):
		players[player_index].sciencebonus = 'scientific conversation'
		return 1
	def valid (self, finished):
		return True

class Insight(card.card.Card):
	def __init__(self):
		super().__init__('insight')
	def evaluate(self, board, players, visible_screen, order, player_index):
		players[player_index].sciencebonus = 'insight'
		return 1
	def valid (self, finished):
		return True

class ClassicalScience(card.card.Card):
	def __init__(self):
		super().__init__('classical science',[('science', 5)])
		self.future_tech = ['animal husbandry']
		self.discover = card.hand.Hand((240, 300), 200,(100, 280))
		self.discover.add_card(Administration())
		self.discover.add_card(EfficiantProduction())
		self.discover.add_card(Insight())
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			return 0
		if len(order) == 2:
			visible_screen['discover'] = self.discover	
		if len(order) == 3:
			if order[2][0] == 'leftclick' and order[2][1] == 'discover card':
				self.discover.hand[order[2][2]].evaluate(board, players, visible_screen, order, player_index)
				players[player_index].material.remove_material(self.cost)
				return 1
			return 0
		return -1
	def valid (self, finished):
		if 'classical science' in finished:
			return True
		return False

class AnimalHusbandry(card.card.Card):
	def __init__(self):
		super().__init__('animal husbandry',[('science', 5)])
		self.future_tech = ['pasture']
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			return 0
		players[player_index].material.remove_material(self.cost)
		players[player_index].material.add_material([('food', 5),('hammer', 1)])
		players[player_index].income.add_material([('horse', 1)])
		return 1
	def valid (self, finished):
		if 'classical science' in finished:
			return True
		return False

class Pasture(card.card.Card):
	def __init__(self):
		super().__init__('Pasture',[('science', 7)])
		self.future_tech = []
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			return 0
		players[player_index].material.remove_material(self.cost)
		for i in range(len(players[player_index].tile_resource['plain'])):
			players[player_index].tile_resource['plain'][i][0] = 'horse'
			players[player_index].tile_resource['plain'][i][1] += 1	
			return 1
		players[player_index].tile_resource['plain'].append(('horse', 1))
		return 1
	def valid (self, finished):
		if 'animal husbandry' in finished:
			return True
		return False

class TechTree():
	def __init__(self):
		self.finished = set()
		self.current = [('classical science', ClassicalScience())]
		self.science_tech = {
			'classical science' : ClassicalScience(),
			'animal husbandry' :  AnimalHusbandry(),
			'pasture' : Pasture()
			# 'order&labor', 
			# 'wood working', 
			# 'irrigation', 
			# 'fishing',
		}
		self.military_tech = {
			'celestial navigation','greek fire',
			'tower', 'engineering',
			'standard uniform','military trandition','bronze weapon', 	
			'cavalary', 'horseback riding'
		}

class ScientificAdvancement(card.card.Card):
	def __init__(self):
		super().__init__('scientific advancement', [])
	def evaluate(self, board, players, visible_screen, order, player_index):
		player_tech = players[player_index].techtree
		if len(order) == 1:
			# (50, 600), 120,(100, 280)
			temp = card.hand.Hand((600 - 200 * len(player_tech.current) + 100,300), 300,(100, 280))
			for i in player_tech.current:
				temp.add_card(i[1])
			visible_screen['discover'] = temp
		elif order[1][0] == 'leftclick' and order[1][1] == 'discover card':
			current_tech = players[player_index].techtree.current[order[1][2]]
			ret = current_tech[1].evaluate(board, players, visible_screen, order, player_index)
			"""
			1 = success
			0 = fail
			-1 = still evaluating
			"""
			if ret == 1: # played succesfully
				player_tech.finished.add(current_tech[0])
				for i in current_tech[1].future_tech:
					avalible = True
					for j in player_tech.current:
						if i == j[0]:
							avalible = False
					if i in players[player_index].techtree.finished:
						avalible = False
					if avalible:# the tech is not researched
						if current_tech[1].valid(player_tech.finished):# avalible
							player_tech.current.append((i, player_tech.science_tech[i]))					
				player_tech.current.pop(order[1][2])
			if ret == 0 or ret == 1:
				visible_screen['discover'] = None
				visible_screen['tile_extra'] = 'unit'
				order.clear()
		else:
			visible_screen['discover'] = None
			visible_screen['tile_extra'] = 'unit'
			order.clear()
