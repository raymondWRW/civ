import pygame, random
from data.dataGame import *
from logic.unit import *
from coreFunction.dictionaryExtended import *
from logic.unit import *
import data.dataKeyValue as dkv
pygame.init()
#cost:	
class Card:
	def  __init__(self, name = 'card', cost = {}, description = "template", index = -1):
		self.name = name	
		self.cost = cost
		self.description = description	
		self.index = player_index.value
		if index != -1:
			self.index = index
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			self.finish_evaluate()
		reset()
	def finish_evaluate(self):
		remove_value(player[self.index].material, self.cost)
		player[self.index].deck.append(player[self.index].hand.pop(order[0][2]))
		reset()
	def valid_placement(self, pos):
		return False

#action
class PopulationGrowth(Card):
	def  __init__(self):
		super().__init__('population growth', {'food': 5}, "give a friendly tile 1 population")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
				return False
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_population(board[order[1][2][0]][order[1][2][1]])
						self.finish_evaluate()
						return True
					else:
						error_message.append([dkv.invalid_placement, 100])
				else:
					error_message.append([dkv.invalid_input, 100])
		else:
			error_message.append([dkv.insufficient_material, 100])
		reset()
		return False
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index:
			if board[pos[0]][pos[1]].population < board[pos[0]][pos[1]].max_population():
				return True
		return False
class Mobolization(Card):
	def  __init__(self):
		super().__init__('mobolization', {'food' : 20, 'hammer' : 5, 'gold' : 5}, "build 5 infantry unit")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			valid_index = []
			for i in range(len(board)):
				for j in range(len(board[i])):
					if self.valid_placement((i,j)):
						valid_index.append((i,j))
			for i in range (5):
				if len(valid_index) == 0:
					break
				temp = random.choice(valid_index)
				player[self.index].remove_population(board[temp[0]][temp[1]])
				player[self.index].add_unit(board[temp[0]][temp[1]],  unitInfantry(self.index))
				valid_index.remove(temp)
			self.finish_evaluate()
			return True
		else:
			error_message.append([dkv.insufficient_material, 100])
		reset()
		return False
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean':	
			if board[pos[0]][pos[1]].population != 0 and board[pos[0]][pos[1]].unit == None:
				return True
		return False
class PopulationBoom(Card):
	def  __init__(self):
		super().__init__('population boom', {'food' : 20, 'hammer' : 2, 'gold' : 5}, "add 10 population to your country")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			valid_index = []
			for i in range(len(board)):
				for j in range(len(board[i])):
					if self.valid_placement((i,j)):
						valid_index.append((i,j))
			for i in range (10):
				if len(valid_index) == 0:
					break
				temp = random.choice(valid_index)
				player[self.index].add_population(board[temp[0]][temp[1]])
				valid_index.remove(temp)
			self.finish_evaluate()
			return True
		else:
			error_message.append([dkv.insufficient_material, 100])
		reset()
		return False
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index:
			if board[pos[0]][pos[1]].population < board[pos[0]][pos[1]].max_population():
				return True
		return False
class Sanction(Card):
	def  __init__(self):
		super().__init__('sanction', {}, "lose 50 percent of your gold target nation loses ")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				return False
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[board[order[1][2][0]][order[1][2][1]].player_index].material['gold'] -= player[self.index].material['gold'] // 2
						player[self.index].material['gold'] =  player[self.index].material['gold'] // 2
						self.finish_evaluate()
						return True
					else:
						error_message.append([dkv.invalid_placement, 100])
				else:
					error_message.append([dkv.invalid_input, 100])
		else:
			error_message.append([dkv.insufficient_material, 100])
		reset()
		return False
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index != self.index and board[pos[0]][pos[1]].player_index != 0:
			return True
		return False
#building
class Farm(Card):
	def  __init__(self): 
		super().__init__('farm', {'hammer' : 2, 'gold' : 2}, 'build a building on a friendly tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
				return
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'farm')
						self.finish_evaluate()
						return
		reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name == 'plain':
			if board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class Workshop(Card):
	def  __init__(self):
		super().__init__('workshop', {'hammer' : 2, 'gold' : 2}, 'build a workshop on a friendly tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
				return
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'workshop')
						self.finish_evaluate()
						return
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean' and board[pos[0]][pos[1]].name != 'coast':	
			if board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class Mine(Card):
	def  __init__(self):
		super().__init__('mine', {'hammer' : 2, 'gold' : 2}, 'biulding to biuld on mountain tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'mine')
						self.finish_evaluate()
				reset()
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name == 'mountain':	
			if board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class LumberCamp(Card):
	def  __init__(self):
		super().__init__('lumber camp', {'hammer' : 2, 'gold' : 2}, 'biulding to biuld on wood tiles')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'lumber camp')
						self.finish_evaluate()
				reset()
		else:
			reset() 
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name == 'wood':	
			if board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class BlackSmith(Card):
	def  __init__(self):
		super().__init__('black smith', {'hammer' : 2, 'gold' : 2}, 'gain the resource gun powder')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'black smith')
						self.finish_evaluate()
				reset()
		else:
			reset() 
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'coast' and board[pos[0]][pos[1]].name != 'ocean':	
			if board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class Village(Card):
	def  __init__(self):
		super().__init__('village', {'food' : 5, 'hammer' : 1, 'gold' : 1}, "give a tile extra housing")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_housing(board[order[1][2][0]][order[1][2][1]], 'village')
						self.finish_evaluate()
				reset()	
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean' and board[pos[0]][pos[1]].name != 'coast':
			if board[pos[0]][pos[1]].housing == 'none':
				return True
		return False
