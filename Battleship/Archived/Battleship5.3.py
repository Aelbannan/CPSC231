
import random
B='~'
grid = [[B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B], 
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B],
        [B,B,B,B,B,B,B,B,B,B]]


VESSEL_SIZE =[5,4,3,2]
VESSEL_NAMES =['aircraft carrier','battleship','submarine','destroyer']
NUM_OF_VESSELS= 4
GRID_WIDTH = 10
GRID_HEIGHT = 10
# Title Screen!
def titlescreen():
    print('________________________________________')
    print('|*********WELCOME TO BATTLESHIP!*******|')
    print('|**************************************|')
    print('|**************************************|')
    print('|*********A game like no other!********|')
    print('|**************************************|')
    print('|**************************************|')
    print('|**************************************|')


def get_location(index) :
    global column
    global row
    global direction


    print("Enter placement of your", VESSEL_NAMES[index], "(", VESSEL_SIZE[index],  "spaces)")
    column = random.randint(0,9)
    row = random.randint(0,9)
    direction=random.randint(1,2)
    if direction == 1:
        direction = 'horizontal'

    else:
        direction = 'vertical'

    # Convert user input to row and column values between 0 and 9
 #   column = ord(column) - ord('A')
    #row = row - 1

    # Check that the input entered by the user is valid.
    if (column < 0 or column >= GRID_WIDTH) :
        # The start column entered is invalid.
        print("Invalid column.  Column must be a value between A and J")
        get_location(index);
    elif (row < 0 or row >= GRID_HEIGHT) :
        # the start row is invalid
        print("Invalid row.  Row must be a value between 1 and 10")
        get_location(index);


    #the column is too long and does not fit the board
    else :
        if (direction == 'horizontal' and column + VESSEL_SIZE[index] > GRID_WIDTH) :
            print("Invalid column.  The vessel is directed horizontally to the right")
            print("and does not fit on the grid with this starting column.")
            get_location(index);


        # the row is too long and it does not fit into the board
        elif (direction == 'vertical' and row + VESSEL_SIZE[index] > GRID_HEIGHT) :
            print("Invalid row.  The vessel is directed vertically downwards")
            print("and does not fit on the grid with this starting row.")
            get_location(index);


        #the location is valid, so it moves on
        else :
            print()
            has_overlap(index,column,row,direction)


def has_overlap(index,column,row,direction):
    
    
    if direction == 'horizontal':
        startpoint=column + 1
        endpoint=column+VESSEL_SIZE[index] 

        while endpoint > (column):
            if grid[column][row] != '~':
                column=column + 1
                get_location(index)

            else:
                column=column+1
    else:
        startpoint=row + 1
        endpoint=row+VESSEL_SIZE[index]
    

        while endpoint > row:
            if grid[column][row] != '~':
                row=row+1
                get_location(index)
            else:
                row=row + 1
def print_grid():
    global grid

    print ('   A B C D E F G H I J')
    for row_index in range (0, GRID_HEIGHT) :
        print(row_index + 1, '' , end='')
        if (row_index + 1 < 10):
                print(' ', end='')
        for column_index in range (0,GRID_WIDTH) :
            print(grid[column_index][row_index], '', end='')
        print('')


#places the position of all vessels into the correct grid position
def print_location(index):
    global column
    global row
    
    if direction == 'horizontal':
        for column in range (column, column +VESSEL_SIZE[index]):
            grid[column][row] = VESSEL_SIZE[index]
            column =column + 1
    else:
        for row in range(row,row + VESSEL_SIZE[index]):
            grid[column][row]= VESSEL_SIZE[index]
            row =row + 1
            


#user is stuck in a loop unless he/she types 'q'
def user_choice():
    choice=input('enter your choice: ')
    quit='q'
    while choice != quit:
        choice=input('enter your choice: ')
    print('you quit')
    

def main() :
    titlescreen()
    print()
    # Get location for aircraft carrier from user, and run it into print_location(index)
    for index in range (0,NUM_OF_VESSELS):
        get_location(index)
       # print(column)
 #       has_overlap(index,column,row,direction)
        print_location(index)
  #      has_overlap(index,column,row,direction)
    #after taking the locations is finished call print_grid() function, and placing all the vessel into it
    print_grid()
 #   has_overlap(index,column,row,direction)    
    user_choice()

main()
