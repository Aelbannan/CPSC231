#Comments go here 

import gui
import ai
#Global Variables
b = '[ ]'
GRID_HEIGHT = 5
GRID_WIDTH = 5
KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]

#Grid Class

class State:
	def __init__(self):
		
		self.dic = {}
		self.char = 'none'
		self.color = 'white'
		self.penalty = 0
		self.board = [[b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
				
				
	

	def save_state(self, file):
		
		#Save the character and ending the line.
		file.write('###CHAR###\n'+str(self.char)+'\n')
		file.write('###COLOR###\n'+self.color + '\n')
		file.write('###PENALTY POINTS###\n'+str(self.penalty)+'\n')
		
		file.write('###PIECES###\n')
		file.write(str(len(self.dic)) + '\n')
		for i in self.dic:
			
			file.write(i+'\n')
			for k in range(len(self.dic[i])):
				file.write(str(self.dic[i][k]))
			file.write('\n')
		

		
	# Used for loading a grid from a file 
	def load_state(self, file):
		
		self.dic = {}
		
		try:
			file.readline()
			self.char = int(file.readline()[:-1])
			
			file.readline()
			self.color = file.readline()[:-1]
		
			file.readline()
			self.penalty = int(file.readline()[:-1])
			
			file.readline()
			
			for i in range(int(file.readline()[:-1])):
			
				key = file.readline()[:-1]
				
				loc = file.readline()[:-1]
				
				if loc != 'dead':
					loc = list(loc)
				
					for n in range(len(loc)):
						loc[n] = int(loc[n])
					
				self.dic[key] = loc
				
			self.board = recreate_grid(self.dic)
			
		except ValueError:
			return True

		
	#initialize board 
	def setup_board(self, piece_loc):
		
		for i in piece_loc:
			
			location = piece_loc[i]
			
			if location != 'dead':
            #row and column are equal to loc's x and y co-ordinates (loc is a list with only two values)
				row = int(location[0])
				col = int(location[1])
				self.board[row][col] = i
			
   #Changes the selected piece's location and updates the grid as well as returning the new co-ordinates of all the pieces(piece_loc)
	def move_piece(self, row, col, piece, piece_loc):
		piece_loc[piece] = [row, col]
		self.board = recreate_grid(piece_loc)
		return piece_loc
		

	
	def validate_location(self, row, col, new_row, new_col, piece, oth_board):
	
      #If piece selected is a knight
		#If piece selected is a knight
		if piece[1] == 'K':
			#Change 'BK' check to 'K' | WE DONT WANT IT TO KILL ITS OWN PIECE
            # We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
			for i in range(8):        
				if (new_col == col + KNIGHT_MOVE[i][0]) and (new_row == row + KNIGHT_MOVE[i][1]) and (self.board[new_row][new_col] == b):
						# if enemy is killed, taunt them!
							return True
      #If the piece is a pawn
		elif piece[1] == 'P':
			#For white, forward is negative
			if piece[0] == 'W':
				forward = -1
			#Vice-versa 
			elif piece[0] == 'B':
				forward = 1
			
            # If there's nothing in front of the piece, move it up 
			if (new_col == col) and (new_row == row + forward) and (self.board[new_row][new_col] == b) and (oth_board[new_row][new_col] == b):
				return True

            # If there is an enemy to the top right, kill it 
			elif (new_col == col + 1) and (new_row == row+ forward) and (self.board[new_row][new_col]== b) and (oth_board[new_row][new_col] != b):
				return True

            # If there is an enemy to the top left, kill it 
			elif (new_col == col - 1) and (new_row == row + forward) and (self.board[new_row][new_col] == b) and (oth_board[new_row][new_col] != b):
				return True
		return False
                    
                    
### Lets pieces kill each other n so on###               
def finalize_move( dic_human, dic_ai, last_human, last_ai):
	#print('new')
	test_h = dict(dic_human)
	test_a = dict(dic_ai)
	msg = ''
	
	for piece_h in test_h:
		
		for piece_a in test_a:
			
			if test_h[piece_h] == test_a[piece_a]:
				#print('same', piece_h, piece_a)
				if piece_h == last_human:
					#print('h')
					if piece_a == last_ai:
						#print('a')
						if piece_h[1] == piece_a[1]:
							msg = ai.speak.get_speech(4)
							dic_human[last_human] = 'dead'
							dic_ai[last_ai] = 'dead'
						elif piece_h[1] > piece_a[1]:
							msg = ai.speak.get_speech(3)
							dic_human[last_human] = 'dead'
						else:
							msg = ai.speak.get_speech(2)
							dic_ai[last_ai] = 'dead'
					
					else:
						msg = ai.speak.get_speech(2)
						dic_ai[piece_a] = 'dead'
				
				else:
					msg = ai.speak.get_speech(3)
					dic_human[piece_h] = 'dead'

	return dic_human, dic_ai, msg
	

### creates a grid from a dictionary ###								
def recreate_grid(dic):
		
		temp_grid = [[b for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]
		
		for i in dic: # loop thru dictionary
		
			location = dic[i]
		
			if location != 'dead': # if not dead
			
				# place the piece on the board
				row = int(location[0])
				col = int(location[1])
				temp_grid[row][col] = i
		
		return temp_grid	

### checks if either side has won (if any pawns left)###		
def get_winner(dic_human, dic_ai):
	
	x = 0 
	y = 0

	
	for piece in dic_human:
		if piece[1] == 'P' and dic_human[piece] != 'dead':
			x =+ 1
	for piece in dic_ai:
		if piece[1] == 'P' and dic_ai[piece] != 'dead':
			y =+ 1
	
	if x == 0 and y == 0:
		return 'draw'
	
	elif x == 0 and y > 0:
		return 'ai'
	
	elif x > 0 and y == 0:
		return 'human'
	else:
		return 'none'		
			
			
### turns pawns to knights if possible ###
def check_knight(dic):
			
		counter = 0
		mp = 'none'
			
		for piece in dic:
			if piece[1] == 'K' and dic[piece] != 'dead':
				counter += 1
                
			if piece[0] == 'B':
				end_row = 4
			elif piece[0] == 'W':
				end_row = 0
      
      
		for piece in dic: 
      
			loc = dic[piece]
      	              
			if loc[0] == end_row and piece[1] == 'P':
      	         
				if counter < 2:
			
					del dic[piece]
					num = int(piece[2]) + 2
					new_piece = str(piece)
					new_piece = new_piece[0] + 'K' + str(num)
					dic[new_piece] = loc
					
				else:
					
					mp = piece
        
		return dic, mp
			


