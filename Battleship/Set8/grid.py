###### Exercise Set 7 - Code supplied for exercise 1 ################

GRID_WIDTH = 10
GRID_HEIGHT = 10

VESSEL_NAMES = ["aircraft carrier", "battleship", "submarine", "destroyer"]
VESSEL_SIZES = [5,4,3,2]
NUM_OF_VESSELS = 4

B = '_'
HIT = 'X'
MISS = 'o'

# The class grid contains a single grid and all the functions that can
# be applied to a grid.  You can create multiple grids using:
# g1 = Grid()  (or grid_provided.Grid() is in a different module)
# g2 = Grid()
# g1 and g2 now are two distinct grids with the same functionality.
class Grid:
    # This code will be executed when a new instance of a grid is created
    def __init__(self) :
        self.grid = [[B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B]]
    
    #checks if grid is empty at location provided
    def is_empty(self,row, column):
        
        if self.grid[row][column] == B:
                return True
        
        else:
                   return False
    
    #checks if grid is on the grid, and a valid location    
    def on_grid(self, row, column):
               if 0 <= row <= GRID_WIDTH and 0 <= column <= GRID_HIEGHT:
                     return True
               
               else:
                     return False

    #true if there is a hit, checks  the row, col provided, then uses a loop to check if its any of vessels listed. 
    def is_hit(self, row, column):
               for i in range(0, len(VESSEL_SIZES)):
                
                     if self.grid[row][column] == VESSEL_SIZES[i]:
                
                          return True

    #Checks entire grid to see if there is anything other then water, misses, or hits. 
    def all_vessels_sunk(self):
               
               for i in range(0, GRID_WIDTH):
                     
                     for e in range(0, GRID_HEIGHT):
                     
                          if self.grid[i][e] != B and self.grid[i][e] != MISS and self.grid[i][e] != HIT:
                     
                              return False
               return True
                              
    #Checks if its a hit, using previous function, then adds hit/miss to the attack and defend grids.                           
    def drop_bomb(self, attack, row, col):
               if self.is_hit(row, col):
                     attack.grid[row][col] = HIT
                     self.grid[row][col] = HIT
               else:
                     attack.grid[row][col] = MISS
                     self.grid[row][col] = MISS
        
    # Drop some random bombs on the grid, just for testing.  All of
    # them are assumed to miss.
    def drop_test_bombs(self) :
        import random
        num_of_bombs = random.randint(5,50)
        for bomb_num in range(0,num_of_bombs) :
            row = random.randint(0,GRID_HEIGHT-1)
            column = random.randint(0,GRID_WIDTH-1)
            self.grid[row][column] = MISS

    # Pretty-prints this grid to the console.
    def print_grid(self) :
        print("   A B C D E F G H I J")
        for row_index in range(0, GRID_HEIGHT) :
            print(row_index + 1, '', end="")
            if (row_index + 1 < 10) :
                print(' ', end="")

            for column_index in range(0, GRID_WIDTH) :
                print(self.grid[row_index][column_index], '', end="")

            print()

    # Adds the vessel specified by the index to the current grid at top-left row,column
    # in direction indicated.  It does so by putting the size of the vessel
    # at each grid point the vessel occupies.
    def add_vessel(self, index, row, column, direction) :
        size = VESSEL_SIZES[index]

        if (direction == 'h') :
            for column_index in range(column, column + size) :
                self.grid[row][column_index] = size
        else :
            for row_index in range(row, row + size) :
                self.grid[row_index][column] = size

    # Adds the vessel specified by the index to the grid at top-left row,column
    # in direction indicated.  It does so by putting the size of the vessel
    # at each grid point the vessel occupies.
    def has_overlap(self, index, row, column, direction) :
        size = VESSEL_SIZES[index]
        overlap_found = False

        if (direction == 'h') :
            for column_index in range(column, column + size) :
                if (self.grid[row][column_index] != B) :
                    overlap_found = True
        else :
            for row_index in range(row, row + size) :
                if (self.grid[row_index][column] != B) :
                    overlap_found = True

        return overlap_found

# We'll have to add these back later.
#
#def drop_bomb(self, attack_grid, bomb_row, bomb_column) :

#    
#def is_hit(defend_grid, bomb_row, bomb_column) :

#def all_vessels_sunk(defend_grid) :

