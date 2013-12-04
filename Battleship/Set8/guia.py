#Tutorial 2 Group 5 Submission for Week 9/Set 8 (8.3)

#Importing 'everything' from tkinter, and messagebox, because apparently everything doesn't mean messagebox as well. 
from tkinter import *
from tkinter import messagebox

#Some standard imports, functools helps us in the create_grid function. 
import functools
import grid
import t00_0_ai

#Setting up the fonts
myfont = ('Trebuchet MS', 16)
myfont2 = ('Trebuchet MS', 10)



#Class which encompasses the gui
class BattleshipGUI:
	def __init__(self):
	
		self.current_vessel = 0
		
		#Creating attack and defend grid. 
		self.defend_grid = grid.Grid()
		self.attack_grid = grid.Grid()
		
		self.root = Tk()
		
		#Labels for the GUI, explain the grid.
		Label(text = 'Attack', font = myfont).grid(row = 0, column = 0)
		Label(text = 'Defend', font = myfont).grid(row = 2, column = 0)
		
		#Attack frame and buttons being set to buttons and a 10x10 grid. 
		self.attack_frame, self.attack_grid_buttons = self.create_grid(grid.GRID_HEIGHT, grid.GRID_WIDTH, self.attack_button_clicked)
		self.attack_frame.grid(row = 1, column = 0)
		
		#Same as above, except with the defend grid. 
		self.defend_frame, self.defend_grid_buttons = self.create_grid(grid.GRID_HEIGHT, grid.GRID_WIDTH, self.defend_button_clicked)
		self.defend_frame.grid(row = 3, column = 0)
		
		#Disables the attack buttons on the attack grid.
		self.set_grid('disabled', self.attack_grid_buttons)
		
		#Updates the buttons on the defend and attack grid. 
		self.update_GUI(self.defend_grid.grid, self.defend_grid_buttons)
		self.update_GUI(self.attack_grid.grid, self.attack_grid_buttons)

		
		self.root.mainloop()
		
	
		
	def create_grid(self, width, height, func):
		#Creates an empty grid.
		grid = []
		
		#Creates a frame to hold the buttons
		frame = Frame(self.root)
		
		#Loop which goes through the grid and adds the buttons. 
		for i in range(width):
			row = []
			for j in range(height):
				button = Button(frame, font = myfont2, text = "   ", command = functools.partial(func, i, j)) #functools.partial replaces lambda
				button.grid(row = i, column = j)
				
				#Adds the button to the row
				row.append(button)
			#Adds the previous row to the grid. 
			grid.append(row)
			
		return frame, grid
		
	#Sets the state of the grid buttons	
	def set_grid(self, status, buttons):
		
		for i in range(len(buttons)):
			
			for j in range(len(buttons[i])):
				
				button = buttons[i][j]
				
				button['state'] = status

	#Updates the buttons according to the grid. 	
	def update_GUI(self, grid, buttons):
	
		for i in range(len(grid)):
	
			for j in range(len(grid[i])):
	
				button = buttons[i][j]
	
				button['text'] = grid[i][j]
		
	#Runs when defend button is clicked. 		
	def defend_button_clicked(self, row, col):
		
		messagebox.showinfo('Defend Grid','You clicked on: \nRow:'+ str(row + 1) + '\nColumn:' + str(col + 1), icon = 'info')
		
		#Error checking, makes sure vessel is placed correctly. 
		if col <= (grid.GRID_WIDTH - grid.VESSEL_SIZES[self.current_vessel]):
			
			for i in range(grid.VESSEL_SIZES[self.current_vessel]):
			
				self.defend_grid.grid[row][col + i] = grid.VESSEL_SIZES[self.current_vessel]
		
				#Updates grid, and tells ai to make move. 
			self.update_GUI(self.defend_grid.grid, self.defend_grid_buttons)
			t00_0_ai.get_location(self.current_vessel)
			self.current_vessel += 1
		
				#If all the vessels are placed disable the defend grid, and enable the attack grid. 
			if self.current_vessel == grid.NUM_OF_VESSELS:
		
				self.set_grid('normal', self.attack_grid_buttons)	
				self.set_grid('disabled', self.defend_grid_buttons)

		
	#Similar to previous function, but for attack buttons. 	
	def attack_button_clicked(self, row, col):
		
		#Shows message box.
		messagebox.showinfo('Attack Grid','You clicked on: \nRow:'+ str(row + 1) + '\nColumn:' + str(col + 1), icon = 'warning')
		
		#User drops bomb on AI defend grid.
		t00_0_ai.defend_grid.drop_bomb(self.attack_grid, row, col)
		
		#Disables buttons. 
		button = self.attack_grid_buttons[row][col]
		button['state'] = 'disabled'
		
		#Gets the ai's chosen location to drop bomb.
		row, column = t00_0_ai.get_choice()
		
		#AI dropbs bomb on you. 
		self.defend_grid.drop_bomb(t00_0_ai.attack_grid, row, col)
		
		#Updates attack and defend grid.
		self.update_GUI(self.attack_grid.grid, self.attack_grid_buttons)
		self.update_GUI(self.defend_grid.grid, self.defend_grid_buttons)
		
		
		#Win statement. Checks if the Vessels are sunk. Then displays winner. 
		if self.defend_grid.all_vessels_sunk():
			
			messagebox.showerror('You Lose!', 'The AI sunk all your ships :(', icon='error')
			self.set_grid('disabled', self.attack_grid_buttons)
			
		elif t00_0_ai.defend_grid.all_vessels_sunk():
			
			messagebox.showerror('You Win!', 'YOU ARE A WINNER!! :)', icon='info')
			self.set_grid('disabled', self.attack_grid_buttons)
