import pygame, sys
from pygame.locals import *
import init
import template
pygame.init()
#last mouse info
def true_pos(pos):
	return (pos[0] - template.screen_pos[0], pos[1] - template.screen_pos[1])

def click(type, pos):
	pass

def reset():
    init.order.clear()
    init.visible_screen['tile'] = True
    init.visible_screen['player_tile'] = True
    init.visible_screen['tile_extra'] = None
    init.visible_screen['resource'] = True
    init.visible_screen['button'] = True
    init.visible_screen['hand'] = True
    
# def left_click():
def mouse_input():
	cursor_pos = pygame.mouse.get_pos()
	cursor_state =  pygame.mouse.get_pressed() 
	if cursor_state[0]:#pressing left click = false
		if init.last_mouse_info['type'] == 'leftclick':
			if init.last_mouse_info['dragging'] == True:#moving screen when pressing leftclick
				init.screen_pos = (init.screen_pos[0] - init.last_mouse_info['pos'][0] + cursor_pos[0], init.screen_pos[1] - init.last_mouse_info['pos'][1] + cursor_pos[1])
	# elif cursor_state[1]:
	# 	if init.last_mouse_info['mouse_type'] == 'rightclick':
	# 		if cursor_pos != init.last_mouse_info['pos']:#moving when pressing leftclick
	# 			init.last_mouse_info['dragging'] = True
	# 			init.screen_pos = (init.screen_pos[0] - init.last_mouse_info['pos'][0] + cursor_pos[0], init.screen_pos[1] - init.last_mouse_info['pos'][1] + cursor_pos[1])
	# else:
	# 	click(player, cursor_pos, cursor_state)
	elif init.last_mouse_info['dragging'] == False:#leftclick & rightclicks
		click(cursor_pos)
	update_mouse(cursor_pos, cursor_state)

def update_mouse(cursor_pos, cursor_state):
	if init.last_mouse_info['type'] == 'leftclick' and cursor_state[0] and init.last_mouse_info['pos'] != cursor_pos:
		init.last_mouse_info['dragging'] = True
	if cursor_state[0]:
		init.last_mouse_info['type'] = 'leftclick'
	elif cursor_state[1]:
		init.last_mouse_info['type'] = 'rightclick'
	else:
		init.last_mouse_info['dragging'] = False
		init.last_mouse_info['type'] = 'none'
	init.last_mouse_info['pos'] = cursor_pos
 
def click(cursor_pos):
	if init.last_mouse_info['type'] == 'leftclick':
		if init.visible_screen['button']:
			#next turn
			if init.next_turn_button.within_boundary((0, 300), cursor_pos):
				print(8)
				init.player_index = (init.player_index + 1) % len(init.players)
				init.players[init.player_index].add_income()
				reset()
				return
			#delete card
			if init.delete_card_button.within_boundary((0, 500), cursor_pos):
				if len(init.order) == 1 and init.order[0][1] == 'hand':
					init.players[init.player_index].hand.remove_card(init.order[0][2])	
					init.players[init.player_index].material.sciencepoint += 1
				reset()
				return
			#add card
		if init.visible_screen['hand']:
			index = init.players[init.player_index].hand.mouse_over_card(cursor_pos)
			if index != -1:
				init.order.append(('leftclick','hand', index))
				evaluate(init.player_index)
				return
		if init.visible_screen['tile']:
			index = init.board.get_tile_index(cursor_pos, init.screen_pos)
			init.order.append(('leftclick','tile', index))
			evaluate(init.player_index)
			return
		print(init.order)
	elif init.last_mouse_info['type'] == 'rightclick':
		pass #right click
			
#left/right click, the button that is click, the index of the button
def evaluate(player_index):#last input = left/right click, what clicked , index
	if init.order[0][0] == 'leftclick':	
		if init.order[0][1] == 'hand':
			init.players[player_index].evaluate_hand(init.board.map, init.players, init.visible_screen, init.order)
	else:
		pass
	# if input[0][0] == 'leftclick':
	# 	if input[0][1] == 'card':
	# 		init.hand[input[0][3]].evaluate(init.order)
	# 	if input[0][1] == 'tile':
	# 		init.map.evaluate(init.order)
