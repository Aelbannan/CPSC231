from tkinter import *
from tkinter import messagebox
import functools

myfont = ('Trebuchet MS', 16)
myfont2 = ('Trebuchet MS', 10)

class BattleshipGUI:
	def __init__(self):
	
		self.defend_grid = [['~' for i in range(10)] for j in range(10)]
		self.attack_grid = [['~' for i in range(10)] for j in range(10)]
		
		self.root = Tk()
		Label(text = 'Attack', font = myfont).grid(row = 0, column = 0)
		Label(text = 'Defend', font = myfont).grid(row = 2, column = 0)
		
		self.attack_frame, self.attack_grid_buttons = self.create_grid(10,10, self.attack_button_clicked)
		self.attack_frame.grid(row = 1, column = 0)
		
		self.defend_frame, self.defend_grid_buttons = self.create_grid(10,10, self.defend_button_clicked)
		self.defend_frame.grid(row = 3, column = 0)
		
		
		self.update_GUI(self.attack_grid, self.attack_grid_buttons)
		self.update_GUI(self.defend_grid, self.defend_grid_buttons)
		
		self.root.mainloop()
		
		#
		
	def create_grid(self, width, height, func):
		grid = []
		
		frame = Frame(self.root)
		
		for i in range(width):
			row = []
			for j in range(height):
				button = Button(frame, font = myfont2, text = "   ", command = functools.partial(func, i, j))
				button.grid(row = i, column = j)
				row.append(button)
			grid.append(row)
			
		return frame, grid
		
	def update_GUI(self, grid, buttons):
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				button = buttons[i][j]
				button['text'] = grid[i][j]
			
	def defend_button_clicked(self, row, col):
		messagebox.showinfo('Defend Grid','You clicked on: \nRow:'+ str(row + 1) + '\nColumn:' + str(col + 1), icon = 'info')
		
		if col <= 5:
			for i in range(5):
				self.defend_grid[row][col + i] = '5'
		
		self.update_GUI(self.defend_grid, self.defend_grid_buttons)
		
	def attack_button_clicked(self, row, col):
		messagebox.showinfo('Attack Grid','You clicked on: \nRow:'+ str(row + 1) + '\nColumn:' + str(col + 1), icon = 'warning')
		
		self.attack_grid[row][col] = '0'
		self.update_GUI(self.attack_grid, self.attack_grid_buttons)
		
BattleshipGUI()
