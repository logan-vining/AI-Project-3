# Class Spot to represent one spot on the board
class Spot:
    
    # Constructor with sensors present in the spot, with 0 = not in, 1 = maybe in, 2 = yes in
    def __init__(self, x_coord, y_coord, empty=True, gold=False, wumpus=0, pit=0, breeze=False, stench=False):
        self.empty = empty
        self.gold = gold
        self.wumpus = wumpus
        self.pit = pit
        self.breeze = breeze
        self.stench = stench
        self.ok = False
        
        self.wumpus_count = 0
        self.pit_count = 0
        self.visited = False