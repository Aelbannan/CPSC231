#Imports
import grid
import ai
import human



# Title Screen! Now a function!
def print_titlescreen():
	
	global NAME
	print()
	print('________________________________________')
	print('|*********WELCOME TO BATTLESHIP!*******|')
	print('|**************************************|')
	print('|**************************************|')
	print('|*********A game like no other!********|')
	print('|**************************************|')
	print('|**************************************|')
	print('|**************************************|')
	print()
	NAME = 'Admiral ' + input('What is your name? ')
	print()
# end

# doesn't quit unless q is entered	
def enter_choice():
	choice = ''
	while not choice == 'q':
		choice = input('Enter choice: ')
		


# now put it all together!
def main():
        
    # prints VESSEL_NAME[index], location, and orientation of a vessel
	print_titlescreen()
	grid.print_grid()
    # Ask user to place all 5 ships
	i = 0
	for i in range(5): # for loop
		human.get_location(i)
		grid.print_grid()
		ai.get_location(i)
		grid.print_grid()
		
	enter_choice()
	return
# end

main() 