class Academy(Card):
	def  __init__(self):
		super().__init__('academy', {'food' : 4, 'hammer' : 6, 'gold' : 6}, "give 1 science, require both housing and building slot")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_housing(board[order[1][2][0]][order[1][2][1]], 'hold')
						player[self.index].add_building(board[order[1][2][0]][order[1][2][1]], 'academy')
						self.finish_evaluate()
				reset()	
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean' and board[pos[0]][pos[1]].name != 'coast':
			if board[pos[0]][pos[1]].housing == 'none' and board[pos[0]][pos[1]].building == 'none':
				return True
		return False
class Town(Card):
	def  __init__(self):
		super().__init__('town', {'food' : 4, 'hammer' : 2, 'gold' : 2}, "give 2 extra housing")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_housing(board[order[1][2][0]][order[1][2][1]], 'town')
						self.finish_evaluate()
				reset()	
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean' and board[pos[0]][pos[1]].name != 'coast':
			if board[pos[0]][pos[1]].housing == 'none':
				return True
		return False
class Tower(Card):
	def  __init__(self):
		super().__init__('tower', {}, "unit recieve 10 percent less damage")
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_housing(board[order[1][2][0]][order[1][2][1]], 'tower')
						self.finish_evaluate()
				reset()
		reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean' and board[pos[0]][pos[1]].name != 'coast':	
			if board[pos[0]][pos[1]].housing == 'none':
				return True
		return False
#unit
class Warrior(Card):
	def  __init__(self):
		super().__init__('warrior', {'food' : 5,'hammer' : 1, 'gold' : 1}, 'deploy a warrior on a friendly tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].remove_population(board[order[1][2][0]][order[1][2][1]])
						player[self.index].add_unit(board[order[1][2][0]][order[1][2][1]],  unitInfantry(self.index))
						self.finish_evaluate()
				reset()
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean':	
			if board[pos[0]][pos[1]].population != 0 and board[pos[0]][pos[1]].unit == None:
				return True
		return False
class Cavalry(Card):
	def  __init__(self):
		super().__init__('cavalry', {'food' : 5 ,'hammer' : 1, 'horse' : 5, 'gold' : 2}, 'deploy a cavalry on a friendly tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].remove_population(board[order[1][2][0]][order[1][2][1]])
						player[self.index].add_unit(board[order[1][2][0]][order[1][2][1]],  unitCavalry(self.index))
						self.finish_evaluate()
				reset()
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].player_index == self.index and board[pos[0]][pos[1]].name != 'ocean':	
			if board[pos[0]][pos[1]].population != 0 and board[pos[0]][pos[1]].unit == None:
				return True
		return False
class Ship(Card):
	def  __init__(self):
		super().__init__('boat', {'food' : 2, 'hammer' : 2, 'gold' : 5}, 'deploy a shop on a nearby coastal tile')
	def evaluate(self):
		if greater(player[self.index].material, self.cost):
			if len(order) == 1:
				for i in range(len(board)):
					for j in range(len(board[i])):
						visible_screen['shadow'][i][j] = not self.valid_placement((i,j))
				visible_screen['tile extra'] = 'population'
			else:
				if order[1][0] == 'leftclick' and order[1][1] == 'tile':
					if self.valid_placement(order[1][2]):
						player[self.index].add_unit(board[order[1][2][0]][order[1][2][1]],  unitShip(self.index))
						self.finish_evaluate()
				reset()
		else:
			reset()
	def valid_placement(self, pos):
		if board[pos[0]][pos[1]].name == 'coast' and board[pos[0]][pos[1]].unit == None:
			if board[pos[0]][pos[1]].player_index == self.index:
				return True
			else:
				edge = get_border_index((pos[0],pos[1]))
				for i in edge:
					if board[i[0]][i[1]].player_index == self.index:
						return True
		return False
#technology
class CivicAdvancement(Card):
	def  __init__(self):
		super().__init__('civic advancement', {}, "choose a scientific advancement to discover!")
	def evaluate(self):
		if len(order) == 1:
			temp = []
			for i in player[self.index].civic_tech:
				temp.append(player[self.index].tech[i])
			visible_screen['discover'] = temp
			visible_screen['shadow'] = [[True for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'discover card':
				player[self.index].tech[player[self.index].civic_tech[order[1][2]]].evaluate()
			else:
				reset()
class MilitaryAdvancement(Card):
	def  __init__(self):
		super().__init__('military advancement', {}, "choose a military advancement to discover!")
	def evaluate(self):
		if len(order) == 1:
			temp = []
			for i in player[self.index].military_tech:
				temp.append(player[self.index].tech[i])
			visible_screen['discover'] = temp
			visible_screen['shadow'] = [[True for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		else:
			if order[1][0] == 'leftclick' and order[1][1] == 'discover card':
				player[self.index].tech[player[self.index].military_tech[order[1][2]]].evaluate()
			else:
				reset()
