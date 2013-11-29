# import dependencies
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import functools
import grid
import ai
import random
import sys
import audio

# fonts
big_font = ('Verdana', 16, 'bold')
little_font = ('Trebuchet MS', 10)

penalty = 0 # penalty points
fps = 10
anim_length = 4

###### APOCALYPSE GUI ######
class ApocalypseGUI:
	
	### Initialization ###
	def __init__(self, w, h):		
		
		self.BASIC_UNIT = 64 # basic unit
		self.CON_LINES = 12 # num of lines in console
		self.CON_SIZE = self.BASIC_UNIT* 5	# console size	
		
		
		# The board for the human
		self.human_board = grid.Grid() 
		ai.board = grid.Grid() # ai board
		
		# Human piece and it's co-ordinates
		self.cur_piece = ''
		self.last_x = 0
		self.last_y = 0
		self.char = 'none'
		self.color = 'white'
		
		# Create the main window
		self.root = Tk()
		self.root.title('Apocalypse')
		
		# Make the screen size stay the same
		self.root.minsize(w,h)
		self.root.maxsize(w,h)
		
		# Save width and height
		self.w = w
		self.h = h
			
				
		# Load sprites
		self.load_resources()
		
		# Make the titlescreen
		self.setup_titlescreen()
		
		# Make the menubar
		self.load_menubar()
		# Tkinter loop
		self.root.mainloop()
	
	def load_menubar(self):
		
		#Creates a Menu Bar
		self.menubar = Menu(self.root)
		
		#Creates a file sub-menu 
		self.filemenu = Menu(self.root, tearoff=0)
		
		#Adds 'commands' options in the menu
		self.filemenu.add_command(label="Difficulty", command = self.get_difficulty)
		self.filemenu.add_command(label="Save")
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command = self.do_exit)
		
		#Adds filemenu to menubar
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		
		#Init
		self.root.config(menu=self.menubar)
	
	#Exits the program
	def do_exit(self):
		global root
		self.root.destroy()
	
	#Difficulty slider, Function is the new dialog that pops up.... 
	def get_difficulty(self):
		
		#Var set
		self.scaledifficulty = 0
	
		#Create TopLevel - Dialog and set size
		self.window = Toplevel(self.root, width = 420, height= 240) #TopLevel Dialog created with a set width and height
		self.window.title('Set the difficulty') #Give it a title
		
		#Create a frame and place it
		self.diff_frame = ttk.Frame(self.window)   #Create ttk Frame within parent window
		self.diff_frame.place(x = 0, y = 0, width = 420, height = 240) # Place diff_frame with set width and height
		
		#Create title text. 
		self.ttext1 = ttk.Label(self.diff_frame, font = big_font, text= "Difficulty Slider: ") #Label created with text desired
		self.ttext1.place(x=210, y=15, anchor = CENTER) #Placing Title Text, with a center justification
		
		#Create a slider, and give the variable ther value of the slider
		self.scale = ttk.Scale(self.diff_frame, from_=0, to=8, orient =HORIZONTAL, value = ai.difficulty) #Creates scale and gives it the value of the current AI. 
		self.scale.place(x = 210, y =60 , anchor=CENTER, height = 30, width = 240, ) #Places slider 

		#Adds a label with information related to the difficulty of the ai; Disclaimer. See text above for a more thorough explanation of what each line does. 
		self.sctext1 = ttk.Label(self.diff_frame, text="The slider controls the difficulty of the AI. Please note that any ", font = little_font)
		self.sctext1.place(x = 210, y = 100, anchor = CENTER)
		self.sctext2 = ttk.Label(self.diff_frame, text="value over 4 will take a huge amount of computation.", font = little_font)
		self.sctext2.place(x = 210, y = 120, anchor = CENTER)
		self.sctext3 = ttk.Label(self.diff_frame, text="So use with caution.", font = little_font)
		self.sctext3.place(x = 210, y = 140, anchor = CENTER)
		
		#Confirming that they what they just did....
		self.ok_button = ttk.Button(self.diff_frame, text = 'Okay', command = self.do_difficulty) #When button pressed it activates the method do_difficulty within the class
		self.ok_button.place(x =320, y =200, anchor = NW) #Place button,  
	
	#Does the action of the changing the difficulty
	def do_difficulty(self):
		
		#Gets the value of the scale before we get rid of it. 
		self.diff = self.scale.get()
		
		#Destroys the window that we no longer need
		self.window.destroy()
		
		#Sets ai difficulty equal to the slider
		ai.difficulty = int(self.diff)

	def load_resources(self):
		
		# background images
		self.title_bac = (PhotoImage(file = 'resources/images/TitleScreen0.gif'))
		self.new_bac = (PhotoImage(file = 'resources/images/NewScreen.gif'))
		self.char_bac = (PhotoImage(file = 'resources/images/CharSelect.gif'))
		self.main_bac = (PhotoImage(file = 'resources/images/GameScreen.gif'))
		
		# These lists will hold the images
		self.spr_board = []
		self.white_pieces = []
		self.black_pieces = []
		self.spr_chars = []
		self.bac_chars = []
		self.spr_yin = []

		o = 0
		
		# Empty pieces
		self.spr_board.append((PhotoImage(file = 'resources/images/boards/' + str(o) + '/LightBlock.gif')))
		self.spr_board.append((PhotoImage(file = 'resources/images/boards/' + str(o) + '/DarkBlock.gif')))
		
		self.bac_chars.append((PhotoImage(file = 'resources/images/char_bac.gif')))
		self.bac_chars.append((PhotoImage(file = 'resources/images/char_bac_selected.gif')))
		
		self.spr_yin.append((PhotoImage(file = 'resources/images/yin0.gif')))
		self.spr_yin.append((PhotoImage(file = 'resources/images/yin1.gif')))
		self.done_button = (PhotoImage(file = 'resources/images/done.gif'))

		
		
		
		for i in range(24):
			self.spr_chars.append((PhotoImage(file = 'resources/images/chars/char'+str(i)+'.gif')))
			#self.white_chars.append((PhotoImage(file = 'resources/images/chars/wchar'+str(i)+'.gif')))
			#self.black_chars.append((PhotoImage(file = 'resources/images/chars/bchar'+str(i)+'.gif')))
			
	def load_pieces(self, white, black):
		
		try:
			file = open('resources/images/pieces/set'+str(black)+'/anim', 'r')
			file.readline()
			file.readline()
			repeat_p = int(file.readline())
			repeat_k = int(file.readline())
			file.close()
		except IOError:
			print('Error loading animations')
		except ValueError:
			print('Error in animation file')
			
		# Load the pieces 
		for i in range(repeat_p):
			self.black_pieces.append((PhotoImage(file = 'resources/images/pieces/set'+str(black)+'/BPawn'+str(i)+'.gif')))
			
		for k in range(repeat_k):
			self.black_pieces.append((PhotoImage(file = 'resources/images/pieces/set'+str(black)+'/BKnight'+str(k)+'.gif')))
			
		try:
			file = open('resources/images/pieces/set'+str(white)+'/anim', 'r')
			repeat_p = int(file.readline())
			repeat_k = int(file.readline())
			file.close()
		except IOError:
			print('Error loading animations')
		except ValueError:
			print('Error in animation file')
				
		for o  in range(repeat_p):
			self.white_pieces.append((PhotoImage(file = 'resources/images/pieces/set'+str(white)+'/WPawn'+str(o)+'.gif')))
			
		for e  in range(repeat_k):
			self.white_pieces.append((PhotoImage(file = 'resources/images/pieces/set'+str(white)+'/WKnight'+str(e)+'.gif')))

		
	### updates the grid ###
	def update_grid(self, anim):
		
		if anim == 10000000:
			anim = 0
			
		for i in range(grid.GRID_HEIGHT):
		
			for j in range(grid.GRID_WIDTH):
			
				# checkerboard pattern color
				#block_color = 1
				
				# this allows us to draw a checkerboard pattern
				#if (i%2)==(j%2):
					#block_color = 0
					
				if self.human_board.board[i][j] != grid.b:
				
					piece = self.human_board.board[i][j]
					
				elif ai.board.board[i][j] != grid.b:
				
					piece = ai.board.board[i][j]
					
				else:
					piece = ''
					
				if piece != '':
					if piece[1] == 'P':
						
						if piece[0] == 'W':

							self.board_canvas.itemconfig('piece' + str(i) + str(j), image = self.white_pieces[anim%int(.5*len(self.white_pieces))])
						
						else:
						
							self.board_canvas.itemconfig('piece' + str(i) + str(j), image = self.black_pieces[anim%int(.5*len(self.black_pieces))])

							
					elif piece[1] == 'K':
					
						if piece[0] == 'W':
							
							self.board_canvas.itemconfig('piece' + str(i) + str(j), image = self.white_pieces[int(.5*len(self.white_pieces)) + anim%int(.5*len(self.white_pieces))])
			
						else:
						
							self.board_canvas.itemconfig('piece' + str(i) + str(j), image = self.black_pieces[int(.5*len(self.black_pieces)) + anim%int(.5*len(self.black_pieces))])
							
							
						
				else:
						
						self.board_canvas.itemconfig('piece' + str(i) + str(j), image = '')
		
		# loop through the grid

		
		self.root.after(int(1000/fps), self.update_grid, anim + 1) # updates every 100ms
		
	### sets up the titlescreen ###
	def setup_titlescreen(self):
	
		# the main frame that holds all	
		self.main_frame = ttk.Frame(self.root)
		self.main_frame.place(x = 0, y = 0, width = self.w, height = self.h)
		
		# add background picture
		self.bac_canvas = Canvas(self.main_frame) # add a canvas (unleash your inner artist)
		self.bac_canvas.place(x = 0, y = 0, width = self.w, height = self.h) # place it
		self.bac_canvas.create_image(0, 0, image = self.title_bac, anchor = NW, tag = 'bac') # add image to background
		self.bac_canvas.bind('<1>', self.titlescreen_clicked) # so we can do that fancy click to start
		#print('hi')
		
	
	### Takes you from the titlescreen to the actual game (sets up the game area) ###
	def titlescreen_clicked(self, *args):
		self.bac_canvas.delete('bac')
		self.bac_canvas.create_image(0, 0, image = self.new_bac, anchor = NW, tag = 'bac')
		self.bac_canvas.unbind('<1>')
		self.bac_canvas.bind('<1>', self.new_game_clicked) # so we can do that fancy click to start
		
		#Plays start notification
		audio.play_music('start.wav')
	
	def new_game_clicked(self, event):
		if 625 <= event.x <= 840 and 460 <= event.y <= 535:
			self.bac_canvas.delete('bac')
			
			self.bac_canvas.unbind('<1>')
			self.bac_canvas.create_image(0, 0, image = self.char_bac, anchor = NW, tag = 'bac') # add spiffy background
			
			#self.bac_canvas.create_text(self.w/2,16, font = big_font, text = '[CHOOSE YOUR TEAM AND CHARACTER]', fill = 'white', tag = 'pick' )
		
		#self.bac_canvas.create_text(self.w/4,64, font = big_font, text = 'WHITE', fill = 'white', tag = 'white' )
		
		#self.bac_canvas.create_text((3 * self.w)/4,64, font = big_font, text = 'BLACK', fill = 'white', tag = 'black' )

		#color = OptionMenu(self.root, None, 'white', 'black')
		#color.place(x = 440, y = 650, width = 40, height = 20)
		
		#self.char = []
		
			for i in range(4):
				for j in range(6):
					row = 32
					if i % 2 == 1:
						row = 0
						
					self.bac_canvas.create_image(row + 32 + j * 156, 96 + i *  116, image = self.bac_chars[0], anchor = NW, tag = 'bac'+str(i)+str(j))
					#self.bac_canvas.tag_bind('board'+str(i)+str(j), '<Button-1>', functools.partial(self.board_clicked, i * 6 + j))
					
					self.bac_canvas.create_image(row + 32 + j * 156, 96 + i *  116, image = self.spr_chars[i * 6 + j], anchor = NW, tag = 'char'+str(i)+str(j))
					self.bac_canvas.tag_bind('char'+str(i)+str(j), '<Button-1>', functools.partial(self.choose_char, i , j))
			
		
			self.bac_canvas.create_image(self.w/4 - 72, self.h - 64, image = self.spr_yin[0], tag = 'yin')
			self.bac_canvas.tag_bind('yin', '<Button-1>', functools.partial(self.choose_char, 99 , 0))
			
			self.bac_canvas.create_image(3*self.w/4 + 72, self.h - 64, image = self.done_button, tag = 'done')
			self.bac_canvas.tag_bind('done', '<Button-1>', functools.partial(self.choose_char, 199 , 0))
			


			
		'''for i in range(4):
			for j in range(3):
			
				button = ttk.Button(self.root, image = self.white_chars[i * 3 + j] , command = functools.partial(self.choose_color, i * 3 + j )) # functools replaces lambda
				button.place(x = 61 + j*116, y = 96 + i*116, height = 106, width = 106)
				self.char.append(button)
				
				button = ttk.Button(self.root, image = self.black_chars[i * 3 + j] , command = functools.partial(self.choose_color, i * 3 + j )) # functools replaces lambda
				button.place(x = self.w/2 + 61 + j*116, y = 96 + i*116, height = 106, width = 106)
				self.char.append(button)'''
		
	def choose_char(self, a, b, event):
		if a == 199:
			if self.char != 'none':
				self.done_setup(self.color, self.char)
		elif a == 99:
			if self.color == 'white':
				self.bac_canvas.itemconfig('yin', image = self.spr_yin[1])
				self.color = 'black'
			else:
				self.bac_canvas.itemconfig('yin', image = self.spr_yin[0])
				self.color = 'white'
		else:
			self.char = a * 6 + b
			
			for i in range(4):
				for j in range(6):
					self.bac_canvas.itemconfig('bac'+str(i)+str(j), image = self.bac_chars[0])
					
			self.bac_canvas.itemconfig('bac'+str(a)+str(b), image = self.bac_chars[1])

		
	def done_setup(self, color, char):

		for i in range(4):
				for j in range(6):
					self.bac_canvas.delete('char'+str(i)+str(j))
			
		self.bac_canvas.delete('pick')
		self.bac_canvas.delete('yin')
		self.bac_canvas.delete('done')
		
		if color == 'white':
			
			self.load_pieces(char, 0)
			self.dic_ai = { 'BP1':[1,0],'BP2':[0,1], 'BP3':[0,2], 'BP4':[0,3], 'BP5':[1,4], 'BK1':[0,0], 'BK2':[0,4]}
			self.dic_human = { 'WP1':[3,0],'WP2':[4,1], 'WP3':[4,2], 'WP4':[4,3], 'WP5':[3,4], 'WK1':[4,0], 'WK2':[4,4] }

		
		elif color == 'black':
			
			self.load_pieces(0, char)
			self.dic_human = { 'BP1':[1,0],'BP2':[0,1], 'BP3':[0,2], 'BP4':[0,3], 'BP5':[1,4], 'BK1':[0,0], 'BK2':[0,4]}
			self.dic_ai = { 'WP1':[3,0],'WP2':[4,1], 'WP3':[4,2], 'WP4':[4,3], 'WP5':[3,4], 'WK1':[4,0], 'WK2':[4,4] }
			#messagebox.showinfo('', 'You are black')
			
		
		# setup the boards
		ai.board.setup_board(self.dic_ai)
		self.human_board.setup_board(self.dic_human)
 
		# send the ai dictionary to ai
		ai.dic_ai = dict(self.dic_ai)	
		
		self.setup_game()
		
	def setup_game(self, *args):
		#self.choose_player()
		audio.play_music("indusalarm.wav")
		self.bac_canvas.delete('bac')

		self.bac_canvas.create_image(0, 0, image = self.main_bac, anchor = NW, tag = 'bac') # add spiffy background
		
		#Empty grid for buttons 
		self.grid = []
		
		## Sets up the game board ##
		
		#Container for the board 
		#self.board_frame = ttk.Frame(self.root)
		#self.board_frame.place(x = self.w/2 - 6*self.BASIC_UNIT, y = self.h/2 - 2*self.BASIC_UNIT, width = 5*self.BASIC_UNIT, height = 5*self.BASIC_UNIT)
		self.board_canvas = Canvas(self.root)
		self.board_canvas.place(x = self.w/2 - 6*self.BASIC_UNIT - 2, y = self.h/2 - 2*self.BASIC_UNIT - 2, width = 5*self.BASIC_UNIT + 4, height = 5*self.BASIC_UNIT + 4)
		
		self.board_canvas.bind('<Button-1>', self.grid_button_clicked)
				
		
		#Places buttons onto the empty grid
		for i in range(grid.GRID_HEIGHT):
		
			row = [] # row so we can append to 2D grid
			
			for j in range(grid.GRID_WIDTH):
			
				block_color = 1
				
				# this allows us to draw a checkerboard pattern
				if (i%2)==(j%2):
					block_color = 0
					
				self.board_canvas.create_image(2 + j * 64, 2 + i *  64, image = self.spr_board[block_color], anchor = NW, tag = 'board'+str(i)+str(j))

				self.board_canvas.create_image(2 + j * 64, 2 + i *  64, image = '', anchor = NW, tag = 'piece'+str(i)+str(j))
				
				self.board_canvas.create_image(2 + j * 64, 2 + i *  64, image = '', anchor = NW, tag = 'overlay'+str(i)+str(j))
				
		
		# update dat griiid
		#self.update_grid()
		
		## Sets up the console (will be used for trash talking computer)##
		
		self.console_text = ['' for i in range(self.CON_LINES)] # the text in the console
		self.console_lines = [] # the line objects
		self.console_icons = [] # emoticons. coming soon!

		#Create canvas for the console
		self.console_canvas = Canvas(self.root, bg = 'white')
		self.console_canvas.place(x = self.w/2 + self.BASIC_UNIT, y = self.h/2 - self.BASIC_UNIT*2, width = self.BASIC_UNIT*6, height = self.CON_SIZE)
		
		#Putting the text lines onto the consoles
		for i in range(self.CON_LINES):
			self.console_lines.append(self.console_canvas.create_text(4, i*(self.CON_SIZE/self.CON_LINES) + 4, anchor = NW))
			self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i])
			
		#Input text 
		self.entry_var = StringVar()
		self.console_entry = ttk.Entry(self.root, textvariable = self.entry_var)
		self.console_entry.place(x = self.w/2 + self.BASIC_UNIT, y = self.h/2 - self.BASIC_UNIT*2 + self.CON_SIZE + 16, width = self.BASIC_UNIT*4, height = 24)

		
		# button to reply to that rude bot (bot not implemented.... yet!)
		self.entry_button = ttk.Button(text = 'Send', command = self.send_button_clicked)
		self.entry_button.place(x = self.w/2 + self.BASIC_UNIT*5.5, y = self.h/2 - self.BASIC_UNIT*2 + self.CON_SIZE + 16, width = self.BASIC_UNIT, height = 24)
		self.root.bind('<Return>', self.send_button_clicked)
		
		self.update_grid(0)
		
		# Command for updating text on console
	def send_button_clicked(self,*args):
		self.output_text(self.entry_var.get()) #lol 1 line
	
	def board_clicked(self, event):
		print(event.x, event.y, (event.x - 2)/64, (event.y - 2)/64)
		
	### This is the game pree much ###
	def grid_button_clicked(self, event):
		
		x = ( int( (event.y - 2) / 64) )
		y = ( int( (event.x - 2) / 64) )
		
		#print('hey',self.cur_piece)
		if self.cur_piece == '': # if you haven't picked a piece yet
			audio.play_music("pickup.wav")
			for e in self.dic_human: # loop thru human dict
				
				if self.human_board.board[x][y] == e: # if this clicked piece is one of yours!!!!
					
					self.cur_piece = self.human_board.board[x][y] # set it current piece (so we can go to phase 2)
					self.last_x = x # save our position
					self.last_y = y # ^ ye
					
					self.output_text('You selected ' + self.cur_piece + ' at (' + str(x) +  ',' +str(y) + ')') # wut dis do? lol output
					
					
		elif self.cur_piece == self.human_board.board[x][y]: # if you click on the piece you already selected, deselect it!
			audio.play_music("putdown.wav")	
			self.output_text('You deselected ' + self.cur_piece) 		
			
			self.cur_piece = '' # i aint select no darn piece
			
			
		else: # else
			audio.play_music("alert.wav")
			if self.human_board.validate_location(self.last_x, self.last_y, x, y, self.cur_piece, ai.board.board): # if valid move
			
				# get the ai move first (so it doesn't cheat ;) )
				dic_ai, piece_ai = ai.get_move(self.dic_human)

				# if ai cant find any moves, it must be stalemate (I trust my ai)
				if dic_ai == False:
					messagebox.showinfo('', 'Stalemate!')
					sys.exit() # will be replaced by restart
					
				# jus sum outbuts
				self.output_text('You moved ' + self.cur_piece + ' to (' + str(x) +  ',' +str(y) + ')')

				# move human piece
				self.dic_human = self.human_board.move_piece(x,y,self.cur_piece, self.dic_human)
				
				# now actually make the moves (let the carnage begin \(>-<)/ )
				self.dic_human, dic_ai = grid.finalize_move( self.dic_human, dic_ai, self.cur_piece, piece_ai)
				#print(self.dic_human, dic_ai)
				
				# check if the peasants are worthy of knighthood
				dic_ai, mb = grid.check_knight(dic_ai)
				
				# make the boards used for display from dicts
				self.human_board.board = grid.recreate_grid(self.dic_human)
				ai.board.board = grid.recreate_grid(ai.dic_ai)
				
				# if you have 2 knights, put random
				if mb != 'none':
					
					x = random.randint(0, grid.GRID_HEIGHT)
					y = random.randint(0, grid.GRID_WIDTH)
				
					while self.human_board.board[x][y] != grid.b and ai.board.board[x][y] != grid.b:
						x = random.randint(0, grid.GRID_HEIGHT)
						y = random.randint(0, grid.GRID_WIDTH)
						
					dic_ai[mb] = [x,y]
					self.output_text('AI relocated ' + mb + ' to (' + str(x) +  ',' +str(y) + ')')
					
				# k
				self.dic_human, mb = grid.check_knight(self.dic_human)
				
				# if you have 2 knights, ask to relocate
				if mb != 'none':
					a = Popup_Knight(self.root, mb, self.dic_human, self)
					
				# send the ai dictionary back (it got updated)
				ai.dic_ai = dic_ai
				
				# make the boards used for display from dicts
				self.human_board.board = grid.recreate_grid(self.dic_human)
				ai.board.board = grid.recreate_grid(ai.dic_ai)
				
				#self.update_grid()
					
				# if WE HAVE A WINNER!
				won = grid.get_winner(self.dic_human, ai.dic_ai)
				
				if won == 'ai': # if my great ai won (and it will ;) )
				
					messagebox.showinfo('', 'You lose! :(')
					sys.exit()
					
				elif won == 'human': # if you fluked out somehow :p
				
					messagebox.showinfo(' ', 'You Win! :)')
					sys.exit()
					
				elif won == 'draw': # if it is stalemate, Nova!
				
					messagebox.showinfo('', 'Stalemate!')
					sys.exit()
				
				#print(grid.recreate_grid(self.dic_human))
				#print(grid.recreate_grid(ai.dic_ai))
				
				self.cur_piece = '' # you already moved so why u need dat piece homie?
				
			else:
			
				global penalty # you goin to penalty!!!!!!!!
				
				self.output_text('You earned a penalty point') # oh no!!!	
				
				penalty += 1 # stacks on stacks
				
				if penalty == 2: # red card + 6 fouls :/
				
					messagebox.showinfo(' ', 'You Lose! :(') # you lose
					sys.exit() # and your kicked out! <(;-;)>
					# no fair play, don't stay
		
		# preeeeety self evident...	
		#self.update_grid()
		#print(self.cur_piece)
		
	#def update_board(self, dic):
		#self.dic_human = dic
		#self.human_board.board = grid.recreate_grid(self.dic_human)	
		
	### pretty much, this is print() for our console ###
	def output_text(self,string):
	
		empty = 0 # if empty
		
		for i in range(self.CON_LINES): # loop thru all lines
			if self.console_text[i] == '': # if empty line
				self.console_text[i] = string # let string live here
				self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i]) # draw the text
				empty = 1 # no homeless strings!!!
				break # we're done here 
                        
		# if all lines are full, then move all lines up one and insert new line in bottom
		if empty == 0: 
			for i in range(self.CON_LINES-1):
				self.console_text[i] = self.console_text[i+1] # move up
				self.console_canvas.itemconfig(self.console_lines[i], text = self.console_text[i]) # update text
            
			# add to last string
			self.console_text[i+1]= string
			# draw last string
			self.console_canvas.itemconfig(self.console_lines[i+1], text = self.console_text[i+1])
	

