import pygame
from data.dataGame import *
from data.dataImage import *
from coreFunction.hexArray import *
from logic.mouseToIndex import *
class Logic():
	def __init__(self):
		pass
	def update(self):
		cursor_pos = pygame.mouse.get_pos()
		cursor_state =  pygame.mouse.get_pressed() 
		if cursor_state[0]:#pressing left click = false
			if last_mouse_info['type'] == 'leftclick':
				if last_mouse_info['dragging'] == True:#moving screen when pressing leftclick
					screen_pos[0] = screen_pos[0] - last_mouse_info['pos'][0] + cursor_pos[0]
					screen_pos[1] = screen_pos[1] - last_mouse_info['pos'][1] + cursor_pos[1]
		elif last_mouse_info['dragging'] == False:#leftclick & rightclicks
			temp_order = mouseToOrder()
			if temp_order != False:
				if temp_order[1] == 'next turn':
					reset()
					current_player().end_turn()
					current_player().screen_pos[0] = screen_pos[0]
					current_player().screen_pos[1] = screen_pos[1]
					player_index.set(player_index.value % (len(player) - 1) + 1)
					current_player().start_turn()
					screen_pos[0] = current_player().screen_pos[0]
					screen_pos[1] = current_player().screen_pos[1]
				else:
					order.append(mouseToOrder())
					current_player().evaluate()
		self.mouse_update()
	def mouse_update(self):
		cursor_pos = pygame.mouse.get_pos()
		cursor_state =  pygame.mouse.get_pressed() 
		if last_mouse_info['type'] == 'leftclick' and cursor_state[0] and last_mouse_info['pos'] != cursor_pos:
			last_mouse_info['dragging'] = True
		if cursor_state[0]:
			last_mouse_info['type'] = 'leftclick'
		elif cursor_state[1]:
			last_mouse_info['type'] = 'rightclick'
		else:
			last_mouse_info['dragging'] = False
			last_mouse_info['type'] = 'none'
		last_mouse_info['pos'] = cursor_pos

	# def click_update(self):
	# 	inpt = mouseToOrder()
	# 	if input != False:
	# 		reset()
	# 	cursor_pos = pygame.mouse.get_pos()
	# 	if last_mouse_info['type'] == 'leftclick':
	# 		if visible_screen['discover'] != None:
	# 			index = visible_screen['discover'].pos_to_index(cursor_pos)
	# 			if index != -1:
	# 				order.append(('leftclick','discover card', index))
	# 				return True
	# 		if visible_screen['button']:
	# 			#next turn
	# 			if within_surface(cursor_pos, BUTTON_NEXT_TURN, button_next_turn_pos):
	# 				player[player_index.value].end_turn(board)
	# 				player[player_index.value].screen_pos = screen_pos
	# 				player_index.set(player_index.value % (len(player) - 1) + 1)
	# 				player[player_index.value].start_turn(board)
	# 				screen_pos[0] = player[player_index.value].screen_pos[0]
	# 				screen_pos[1] = player[player_index.value].screen_pos[1]
	# 				reset()
	# 				return False
	# 			if within_surface(cursor_pos, BUTTON_DRAW_CARD, button_draw_card_pos):
	# 				order.append(('leftclick','draw card'))
	# 				return True
	# 			if within_surface(cursor_pos, BUTTON_DELETE_CARD, button_delete_card_pos):
	# 				order.append(('leftclick','delete card'))
	# 				return True
	# 		if visible_screen['hand']:
	# 			index = player[player_index.value].hand.pos_to_index(cursor_pos)
	# 			if index != -1:
	# 				order.append(('leftclick','hand', index))
	# 				return True
	# 		if visible_screen['board']['tile']:
	# 			index = get_tile_index((cursor_pos[0] - screen_pos[0], cursor_pos[1] - screen_pos[1]), 10)
	# 			order.append(('leftclick','tile', index))
	# 			return True
	# 	return False