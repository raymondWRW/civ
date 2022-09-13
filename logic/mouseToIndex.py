from data.dataGame import *
from data.dataImage import *
from coreFunction.surfaceExtended import *
from coreFunction.hexArray import *
# visible_screen = {
# 	'board' : True,
# 	'tile extra' : 'unit',
# 	'shadow' : [[False for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
# 	'hand' : True,
# 	'background' : True,
# 	'discover' : None
# }
def mouseToOrder():
	cursor_pos = pygame.mouse.get_pos()
	if last_mouse_info['type'] == 'leftclick':
		if visible_screen['discover'] != None:
			index = mouseToDiscover()
			if index != -1:
				return ['leftclick', 'discover card', index]
		if visible_screen['background']:
			if within_surface(cursor_pos, BUTTON_NEXT_TURN, button_next_turn_pos):
				return ['leftclick', 'next turn']
			if within_surface(cursor_pos, BUTTON_DRAW_CARD, button_draw_card_pos):
				return ['leftclick', 'draw card']
			if within_surface(cursor_pos, BUTTON_DELETE_CARD, button_delete_card_pos):
				return ['leftclick', 'delete card']
		if visible_screen['hand']:
			index = mouseToHand()
			if index != -1:
				return ['leftclick', 'hand', index]
		if visible_screen['board']:
			index = mouseToTile()
			return['leftclick','tile', index]
	return False
def mouseToHand():
	for i in range(len(current_player().hand) - 1, - 1,-1):
		if within_dimesion(last_mouse_info['pos'], (CARD_WIDTH, CARD_HEIGHT), (i * 120, 600)):
			return i
	return -1
def mouseToTile():
    return get_tile_index((last_mouse_info['pos'][0] - screen_pos[0], last_mouse_info['pos'][1] - screen_pos[1]), CELL_SIZE)
def mouseToDiscover():
	for i in range(len(visible_screen['discover']) - 1, - 1,-1):
		if within_dimesion(last_mouse_info['pos'], (CARD_WIDTH, CARD_HEIGHT), (i * 120, 300)):
			return i
	return -1