
#Imports
import grid
import sys

#One grid for the human to attack with, another that stores his vessels.
grid_attack = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]
grid_defend = [ [grid.B for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]


#User places location vessel will be placed using row, and column
def get_location(index):

	#User information pertaining to following steps
	print ('Where would you like to place your ' + grid.VESSEL_NAME[index] + '? (' + str(grid.VESSEL_SIZE[index]) + ' spaces)')
	
	#Getting user input 
	col = input('Horizontal position?\t(A-J):')
	row = input('Vertical position? \t(1-10):')
	dir = input('Direction? [h]orizontal or [v]ertical:')
	
	print()

	#Calling to validate input
	validate_location(index, row, col, dir)
	
#User places location bomb will be placed using row, and column	
def get_choice():
	
	#User information pertaining to following steps
	print("Where would you like to bomb the enemy") 
	
	print()
	
	#Getting input
	col = input("Horizontal bomb position?\t(A-J): ")
	row = input("Vertical bomb position?\t (1-10): ")

	col = (ord(col.upper()) - ord('A'))
	row = (int(row) - 1)
	#If the attack grid contains a 'o', or 'x' it means theres a hit, therefore if it DOESNT equal '~' it means
	#there a move made there. If that is true, we call for a valid input
	if grid_attack[col][row] != '~':
		row, col = get_choice()
	print(row, col)
	#If input equals '~' it is a valid move, therefore we return the values required back. 	
	return row, col


def validate_location(index, row, col, dir):

	#Converting row, and column into values that are workable using numbers.
	col = (ord(col.upper()) - ord('A'))
	row = (int(row) - 1)
	
	
	
	#Checks if horizontal and if the column and row don't go over
	if (dir == 'h') and (-1 < col < (grid.GRID_WIDTH - grid.VESSEL_SIZE[index])) and (-1 < row < grid.GRID_HEIGHT):
		
		#Checks if it is overlapping with another vessel, if so, it gets input, otherwise it sends to grid module.
		if not grid.has_overlap(grid_defend, index, row, col, dir):
			grid.add_vessel(grid_defend, index, row, col, dir)
	
		else:
			print('This ship overlaps with another!')
	
			get_location(index);
	
	#Similar to above but, vertical.
	elif dir == 'v' and (-1 < row < (grid.GRID_HEIGHT - grid.VESSEL_SIZE[index])) and (-1 < col < grid.GRID_WIDTH):  
	
		if not grid.has_overlap(grid_defend, index, row, col, dir):
			grid.add_vessel(grid_defend, index, row, col, dir)
	
		else:
			print('This ship overlaps with another!')
			get_location(index);
	#If neither are true, theres more then one mistake with the location, asks user to try again.
	else:
		print('Not a valid location!')

		#Recurse
		get_location(index);
	
	print()
	
def enter_choice():
    
	choice = input('Enter choice: ')
	while not (choice == 'q' or choice == 'a'):
	    choice = input('Enter choice: ')
	
	if choice == 'q':
	    sys.exit()
#end

#end
