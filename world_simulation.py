# Helper function that creates the wumpus world based on the provided maze size
def init_maze(maze, size):
    temp_list = []
    # Create an empty maze that is the given size
    for y in range(size):
        for x in range(size):
            temp_list.append('_')
        maze.append(temp_list)
    
# Helper function to print out the wumpus world
def print_maze(maze):
    
    for y in range(len(maze)):
        for x in range(len(maze)):
            print(maze[y][x], end='')

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