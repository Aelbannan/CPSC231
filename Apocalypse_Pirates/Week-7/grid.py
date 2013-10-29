
#Global grid constants

GRID_HEIGHT = 5
GRID_WIDTH = 5
NUM_OF_PIECES = 7 # number of pieces for each side
PIECE_W_START = [15, 21, 22, 23, 19, 20, 24] # starting location for white pieces
PIECE_W = ['WP', 'WP', 'WP', 'WP', 'WP', 'WK', 'WK'] # white pieces
PIECE_B_START = [5, 1, 2, 3 ,9, 0, 4] # starting location for white pieces
PIECE_B = ['BP', 'BP', 'BP', 'BP', 'BP', 'BK', 'BK'] # black pieces
KNIGHT_MOVE = [[2,1], 
			  [2,-1], 
			  [-2,1], 
			  [-2,-1], 
			  [1,2], 
			  [1,-2], 
			  [-1,2], 
			  [-1,-2]] # all moves a knight can make
			  
#Grid; Global variables 
b = '[]'



# puts all pieces on board
def setup_board(board):
	
	# place pieces on board according to thier locations in the arrays
	for i in range(7):
		board[PIECE_W_START[i]] = PIECE_W[i]
		board[PIECE_B_START[i]] = PIECE_B[i]
	return board

# changes a 2d index to a 1d index in a list
def List2Dto1D(row, col):
	return (col + (row * GRID_WIDTH))

# prints out the grid		
def print_board(board):

	# board header
	print('__________________________');
	print('|  |  A  B  C  D  E |');
	print('--------------------------');

	for row in range(GRID_HEIGHT):
		# print row number
		print( '|0' + str(row + 1) + '| ', end = '');

		# print entire row on one line
		for col in range(GRID_WIDTH):
			print(board[List2Dto1D(row, col)] + ' ', end = '');
		print('|');

	print();
	print('WP = White Pawn \t WK = White Knight') # tell user what piece is what
	print('BP = Black Pawn \t BK = Black Knight') 
	print()
	
	
def check_knight(board): #Checks if Pawn can become a knight. 4 is the end of the grid, 0 is the other end. 
	for i in range(GRID_WIDTH):
		if board[List2Dto1D(0, i)] == 'WP':
			board[List2Dto1D(0, i)] = 'WK'
		if board[List2Dto1D(4, i)] == 'BP':
			board[List2Dto1D(4, i)] = 'BK'
	return board
			
def get_winner(board): #Checks if AI, or Human has won, prints trophy if human wins, otherwise prints you lose. 
	black_alive = False
	white_alive = False
	
	for i in range(GRID_HEIGHT * GRID_WIDTH): #Running loop a total of 5x5 times; 25
		if board[i] == "BP" or board[i] ==  "BK": 
			black_alive = True
		if board[i] == "WP" or board[i] == "WK":
			white_alive = True
			
	if white_alive == True and black_alive == True:		
		return True
	elif white_alive == True and black_alive == False:
		print(	'/---------------------------\\n|----------YOU WIN!----------|\n==============================\n| | | | | | | | | | | | | | ||\n******************************\n             | |                \n       ==============')
		return False
	elif black_alive == True and white_alive == False:
		print("You Lose.")
		return False
	
	
	
