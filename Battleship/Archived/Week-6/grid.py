# contains all functions relating to the grid

#CONSTANTS
GRID_HEIGHT = 10;
GRID_WIDTH = 10;
VESSEL_NAME = ['Aircraft Carrier', 'Battleship', 'Submarine', 'Destroyer', 'Patrol Boat'];
VESSEL_SIZE = [5, 4, 3, 2, 2];
NUM_OF_VESSELS = 5
B = '~' # this is water
HIT = 'X'
MISS = 'O'
	
	
def print_grid(grid):
	print('__________________________');
	print('|  | A B C D E F G H I J |');
	print('--------------------------');
	row = 0;
	column = 0;
	for row in range(GRID_HEIGHT):
		if row  == 9:
			print( '|' + str(row + 1) + '| ', end = '');
		else:
			print( '|0' + str(row + 1) + '| ', end = '');			
		for col in range(0, GRID_WIDTH):
			print(grid[row][col] + ' ', end = '');
		print('|');
	print();
# end		

def add_vessel(grid, index, row, col, direction):

	if direction == 'h': 
			for col in range(col, col + VESSEL_SIZE[index]):
				grid[row][col] = str(VESSEL_SIZE[index]);
	elif direction == 'v':
			for row in range(row, row + VESSEL_SIZE[index]):
				grid[row][col] = str(VESSEL_SIZE[index]);
				
	return grid
	
def has_overlap(grid, index, row, col, direction):
	# TEMP VARIABLES
	check_x = col
	check_y = row
	
	if direction == 'h': 
			for check_x in range(check_x, check_x + VESSEL_SIZE[index]):
				if grid[check_y][check_x] !='~':
						return True;
					
	elif direction == 'v':
			for check_y in range(check_y, check_y + VESSEL_SIZE[index]):
				if grid[check_y][check_x] !='~':
						return True;
	
	return False
	
# check the location picked by ai or human is a hit or a miss and print 
#a grid with an 'X' for a hit and an 'o' for a miss	
def drop_bomb(grid_defend, grid_attack, row, col):

	#if the location picked to bomb equal any of the VESSEL_SIZE its is a hit
	hit = False
	for i in range(len(VESSEL_SIZE)):
		
		if grid_defend[row][col] == str(VESSEL_SIZE[i]):
			
			grid_attack[row][col] = HIT
			grid_defend[row][col] = HIT
			print("HIT!")
			hit = True
				
	
	if hit == False:
			grid_attack[row][col] = MISS
			grid_defend[row][col] = MISS 
			print('MISS')
			
	

#check to see if there is any ship left on the grid, if no ship left return True as sunk else return false						
def all_vessels_sunk(grid):
	
	for row in range(GRID_HEIGHT):
		for col in range(GRID_WIDTH):
			for i in range(len(VESSEL_SIZE)):
				if grid[row][col] == VESSEL_SIZE[i]:
					return True
				


