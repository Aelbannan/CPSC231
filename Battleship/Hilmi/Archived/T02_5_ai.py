#********************************************
# By Hilmi Abou-Saleh
# October 14, 2013
# Battleship CPSC231 - Brown Edition
# - This program is not fully functional, it only demonstrates set5_ex1
# - It will not ask the user for input, a second for loop has to be integrated
# - And a second grid. 
# - I have taken the group submission and added my code to it.
# - So it has T02G05 Code in the program
# - The consequence of it being edited by Ahmed is that you see a ton of these ';'....
#********************************************

# Getting Imports
import random 

# CONSTANTS values 
GRID_HEIGHT = 10;
GRID_WIDTH = 10;
VESSEL_NAME = ['Aircraft Carrier', 'Battleship', 'Submarine', 'Destroyer', 'Patrol Boat'];
VESSEL_SIZE = [5, 4, 3, 2, 2];
NAME = '';

# global variables
direction = 'horizontal';
x = ord('A');
y = 0;
#Setting grid variables
w = '~'
grid = 		[
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
			[w,w,w,w,w,w,w,w,w,w]];

# Title Screen! Now a function!
def print_titlescreen():
	
	global NAME;
	print();
	print('________________________________________');
	print('|*********WELCOME TO BATTLESHIP!*******|');
	print('|**************************************|');
	print('|**************************************|');
	print('|*********A game like no other!********|');
	print('|**************************************|');
	print('|**************************************|');
	print('|**************************************|');
	print();
	NAME = 'Admiral ' + input('What is your name? ');
	print();
# end
			
# print out the grid			
def print_grid():
	
	print('__________________________');
	print('|  | A B C D E F G H I J |');
	print('--------------------------');
	row = 0;
	column = 0;
	
	# print the grid using a nested for loop
	for row in range(GRID_HEIGHT):
		
		if row  == 9:
			print( '|' + str(row + 1) + '| ', end = '');
		else:
			print( '|0' + str(row + 1) + '| ', end = '');			
		for column in range(0, GRID_WIDTH):
			print(grid[column][row] + ' ', end = '');
		print('|');
		
	print();

# let's the user choose where to place vessel
def get_location_user(index):
	
	global x; # this function can edit x
	global y; # this function can edit y
	global direction; # this function can edit direction
	# Get row, column, direction from player
	print (NAME + ', where would you like to place your ' + VESSEL_NAME[index] + '? (' + str(VESSEL_SIZE[index]) + ' spaces)');
	x = input('Horizontal position, Sir?(A-J):');
	y = input('Vertical position? (1-10):');
	direction = input('Direction? [h]orizontal or [v]ertical:');
	print();
# end

def get_location(index):
	#Setting globals for editing
	global x
	global y
	global direction
	#Selecting Random Values for row, column and direction
	x = random.randint(1, 10)
	y = random.randint(1, 10)
	#y = chr(y + 64)
	direction = random.randint(1,2)
	
	#Loop sets a number to a character for place vessel to 'decode' 
	if direction == 1:
		direction = 'v'
	else:
		direction = 'h'
		
	#This loop makes sure the end of the vessel does not go over the edge of the board.
	if (direction == 'h') and (-1 < x < (GRID_WIDTH - VESSEL_SIZE[index])) and (-1 < y < GRID_HEIGHT):
		place_vessel(index);
	
	elif direction == 'v' and (-1 < y < (GRID_HEIGHT - VESSEL_SIZE[index])) and (-1 < x < GRID_WIDTH):  
		place_vessel(index);
	
	#Recursive statement, to retry if fails.
	else:
		get_location(index)
#No need for user input or any sort of warning.

# put vessel on board
def place_vessel(index):
	
	global x;
	global y;
	
	#check if direction is h or v, then places ship accordingly
	if direction == 'h': 
			for x in range(x, x + VESSEL_SIZE[index]):
				grid[x][y] = str(VESSEL_SIZE[index]);
				
	elif direction == 'v':
			for y in range(y, y + VESSEL_SIZE[index]):
				grid[x][y] = str(VESSEL_SIZE[index]);
				
# checks if the location is valid
def validate_location(index):
	
	global x; # this function can edit x
	global y; # this function can edit y
	# check if string is a single letter or smaller than a three digit number, if not, asks for input again, then checks
	
	#check if strings are appropriate length
	if (len(x) == 1) and (len(y) < 3):
		x = (ord(x) - ord('A'));
		y = (int(y) - 1);
		
		# checks if location is on the board and if the ship will fit, if not asks for input again and checks again
		if (direction == 'h') and (-1 < x < (GRID_WIDTH - VESSEL_SIZE[index])) and (-1 < y < GRID_HEIGHT):
			place_vessel(index);
			
		elif direction == 'v' and (-1 < y < (GRID_HEIGHT - VESSEL_SIZE[index])) and (-1 < x < GRID_WIDTH):  
			place_vessel(index);
			
		else:
			print('The location you entered is not on the board!');
			get_location(index);
			validate_location(index); # recursive
			
	else:
		print('Please enter a LETTER (between A-J) and a NUMBER (between 1-10!)');
		get_location(index);
		validate_location(index); # recursive
	return;
	
# doesn't quit unless q is entered	
def enter_choice():
	choice = '';
	while not choice == 'q':
		choice = input('Enter choice: ');
		
# now put it all together!
def main():
        
        # prints VESSEL_NAME[index], location, and orientation of a vessel
	print_titlescreen();
	print_grid();
        # Ask user to place all 5 ships
	i = 0;
	for i in range(5): # for loop
		get_location(i);
		#validate_location(i);
		print_grid();

#Commented out because it is still in the works so to speak.	
"""
	i = 0;
	for i in range(5): # for loop
		get_location_old(i);
		validate_location(i);
		print_grid();
"""		
	enter_choice();
	return;
# end

main(); 
