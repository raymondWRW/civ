#hex array is to make sure the hexagon makes sense in arrays
# function for hex array
BORDER_INDEX_EVEN   = [(-1, 1), (0, 1), (1, 1), (1,  0), (0, -1), (-1,  0)]
BORDER_INDEX_ODD  = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def axial_to_cube(index):#returns the cube cordiantes
	q = index[1] - (index[0] + (index[0]&1)) // 2
	r = index[0]
	s = 0 - q - r
	return(q,r,s)
def get_border_index(index):
	border_index = []
	if index[0] % 2 == 1:
		for i in range(6):
			border_index.append((BORDER_INDEX_ODD[i][0] + index[0], BORDER_INDEX_ODD[i][1] + index[1]))
	else:
		for i in range(6):
			border_index.append((BORDER_INDEX_EVEN[i][0] + index[0], BORDER_INDEX_EVEN[i][1] + index[1]))
	return border_index
def get_distance(start_hex_index, end_hex_index):
	#convert the index to axial cordiantes
	temp1 = axial_to_cube(start_hex_index)
	temp2 = axial_to_cube(end_hex_index)
	return max(abs(temp1[0] - temp2[0]), abs(temp1[1] - temp2[1]), abs(temp1[2] - temp2[2]))
def get_tile_index(pos, cell_size):
	#evenrow
	even_pos = (int(pos[1]/cell_size/24 + 0.5) * 2, int(pos[0]/cell_size/12 + 0.5))
	#oddrow
	odd_pos = (int((pos[1] - cell_size * 4)/cell_size/24) * 2 + 1, int((pos[0] + cell_size * 6)/cell_size/12 + 0.5))
	distance = (pos[0] -  (even_pos[1] * cell_size * 12)) * (pos[0] -  (even_pos[1] * cell_size * 12)) + (pos[1] -  (even_pos[0] * cell_size * 12)) * (pos[1] -  (even_pos[0] * cell_size * 12))
	if distance <= 8 * cell_size *  8 * cell_size:
		return	even_pos
	distance = (pos[0] -  (odd_pos[1] * cell_size * 12 - cell_size * 6)) * (pos[0] -  (odd_pos[1] * cell_size * 12 - cell_size * 6)) + (pos[1] -  (odd_pos[0] * cell_size * 12)) * (pos[1] -  (odd_pos[0] * cell_size * 12))
	if distance <= 8 * cell_size *  8 * (cell_size - 1):
		return odd_pos
	# raise Exception("unexpected index position %d"%(pos))
	return (-1,-1)