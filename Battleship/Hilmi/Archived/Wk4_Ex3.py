# Title Screen! Now a function!
def titlescreen():
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
    return;
# end


def print_vessel(name, column, row, direction):

    #Calculate Vessel Information relvant to displaying correct values 
    rowd = row + 1 #Prints row location, because 10 cannot be converted into a strings ASCII number
    columnd = chr(column + ord('A')) #Similar to above, but converting to a string, so it can be displayed
    
    #Print information related to Vessel
    print(name, "Position: ")
    print("Column: ", columnd)
    print("Row: ", rowd)
    print("Direction: ", direction)
     

def modify_row(previous_vessel_size, vessel_name): 
    #Applies row calculations to ensure valid entry of concurrent vessels
    global row
    row = (row + previous_vessel_size) % 10
    print_vessel(vessel_name, column, row, direction)
 

def modify_column(previous_vessel_size, vessel_name):
	#Applies column calculations to ensure valid entry of concurrent vessels
	global column
	column = (column + previous_vessel_size) % 10
	print_vessel(vessel_name, column, row, direction)     

def get_location(name, size):
    #Global variables pertaining to local function
    global row
    global column 
    global direction
    #Begins getting user input for vessel row and column
    print("Enter the placement of your", name, "(" , size, "spaces)")
    column = input("Left Column (A-J): ")
    row = input("Top Row (1 - 10): ")
    #Performs calculations relevant to validate location's ability to check.
    row = int(row) - 1
    column = ord(column) - ord('A')
    print_vessel(name, column, row, direction)
    direction = direction.lower()
    
    #If statement performing different calculations for various vessels
    if direction == "horizontal":
       if  0 <= row  < 10 and 0 <= column < 10: #ASCII Values between 0-9 are valid
         row = int(row)
         vessel_size_end = (column + vessel_size - 1) % 10#Pertaining to print_vessels adding 1
         vessel_size_end = chr(vessel_size_end + ord('A')) #Converting to printable string
         print("Vessel End Location: ", vessel_size_end, str(row + 1))
       else:
         row = 0
         column = 0     
         print("Please enter an acceptable row or/and column!")
         get_location(name, vessel_size) #Retrying entry  

    #Performs same as above function except as noted    
    elif direction == "vertical":
        if  0 <= row  < 10 and 0 <= column < 10:
            row = int(row)
            vessel_size_end = (row + vessel_size) % 10 #Row not column!
            print("Row End: ", vessel_size_end)
        else:          
            row = 0 
            column = 0
            print("Please enter an acceptable row or/and column!")
            get_location(name, vessel_size)         
    else:
        print("You have entered a wrong direction, please try again.")
        get_location(name, vessel_size)
     
   
def main():
    global direction
    titlescreen()
    global name
    global vessel_size
    name = "Aircraft Carrier"
    vessel_size = 5
    direction = "Horizontal"
    get_location(name, vessel_size)

	#Calling functions to modify locations of vessels. 
    direction = "Vertical"
    modify_column(5, "Submarine")
     
    direction = "Horizontal"
    modify_row(4, "Battleship")
     
    direction = "Vertical"
    modify_column(3, "Destroyer")
     
    direction = "Horizontal"
    modify_row(3, "Patrol Boat")
 
main()
