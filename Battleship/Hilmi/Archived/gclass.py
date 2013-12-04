#This is a class that will do things?

class Grid:

	def is_empty(row, column):
		if grid[row, column] == "~":
			return True
		else:
			return False
	
	def on_grid(row, column):
		if grid[row, column] != "~":
			return True
		else:
			return False
	
	def is_hit(row, column):
		for i in range(0, len(VESSEL_SIZE)):
			if grid[row, column] == VESSEL_SIZE[i]:
				return True
			else:
				return False
	
	def all_vessels_sunk():
		for i in range(0, GRID_WIDTH):
			for e in range(0, GRID_HEIGHT):
				if grid[i][e] == "~"
					return True
				else:
					return False
	
	#What does this do?
	#def drop_bomb(attack_grid, row, column):
	
