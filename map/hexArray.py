#hex array is to make sure the hexagon makes sense in arrays
class HexArray:
	def __init__(self, map):
		self.map = map
	def get_hex(self, hex_index):
		return self.map[hex_index[0]][hex_index[1]]
	def to_cube(self, index, cell_size):#returns the cube cordiantes
		q = index[1] - (index[0] + (index[0]&1)) // 2
		r = index[0]
		s = 0 - q - s
		return(q / cell_size,r / cell_size,s / cell_size)
	def get_distance(self, start_hex_index, end_hex_index):
		#convert the index to axial cordiantes
		temp1 = self.to_cube(start_hex_index)
		temp2 = self.to_cube(end_hex_index)
		return max(abs(temp1[0] - temp2[0]), abs(temp1[1] - temp2[1]), abs(temp1[2] - temp2[2]))
	def get_tile_index(self,pos, cell_size):
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
		return (-1, -1)