#init contain prety much all the varibles needed to be used 
import pygame, sys, template
from pygame.locals import *
import map.map, map.tile
import card.hand,card.card
import player.player
pygame.init()

# initializing the board
board_row = 20
board_col = 40
board = map.map.Board([[map.tile.Tile() for i in range(board_col + j % 2)] for j in range(board_row)])
screen_pos = (0,0)

#initializing the players
player1 = player.player.Player((255, 0, 0))
player1.tile.tile
#initializing the draw file
visible_screen = {
	'tile' : True,
	'tile_extra' : None,
	'hand' : True,
}

#initializing the evaluate file
order = []
last_mouse_info = {
	'type' : 'none',
	'pos' : (0,0),
	'dragging' : False
}
