#********************************************
# By T02G05 Group Submission
# October 17, 2013
# Battleship CPSC231 - Brown Edition
# - This is the group submission for Ex 5.3 
# - It demonstrates a random ai, that will make
# - valid moves. 
#********************************************

# Getting Imports
import random 
import grid

NAME = ''

# global variables
direction = 'horizontal'
x = ord('A')
y = 0

		
def get_location(index):
	#Setting globals for editing
	global x
	global y
	global direction
	
	#Selecting Random Values for row, column and direction
	x = random.randint(1, 10)
	y = random.randint(1, 10)
	direction = random.randint(1,2)
	
	#Loop sets a number to a character for place vessel to 'decode' the direction
	if direction == 1:
		direction = 'v'
	else:
		direction = 'h'
	
	#This loop makes sure the end of the vessel does not go over the edge of the board.
	if (direction == 'h') and (-1 < x < (grid.GRID_WIDTH - grid.VESSEL_SIZE[index])) and (-1 < y < grid.GRID_HEIGHT):
		
		#If has_overlap returns True then get location is called.
		if grid.has_overlap(index, x, y, direction):
			get_location(index)
		
		#If it returns not true(false), then we place the vessel.		
		if not grid.has_overlap(index, x, y, direction):
			grid.place_vessel(index, direction, x, y)
	
	#Same as previous function, except with vertical/y direction.
	elif direction == 'v' and (-1 < y < (grid.GRID_HEIGHT - grid.VESSEL_SIZE[index])) and (-1 < x < grid.GRID_WIDTH):  
	
		if grid.has_overlap(index, x, y, direction):
			get_location(index)
	
		if not grid.has_overlap(index, x, y, direction):
			grid.place_vessel(index, direction, x, y)
	
	#Recursive statement, to retry if fails.
	else:
		get_location(index)
