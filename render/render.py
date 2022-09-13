from data.dataGame import *
from data.dataImage import *
from coreFunction.hexArray import *
from coreFunction.dictionaryExtended import *
from logic.mouseToIndex import *
from cmath import pi
# visible_screen = {
# 	'board' : True,
# 	'tile extra' : 'unit',
# 	'shadow' : [[False for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)],
# 	'hand' : True,
# 	'background' : True,

# 	'discover' : None
# }
class Render():
	def __init__(self):
		self.display_layer = {
			'background' : pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha(),
			'board' : pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha(),
			'board extra' : pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha(),
			'hand' : pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha(),
			'discover' : pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT)).convert_alpha()
		}
		self.tile_surface = pygame.Surface((CELL_SIZE * 16, CELL_SIZE * 16)).convert_alpha()
		self.card_surface = pygame.Surface((200, 280)).convert_alpha()
	def update(self):
		screen.fill((255,255,255))
		self.update_board()
		self.update_board_extra()
		self.update_background()
		self.update_hand()
		self.update_discover()
		self.update_market()
		self.update_error_message()

	def draw_tile_terrain(self, tile):
		return tile_image[tile.name]
	def draw_tile_unit(self, tile):
		self.tile_surface.fill((255,255,255,0))
		if tile.unit != None:
			current_player = player[tile.unit.player_index]
			health_percentage = tile.unit.health/current_player.unit[tile.unit.name]['max health']
			if tile.unit.movement == 0:
				pygame.draw.arc(self.tile_surface, (255,255,255), Rect(CELL_SIZE * 4 - 5, CELL_SIZE * 4 - 5, CELL_SIZE * 9, CELL_SIZE * 9), pi/2, pi * 2 * health_percentage + pi/2, 5)
			else:
				pygame.draw.arc(self.tile_surface, current_player.color, Rect(CELL_SIZE * 4 - 5, CELL_SIZE * 4 - 5, CELL_SIZE * 9, CELL_SIZE * 9), pi/2, pi * 2 * health_percentage + pi/2, 5)
			pygame.draw.circle(self.tile_surface, current_player.color, (CELL_SIZE * 8, CELL_SIZE * 8), CELL_SIZE * 4)
			self.tile_surface.blit(unit_image[tile.unit.name], (CELL_SIZE * 4 , CELL_SIZE * 4))
		return self.tile_surface
	def draw_tile_population(self, tile):
		self.tile_surface.fill((255,255,255,0))
		for i in range(tile.max_population()):
			pos = (RESOURCE_POS[tile.max_population()][i][0] * CELL_SIZE + CELL_SIZE * 6.5, RESOURCE_POS[tile.max_population()][i][1] * CELL_SIZE + CELL_SIZE * 6.5)
			if i < tile.population:
				self.tile_surface.blit(tile_resource_image['full population'], pos)
			else:
				self.tile_surface.blit(tile_resource_image['empty population'], pos)
		return self.tile_surface
	def draw_tile_resource(self, tile):
		self.tile_surface.fill((255,255,255,0))
		total = total_count(tile.tile_resource())
		index = 0
		for i,j in tile.tile_resource().items():
			for k in range(j):
				pos = (RESOURCE_POS[total][index][0] * CELL_SIZE + CELL_SIZE * 7, RESOURCE_POS[total][index][1] * CELL_SIZE + CELL_SIZE * 7)
				self.tile_surface.blit(tile_resource_image[i], pos)
				index += 1
		return self.tile_surface
	def draw_tile_building(self, tile):
		self.tile_surface.fill((255,255,255,0))
		if tile.building != 'none':
			self.tile_surface.blit(tile_building_image[tile.building], (CELL_SIZE * 2.5, CELL_SIZE * 2.5))
		return self.tile_surface
	def draw_tile_shadow(self, color):
		self.tile_surface.fill((255,255,255,0))
		pygame.draw.polygon(self.tile_surface, (color[0], color[1], color[2], color[3]), [(x * CELL_SIZE + CELL_SIZE * 8, y * CELL_SIZE + CELL_SIZE * 8) for x, y in TILE_EDGE])
		return self.tile_surface
	def draw_card(self, card):
		self.card_surface.blit(CARD_IMAGE,(0,0))
		#title
		self.card_surface.blit(CARD_TITLE_FONT.render(card.name, 1, (0,0,0)), (20, 10))
		#text
		temp = ""
		row = 0
		word = card.description.split(" ")
		for i in word:
			size = pygame.font.Font.size(CARD_TEXT_FONT, temp + " " + i)
			if size[0] > CARD_WIDTH:
				self.card_surface.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), ((CARD_WIDTH - pygame.font.Font.size(CARD_TEXT_FONT, temp)[0]) // 2, 170 + row * 30))
				row += 1		
				temp = ""
			if temp == "":
				temp = i
			else:
				temp = temp + "  " + i
		if temp != "":
			self.card_surface.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), ((CARD_WIDTH - pygame.font.Font.size(CARD_TEXT_FONT, temp)[0]) // 2, 170 + row * 30))
		#cost	
		row = 0
		for i,j in card.cost.items():
			res = CARD_RESOURCE_IMAGE[i]
			self.card_surface.blit(res, (10, 25 + row * 25))
			temp = "X" + str(j)
			self.card_surface.blit(CARD_TEXT_FONT.render(temp, 1, (0,0,0)), (32, 30 + row * 25))
			row += 1
		return self.card_surface
	def update_board(self):
		if visible_screen['board']:
			for i in range(BOARD_ROW):
				for j in range(BOARD_COL):
					tile_center_pos = (j * CELL_SIZE * 12 + screen_pos[0] - CELL_SIZE * 6 * (i % 2), i * CELL_SIZE * 12 + screen_pos[1])
					blit_pos = (tile_center_pos[0] - CELL_SIZE * 8, tile_center_pos[1] - CELL_SIZE * 8)
					if within_surface(tile_center_pos, screen, (0,0), CELL_SIZE * 8):
						screen.blit(self.draw_tile_terrain(board[i][j]), blit_pos)
	def update_board_extra(self):
		for i in range(len(board)):
			for j in range(len(board[i])):
				tile_center_pos = (j * CELL_SIZE * 12 + screen_pos[0] - CELL_SIZE * 6 * (i % 2), i * CELL_SIZE * 12 + screen_pos[1])
				blit_pos = (tile_center_pos[0] - CELL_SIZE * 8, tile_center_pos[1] - CELL_SIZE * 8)
				if within_surface(tile_center_pos, screen, (0,0), CELL_SIZE * 8):
					#shadow
					if visible_screen['shadow'][i][j]:
						screen.blit(self.draw_tile_shadow((50, 50, 50, 200)), blit_pos)
					elif board[i][j].player_index != 0:
						screen.blit(self.draw_tile_shadow((player[board[i][j].player_index].color[0], player[board[i][j].player_index].color[1], player[board[i][j].player_index].color[2], 100)), blit_pos)
					#border
					if board[i][j].player_index != 0:
						edge = get_border_index((i,j))
						for k, tile_pos in enumerate(edge):
							s_pos = (TILE_EDGE[k][0] * CELL_SIZE + tile_center_pos[0], TILE_EDGE[k][1] * CELL_SIZE + tile_center_pos[1])
							t_pos = (TILE_EDGE[(k + 1) % 6][0]) * CELL_SIZE + tile_center_pos[0], (TILE_EDGE[(k + 1) % 6][1] * CELL_SIZE + tile_center_pos[1])
							if 0 <= tile_pos[0] < len(board) and 0 <= tile_pos[1] < len(board[tile_pos[0]]):
								if board[tile_pos[0]][tile_pos[1]].player_index != board[i][j].player_index:
									pygame.draw.line(screen, player[board[i][j].player_index].color, s_pos, t_pos, 5)
							else:
								pygame.draw.line(screen, player[board[i][j].player_index].color, s_pos, t_pos, 5)
					#tile extra
					if pygame.key.get_pressed()[pygame.K_1] == True: # unit
						screen.blit(self.draw_tile_unit(board[i][j]), blit_pos)
						screen.blit(self.draw_tile_building(board[i][j]), blit_pos)
					elif pygame.key.get_pressed()[pygame.K_2] == True: # population
						screen.blit(self.draw_tile_population(board[i][j]), blit_pos)
					elif pygame.key.get_pressed()[pygame.K_3] == True: # resource
						screen.blit(self.draw_tile_resource(board[i][j]), blit_pos)
					elif visible_screen['tile extra'] == 'unit':
						screen.blit(self.draw_tile_unit(board[i][j]), blit_pos)
						screen.blit(self.draw_tile_building(board[i][j]), blit_pos)
					elif visible_screen['tile extra'] == 'population':
						screen.blit(self.draw_tile_population(board[i][j]), blit_pos)
					elif visible_screen['tile extra'] == 'resource':
						screen.blit(self.draw_tile_resource(board[i][j]), blit_pos)
		#highlight
		index = mouseToTile()
		index_pos = (index[1] * CELL_SIZE * 12 + screen_pos[0] - CELL_SIZE * 6 * (index[0] % 2), index[0] * CELL_SIZE * 12 + screen_pos[1])
		pygame.draw.polygon(screen, (255,255,0), [(x * CELL_SIZE + index_pos[0], y * CELL_SIZE + index_pos[1]) for x, y in TILE_EDGE],2)
	def update_background(self):
		if visible_screen['background']:
			#resource
			current_player = player[player_index.value]
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
			#horse (0,240)
			screen.blit(RESOURCE_BACKGROUND_HORSE,(0, 240))
			screen.blit(RESOURCE_FONT.render(str(current_player.material['horse']), 1, (0,0,0)), (50, 240))
			#button
			#next turn
			screen.blit(BUTTON_NEXT_TURN, (button_next_turn_pos))
			#draw card
			screen.blit(BUTTON_DRAW_CARD, (button_draw_card_pos))
			#deleted
			screen.blit(BUTTON_DELETE_CARD, (button_delete_card_pos))
	def update_hand(self):
	# 	hand_ui.fill((255,255,255, 0))
		if visible_screen['hand']:
			temp = mouseToHand()
			for index, i in enumerate(current_player().hand):
				if temp == index:
					pass
				else:
					screen.blit(self.draw_card(i),(index * 120, 600))
			if temp != -1:
				screen.blit(self.draw_card(current_player().hand[temp]),(temp * 120, 500))
	def update_discover(self):
		if visible_screen['discover'] != None:
			temp = mouseToDiscover()
			for index, i in enumerate(visible_screen['discover']):
				if temp == index:
					pass
				else:
					screen.blit(self.draw_card(i),(index * 120, 300))
			if temp != -1:
				screen.blit(self.draw_card(visible_screen['discover'][temp]),(temp * 120, 300))
	def update_error_message(self):
		for i in range (len(error_message) - 1, -1, -1):
			screen.blit(ERROR_MESSAGE_FONT.render(error_message[i][0], 1, (0,0,0)), ((DISPLAY_WIDTH - pygame.font.Font.size(ERROR_MESSAGE_FONT, error_message[i][0])[0]) // 2, error_message[i][1]))
			error_message[i][1] -= 2
			if error_message[i][1] <= 0:
				error_message.pop(i)
	def update_market(self):
		if visible_screen['market']:
			screen.blit(MARKET_IMAGE,(0,0))
		for i in range(1, len(player)):
			screen.blit(MARKET_PLAYER_NAME, (30 +  170 * i , 130))
			screen.blit(MARKET_NAME_FONT.render(player[i].name, 1, (0,0,0)),((30 +  170 * i , 130)))

#   'market' : True,
# 	'market_player_index' : 1