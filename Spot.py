# Class Spot to represent one spot on the board
class Spot:
    
    def __init__(self, x_coord, y_coord, empty=True, gold=False, wumpus=False, pit=False, shiny=False, breeze=False, stench=False):
        self.empty = empty
        self.gold = gold
        self.wumpus = wumpus
        self.pit = pit
        self.shiny = shiny
        self.breeze = breeze
        self.stench = stench