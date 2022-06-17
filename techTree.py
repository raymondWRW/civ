import card.card, card.hand
import material
# class Card:
# 	def  __init__(self, name = 'card', cost = material.Material()):
# 		self.name = name
# 		self.image = pygame.image.load("image/cardImage/card.png").convert_alpha()
# 		self.image.blit(template.CARD_TITLE_FONT.render(self.name, 1, (0,0,0)), (20, 10))
# 		self.mask = pygame.mask.from_surface(self.image)		
# 		self.cost = cost
# 	def draw_pos(self, screen, pos):
# 		temp = self.image	
# 		index = 0
# 		for i in self.cost:
# 			res = template.cost_image[i[0]]
# 			for j in range(i[1]):
# 				pygame.draw.circle(temp,(255,255,255),(10 + index * template.CELL_SIZE + template.CELL_SIZE, 20 + template.CELL_SIZE),template.CELL_SIZE)
# 				temp.blit(res, (10 + index * template.CELL_SIZE, 20))
# 				index += 1
# 		screen.blit(temp, pos)


class TechTree():
	def __init__(self):
		self.finished = set()
		self.current = [('classical science', ClassicalScience())]
		self.future_classical_sceince_tech = {
			'animal husbandry', 'pasture',
			'order&labor', 'wood working', 'irrigation', 
			'fishing',
		}
		self.future_medieval_sceince_tech = {}
		self.future_modern_sceince_tech = {}
		self.future_classical_military_tech = {
			'celestial navigation','greek fire',
			'tower', 'engineering',
			'standard uniform','military trandition','bronze weapon', 	
			'cavalary', 'horseback riding'
		}
		self.future_medieval_military_tech = {}
		self.future_modern_military_tech = {}

class ClassicalScience(card):
	def __init__(self):
		super().__init__('classical science',[])
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			players[player_index].material.add_material(('food', 5),('hammer', 1))
			players[player_index].income.add_material(['horse', 1])
			order.clear()
class AnimalHusbandry(card):
	def __init__(self):
		super().__init__('animal husbandry',[('science', 5)])
		self.future_tech = 4
	def evaluate(self, board, players, visible_screen, order, player_index):
		if not players[player_index].material.greater(self.cost):
			order.clear()
			return
		if len(order) == 1:
			visible_screen['tile_extra'] = 'population'
		else:
			players[player_index].material.add_material(('food', 5),('hammer', 1))
			players[player_index].income.add_material(['horse', 1])
			order.clear()