# nice custom popup. Pre-order only!
	
class Popup_Knight:
	def __init__(self, root, piece, dic, gui):
		
		# we need these for a while
		self.piece = piece
		self.dic = dic
		self.gui = gui
		
		#create the popup n add title
		self.top = Toplevel(root)
		self.top.title('Too much knights!')
		
		# grab attention
		self.top.grab_set()
		
		# widget lyfe, grid syde
		top_label= ttk.Label(self.top, text='You have 2 knights! Where would you like to move your pawn?', anchor = CENTER)
		top_label.grid(column = 0, row = 0, columnspan = 3)
		row_label= ttk.Label(self.top, text='Row  (1-5)')
		row_label.grid(row = 1, column = 0)
		col_label= ttk.Label(self.top, text='Column  (1-5)')
		col_label.grid(row = 1, column = 2)
		self.row_entry = ttk.Entry(self.top, width = 16)
		self.row_entry.grid(row = 2, column = 0)
		self.col_entry = ttk.Entry(self.top, width = 16)
		self.col_entry.grid(row = 2, column = 2)
		go_button = ttk.Button(self.top, text = 'Go!', command = self.button_click)
		go_button.grid(row = 3, column = 0, columnspan = 3)
		
	# when go button is clicked
	def button_click(self):
	
		# get row/col from entries (can only handle integers)
		row = int(self.row_entry.get()) - 1
		col = int(self.col_entry.get()) - 1
		
		# recreate dem 2 boards...
		board = grid.recreate_grid(self.dic)
		o_board = grid.recreate_grid(ai.dic_ai)
		
		# if on grid...
		if 0 <= col < grid.GRID_WIDTH and 0 <= row < grid.GRID_HEIGHT:
		
			if board[row][col] == grid.b and  o_board[row][col] == grid.b: # if nobody on dat spot homebody
			
				self.dic[self.piece] = [row, col] # set the chance
				self.gui.human_board.board = grid.recreate_grid(self.dic) # and add to official board
				
				#method = getattr(ApocalypseGUI, 'update_board')
				#method(self.dic)
				
				# update original...
				self.gui.dic_human = self.dic
				
				# ye
				#self.gui.update_grid()
				
				self.top.destroy() # :( ill miss him
				
			else:
			
				messagebox.showinfo('!', 'Invalid coordinates')
				
		else:
		
			messagebox.showinfo('!', 'Not on board')
