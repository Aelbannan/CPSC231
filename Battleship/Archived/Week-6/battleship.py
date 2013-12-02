#AHMED ELBANNAN
#T2G5

import grid
import ai
import human


def main():
	
	for i in range(grid.NUM_OF_VESSELS):
		
		#human.get_location(i)
		grid.add_vessel(human.grid_defend, i, i, 0, 'h') 
		ai.get_location(i)
		print("AI Grid:")
		grid.print_grid(ai.grid_defend)
		print("Human Grid:")
		grid.print_grid(human.grid_defend)  

	while not (grid.all_vessels_sunk(ai.grid_defend) and grid.all_vessels_sunk(human.grid_defend)):
		
		human.enter_choice()
		
		row, col = human.get_choice()
		grid.drop_bomb(ai.grid_defend, human.grid_attack, row, col)
		
		row, col = ai.get_choice()
		grid.drop_bomb(human.grid_defend, ai.grid_attack, row, col)
		
		print("AI Grid:")
		grid.print_grid(ai.grid_defend)
		print("Human Grid:")
		grid.print_grid(human.grid_defend)  
		print("AI Grid A:")
		grid.print_grid(ai.grid_attack)
		print("Human Grid A:")
		grid.print_grid(human.grid_attack)  
		
		
main()
	
	
	


	
