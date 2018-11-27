from Spot import Spot
from random import randint

# Helper function that creates the wumpus world based on the provided maze size
def init_maze(maze, size):
    temp_list = []
    # Create an empty maze that is the given size
    for y in range(size):
        for x in range(size):
            temp_list.append(Spot(x, y))
        maze.append(temp_list)
        temp_list = []
        
    # First pick random spot for gold
    gold_x = randint(0, size - 1)
    gold_y = randint(0, size - 1)
    maze[gold_y][gold_x].empty = False
    maze[gold_y][gold_x].gold = True
    
    # Set spots around gold to shiny
    if gold_x - 1 >= 0:
        maze[gold_y][gold_x - 1].shiny = True
    if gold_y - 1 >= 0:
        maze[gold_y - 1][gold_x].shiny = True
    if gold_x + 1 < len(maze):
        maze[gold_y][gold_x + 1].shiny = True
    if gold_y + 1 < len(maze):
        maze[gold_y + 1][gold_x].shiny = True
    
    # Next pick a spot for the wumpus
    wump_x = randint(0, size - 1)
    wump_y = randint(0, size - 1)
    maze[wump_y][wump_x].empty = False
    maze[wump_y][wump_x].wumpus = True
    
    # Set spots around wumpus to smelly
    if wump_x - 1 >= 0:
        maze[wump_y][wump_x - 1].stench = True
    if wump_y - 1 >= 0:
        maze[wump_y - 1][wump_x].stench = True
    if wump_x + 1 < len(maze):
        maze[wump_y][wump_x + 1].stench = True
    if wump_y + 1 < len(maze):
        maze[wump_y + 1][wump_x].stench = True
    
    # Now loop through each remaining spot and determine if it will be a pit
    for pit_y in range(size):
        for pit_x in range(size):
            test_int = randint(1, 10)
            
            # Test if the spot is within the 20% margin
            if test_int < 3 and maze[pit_y][pit_x].empty:
                maze[pit_y][pit_x].empty = False
                maze[pit_y][pit_x].pit = True
                
                # Set spots around pit to breezy
                # Set spots around wumpus to smelly
                if pit_x - 1 >= 0:
                    maze[pit_y][pit_x - 1].breeze = True
                if pit_y - 1 >= 0:
                    maze[pit_y - 1][pit_x].breeze = True
                if pit_x + 1 < len(maze):
                    maze[pit_y][pit_x + 1].breeze = True
                if pit_y + 1 < len(maze):
                    maze[pit_y + 1][pit_x].breeze = True
    
# Helper function to print out the wumpus world
def print_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[y][x].gold:
                print('G', end = ' ')
            elif maze[y][x].wumpus:
                print('W', end = ' ')
            elif maze[y][x].pit:
                print('P', end = ' ')
            elif maze[y][x].empty:
                print('_', end = ' ')
        
        print('\n')

def main():
    maze = []   # List to hold current wumpus world maze
    
    # User-Friendly menu where the user can select a world to simulate
    print('Welcome to Wumpus World!')
    print('------------------------')
    print()
    
    # Loop until user selects a valid world to simulate
    while True:
        print('Wumpus World Simulator:')
        print('Enter 4 for 4x4 World')
        print('Enter 5 for 5x5 World')
        print('Enter 8 for 8x8 World')
        print('Enter 10 for 10x10 World')
        size = input('Please select a world to simulate: ')
        
        # Process the user input
        if size == '4':
            init_maze(maze, int(size))
            print_maze(maze)
            break
        elif size == '5':
            init_maze(maze, int(size))
            print_maze(maze)
            break
        elif size == '8':
            init_maze(maze, int(size))
            print_maze(maze)
            break
        elif size == '10':
            init_maze(maze, int(size))
            print_maze(maze)
            break
        
        # If user input invalid value, produce error message
        else:
            print('Invalid input!')
            print()
            
main()