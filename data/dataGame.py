import pygame
from coreFunction.mutableInt import mutableInt
DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 750
BOARD_ROW = 15
BOARD_COL  = 30
FPS = 30
last_mouse_info = {
	'type' : 'none',
	'pos' : (0,0),
	'dragging' : False
}
visible_screen = {
	'board' : True,
	'tile extra' : 'unit',
	'shadow' : [[False for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
	'hand' : True,
	'background' : True,
	'discover' : None,
	'market' : True,
	'market_player_index' : 1
}
error_message = []
screen_pos = [0,0]
player_index = mutableInt(1)
order = []
board = [[False for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
player = [0,0,0,0,0]
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
def reset():
	order.clear()
	visible_screen['board'] = True
	visible_screen['tile extra'] = 'unit'
	visible_screen['shadow'] = [[False for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
	visible_screen['hand'] = True
	visible_screen['background'] = True
	visible_screen['discover'] = None
 
def current_player():
    return player[player_index.value]