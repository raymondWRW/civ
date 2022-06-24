#init contain prety much all the varibles needed to be used 
import pygame, sys, template, random
from pygame.locals import *
import map.map, map.tile
import card.hand,card.card
import player
import button
import tileGenerator
pygame.init()

# initializing the board
board_row = 15
board_col = 30
board = map.map.Board(tileGenerator.tile_generator(board_row, board_col, 7))
# board = map.map.Board([[map.tile.Tile() for i in range(board_col + j % 2)] for j in range(board_row)])
screen_pos = (0,0)

#initializing the players
players = [player.Player((255, 0, 0), 0), player.Player((0, 0, 255), 1)]
players[0].add_tile((random.randint(0,14),random.randint(0,29)), board.map)
players[1].add_tile((random.randint(0,14),random.randint(0,29)), board.map)
current_player_index = 0#current player's index
#draw buttons and stuff
next_turn_button = button.Button(template.BUTTON_NEXT_TURN,'next turn')
draw_card_button = button.Button(template.BUTTON_DRAW_CARD,'draw card')
delete_card_button = button.Button(template.BUTTON_DELETE_CARD,'delete card')

#initializing the draw file
visible_screen = {
	'tile' : True,
	'player_tile': True,
	'tile_extra' : None,
	'resource' : True,
	'button' : True,
	'hand' : True,
	'discover' : None
}

#initializing the evaluate file
order = []
last_mouse_info = {
	'type' : 'none',
	'pos' : (0,0),
	'dragging' : False
}
