import random

VACIO = None

class MinesweeperGrid:
    def __init__(self, sizes, mines_cuantities):
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = self.new_grid()
        #        self.set_values_in_grid()
        self.sweep = set()

    def new_grid(self):
        grid = []
        for y in range(self.sizes):
            grid.append([])
            for x in range(self.sizes): grid[y].append(VACIO)

        mines_underground = 0
        while mines_underground < self.mines_cuantities:
            pos_row = random.randrange(0, self.sizes, 1)
            pos_col = random.randrange(0, self.sizes, 1)
            #            print(pos_row,pos_col)
            if grid[pos_row][pos_col] == 'x':
                continue
            else:
                grid[pos_row][pos_col] = 'x'
                mines_underground += 1
        return grid


grid = MinesweeperGrid(10, 10)
print(grid.grid)
