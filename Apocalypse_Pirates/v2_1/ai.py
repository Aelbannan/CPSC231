import grid
import random

KNIGHT_MOVE = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
b = '[ ]'

difficulty = 1

possible_moves = []


class node:
	
	def __init__(self):
		self.children = list()
		self.parent = 'none'
		self.level = 0
		self.dic_turn = {}
		self.dic_other = {}
	
	def add_child(self):
		new_node = node()
		self.children.append(new_node)
		new_node.parent = self
		new_node.level = self.level + 1
		return new_node
	
	def get_ancestor(self):
		cur = self
		while cur.level !=2:
			cur = cur.parent
			
		anc = cur
		
		return anc
	
	def get_valid_moves(self, dic_main, dic_oth ):
			
		print('new')

		for piece in dic_main:
		
			loc = dic_main[piece]
		
			if loc != 'dead':
		
		#If piece selected is a knight
				if piece[1] == 'K':
					# We check if the knight is moving in an L-shape, and if the spot is either empty or has an enemy piece
					for i in range(8):
							
						can_move = True
					
						new_row = loc[0] + KNIGHT_MOVE[i][0]
						new_col = loc[1] + KNIGHT_MOVE[i][1] 
							
						#print(piece, new_row, new_col, loc[0], loc[1])
							
						if 0 <= new_col < 5 and 0 <= new_row < 5:
						
							for j in dic_main:
								if dic_main[j] == [new_row, new_col]:
									can_move = False
								
							if can_move:
								print(True)
								
								child = self.add_child()
				
								child.dic_turn = dict(dic_main)
								child.dic_turn[piece] = [new_row, new_col]
								print(child.dic_turn)
								child.dic_other = dict(dic_oth)
								child.last_piece = piece
								
								if self.level % 2 == 1:
									a,b, self.dic_main, child.dic_turn = grid.finalize_move(self.recreate_grid(self.dic_turn), self.recreate_grid(child.dic_turn), self.last_piece, child.last_piece, self.dic_turn, child.dic_turn)	
									
									
								if difficulty > self.level:
									child.get_valid_moves(child.dic_other, child.dic_turn)
								else:
									possible_moves.append(child)
									print('added!', len(possible_moves))
								
					
	def analyze_board(self, dic_1, dic_2):
		total = 0
		
		for i in dic_1:
			if dic_1[i] != 'dead':
				if i[1] == 'P':
					total += 1
				elif i[1] == 'K':
					total += 2
					
		for i in dic_2:
			if dic_2[i] != 'dead':
				if i[1] == 'P':
					total -= 1
				elif i[1] == 'K':
					total -= 2
		
		return total
		
					
		
	def recreate_grid(self, dic):
		
		temp_grid = [[grid.b for i in range(grid.GRID_WIDTH)] for j in range(grid.GRID_HEIGHT)]
		
		for i in dic:
		
			location = dic[i]
		
			if location != 'dead':
				#row and column are equal to loc's x and y co-ordinates (loc is a list with only two values)
				row = int(location[0])
				col = int(location[1])
				temp_grid[row][col] = i
		
		return temp_grid

		
		
def best_moves(node_list):
		high_score = -999
		hi_list = []
		for e in node_list:
			cur_score = e.analyze_board(e.dic_other, e.dic_turn)
			if cur_score > high_score:
				high_score = cur_score
		print (high_score)
			
		e = 0	
		for e in range(len(node_list)):
			cur_score = node_list[e].analyze_board(node_list[e].dic_other, node_list[e].dic_turn)
			if cur_score == high_score:
				hi_list.append(e)
				
		return hi_list




		
def get_move():
	
	global possible_moves

	top = node()
	top.board_ai = top.recreate_grid(dic_ai)
	top.board_human = top.recreate_grid(dic_human)

	top.get_valid_moves( dic_ai, dic_human)
	
	best = best_moves(possible_moves)
	print(best)
	num = random.randint(0, len(best) - 1)
	
	choose = best[num]
	
	chosen_node = possible_moves[choose].get_ancestor()
	
	board.board = chosen_node.recreate_grid(chosen_node.dic_other)
	
	possible_moves = []
	
	return chosen_node.dic_other, chosen_node.last_piece
