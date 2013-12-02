#********************************************
# By Hilmi Abou-Saleh
# October, 7 2013
# Battleship CPSC231 - Brown Edition
#********************************************

# global variables kept in lists
VESSEL_NAMES = ["Aircraft Carrier", "Battleship", "Submarine", "Destroyer", "Patrol Boat"]
VESSEL_SIZES = [5, 4, 3, 3, 2]
GRID_WIDTH = 10
GRID_HEIGHT = 10

#Water
W = "~"

grid = [[W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W], \
            [W,W,W,W,W,W,W,W,W,W]]


#Intro - Titlescreen no input. * - are for formatting
def print_titlescreen():
    print();
    print('________________________________________')
    print('|*********WELCOME TO BATTLESHIP!*******|')
    print('|**************************************|')
    print('|**************************************|')
    print('|*********  The Game For All!  ********|')
    print('|**************************************|')
    print('|**************************************|')
    print('|**************************************|')
    print()
    
# end

def print_vessel(x, y, direction, vessel_index):
	name = VESSEL_NAMES[vessel_index] #Pulling name of vessel desired - from list of names

	#Printing position/direction in a easy to read format (on console)
	print('Your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(y + 1) + ')')
	print('It is positioned ' + direction + 'ly.')
	print() #empty line

	print("  | A B C D E F G H I J")
	print("1 |",grid[0])
	print("2 |",grid[1])
	print("3 |",grid[2])
	print("4 |",grid[3])
	print("5 |",grid[4])
	print("6 |",grid[5])
	print("7 |",grid[6])
	print("8 |",grid[7])
	print("9 |",grid[8])
	print("10|",grid[9])									
	global grid
	


# end

def get_location(vessel_index):
    #global variables that we are editing
    global x # this function can edit x
    global y # this function can edit y
    global direction
   
    #Getting name and size of vessel for next statements
    name = VESSEL_NAMES[vessel_index]
    size = VESSEL_SIZES[vessel_index]
    
    #Printing prompt for user, following the user's input. 
    print ('Where would you like to place your ' + name + ' (' + str(size) + ' spaces)')
    x = input('Enter horizontal position (A-J):')
    y = input('Enter vertical position (1-10) :')
    direction = input("Enter direction of vessel (Horizontal/Vertical): ")
    print() #Adding a empty line
	
# end

def validate_location(x, y, direction, vessel_index):
	# check if string is a single letter or smaller than a three digit number, if not, asks for input again, then checks
	global grid
	name = VESSEL_NAMES[vessel_index]
	size = VESSEL_SIZES[vessel_index]
	
	if (len(x) == 1) and (len(y) < 3):
		
		#Converting row(x) and column(y) into integers which can be easily modified.
		x = (ord(x) - ord('A'))
		y = (int(y) - 1)
		#Puts vessel starting point onto grid
		grid[x][y] = VESSEL_SIZES[vessel_index] 		
		
		# checks if location is on the board and if the ship will fit, if not asks for input again and checks again
		if (direction == 'Horizontal') and (-1 < x < (10 - size)) and (-1 < y < 10):
			index_h = 0
			while index_h <= VESSEL_SIZES[vessel_index]:
				index_h = index_h + 1 
				y = y + 1
				grid[x][y] = VESSEL_SIZES[vessel_index]
			
			y = y - VESSEL_SIZES[vessel_index]	
			print_vessel(x, y, direction, vessel_index)
			print('The end of your ' + name + ' is located at (' + chr(((x + size - 1) % 10) + ord('A')) + ', ' + str(y + 1) + ')')
			print()
		elif direction == 'Vertical' and (-1 < y < (10 - size)) and (-1 < x < 10):  
			index_v = 0
			while index_v <= VESSEL_SIZES[vessel_index]:
				index_v = index_v + 1
				x = x + 1
				grid[x][y] = VESSEL_SIZES[vessel_index]
				
			x = x - VESSEL_SIZES[vessel_index]	
			print_vessel(x, y, direction, vessel_index)
			print('The end of your ' + name + ' is located at (' + chr(x + ord('A')) + ', ' + str(((y + size - 1) % 10) + 1) + ')')
			print()
		else:
			print('The location you entered is not on the board!')
			get_location(index)
			validate_location(name, size, direction, vessel_index)
	else:
		print('Please enter a LETTER (between A-J) and a NUMBER (between 1-10!)')
		get_location(index)
		validate_location(name, size, direction, vessel_index)


#Enter quits the program when the user inputs q
def program_stop():
	quit = 'n'
	while quit == 'n':
		quit = input("Do you want to quit(y/n): ")	
	

def main():
	print_titlescreen();
	global index
	index = 0
	for index in range(len(VESSEL_NAMES)):
		get_location(index)
		validate_location(x, y, direction, index)
		index = index + 1    	
	
	#Calling Program to stop program.
	program_stop()
	
# end

main()
