import pygame
from settingGame import *
visible_screen = {
	'board' : {
		'tile' : True,
		'player_shadow' : True,
		'tile_shadow' : [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
		'tile_extra' : 'unit',
		'tile_edge' : True,
		'tile_highlight' : True
	},
	'resource' : True,
	'button' : True,
	'hand' : True,
	'discover' : None
}
data = {
	'screen_pos' : (0,0),
	'player_index' : 1,
	'order' : [],
}
last_mouse_info = {
	'type' : 'none',
	'pos' : (0,0),
	'dragging' : False
}
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
player = [(),(), ()]
def reset():
	data['order'].clear()
	visible_screen['board'] = {
		'tile' : True,
		'player_shadow' : True,
		'tile_shadow' : [[-1 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
		'tile_extra' : 'unit',
		'tile_edge' : True,
		'tile_highlight' : True
	}
	visible_screen['resource'] = True
	visible_screen['button'] = True
	visible_screen['hand'] = True
	visible_screen['discover'] = None