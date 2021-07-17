
class MinesweeperBoard:
    def __init__(self,sizes, bombs_cuantities):
        self.sizes = sizes
        self.bombs_cuantities = bombs_cuantities
        self.grid =self.new_grid()
        self.set_values_in_grid()
        self.holes = set()

    