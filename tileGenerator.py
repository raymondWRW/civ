import random, template, queue,map.tile
def tile_generator(row,col, plate):
	# choose the center of plates
	continent = [[-1 for i in range(col + j % 2)] for j in range(row)]
	pos = queue.Queue()
	for i in range(plate):
		temp = (random.randint(0,row - 1),random.randint(0,col - 1))
		if continent[temp[0]][temp[1]] == -1:
			pos.put(temp)
			continent[temp[0]][temp[1]] = i
	while pos.qsize() != 0:
		temp = pos.get()
		border_index = []
		if temp[0] % 2 == 1:
			border_index = template.BORDER_INDEX_ODD	
		else:
			border_index = template.BORDER_INDEX_EVEN
		for i in range(len(border_index)):
			if temp[0] + border_index[i][0] >= 0 and temp[1] + border_index[i][1] >= 0 and temp[0] + border_index[i][0] < row and temp[1] + border_index[i][1] < col + (temp[0] + border_index[i][0]) % 2:
				if continent[temp[0] + border_index[i][0]][temp[1] + border_index[i][1]] == -1:
					pos.put((temp[0] + border_index[i][0], temp[1] + border_index[i][1]))
					continent[temp[0] + border_index[i][0]][temp[1] + border_index[i][1]] = continent[temp[0] + border_index[i][0]][temp[1] + border_index[i][1]] = continent[temp[0]][temp[1]]
	# height map
	type = [-1 for i in range(plate)]
	plate_movement = [[-10 for i in range(col)] for j in range(row)]
	height = [[-1 for i in range(col + j % 2)] for j in range(row)]
	for i in range (plate):#the height of the plate
		type[i] = random.randint(-2,5)
	for i in range (row):
		border_index
		if i % 2 == 1:
			border_index = template.BORDER_INDEX_ODD	
		else:
			border_index = template.BORDER_INDEX_EVEN
		for j in range(i % 2 + col):
			temp_height = 0
			index1 = continent[i][j]
			for k in border_index:
				temp_pos = (i + k[0], j + k[1])	
				if temp_pos[0] >= 0 and temp_pos[1] >= 0 and temp_pos[0] < row and temp_pos[1] < col + temp_pos[0] % 2:
					index2 = continent[temp_pos[0]][temp_pos[1]]
					if index1 < index2:
						if (type[index1]) < 1 == type[index2] < 1:
							temp_height += random.randint(1,2)
						else:
							temp_height -= random.randint(0,1)
			temp_height += type[index1] + random.randint(-2,2)
			height[i][j] = temp_height
	# converting to tiles
	board = [[map.tile.Tile() for i in range(col + j % 2)] for j in range(row)]
	for i in range (row):
		for j in range(i % 2 + col):
			if height[i][j] < 0:
				board[i][j].tile_color = (29, 78, 137)
			elif height[i][j] < 4:
				board[i][j].tile_color = (152, 251, 152)
			elif height[i][j] < 5:
				board[i][j].tile_color = (230,170,104)
			else:
				board[i][j].tile_color = (93, 115, 126)
	return board
# a = tile_generator(10,10,10)
# for i in range(len(a)):
# 	if i % 2 == 0:
# 		print(" ", a[i])
# 	else:
# 		print(a[i])