###### Exercise Set 7 - Solution - ai module ################


import random
import grid
from grid import B

defend_grid = grid.Grid()
attack_grid = grid.Grid()

# Asks the AI to choose a row,column to drop a bomb.  This AI
# randomly chooses a location that does not have a bomb on the
# attach grid yet.
def get_choice() :
    column = random.randint(0, grid.GRID_WIDTH - 1)
    row = random.randint(0, grid.GRID_HEIGHT - 1)
    if (not attack_grid.is_empty(row,column)) :
        row,column = get_choice()

    return row,column

# Function randomly chooses and returns a row, column and direction
def get_random_location() :
    column = random.randint(0, grid.GRID_WIDTH - 1)
    row = random.randint(0, grid.GRID_HEIGHT - 1)
    direction = random.randint(0,1)
    if (direction == 0) :
        direction = 'h'
    else :
        direction = 'v'

    return row,column,direction

# checks if location and direction is valid for vessel indicated
# by index.  If The vessel would fall outside of the bounds or if it
# overlaps with an existing vessel on the defend grid
# it is considered invalid.
#
# This function assumes that the row and column are inside the grid.
def location_is_valid(vessel_index, row, column, direction) :
    size = grid.VESSEL_SIZES[vessel_index]
    valid = True
    if (direction == 'h' and column + size > grid.GRID_WIDTH) :
        valid = False
    elif (direction == 'v' and row + size > grid.GRID_HEIGHT) :
        valid = False
    elif (defend_grid.has_overlap(vessel_index, row, column, direction)) :
        valid = False
    return valid

# This function asks an AI to insert specified vessel in its defense
# grid.  Current implementation get the AI to make a random choice.
def get_location(vessel_index) :
    name = grid.VESSEL_NAMES[vessel_index]
    size = grid.VESSEL_SIZES[vessel_index]

    row,column,direction = get_random_location()

    if (location_is_valid(vessel_index, row, column, direction)) :
        defend_grid.add_vessel(vessel_index, row, column, direction)
    else :
        get_location(vessel_index)
