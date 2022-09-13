import pygame, sys, random
from coreFunction.hexArray import *
from render.render import Render
from logic.logic import Logic
from logic.tile import Tile
from logic.civ.civ import Civ
from logic.civ.mongolia import Mongolia
from logic.civ.china import China
from logic.civ.ottoman import Ottoman
from data.dataGame import FPS, BOARD_COL, BOARD_ROW, board,player, screen_pos, player_index
class Game:
	def __init__(self):
		self.render = Render()
		self.logic = Logic()
		self.clock = pygame.time.Clock()
	def tile_generation(self):
		# choose the center of plates
		# -2 ocean
		# -1 coast
		# 1 plain
		# 2 forest
		# 3 mountain
		#
		index_map = [[-2 for i in range(BOARD_COL + j % 2)] for j in range(BOARD_ROW)]
		count = 0
		index = []
		for i in range(2):
			center = (random.randint(BOARD_ROW//4, BOARD_ROW//4 * 3), random.randint(BOARD_COL//4, BOARD_COL//4 * 3))
			index.append(center)
		while count < 200 and len(index) != 0:
			temp_pos = index.pop(random.randint(0, len(index) - 1))
			if 0 <= temp_pos[0] < len(index_map) and 0 <= temp_pos[1] < len(index_map[temp_pos[0]]):
				if index_map[temp_pos[0]][temp_pos[1]] == -2:
					index_map[temp_pos[0]][temp_pos[1]] = 1
					edge = get_border_index(temp_pos)
					for k in edge:
						index.append(k)
					count += 1
		#coast generation
		for i in range(BOARD_ROW):
			for j in range(BOARD_COL):
				if index_map[i][j] == -2:
					edge = get_border_index((i,j))
					for k in edge:
						if 0 <= k[0] < len(index_map) and 0 <= k[1] < len(index_map[k[0]]):
							if index_map[k[0]][k[1]] == 1:
								index_map[i][j] = -1
		# wood mountain generation
		for i in range(BOARD_ROW):
			for j in range(BOARD_COL):
				if index_map[i][j] == 1:
					rnd = random.randint(1, 10)
					if rnd < 3:
						index_map[i][j] = 2
					elif rnd > 9:
						index_map[i][j] = 3
		#wood growth and decay
		for i in range(BOARD_ROW):#decay
			for j in range(BOARD_COL):
				if index_map[i][j] == 2:
					edge = get_border_index((i,j))
					border_wood = False
					for k in edge:
						if 0 <= k[0] < len(index_map) and 0 <= k[1] < len(index_map[k[0]]):
							if index_map[k[0]][k[1]] == 2:
								border_wood = True
					if not border_wood:
						index_map[i][j] = 1
		for i in range(BOARD_ROW):#growth
			for j in range(BOARD_COL):
				if index_map[i][j] == 1:
					edge = get_border_index((i,j))
					edge_wood_count = 0
					for k in edge:
						if 0 <= k[0] < len(index_map) and 0 <= k[1] < len(index_map[k[0]]):
							if index_map[k[0]][k[1]] == 2:
								edge_wood_count += 1
					if edge_wood_count > random.randint(0, 5):
						index_map[i][j] = 2
		for i in range(len(board)):#change the map
			for j in range(len(board[i])):
				if index_map[i][j] == -2:
					board[i][j] = Tile('ocean', (i,j))
				if index_map[i][j] == -1:
					board[i][j] = Tile('coast', (i,j))
				if index_map[i][j] == 1:
					board[i][j] = Tile('plain', (i,j))
				if index_map[i][j] == 2:
					board[i][j] = Tile('wood', (i,j))
				if index_map[i][j] == 3:
					board[i][j] = Tile('mountain', (i,j))
	def init_player(self):
		player_index.set(0)
		player[0] = Civ(0, (0,0,0))
		player[0].start_game()
		player_index.set(1)
		player[1] = Ottoman(1)
		player[1].start_game()
		player_index.set(2)
		player[2] = China(2)
		player[2].start_game()
		player_index.set(3)
		player[3] = Mongolia(3)
		player[3].start_game()
		player_index.set(4)
		player[4] = Civ(4, (115,66,34))
		player[4].start_game()
		player_index.set(1)
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.render.update()
			self.logic.update()
			pygame.display.update()
			self.clock.tick(FPS)
if __name__ == '__main__':
	game = Game()
	game.tile_generation()
	game.init_player()
	screen_pos[0] = player[1].screen_pos[0]
	screen_pos[1] = player[1].screen_pos[1]
	game.run()
