
# CONSTANTS values 
GRID_HEIGHT = 10
GRID_WIDTH = 10
VESSEL_NAME = ['Aircraft Carrier', 'Battleship', 'Submarine', 'Destroyer', 'Patrol Boat']
VESSEL_SIZE = [5, 4, 3, 2, 2]

#Grid
w = '~'
grid = 	[
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w],
		[w,w,w,w,w,w,w,w,w,w]]
			
def print_grid():
	print('__________________________')
	print('|  | A B C D E F G H I J |')
	print('--------------------------')
	row = 0
	column = 0
	 
	for row in range(GRID_HEIGHT):
		if row  == 9:
			print( '|' + str(row + 1) + '| ', end = '')
		else:
			print( '|0' + str(row + 1) + '| ', end = '')
		for column in range(0, GRID_WIDTH):
			print(grid[column][row] + ' ', end = '')
		print('|')

def place_vessel(index, direction, x, y):
	#Global Variables, that place in more then one place

	
	#check if direction is h or v, then places ship accordingly
	if direction == 'h': 
		for x in range(x, x + VESSEL_SIZE[index]):
				grid[x][y] = str(VESSEL_SIZE[index])
				
	elif direction == 'v':
		for y in range(y, y + VESSEL_SIZE[index]):
			grid[x][y] = str(VESSEL_SIZE[index])

def has_overlap(index, x, y, direction):
	#Setting Local Variables
	size = VESSEL_SIZE[index]
	chk_x = x
	chk_y = y
	
	#Checking if any overlapping vessels to the right of the original cord
	if direction == 'h':
		for chk_x in range(chk_x, chk_x + size):
			if grid[chk_x][chk_y] != "~":
				return True
	#Checking if any overlapping vessels to the bottom of the original cord				
	elif direction == 'v':
		for chk_y in range(chk_y, chk_y + size):
			if grid[chk_x][chk_y] != "~": 
				return True
				
	#If none of those return true, we return False, meaning there is no overlap		
	else:
		return False	
