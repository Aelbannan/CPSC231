#Exercise Set 11 - Exercise 1
#Tutorial 2 Group 5 - Hilmi Abou-Saleh
#Advanced list and string handling. 

def open_file(name):
	#Tries to open the file requested
	try:
		read = open(name, 'r')
		return True
	#If it returns with a IOError, it will print an error message and call the main function	
	except IOError:
		print("Invalid file name.")
		return False

#Function deals with the amount of lines present in the code.
def line_total(name):
	#variables
	total = 0
	#Reading begin
	read = open(name, 'r')
	
	#Set the first line to x  
	x = read.readline()
	while x != "": #If the line does not equal EOF.
	
		x = read.readline() #Read the next line
		total = total +1  #Add one to the total
	
	read.seek(0)#Returns the file to the first position
	return total - 1 #For the range function. 0 = 1 therefore 6 = 7 


#Function calculates the total number from file. 
def add_list(name, line):
	#Reading bein
	read = open(name, 'r') 
	#First line variable
	y = read.readline()
	#Sets list variable
	li = []
	#For loop that runs until its out of lines.
	for total in range(0, line):
		#Reading then next line
		x = read.readline()
		#Try to make it an integer 
		try:
			x = int(x)
			#Adds x into the list		
			li.append(x)
			
		#Return with an exception and continue the calculation	
		except ValueError:
			print("Problem reading file. Cannot convert " + str(x) + " to an integer.")
	
	#Prints the final total after sorting. 
	li.sort()
	print(li)	
		
#Function asks the user for the filename and then calls the open_file function with the name provided.
def main():
	#Asks user for input
	name = input("Enter a filename: ")
	
	#Checks if the file is a valid file name
	if open_file(name):
		#If true, calculates the total amount of lines present in the code
		lineno = line_total(name)
		#Finally doing the actual calculation. 
		add_list(name, lineno)
	
	#Prompts user for input after failed input
	else:
		main()

main()