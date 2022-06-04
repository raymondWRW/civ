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
player1 = player.player.Player((255, 0, 0), 0)
players = []
players.append(player1)
player1.tile.append((1,1))
player1.tile.append((1,2))
player1.tile.append((1,3))
player1.tile.append((1,4))
player1.tile.append((1,5))
#initializing the draw file
visible_screen = {
	'tile' : True,
	'player_tile': True,
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
