from data.dataGame import *
from coreFunction.hexArray import get_border_index
def modAnimalHusbandry(pos):
	if board[pos[0]][pos[1]].building == 'none':
		return {'food' : 1}
	return {}
def modPasture(pos):
	if board[pos[0]][pos[1]].building == 'none':
		return {'horse' : 1, 'gold' : 1}
	return {}
def modFishingVillage(pos):
	edge = get_border_index((pos[0],pos[1]))
	for i in edge:
		if board[i[0]][i[1]].name == 'coast':
			return {'gold' : 3}
	return {}