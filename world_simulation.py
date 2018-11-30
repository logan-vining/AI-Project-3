from Spot import Spot
from Agent import Agent
from random import randint
import heapq

# Helper function that creates the wumpus world based on the provided maze size
def init_maze(maze, size):
    
    # Temp list to hold new spots that are added to the maze
    temp_list = []
    
    # Create an empty maze that is the given size
    for y in range(size):
        for x in range(size):
            temp_list.append(Spot(x, y))
        maze.append(temp_list)
        temp_list = []

    # First pick random spot for gold
    gold_x = 0
    gold_y = 0
    while gold_x == 0 and gold_y == 0:
        gold_x = randint(0, size - 1)
        gold_y = randint(0, size - 1)

        if gold_x != 0 or gold_y != 0:
            maze[gold_y][gold_x].gold = True

    # Next pick a spot for the wumpus
    wump_x = 0
    wump_y = 0
    while wump_x == 0 and wump_y == 0:
        wump_x = randint(0, size - 1)
        wump_y = randint(0, size - 1)

        if wump_x != 0 or wump_y != 0:
            maze[wump_y][wump_x].empty = False
            maze[wump_y][wump_x].wumpus = 2

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
            if pit_y == 0 and pit_x == 0:
                continue

            test_int = randint(1, 10)

            # Test if the spot is within the 20% margin
            if test_int < 3 and maze[pit_y][pit_x].empty and pit_x != gold_x and pit_y != gold_y:
                maze[pit_y][pit_x].empty = False
                maze[pit_y][pit_x].pit = 2

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
def print_maze(maze, agent):
    for y in range(len(maze)):
        for x in range(len(maze)):
            if y == agent.current_y and x == agent.current_x:
                print('A', end = ' ')
            elif maze[y][x].gold == True:
                print('G', end = ' ')
            elif maze[y][x].wumpus == 2:
                print('W', end = ' ')
            elif maze[y][x].pit == 2:
                print('P', end = ' ')
            elif maze[y][x].empty:
                print('_', end = ' ')

        print('\n')

# Helper function that moves the agent back to the start to leave once he gets the gold
def path_to_victory(maze, agent):

    agent.current_x = 0
    agent.current_y = 0

    print('---------------------')
    print_maze(maze, agent)
    print("Agent, leave the dungeon now and rest. You've earned it!")

# Helper function that calculates the cost to move between spaces
def move_points(maze, agent, points):
    
    

# Main function that processes the spot the agent moved into and calculates points
def process_move(maze, agent, points):
    
    # Check if agent ran into live wumpus
    if maze[agent.current_y][agent.current_x].wumpus == 2:
        print('Agent eviscerated by the Wumpus!')
        agent.dead = True
        points = points - 1000

    # Then check if agent fell into a pit
    elif maze[agent.current_y][agent.current_x].pit == 2:
        print('Agent tripped and fell to their demise!')
        agent.dead = True
        points = points - 1000
        
    # Then check if the agent found the gold and pick it up
    elif maze[agent.current_y][agent.current_x].gold:
        print('Agent retrieved the gold!')
        agent.has_gold = True
        points = points + 1000
        
    # Finally check if the agent deduced where the wumpus is
    if (agent.current_x - 1 >= 0 and agent.knowledge[agent.current_y][agent.current_x - 1].wumpus_count == 3 and agent.arrow):
        agent.arrow = False
        points = points - 10
        print('Agent shot arrow!')
        if maze[agent.current_y][agent.current_x - 1].wumpus == 2:
            maze[agent.current_y][agent.current_x - 1].wumpus = 0
            maze[agent.current_y][agent.current_x - 1].stench = True
            agent.wumpus_dead = True
            print('Wumpus killed!')

    elif (agent.current_y - 1 >= 0 and agent.knowledge[agent.current_y - 1][agent.current_x].wumpus_count == 3 and agent.arrow):
        agent.arrow = False
        print('Agent shot arrow!')
        points = points - 10
        if maze[agent.current_y - 1][agent.current_x].wumpus == 2:
            maze[agent.current_y - 1][agent.current_x].wumpus = 0
            maze[agent.current_y - 1][agent.current_x].stench = True
            agent.wumpus_dead = True
            print('Wumpus killed!')

    elif (agent.current_x + 1 < len(maze) and agent.knowledge[agent.current_y][agent.current_x + 1].wumpus_count == 3 and agent.arrow):
        agent.arrow = False
        print('Agent shot arrow!')
        points = points - 10
        if maze[agent.current_y][agent.current_x + 1].wumpus == 2:
            maze[agent.current_y][agent.current_x + 1].wumpus = 0
            maze[agent.current_y][agent.current_x + 1].stench = True
            agent.wumpus_dead = True
            print('Wumpus killed!')

    elif (agent.current_y + 1 < len(maze) and agent.knowledge[agent.current_y + 1][agent.current_x].wumpus_count == 3 and agent.arrow):
        agent.arrow = False
        print('Agent shot arrow!')
        points = points - 10
        if maze[agent.current_y + 1][agent.current_x].wumpus == 2:
            maze[agent.current_y + 1][agent.current_x].wumpus = 0
            maze[agent.current_y + 1][agent.current_x].stench = True
            agent.wumpus_dead = True
            print('Wumpus killed!')

    print('points = ' + str(points))

