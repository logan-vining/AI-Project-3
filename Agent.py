from Spot import Spot

# Class for an agent within the wumpus World
class Agent:
    
    def __init__(self, maze_size, current_x = 0, current_y = 0, arrow = True, dead = False):
        
        self.knowledge = []
        temp_list = []
        
        # Create an empty maze that is the given size
        for y in range(maze_size):
            for x in range(maze_size):
                temp_list.append(Spot(x, y))
            self.knowledge.append(temp_list)
            temp_list = []
            
            
        self.current_x = current_x
        self.current_y = current_y
        self.arrow = arrow
        self.dead = dead
        self.has_gold = False
        
        # Var with values 0 = wumpus location unknown and alive
        # 1 = Wumpus location known and alive
        # 2 = Wumpus location known and dead
        self.knows_wumpus = 0
        
        
    def update_knowledge(self, spot):
        spot.visited = True
        x = self.current_x
        y = self.current_y
        
        if not spot.stench and not spot.breeze:
            if x - 1 >= 0:
                self.knowledge[y][x - 1].ok = True
                self.knowledge[y][x - 1].wumpus_count = 0
                self.knowledge[y][x - 1].pit_count = 0
            if y - 1 >= 0:
                self.knowledge[y - 1][x].ok = True
                self.knowledge[y - 1][x].wumpus_count = 0
                self.knowledge[y - 1][x].pit_count = 0
            if x + 1 < len(self.knowledge):
                self.knowledge[y][x + 1].ok = True
                self.knowledge[y][x + 1].wumpus_count = 0
                self.knowledge[y][x + 1].pit_count = 0
            if y + 1 < len(self.knowledge):
                self.knowledge[y + 1][x].ok = True
                self.knowledge[y + 1][x].wumpus_count = 0
                self.knowledge[y + 1][x].pit_count = 0
                
        if spot.stench:
            if x - 1 >= 0 and not self.knowledge[y][x - 1].ok:
                self.knowledge[y][x - 1].wumpus = 1
                self.knowledge[y][x - 1].wumpus_count += 1                    
            if y - 1 >= 0 and not self.knowledge[y - 1][x].ok:
                self.knowledge[y - 1][x].wumpus = 1
                self.knowledge[y][x - 1].wumpus_count += 1
            if x + 1 < len(self.knowledge) and not self.knowledge[y][x + 1].ok:
                self.knowledge[y][x + 1].wumpus = 1
                self.knowledge[y][x - 1].wumpus_count += 1
            if y + 1 < len(self.knowledge) and not self.knowledge[y + 1][x].ok:
                self.knowledge[y + 1][x].wumpus = 1
                self.knowledge[y][x - 1].wumpus_count += 1
                
        if spot.breeze:
            if x - 1 >= 0 and not self.knowledge[y][x - 1].ok:
                self.knowledge[y][x - 1].pit = 1
                self.knowledge[y][x - 1].pit_count += 1
            if y - 1 >= 0 and not self.knowledge[y - 1][x].ok:
                self.knowledge[y][x - 1].pit = 1
                self.knowledge[y][x - 1].pit_count += 1
            if x + 1 < len(self.knowledge) and not self.knowledge[y][x + 1].ok:
                self.knowledge[y][x + 1].pit = 1
                self.knowledge[y][x + 1].pit_count += 1
            if y + 1 < len(self.knowledge) and not self.knowledge[y + 1][x].ok:
                self.knowledge[y][x - 1].pit = 1
                self.knowledge[y][x - 1].pit_count += 1
                
        
        