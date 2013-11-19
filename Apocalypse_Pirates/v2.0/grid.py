#Comments


b = '[ ]'
GRID_HEIGHT = 5
GRID_WIDTH = 5

#Grid Class

class Grid:
	def __init__(self):
	

		self.board = [[b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
	

	def save_grid(_file, header, grid):
	# Saves the grid to an open file
	
		_file.write(header)	
	
		for i in grid:
			
			for j in i:
				
				_file.write(str(j))
				
			_file.write('\n')



			
		

	def load_file(_file):
		
		grid = []
		
		_file.readline() # reads the header
		
		for i in range(GRID_WIDTH):
			line = _file.readline()[:-1]
			grid.append(list(line))
				
		return grid
		
	
	def setup_board(self, piece_loc):
		
		for i in piece_loc:
			
			loc = piece_loc[i]
			
			if loc != 'dead':
				row = int(loc[0])
				col = int(loc[1])
				self.board[row][col] = i
			
	
	def move_piece(self, row, col, piece, p_loc):
		p_loc[piece] = [row, col]
		update_grid(p_loc) 
		return p_loc
		
	def update_grid(self, p_loc):			
		self.board = [[b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b], \
                [b,b,b,b,b]]
		for i in p_loc:
			if p_loc[i] != 'dead':
				self.board[p_loc[i][0]][p_loc[i][1]] = i
	
	def validate_location(self, row, col, new_row, new_col, piece, p_loc):
	
        #If piece selected is a white knight
		if piece[1] == 'K':
			#Change 'BK' check to 'K' | WE DONT WANT IT TO KILL ITS OWN PIECE
            # We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
			for i in range(8):        
				if (new_col == col + KNIGHT_MOVE[i][0]) and (new_row == row + KNIGHT_MOVE[i][1]) and ((board[new_row][new_col] == 'BK') or (board[new_row][new_col] == 'BP') or (board[new_row][new_col] == grid.b)):
						# if enemy is killed, taunt them!
						if (board[new_row][new_col] == 'BK' or board[new_row][new_col] == 'BP'): 
							return True
       
		elif piece[1] == 'P':
			if piece[0] == 'W':
				forward = -1
			elif piece[0] == 'B':
				forward = 1
			
            # If there's nothing in front of the piece, move it up 
			if (new_col == col) and (new_row == row + forward) and (board[new_row][new_col] == grid.b):
				return True

            # If there is an enemy to the top right, kill it 
			elif (new_col == col + 1) and (new_row == row+ forward) and (board[new_row][new_col][0] == 'B'):
				return True

            # If there is an enemy to the top left, kill it 
			elif (new_col == col - 1) and (new_row == row + forward) and (board[new_row][new_col][0] == 'B'):
				return True
                    
                    
                    
def finalize_move(human_grid, ai_grid, last_human, last_ai):
	for i in range(len(human_grid)):
		for j in range(len(human_grid[i])):
			if human_grid[i][j]== b or ai_grid[i][j] == b:
				pass
			else:
				if human_grid[i][j] == last_human:
					if ai_grid[i][j] == last_ai:
						if last_human[1] < last_ai[1]:
							ai_grid[i][j] == b
							ai.pieces[last_ai] = 'dead'
						elif last_human[1] > last_ai[1]:
							human_grid[i][j] == b
							human.pieces[last_human] = 'dead'
						else:
							human_grid[i][j] == b
							human.pieces[last_human] = 'dead'
							ai_grid[i][j] == b
							ai.pieces[last_ai] = 'dead'
					else:
						ai_grid[i][j] == b
						ai.pieces[last_ai] = 'dead'	
				else:
					human_grid[i][j] == b
					human.pieces[last_human] = 'dead'
	return human_grid, ai_grid

def print_grid(human_grid, ai_grid):
	
	for i in range(len(human_grid)):
		for j in range(len(human_grid[i])):
			if human_grid[i][j] != b:
				print(human_grid[i][j], end = "")
			elif ai_grid[i][j] != b:
				print(ai_grid[i][j], end = "")
			else:
				print(b, end = "")
		print()


			
			
			
			
				
