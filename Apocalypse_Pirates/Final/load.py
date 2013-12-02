read = open('ai.apoc', 'r')
board = [['']*5 for i in range(5)]


for  x in range(0, 5):
	line = read.readline()
	line = line.split(',')
	for y in range(0, 5):
		gridvar = line[y]
		board[x][y] = gridvar


for i in range(0, 5):
	for j in range(0, 5):
		if board[i][j] == '[ ]':
			print(" ", end =" ")
		else:
			print(board[i][j], end=" ")
	print('\n')