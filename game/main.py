import pygame, sys
from pygame.locals import *
from board.settingTile import CELL_SIZE
from coreFunction.surfaceExtended import within_surface
from coreFunction.hexArray import *
import game.settingGame
from game.settingGame import *
from board.board import Board
from game.variable import *
from civ.civ import Civ
from civ.country.china import China
from UI import *
pygame.init()
class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Modernity')
		self.clock = pygame.time.Clock()
		self.board = Board()
		self.board.tileGeneration()
		player[2] = Civ(2, (50, 168, 82))
		player[1] = China(1)
		player[0] = Civ(0, (255,255,255))
		self.board.board[3][3].player_index = 1
		self.board.board[4][5].player_index = 2
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.evaluate()
			self.UI()
			pygame.display.update()
			self.clock.tick(FPS)
	def UI(self):
		screen.fill((255,255,255,255))
		if visible_screen['board']['tile']:
			self.board.update()
			screen.blit(self.board.display,(0,0))
		if visible_screen['resource']:
			background = pygame.Surface((100,50))
			background.fill((255,255,255))	
			current_player = player[data['player_index']]
			#gold (0, 0)
			screen.blit(RESOURCE_BACKGROUND_GOLD,(0, 0))
			screen.blit(RESOURCE_FONT.render(str(current_player.material['gold']), 1, (0,0,0)) , (50, 0))
			#food (0, 60)
			screen.blit(RESOURCE_BACKGROUND_FOOD,(0, 60))
			screen.blit(RESOURCE_FONT.render(str(current_player.material['food']), 1, (0,0,0)), (50, 60))
			#hammer (0, 120)
			screen.blit(RESOURCE_BACKGROUND_HAMMER,(0, 120))
			screen.blit(RESOURCE_FONT.render(str(current_player.material['hammer']), 1, (0,0,0)), (50, 120))
			#research (0, 180)
			screen.blit(RESOURCE_BACKGROUND_RESEARCH,(0, 180))
			screen.blit(RESOURCE_FONT.render(str(current_player.material['research']), 1, (0,0,0)), (50, 180))
		if visible_screen['button']:
			#next turn
			screen.blit(BUTTON_NEXT_TURN, (button_next_turn_pos))
			#draw card
			screen.blit(BUTTON_DRAW_CARD, (button_draw_card_pos))
			#deleted
			screen.blit(BUTTON_DELETE_CARD, (button_delete_card_pos))
		if visible_screen['hand']:
			current_player = player[data['player_index']]
			screen.blit(HandUI(current_player.hand),(0, 0))
			# index = current_player.hand.pos_to_index(last_mouse_info['pos'])
			# if 0 <= index < len(current_player.hand.hand):
			# 	screen.blit(current_player.hand.hand[index].display, (index * 120, 470))
		if visible_screen['discover'] != None:	
			screen.blit(HandUI(visible_screen['discover']),(0, 0))

	def evaluate(self):
		cursor_pos = pygame.mouse.get_pos()
		cursor_state =  pygame.mouse.get_pressed() 
		current_player = player[data['player_index']]
		if cursor_state[0]:#pressing left click = false
			if last_mouse_info['type'] == 'leftclick':
				if last_mouse_info['dragging'] == True:#moving screen when pressing leftclick
					data['screen_pos'] = (data['screen_pos'][0] - last_mouse_info['pos'][0] + cursor_pos[0], data['screen_pos'][1] - last_mouse_info['pos'][1] + cursor_pos[1])
					# variable.screen_pos = (variable.screen_pos[0] - variable.last_mouse_info['pos'][0] + cursor_pos[0], variable.screen_pos[1] - variable.last_mouse_info['pos'][1] + cursor_pos[1])
		elif last_mouse_info['dragging'] == False:#leftclick & rightclicks
			if self.click_update():
				current_player.evaluate(self.board.board)
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

	def click_update(self):
		cursor_pos = pygame.mouse.get_pos()
		if last_mouse_info['type'] == 'leftclick':
			if visible_screen['discover'] != None:
				index = visible_screen['discover'].pos_to_index(cursor_pos)
				if index != -1:
					data['order'].append(('leftclick','discover card', index))
					return True
			if visible_screen['button']:
				#next turn
				if within_surface(cursor_pos, BUTTON_NEXT_TURN, button_next_turn_pos):
					player[data['player_index']].end_turn(self.board.board)
					player[data['player_index']].screen_pos = data['screen_pos']
					data['player_index'] = (data['player_index'] % (len(player) - 1)) + 1	
					player[data['player_index']].start_turn(self.board.board)
					data['screen_pos'] = player[data['player_index']].screen_pos
					reset()
					return False
				if within_surface(cursor_pos, BUTTON_DRAW_CARD, button_draw_card_pos):
					data['order'].append(('leftclick','draw card'))
					return True
				if within_surface(cursor_pos, BUTTON_DELETE_CARD, button_delete_card_pos):
					data['order'].append(('leftclick','delete card'))
					return True
			if visible_screen['hand']:
				index = player[data['player_index']].hand.pos_to_index(cursor_pos)
				if index != -1:
					data['order'].append(('leftclick','hand', index))
					return True
			if visible_screen['board']['tile']:
				index = get_tile_index((cursor_pos[0] - data['screen_pos'][0], cursor_pos[1] - data['screen_pos'][1]), CELL_SIZE)
				data['order'].append(('leftclick','tile', index))
				return True
		return False
	# 	if init.visible_screen['hand']:
	# 		index = init.players[init.current_player_index].hand.mouse_over_card(cursor_pos)
	# 		if index != -1:
	# 			init.order.append(('leftclick','hand', index))
	# 			evaluate()
	# 			return
	# 	if init.visible_screen['tile']:
	# 		index = init.board.get_tile_index(cursor_pos, init.players[init.current_player_index].screen_pos)
	# 		init.order.append(('leftclick','tile', index))
	# 		evaluate()
	# 		return
	# 		player[player_index].evaluate()
	# 				return
	# elif init.last_mouse_info['type'] == 'rightclick':
	# 	pass
			
			# #add card
			# if init.draw_card_button.within_boundary((0, 400), cursor_pos):
			# 	init.players[init.current_player_index].hand.add_card(init.players[init.current_player_index].deck.draw())
			# 	if len(init.order) == 1 and init.order[0][1] == 'hand':
			# 		init.players[init.current_player_index].hand.remove_card(init.order[0][2])	
			# 		init.players[init.current_player_index].material.science += 1
			# 	reset()
			# 	return
			# #delete card
			# if init.delete_card_button.within_boundary((0, 500), cursor_pos):
			# 	if len(init.order) == 1 and init.order[0][1] == 'hand':
			# 		init.players[init.current_player_index].hand.remove_card(init.order[0][2])	
			# 		init.players[init.current_player_index].material.material['science'] += 1
			# 	reset()
			# 	return
if __name__ == '__main__':
	game = Game()
	game.run()
