
def print_vessel(name, column, row, direction):
	rowd = row + 1
	columnd = chr(column + ord('A'))
	print(name, "Position: ")
	print("Column: ", columnd)
	print("Row: ", rowd)
	print("Direction: ", direction)
	
def modify_row(previous_vessel_size, vessel_name):
	global row
	row = (row + previous_vessel_size) % 10
	print_vessel(vessel_name)

def modify_column(previous_vessel_size, vessel_name):
	global column
	column = (column + previous_vessel_size) % 10
	print_vessel(vessel_name)
	
def get_location(name, size):
	global row
	global column
	
	print("Enter the placement of your", name, "(" , size, "spaces)")
	column = input("Left Column (A-J): ")
	row = input("Top Row (0 - 9): ")
	row = ord(row)
	column = ord(column.upper())
	
	
	
def validate_location(vessel_size):
	global row
	global direction
	global column
	direction = direction.lower()
	
	if direction == "horizontal":
		if  64 < column < 91 or 48 < row < 58 :		
			row = int(row)
			vessel_size_end = column + vessel_size
			vessel_size_end = str(vessel_size_end)
			print(vessel_size_end, str(row))
		else:
			row = 0 
			column = 0 		
			print("Please enter acceptable characters!")
			
	elif direction == "vertical":
		if  64 < column < 91 or 48 < row < 58 :			
			row = int(row)
			column = column.upper() - ord('A')
			vessel_size_end = row + vessel_size
			print("Row End: ", vessel_size_end)
		else:			
			row = 0
			column = 0 
			print("Please enter acceptable characters!")
		
	else:
		print("You have entered a wrong column/direction, please try again.")
		get_location(name, vessel_size)
	

def main():
	global direction
	#titlescreen()
	global name
	global vessel_size
	name = "Aircraft Carrier"
	vessel_size = 5
	direction = "Horizontal"
	get_location(name, vessel_size)
	validate_location(vessel_size)	
	print_vessel(name, column, row, direction)
	#direction = "Vertical"
	#modify_column(5, "Submarine")
	
	#direction = "Horizontal"
	#modify_row(4, "Battleship")
	
	#direction = "Vertical"
	#modify_column(3, "Destroyer")
	
	#direction = "Horizontal"
	#modify_row(3, "Patrol Boat")

main()
