#********************************************
# By Ahmed Elbannan
# September 22nd 2013
# Battleship CPSC231 (Limited Edition! ] )
#********************************************
#Imports
import grid


# CONSTANTS values
NAME = ''

# global variables
direction = 'horizontal'
x = ord('A')
y = 0

# let's the user choose where to place vessel
def get_location(index):
	
	global x # this function can edit x
	global y # this function can edit y
	global direction # this function can edit direction
	
	# Get row, column, direction from player
	print (NAME + ', where would you like to place your ' + grid.VESSEL_NAME[index] + '? (' + str(grid.VESSEL_SIZE[index]) + ' spaces)')
	x = input('Horizontal position, Sir?(A-J):')
	y = input('Vertical position? (1-10):')
	direction = input('Direction? [h]orizontal or [v]ertical:')
	print()
	validate_location(index)
# end

# checks if the location is valid
def validate_location(index):
	
	global x # this function can edit x
	global y # this function can edit y
	# check if string is a single letter or smaller than a three digit number, if not, asks for input again, then checks
	
	#check if strings are appropriate length
	if (len(x) == 1) and (len(y) < 3):
		x = (ord(x) - ord('A'))
		y = (int(y) - 1)
		
		# checks if location is on the board and if the ship will fit, if not asks for input again and checks again
		if (direction == 'h') and (-1 < x < (grid.GRID_WIDTH - grid.VESSEL_SIZE[index])) and (-1 < y < grid.GRID_HEIGHT):
			if grid.has_overlap(index, x, y, direction):
				print("Location Invalid")
				get_location(index)
	
			if not grid.has_overlap(index, x, y, direction):
				grid.place_vessel(index, direction, x, y)
			
		elif direction == 'v' and (-1 < y < (grid.GRID_HEIGHT - grid.VESSEL_SIZE[index])) and (-1 < x < grid.GRID_WIDTH):  
			if grid.has_overlap(index, x, y, direction):
				print("Location Invalid")
				get_location(index)
	
			if not grid.has_overlap(index, x, y, direction):
				grid.place_vessel(index, direction, x, y)
			
		else:
			print('The location you entered is not on the board!')
			get_location(index)
			validate_location(index) # recursive
			
	else:
		print('Please enter a LETTER (between A-J) and a NUMBER (between 1-10!)')
		get_location(index)
		validate_location(index) # recursive
	return

	

		