# Main function that simulates the agent moving throughout the maze
def search_board(maze):
    points = 0
    next_spots = []
    
    # First make the agent and place him in the start spot
    agent = Agent(len(maze))
    agent.knowledge[agent.current_y][agent.current_x].ok = True

    print('---------------------')
    print_maze(maze, agent)
    
    # Continue moving through the maze until the agent dies or found the gold
    while not agent.dead and not agent.has_gold:
        
        # Update the KB of the agent
        agent.update_knowledge(maze[agent.current_y][agent.current_x])

        # Check surrounding spaces for the least risky spot
        if ((agent.current_x - 1 >= 0) and not agent.knowledge[agent.current_y][agent.current_x - 1].visited):
            if (maze[agent.current_y][agent.current_x - 1] not in next_spots):
                next_spots.append(maze[agent.current_y][agent.current_x - 1])

        if ((agent.current_y - 1 >= 0) and not agent.knowledge[agent.current_y - 1][agent.current_x].visited):
            if (maze[agent.current_y - 1][agent.current_x] not in next_spots):
                next_spots.append(maze[agent.current_y - 1][agent.current_x])

        if ((agent.current_x + 1 < len(maze)) and not agent.knowledge[agent.current_y][agent.current_x + 1].visited):
            if (maze[agent.current_y][agent.current_x + 1] not in next_spots):
                next_spots.append(maze[agent.current_y][agent.current_x + 1])

        if ((agent.current_y + 1 < len(maze)) and not agent.knowledge[agent.current_y + 1][agent.current_x].visited):
            if (maze[agent.current_y + 1][agent.current_x] not in next_spots):
                next_spots.append(maze[agent.current_y + 1][agent.current_x])

        # If the agent knows the wumpus isn't dead, find the least riskiest spot based on wumpus and pits
        if not agent.wumpus_dead:
            next_spots.sort(key = lambda x: (agent.knowledge[x.y_coord][x.x_coord].total_risk, (abs(x.x_coord - agent.current_x) + abs(x.y_coord - agent.current_y))))
        
        # If the agent knows the wumpus is dead, find the least riskiest spot based on pits only
        elif agent.wumpus_dead:
            next_spots.sort(key = lambda x: (agent.knowledge[x.y_coord][x.x_coord].pit_count, (abs(x.x_coord - agent.current_x) + abs(x.y_coord - agent.current_y))))

        #Check if the next spot is adjacent
        if (((next_spots[0].x_coord == agent.current_x) and (next_spots[0].y_coord == agent.current_y + 1))
                or
            ((next_spots[0].x_coord == agent.current_x) and (next_spots[0].y_coord == agent.current_y - 1))
                or
            ((next_spots[0].y_coord == agent.current_y) and (next_spots[0].x_coord == agent.current_x + 1))
                or
            ((next_spots[0].y_coord == agent.current_y) and (next_spots[0].x_coord == agent.current_x - 1))):

            agent.current_x = next_spots[0].x_coord
            agent.current_y = next_spots[0].y_coord

            next_spots.pop(0)

        # Do a search for the cost to the next spot
        else:
            agent.current_x = next_spots[0].x_coord
            agent.current_y = next_spots[0].y_coord

            next_spots.pop(0)

        process_move(maze, agent, points)

        print('---------------------')
        print_maze(maze, agent)


    if agent.has_gold:
        path_to_victory(maze, agent)

def main():

    # List to hold current wumpus world maze
    maze = []

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
            break
        elif size == '5':
            init_maze(maze, int(size))
            break
        elif size == '8':
            init_maze(maze, int(size))
            break
        elif size == '10':
            init_maze(maze, int(size))
            break

        # If user input invalid value, produce error message
        else:
            print('Invalid input!')
            print()

    search_board(maze)


main()
